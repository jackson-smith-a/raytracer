import math
import random


class Vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        
    def reflect(self, other: "Vec3") -> "Vec3":
        return self - 2 * self.dot(other) * other
        
    def __add__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __neg__(self) -> "Vec3":
        return Vec3(-self.x, -self.y, -self.z)
    
    def __mul__(self, other: float | "Vec3") -> "Vec3":
        """If other is a Vec3, multiplies elementwise.
        Otherwise multiplies each element by other.
        """
        if isinstance(other, Vec3):
            return Vec3(self.x*other.x, self.y*other.y, self.z*other.z)
        return Vec3(self.x*other, self.y*other, self.z*other)
    
    def __rmul__(self, other: float | "Vec3") -> "Vec3":
        """If other is a Vec3, multiplies elementwise.
        Otherwise multiplies each element by other.
        """
        if isinstance(other, Vec3):
            return Vec3(self.x*other.x, self.y*other.y, self.z*other.z)
        return Vec3(self.x*other, self.y*other, self.z*other)
    
    def __truediv__(self, other: float) -> "Vec3":
        return self * (1.0/other)
    
    def unit(self) -> "Vec3":
        return self / self.mag()
    
    def mag(self) -> float:
        return math.sqrt(self.mag2())
    
    def mag2(self) -> float:
        return self.dot(self)
    
    def dot(self, other: "Vec3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
        
    def cross(self, other: "Vec3") -> "Vec3":
        return Vec3(self.y * other.z - self.z * other.y,
                    self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.x)
        
    def __repr__(self) -> str:
        return f"Vec3(x={self.x}, y={self.y}, z={self.z})"

    def about_zero(self) -> bool:
        s = 1e-8
        return abs(self.x) < s and abs(self.y) < s and abs(self.z) < s


def random_vec(min: float = 0.0, max: float = 1.0) -> Vec3:
    return Vec3(random.uniform(min, max),
                random.uniform(min, max),
                random.uniform(min, max))
    
def random_vec_sphere(radius: float = 1.0) -> Vec3:
    vec = random_vec(-radius, radius)
    while vec.mag2() > radius:
        vec = random_vec(-radius, radius)
    return vec

def random_vec_on_hemisphere(normal: Vec3) -> Vec3:
    vec = random_unit_vec()
    if vec.dot(normal) > 0:
        return vec
    return -vec

def random_unit_vec() -> Vec3:
    return random_vec_sphere().unit()