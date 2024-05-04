import math
import time
from view import view
from vec3 import Vec3
from ray import Ray
from hittable_list import HittableList
from hittable import Sphere, Hittable
from camera import Camera
from material import Lambertian, Metal
from multiprocessing import Process
from mixer import mix

def gen_image(image: str, world: Hittable):
    cam = Camera(image, samples=20, image_width=400)

    cam.render(world)

PROCESSES = 5
if __name__ == "__main__":
    world = HittableList()

    material_ground = Lambertian(Vec3(0.8, 0.8, 0.0))
    material_center = Lambertian(Vec3(0.1, 0.2, 0.5))
    material_left = Metal(Vec3(0.8, 0.8, 0.8), 0.3)
    material_right = Metal(Vec3(0.8, 0.6, 0.2), 0.0)

    material_front = Metal(Vec3(1.0, 0.5, 0.5), 1.0)

    world.add(Sphere(Vec3(0, -100.5, -1), 100, material_ground))
    world.add(Sphere(Vec3(0.0, 0.0, -1.2), 0.5, material_center))
    world.add(Sphere(Vec3(-1.0,0.0,-1.0), 0.5, material_left))
    world.add(Sphere(Vec3(1.0,0.0,-1.0), 0.5, material_right))

    world.add(Sphere(Vec3(0.0, 0.3, -0.5), 0.1, material_front))

    start = time.time()
    procs = []
    for i in range(PROCESSES):
        procs.append(Process(target=gen_image, args=(f"image{i}.ppm",world)))
        procs[-1].start()
        
    for proc in procs:
        proc.join()
        
    print("Elapsed:", time.time() - start, "seconds")
        
    images = []
    for i in range(PROCESSES):
        images.append(f"image{i}.ppm")
    
    mix(images, "image.ppm")
    view("image.ppm")
