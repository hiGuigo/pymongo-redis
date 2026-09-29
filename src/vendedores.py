from connection import connectMongo, connectRedis

mongoDatabase = connectMongo()
mongoCollection = mongoDatabase["vendedores"]

redisDatabase = connectRedis()

def popularRedisVendedores():
    vendedores = list(mongoCollection.find().sort("nome"))

    try:
        for v in vendedores:
            redisDatabase.hset(
                f"vendedor:{v['_id']}",
                mapping={
                    "nome": v["nome"],
                    "email": v["email"]
                }
            )
        print()
        print("Redis populado com sucesso!.")
    except Exception as erro:
        print()
        print("Não foi possível popular o Redis.")
        print(erro)

def atualizarMongoVendedores():
    vendedores = list(mongoCollection.find().sort("nome"))

    for v in vendedores:
        vendedoresRedis = redisDatabase.hgetall(f"vendedor:{v['_id']}")

        alteracoes = {}

        if vendedoresRedis.get("nome") != v.get("nome"):
            alteracoes["nome"] = vendedoresRedis["nome"]
        
        if vendedoresRedis.get("email") != v.get("email"):
            alteracoes["email"] = vendedoresRedis["email"]

        try:
            if alteracoes:
                mongoCollection.update_one(
                    {"_id": v["_id"]},
                    {"$set": alteracoes}
                )

                print()
                print(f"Vendedor alterado com sucesso:")
                print()
                
                if vendedoresRedis.get("nome") != v.get("nome"):
                    print(f"{v['nome']} -> {vendedoresRedis['nome']}")
                if vendedoresRedis.get("email") != v.get("email"):
                    print(f"{v['email']} -> {vendedoresRedis['email']}")
        except Exception as erro:
            print("Não foi possível alterar o vendedor.")
            print(erro)