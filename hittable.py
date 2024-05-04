import math
from ray import Ray
from interval import Interval

class HitRecord:
    def __init__(self, pos, normal, t, ff, mat):
        self.pos = pos
        self.normal = normal
        self.t = t
        self.ff = ff
        self.mat = mat
        
class Hittable:
    def hit(self, ray, ray_t):
        return None
    
class Sphere(Hittable):
    def __init__(self, pos, radius, mat):
        self.pos = pos
        self.radius = radius
        self.mat = mat
        
    def hit(self, ray, ray_t):
        oc = self.pos - ray.origin
        a = ray.direction.mag2()
        b = ray.direction.dot(oc)
        c = oc.mag2() - self.radius**2
        
        disc = b**2 - a*c
        
        if disc < 0:
            return None
        
        sqrtd = math.sqrt(disc)
        
        root = (b - sqrtd) / a
        if not ray_t.surrounds(root):
            root = (b + sqrtd) / a
            if not ray_t.surrounds(root):
                return None
            
        pos = ray.at(root)
        normal = (pos - self.pos) / self.radius
        
        ff = True
        if ray.direction.dot(normal) > 0:
            ff = False
            normal = -normal
    
        return HitRecord(pos, normal, root, ff, self.mat)