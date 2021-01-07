from abc import ABC
import pendulum
import redis


class CacheBase(ABC):
    def __init__(self):
        self.r = redis.Redis(port=6379)

    def put(self):
        pass
        
    # def get(self, item):
    #     pass

    def exists(self, id):
        return self.r.exists(id)


class ProjectCache(CacheBase):
    def put(self):
        self.r.set("last_call", pendulum.now('UTC').format('YYYY-MM-DD HH:mm:ss'))

    # def get(self, item="last_call"):
    #     self.r.get(item)
