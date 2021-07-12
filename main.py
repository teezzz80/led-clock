from machine import Pin, RTC
from neopixel import NeoPixel
import time, utime, random
from s7display import S7Display
from s7digit import S7Digit
from s7segment import S7Segment
from nettime import NetTime
from constants import *
from secrets import *


def get_datetime_element(datetime, element):
    return list(datetime)[DATETIME_ENUM[element]]

    
def display_clock(datetime):
    if not is_display_off:
        render_time(datetime, False)
        render_colon()


def render_time(datetime, force):
    hour = get_datetime_element(datetime, "hour")
    minute = get_datetime_element(datetime, "minute")
    (upper_hour, lower_hour) = divmod(hour, 10)
    (upper_minute, lower_minute) = divmod(minute, 10)
    if upper_hour != 0:
        display.pattern(0, CHARS[str(upper_hour)], force)
    else:
        display.digit_list[0].off()
    display.pattern(1, CHARS[str(lower_hour)], force)
    display.pattern(2, CHARS[str(upper_minute)], force)
    display.pattern(3, CHARS[str(lower_minute)], force)


def render_colon():
    global colon_counter
    if colon_counter < 5 and not colon.is_on:  # randomize colon color
        r = randrange(0, 255)
        g = randrange(0, 255)
        b = randrange(0, 255)
        colon.set_color([(r, g, b)])
        colon.on()
    elif colon_counter >= 5 and colon.is_on:
        colon.off()
    
    colon_counter += 1
    if colon_counter > 9:
        colon_counter = 0


def randrange(start, stop=None):
    if stop is None:
        stop = start
        start = 0
    upper = stop - start
    bits = 0
    pwr2 = 1
    while upper > pwr2:
        pwr2 <<= 1
        bits += 1
    while True:
        r = random.getrandbits(bits)
        if r < upper:
            break
    return r + start


def handle_button1(cycle):
    global is_display_off
    if cycle > 1 and cycle <= 3:
        print("Button1 pressed: toggle display")
        if display.is_on:
            display.off()
            colon.off()
            is_display_off = True
        else:
            render_time(now, True)
            is_display_off = False 
    if cycle > 3 and not is_display_off and not is_sleeping:
        print("Button1 long pressed: decrease brightness")
        global BRIGHTNESS
        BRIGHTNESS -= 0.1
        BRIGHTNESS = round(BRIGHTNESS, 1) if BRIGHTNESS > 0 else 0.1
        display.message("BR" + str(BRIGHTNESS * 10).split(".")[0])
        time.sleep(1)
        display.set_brightness(BRIGHTNESS)
        render_time(now, True)


def handle_button2(cycle):
    if cycle > 1 and cycle <= 3 and not is_display_off and not is_sleeping:
        print("Button2 pressed: next theme")
        display.next_theme()
        render_time(now, True)
    if cycle > 3 and not is_display_off and not is_sleeping:
        print("Button2 long pressed: increase brightness")
        global BRIGHTNESS
        BRIGHTNESS += 0.1
        BRIGHTNESS = round(BRIGHTNESS, 1) if BRIGHTNESS <= 1 else 1
        display.message("BR" + str(BRIGHTNESS * 10).split(".")[0])
        time.sleep(1)
        display.set_brightness(BRIGHTNESS)
        render_time(now, True)


API_URL = "http://worldtimeapi.org/api/timezone/America/Edmonton"
WEB_QUERY_DELAY = 3600  # sync time delay in s, default is 3600
RETRY_DELAY = 5  # sync time retry delay in s

SLEEP_AT_NIGHT = False  # turn on or off sleep function
NIGHT_START = 23  # night start hour
SLEEP_DURATION = 9  # hours of sleep at night
REFRESH_DELAY = 100  # display refresh delay in ms

BRIGHTNESS = 0.1  # screen brightness between 0 and 1

colon_counter = 0
is_sleeping = False
is_display_off = False
wake_time = 0

n = 67
np_pin = Pin(14, Pin.OUT)
np = NeoPixel(np_pin, n)
button1 = Pin(0, Pin.IN) # default 1, pressed 0
button2 = Pin(5, Pin.IN) # default 0, pressed 1
button1_cycle = 0
button2_cycle = 0

lm_display = S7Digit([
    S7Segment(np, [4, 5]), S7Segment(np, [6, 7]), S7Segment(np, [9, 10]), S7Segment(np, [11, 12]),
    S7Segment(np, [13, 14]), S7Segment(np, [2, 3]), S7Segment(np, [0, 1])
])

um_display = S7Digit([
    S7Segment(np, [26, 27]), S7Segment(np, [28, 29]), S7Segment(np, [17, 18]), S7Segment(np, [19, 20]),
    S7Segment(np, [21, 22]), S7Segment(np, [24, 25]), S7Segment(np, [30, 31])
])

lh_display = S7Digit([
    S7Segment(np, [39, 40]), S7Segment(np, [41, 42]), S7Segment(np, [44, 45]), S7Segment(np, [46, 47]),
    S7Segment(np, [48, 49]), S7Segment(np, [37, 38]), S7Segment(np, [35, 36])
])

uh_display = S7Digit([
    S7Segment(np, [61, 62]), S7Segment(np, [63, 64]), S7Segment(np, [52, 53]), S7Segment(np, [54, 55]),
    S7Segment(np, [56, 57]), S7Segment(np, [59, 60]), S7Segment(np, [65, 66])
])

display = S7Display([uh_display, lh_display, um_display, lm_display])
display.off()
display.set_brightness(BRIGHTNESS)
display.set_theme(0)

colon = S7Digit([S7Segment(np, [32, 34])])  # colon is not part of display

nt = NetTime(WIFI_SSID, WIFI_PASSWORD)
rtc = RTC()
now = None

update_time = utime.time() - WEB_QUERY_DELAY  # always sync time on start

while True:
    if utime.time() - update_time >= WEB_QUERY_DELAY:
        display.message("Sync")
        netTime = nt.sync_time(API_URL)
        if netTime[0] != "error":
            rtc.datetime(netTime) # update internal rtc time
            update_time = utime.time()
        else:
            display.message("Err")
            update_time = utime.time() - WEB_QUERY_DELAY + RETRY_DELAY
    
    now = rtc.datetime()

    if SLEEP_AT_NIGHT:
        hour = get_datetime_element(now, "hour")
        if hour >= NIGHT_START or is_sleeping:
            if not is_sleeping: # starts sleeping
                print("Start sleeping...")
                display.off()
                colon.off()
                is_sleeping = True
                is_display_off = True
                wake_time = utime.time() + 3600 * SLEEP_DURATION
            if utime.time() >= wake_time: # waking up
                print("Waking up...")
                render_time(now, True)
                is_sleeping = False
                is_display_off = False

    display_clock(now)

    if button1.value() == 0: # button1 is pressed
        button1_cycle += 1
    elif button1.value() == 1 and button1_cycle > 0: # button1 is released
        handle_button1(button1_cycle)
        button1_cycle = 0
    
    if button2.value() == 1: # button2 is pressed
        button2_cycle += 1
    elif button2.value() == 0 and button2_cycle > 0: # button2 is released
        handle_button2(button2_cycle)
        button2_cycle = 0

    time.sleep_ms(REFRESH_DELAY)




