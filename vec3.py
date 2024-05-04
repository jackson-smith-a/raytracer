import math
import random

def random_vec(min=0, max=1):
    return Vec3(random.uniform(min, max),
                random.uniform(min, max),
                random.uniform(min, max))
    
def random_vec_sphere(radius=1):
    vec = random_vec(-radius, radius)
    while vec.mag2() > radius:
        vec = random_vec(-radius, radius)
    return vec

def random_vec_on_hemisphere(normal):
    vec = random_unit_vec()
    if vec.dot(normal) > 0:
        return vec
    return -vec

def random_unit_vec():
    return random_vec_sphere().unit()

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def reflect(self, other):
        return self - 2 * self.dot(other) * other
        
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    
    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x*other.x, self.y*other.y, self.z*other.z)
        return Vec3(self.x*other, self.y*other, self.z*other)
    
    def __rmul__(self, other):
        return Vec3(self.x*other, self.y*other, self.z*other)
    
    def __truediv__(self, other):
        return self * (1.0/other)
    
    def unit(self):
        return self / self.mag()
    
    def mag(self):
        return math.sqrt(self.mag2())
    
    def mag2(self):
        return self.dot(self)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
        
    def cross(self, other):
        return Vec3(self.y * other.z - self.z * other.y,
                    self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.x)
        
    def __repr__(self):
        return f"Vec3(x={self.x}, y={self.y}, z={self.z})"

    def about_zero(self):
        s = 1e-8
        return abs(self.x) < s and abs(self.y) < s and abs(self.z) < s
