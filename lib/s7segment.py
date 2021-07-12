class S7Segment:
    def __init__(self, np, address_list): # address_list: [id1, id2]
        self.brightness = 1
        self.np = np
        self.led_list = []
        self.led_list.append([address_list[0], (255, 0, 0), 1]) # [id, (r, g, b), brightness]
        self.led_list.append([address_list[1], (255, 0, 0), 1])
        
    
    def set_color(self, color_list):
        self.led_list[0][1] = color_list[0]
        self.led_list[1][1] = color_list[1] if len(color_list) > 1 else color_list[0]


    def set_brightness(self, brightness):
        for i in range(len(self.led_list)):
            self.led_list[i][2] = brightness


    def get_raw_color(self, color, brightness):
        raw_color = [0, 0, 0]
        for i in range(3):
            raw_color[i] = int(color[i] * brightness)
        return tuple(raw_color)


    def on(self):
        self.np[self.led_list[0][0]] = self.get_raw_color(self.led_list[0][1], self.led_list[0][2])
        self.np[self.led_list[1][0]] = self.get_raw_color(self.led_list[1][1], self.led_list[1][2])
        self.np.write()
        
    
    def off(self):
        self.np[self.led_list[0][0]] = (0, 0, 0)
        self.np[self.led_list[1][0]] = (0, 0, 0)
        self.np.write()
    
        