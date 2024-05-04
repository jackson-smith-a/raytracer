from vec3 import Vec3, random_unit_vec
from ray import Ray

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from hittable import HitRecord

class Material:
    def scatter(self, ray: Ray, rec: "HitRecord"):
        return None

class Lambertian(Material):
    def __init__(self, albedo: Vec3):
        self.albedo = albedo
        
    def scatter(self, ray: Ray, rec: "HitRecord") -> tuple[Ray, Vec3]:
        scatter_direction = rec.normal + random_unit_vec()
        
        if scatter_direction.about_zero():
            scatter_direction = rec.normal
        
        scattered = Ray(rec.pos, scatter_direction)
        return (scattered, self.albedo)

class Metal(Material):
    def __init__(self, albedo: Vec3, fuzz: float):
        self.albedo = albedo
        self.fuzz = fuzz
        
    def scatter(self, ray: Ray, rec: "HitRecord") -> tuple[Ray, Vec3]:
        reflected = ray.direction.reflect(rec.normal)
        reflected = reflected.unit() + (self.fuzz * random_unit_vec())
        while reflected.dot(rec.normal) < 0.0:
            reflected = reflected.unit() + (self.fuzz * random_unit_vec())
        scatter = Ray(rec.pos, reflected)
        return (scatter, self.albedo)
