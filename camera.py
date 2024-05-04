from hittable_list import HittableList
from vec3 import Vec3, random_vec_on_hemisphere, random_unit_vec
from ray import Ray
from ppm import PPM
from interval import Interval
import random
import math

def sample_square():
    return Vec3(random.uniform(-0.5, 0.5),
                random.uniform(-0.5, 0.5),
                0)

class Camera:
    def __init__(self,
                 img,
                 pos=Vec3(0, 0, 0),
                 image_width=400,
                 aspect_ratio=16.0/9.0,
                 focal_length=1.0,
                 viewport_height=2.0,
                 samples=15,
                 max_bounces=10):
        self.pos = pos
        
        self.samples = samples
        
        self.image_width = image_width
        self.aspect_ratio = aspect_ratio
        self.image_height = int(image_width / aspect_ratio)
        self.focal_length = focal_length
        
        self.max_bounces = max_bounces
        
        self.img = PPM(img, self.image_width, self.image_height)

        self.viewport_height = viewport_height
        self.viewport_width = viewport_height * (self.image_width/self.image_height)

        self.camera_center = pos

        self.viewport_u = Vec3(self.viewport_width, 0, 0)
        self.viewport_v = Vec3(0, -self.viewport_height, 0)

        self.pixel_delta_u = self.viewport_u / self.image_width
        self.pixel_delta_v = self.viewport_v / self.image_height

        self.viewport_upper_left = pos - Vec3(0, 0, focal_length) \
            - self.viewport_u/2 - self.viewport_v/2

        self.pixel00_loc = self.viewport_upper_left + \
            0.5*(self.pixel_delta_u + self.pixel_delta_v)

        if self.image_height < 1:
            self.image_height = 1

        
    def render(self, world):
        for j in range(self.image_height):
            for i in range(self.image_width):
                color = Vec3(0, 0, 0)
                
                for _ in range(self.samples):
                    ray = self.get_ray(i, j)
                    color += self.ray_color(ray, world)
                
                color /= self.samples
                self.img.write(color)
        self.img.close()
        
    def get_ray(self, i, j):
        offset = sample_square()
        
        pixel_sample = self.pixel00_loc \
            + ((i + offset.x) * self.pixel_delta_u) \
            + ((j + offset.y) * self.pixel_delta_v)
            
        ray_origin = self.pos
        ray_dir = pixel_sample - ray_origin
        
        return Ray(ray_origin, ray_dir)
    
    def ray_color(self, ray, world, bounces=None):
        if bounces is None:
            bounces = self.max_bounces
        if bounces <= 0:
            return Vec3(0, 0, 0)

        rec = world.hit(ray, Interval(0.01, float("inf")))
        if rec is not None:
            scattered, attenuation = rec.mat.scatter(ray, rec)
            return attenuation * self.ray_color(scattered, world, bounces-1)

        a = (ray.direction.unit().y + 1) * 0.5
        return (1-a)*Vec3(1.0, 1.0, 1.0) + a*Vec3(0.5,0.7,1.0)
