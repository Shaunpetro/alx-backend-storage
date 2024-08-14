#!/usr/bin/env python3
"""module that declares a redis class & methods"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of cache class are called"""
    key = method.__qualname__
    
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap the decorated func & return wrapper'''
        self._redis_.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''stores the hiostory of I&O for a particular func'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap decorated func & return the wrapper'''
        input = str(args)
        self._redis_.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    '''display the history of calls of a part func'''
    r = redis.Redis()
    func_name = fn.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format()(func_name, inp, outp))


class Cache:
    '''declares cache redis class'''
    def __init__(self):
        '''upon init to store an instance & flush'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''takes a data arg & returns a str'''
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''convert the data back to desired format'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''parametize cache.get with the right conversion fn'''
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        '''parametize cache.get eith the right conversion fn'''
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
