from connection import connectMongo, connectRedis
import uuid

mongoDatabase = connectMongo()
mongoCollection = mongoDatabase["vendedores"]

redisDatabase = connectRedis()

def login():
    while True:
        print("\n========== LOGIN ==========")

        email = input("Email: ")

        usuario = mongoCollection.find_one({
            "email": email
        })

        if not usuario:
            print("\nEmail inválido.")
            continue

        token = str(uuid.uuid4())

        redisDatabase.set(
            f"sessao:{token}",
            str(usuario["_id"]),
            ex=60
        )

        print("\nLogin realizado com sucesso!")

        return token


def verificarSessao(token):
    sessao = redisDatabase.get(f"sessao:{token}")

    if sessao is None:
        print("\nSessão expirada!")
        return False

    return True