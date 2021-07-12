class S7Digit:
    def __init__(self, segment_list):
        self.last_pattern = None
        self.is_on = False
        self.segment_list = segment_list
        

    def set_segment_color(self, segment_id, color_list):
        segment = self.segment_list[segment_id]
        segment.set_color(color_list)
        
        
    def set_color(self, color_list): # color_list: [led1_color, led2_color]
        for segment in self.segment_list:
            segment.set_color(color_list)
            
    
    def set_brightness(self, brightness):
        for segment in self.segment_list:
            segment.set_brightness(brightness)
        
    
    def segment_on(self, segment_id):
        segment = self.segment_list[segment_id]
        segment.on()
    
    
    def segment_off(self, segment_id):
        segment = self.segment_list[segment_id]
        self.is_on = False
        segment.off()
        

    def on(self):
        for segment in self.segment_list:
            segment.on()
        self.is_on = True
            
    
    def off(self):
        for segment in self.segment_list:
            segment.off()
        self.is_on = False
            
    
    def pattern(self, segment_list, force):
        if self.last_pattern != segment_list or force:
            self.off()
            for id in segment_list:
                segment = self.segment_list[id]
                segment.on()
            self.last_pattern = segment_list

        
        
        
        
        
        
    