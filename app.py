import facebook
from groq import Groq

# --- CONFIGURAÇÕES ---
FB_TOKEN = "EAANhJupL2y8BRTuAKAxqXxgZCGUN46HZATwZB2vUI1CkTGN2nIXxCZAspMAYZBxXIXJuXjIkCZAm77QdEM4XtAmZC0jTrr2YQXIbkF6dT3tZBZB8ElCZCsAphQXcvqIBi7BvZC7pNMXuwnH3GjUPz9I9Kmij8pr6hKBmiUqGYLIQ1LcuSKZCjE8egTgXW7uGHCIKIyQHkWY5tnAnxNxdFptrklBG6Jk8mTqEoaFh1nTEnOLi2AeYcri66Nq5l3bweiUNNEZBXr2YHKRdafNJzG5D60QZAkVwZDZD"
GROQ_KEY = "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"

# --- CONEXÃO ---
def iniciar_conector():
    try:
        # 1. Conecta ao Facebook
        graph = facebook.GraphAPI(access_token=FB_TOKEN)
        perfil = graph.get_object('me')
        
        # 2. Conecta à IA (Groq)
        client = Groq(api_key=GROQ_KEY)
        
        print(f"Sistemas ativos para: {perfil['name']}")
        print("Aguardando comandos para analisar seus anúncios...")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    iniciar_conector()
