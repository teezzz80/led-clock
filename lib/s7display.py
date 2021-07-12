from constants import *

class S7Display:
    def __init__(self, digit_list):
        self.digit_list = digit_list
        self.theme_id = 0
        self.is_on = False


    def on(self):
        for digit in self.digit_list:
            digit.on()
            self.is_on = True


    def off(self):
        for digit in self.digit_list:
            digit.off()
            self.is_on = False
            
    
    def set_brightness(self, brightness):
        for digit in self.digit_list:
            digit.set_brightness(brightness)
            
            
    def set_theme(self, theme_id):
        for i, color in enumerate(THEMES[theme_id]):
            if type(color) is str:
                self.digit_list[i].set_color([COLORS[color]])
            if type(color) is tuple:
                self.digit_list[i].set_color([color])
        self.theme_id = theme_id


    def next_theme(self):
        self.theme_id += 1
        if self.theme_id >= len(THEMES):
            self.theme_id = 0
        self.set_theme(self.theme_id)


    def message(self, message):
        if self.is_on:
            self.off()
            msg = message[:5].upper() if len(message) >= 4 else message.upper()
            m = ""
            for c in msg:
                if c in CHARS:
                    m += c
            digit_id = 0
            for c in msg:
                self.digit_list[digit_id].pattern(CHARS[c], True)
                digit_id += 1


    def pattern(self, digit_id, segment_list, force):
        self.digit_list[digit_id].pattern(segment_list, force)
        self.is_on = True