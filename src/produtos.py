from connection import connectMongo, connectRedis

mongoDatabase = connectMongo()
mongoCollection = mongoDatabase["produtos"]

redisDatabase = connectRedis()

def popularRedisProdutos():
    produtos = list(mongoCollection.find().sort("nome"))

    try:
        for p in produtos:
            redisDatabase.hset(
                f"produto:{p['_id']}",
                mapping={
                    "nome": p["nome"],
                    "preco": p["preco"]
                }
            )
        print()
        print("Redis populado com sucesso!.")
    except Exception as erro:
        print()
        print("Não foi possível popular o Redis.")
        print(erro)

def atualizarMongoProdutos():
    produtos = list(mongoCollection.find().sort("nome"))

    for p in produtos:
        produtosRedis = redisDatabase.hgetall(f"produto:{p['_id']}")

        alteracoes = {}

        if produtosRedis.get("nome") != p.get("nome"):
            alteracoes["nome"] = produtosRedis["nome"]
        
        if produtosRedis.get("preco") != p.get("preco"):
            alteracoes["preco"] = produtosRedis["preco"]

        try:
            if alteracoes:
                mongoCollection.update_one(
                    {"_id": p["_id"]},
                    {"$set": alteracoes}
                )

                print()
                print(f"Produto alterado com sucesso:")
                print()
                
                if produtosRedis.get("nome") != p.get("nome"):
                    print(f"{p['nome']} -> {produtosRedis['nome']}")
                if produtosRedis.get("preco") != p.get("preco"):
                    print(f"{p['preco']} -> {produtosRedis['preco']}")
        except Exception as erro:
            print("Não foi possível alterar o produto.")
            print(erro)