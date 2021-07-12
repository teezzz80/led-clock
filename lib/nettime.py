import network, urequests

class NetTime:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = None
        
        
    def wifi_connect(self):
        if not self.wlan.isconnected():
            self.wlan.connect(self.ssid, self.password)
            while not self.wlan.isconnected():
                pass

    
    def wifi_disconnect(self):
        self.wlan.disconnect()
        self.wlan.active(False)
    

    def sync_time(self, api_url):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        print("Connecting to network...")
        self.wifi_connect()
        
        try:
            print("Syncing time...")
            response = urequests.get(api_url)

            if response.status_code == 200: # query success
                print("API response:\n", response.text)
                
                # parse JSON
                parsed = response.json()
                datetime_str = str(parsed["datetime"])
                year = int(datetime_str[0:4])
                month = int(datetime_str[5:7])
                day = int(datetime_str[8:10])
                hour = int(datetime_str[11:13])
                minute = int(datetime_str[14:16])
                second = int(datetime_str[17:19])
                subsecond = int(round(int(datetime_str[20:26]) / 10000))
                
                self.wifi_disconnect()
                return (year, month, day, 0, hour, minute, second, subsecond)
            else:  # query failed
                print("Error occured")
                return ("error", 0)
        except:
            print("Error occured")
            return ("error", 0)

    
    
    
