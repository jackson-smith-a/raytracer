import math
from ray import Ray
from interval import Interval
from vec3 import Vec3

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from material import Material

class HitRecord:
    def __init__(self,
                 pos: Vec3,
                 normal: Vec3,
                 t: float,
                 ff: bool,
                 mat: "Material"):
        self.pos = pos
        self.normal = normal
        self.t = t
        self.ff = ff
        self.mat = mat
        
class Hittable:
    def hit(self, ray: Ray, ray_t: Interval):
        return None
    
class Sphere(Hittable):
    def __init__(self, pos: Vec3, radius: float, mat: "Material"):
        self.pos = pos
        self.radius = radius
        self.mat = mat
        
    def hit(self, ray: Ray, ray_t: Interval) -> HitRecord:
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
