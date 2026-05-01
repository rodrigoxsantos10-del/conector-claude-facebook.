import facebook
from groq import Groq

# --- CONFIGURAÇÕES ---
FB_TOKEN = "EAANhJupL2y8BRaTvv7oCZADxZBMZCoxxOiQnpZAhxaiyyd9IN6dRiqxoimOHV4CaaHdbaNGbFuZC9hwDZCZCa7AqIYvIWHdzB9GPggJlXjeGIUZBD68WZCEHPfdkfAosXKpEfV4EjXVM2hYElXI0dsFCSyNq9w2BsORbh55caSZAHsSxWai9ChDVfUlh68mo8LhHZBYbHyCV5anJSSQ3Jvlm4GVuRQ78RDcLZBy8XYOGOtQdOKTCCOyI7htnWZCzcVqTs4SkaPJ0M869wcmJZAHSExG7rUxAZDZD"
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
