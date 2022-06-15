# redis-essentials
Redis Essentials topics 

## Fundamentals of Redis for Caching


Redis, which stands for Remote Dictionary Server, is an open-source in-memory data structure store that can be used as an in-memory key-value database, caching system, and pub/sub message broker.

# installation

We can install redis on kubernetes using the files in kubernetes-manifests folder, I'm using my openshift cluster for my lab tests 


```
oc apply -f deployment.
```


# Fundamentals

Redis is a key-value database, the primitive type is string, I list here some basics commands of redis-cli:

- SET : used to create a key with a single string value 
- MSET: To set multiple values at the same time
- GET:  used to get the value of a single key
- MGET: get the values of multiple keys at the same time
- KEYS: find all keys with a pattern ( Not recommended in production env)
- SCAN: is a cursor-based iterator and only returns a limited number of keys per call
- TTL: TTL command is used to get the remaining time of key expiry in seconds.



## Data types in Redis

- list
- Set
- Sorted set
- hashes
