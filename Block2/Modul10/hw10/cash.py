import random
import redis
from time import sleep


class PyLRUcache():
    def __init__(self, max_size=5, life_time=40):
        self._r = redis.Redis(host='localhost')
        self._max_size = max_size
        self._life_time = life_time

    def to_cache(self, key, data):
        print(len(self._r.keys()))
        if len(self._r.keys()) >= self._max_size:
            s_keys = sorted(self._r.keys(), key=self._r.ttl, reverse=True)
            self._r.delete(s_keys[-1])
        self._r.set(key, data)
        self._r.expire(key, self._life_time)

    def from_cache(self, key):
        data = self._r.get(key)
        if data:
            self._r.expire(key, self._life_time)
        return data

    def all_keys(self):
        s_keys = sorted(self._r.keys(), key=self._r.ttl, reverse=True)
        return s_keys


if __name__ == '__main__':
    c = PyLRUcache()
    for item in range(0, 10):
        c.to_cache(item, f'data{item}')
        sleep(1)
        print(c.from_cache(random.randint(0, 10)))
    print(c.all_keys())