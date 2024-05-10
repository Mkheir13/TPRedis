import redis

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)

    r.set('nom', 'kheir')
    print(r.get('nom'))

    r.lpush('lists:shopping', 'milk', 'bread')
    print(r.lrange('lists:shopping', 0, -1))

    r.sadd('tags:post', 'redis', 'cluster')
    print(r.smembers('tags:post'))

    r.hset('user:profile', mapping={'name': 'Kheir', 'age': 23})
    print(r.hgetall('user:profile'))

if __name__ == "__main__":
    main()