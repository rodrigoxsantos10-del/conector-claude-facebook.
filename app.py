import facebook

# Cole o seu TOKEN longo entre as aspas abaixo
TOKEN_ACESSO = "EAANhJupL2y8BRTuAKAxqXxgZCGUN46HZATwZB2vUI1CkTGN2nIXxCZAspMAYZBxXIXJuXjIkCZAm77QdEM4XtAmZC0jTrr2YQXIbkF6dT3tZBZB8ElCZCsAphQXcvqIBi7BvZC7pNMXuwnH3GjUPz9I9Kmij8pr6hKBmiUqGYLIQ1LcuSKZCjE8egTgXW7uGHCIKIyQHkWY5tnAnxNxdFptrklBG6Jk8mTqEoaFh1nTEnOLi2AeYcri66Nq5l3bweiUNNEZBXr2YHKRdafNJzG5D60QZAkVwZDZD"

def testar_conexao():
    try:
        graph = facebook.GraphAPI(access_token=TOKEN_ACESSO)
        perfil = graph.get_object('me')
        print(f"Sucesso! Conectado como: {perfil['name']}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    testar_conexao()
