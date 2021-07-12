import gc
import machine
import network
import senko
import constants
import secrets

USE_SENKO = False

def connect_wlan(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

    if not sta_if.isconnected():
        print("Connecting to WLAN ({})...".format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass

    return True


def main():
    """Main function. Runs after board boot, before main.py
    Connects to Wi-Fi and checks for latest OTA version.
    """

    gc.collect()
    gc.enable()

    if USE_SENKO:
        connect_wlan(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        
        OTA = senko.Senko(
            user="teezzz80",
            repo="led-clock",
            files=[
                "boot.py",
                "main.py",
                "lib/constants.py",
                "lib/nettime.py",
                "lib/s7digit.py",
                "lib/s7display.py",
                "lib/s7segment.py",
                "lib/senko.py",
                "lib/urequests.py",
            ]
        )

        if OTA.update():
            print("Updated to the latest version! Rebooting...")
            machine.reset()


if __name__ == "__main__":
    main()