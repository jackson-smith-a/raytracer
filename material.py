from vec3 import Vec3, random_unit_vec
from ray import Ray

class Material:
    def scatter(self, ray, rec):
        return None
    
class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo
        
    def scatter(self, ray, rec):
        scatter_direction = rec.normal + random_unit_vec()
        
        if scatter_direction.about_zero():
            scatter_direction = rec.normal
        
        scattered = Ray(rec.pos, scatter_direction)
        return (scattered, self.albedo)

class Metal(Material):
    def __init__(self, albedo, fuzz):
        self.albedo = albedo
        self.fuzz = fuzz
        
    def scatter(self, ray, rec):
        reflected = ray.direction.reflect(rec.normal)
        reflected = reflected.unit() + (self.fuzz * random_unit_vec())
        while reflected.dot(rec.normal) < 0.0:
            reflected = reflected.unit() + (self.fuzz * random_unit_vec())
        scatter = Ray(rec.pos, reflected)
        return (scatter, self.albedo)
