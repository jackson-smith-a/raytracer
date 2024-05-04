from vec3 import Vec3
from interval import Interval
import math

def linear_to_gamma(lin: float) -> float:
    if lin > 0:
        return math.sqrt(lin)
    return 0.0

class PPM:
    def __init__(self, filename: str, width: int, height: int):
        self.filename = "images/" + filename
        self.width = width
        self.height = height
        
        with open(self.filename, "w") as file:
            file.write(f"P3\n{width} {height}\n255\n")

        self.file = open(self.filename, 'a')
        
    def write(self, color: Vec3):
        r,g,b = color.x, color.y, color.z
        
        r = linear_to_gamma(r)
        g = linear_to_gamma(g)
        b = linear_to_gamma(b)
        
        intensity = Interval(0, 0.999)
        
        r = int(256 * intensity.clamp(r))
        g = int(256 * intensity.clamp(g))
        b = int(256 * intensity.clamp(b))
        
        self.file.write(f"{r} {g} {b}\n")
        
    def close(self):
        self.file.close()

    def __del__(self):
        self.close()
