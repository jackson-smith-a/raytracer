class Interval:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        
    def span(self):
        return self.max_value - self.min_value
    
    def contains(self, value):
        return self.min_value <= value <= self.max_value
    
    def surrounds(self, value):
        return self.min_value < value and value < self.max_value

    def clamp(self, value):
        return min(self.max_value, max(self.min_value, value))
