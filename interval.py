class Interval:
    def __init__(self,
                 min_value: float,
                 max_value: float):
        self.min_value = min_value
        self.max_value = max_value
        
    def span(self) -> float:
        return self.max_value - self.min_value
    
    def contains(self, value: float) -> float:
        return self.min_value <= value <= self.max_value
    
    def surrounds(self, value: float) -> float:
        return self.min_value < value and value < self.max_value

    def clamp(self, value: float) -> float:
        return min(self.max_value, max(self.min_value, value))
