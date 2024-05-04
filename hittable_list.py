from hittable import Hittable, HitRecord
from interval import Interval

class HittableList(Hittable):
    def __init__(self):
        self.objects = []
        
    def clear(self):
        self.objects.clear()
        
    def add(self, obj):
        self.objects.append(obj)
        
    def hit(self, r, ray_t):
        best_rec = None
        closest = ray_t.max_value
        
        for obj in self.objects:
            rec = obj.hit(r, Interval(ray_t.min_value, closest))
            if rec is not None:
                closest = rec.t
                best_rec = rec
        return best_rec