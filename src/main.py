from login import login, verificarSessao
from vendedores import popularRedisVendedores, atualizarMongoVendedores
from produtos import popularRedisProdutos, atualizarMongoProdutos

def menu():
    token = login()

    while True:
        print()
        print("--############### MENU DAORA ###############--")
        print("--## 1 - Popular Redis com vendedores     ##--")
        print("--## 2 - Atualizar Mongo com vendedores   ##--")
        print("--## 3 - Popular Redis com produtos       ##--")
        print("--## 4 - Atualizar Mongo com produtos     ##--")
        print("--##########################################--\n")

        key = input("Digite a opção desejada ('sair' para sair): ")

        if key == '1':
            if verificarSessao(token):
                popularRedisVendedores()
            else:
                token = login()
        elif key == '2':
            if verificarSessao(token):
                atualizarMongoVendedores()
            else:
                token = login()
        elif key == '3':
            if verificarSessao(token):
                popularRedisProdutos()
            else:
                token = login()
        elif key == '4':
            if verificarSessao(token):
                atualizarMongoProdutos()
            else:
                token = login()
        elif key == 'sair':
            break
        else:
            print("Opção inválida!")
menu()