import redis

def main():
    # Créer une connexion à Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Définir une clé
    r.set('nom', 'kheir')

    # Obtenir une clé
    print(r.get('nom'))

    # Créer une liste
    r.lpush('lists:shopping', 'milk', 'bread')

    # Obtenir tous les éléments d'une liste
    print(r.lrange('lists:shopping', 0, -1))

    # Créer un set
    r.sadd('tags:post', 'redis', 'cluster')

    # Obtenir tous les éléments d'un set
    print(r.smembers('tags:post'))

    # Créer un hash
    r.hset('user:profile', mapping={'name': 'Kheir', 'age': 23})

    # Obtenir tous les éléments d'un hash
    print(r.hgetall('user:profile'))

if __name__ == "__main__":
    main()