import redis
import hashlib
import random
r = redis.Redis(host='localhost', port=6379, decode_responses=True) 
r.set('mykey','helloworld',10)


print(len(hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()))
print(hashlib.md5(str(random.getrandbits(256)).encode('utf-8')).hexdigest())


