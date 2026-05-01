import facebook
from groq import Groq

# --- CONFIGURAÇÕES ---
# Token que você acabou de gerar
FB_TOKEN = "EAANhJupL2y8BRaTvv7oCZADxZBMZCoxxOiQnpZAhxaiyyd9IN6dRiqxoimOHV4CaaHdbaNGbFuZC9hwDZCZCa7AqIYvIWHdzB9GPggJlXjeGIUZBD68WZCEHPfdkfAosXKpEfV4EjXVM2hYElXI0dsFCSyNq9w2BsORbh55caSZAHsSxWai9ChDVfUlh68mo8LhHZBYbHyCV5anJSSQ3Jvlm4GVuRQ78RDcLZBy8XYOGOtQdOKTCCOyI7htnWZCzcVqTs4SkaPJ0M869wcmJZAHSExG7rUxAZDZD"

# Sua chave do Groq (IA Gratuita)
GROQ_KEY = "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"

def iniciar_conector():
    try:
        # Conexão com Facebook
        graph = facebook.GraphAPI(access_token=FB_TOKEN)
        perfil = graph.get_object('me')
        
        # Conexão com a IA
        client = Groq(api_key=GROQ_KEY)
        
        print(f"\n✅ CONECTADO: Olá, {perfil['name']}!")
        print("🤖 IA PRONTA: Estou pronta para analisar os anúncios da MS Manutenção.")
        
        # Teste de conversa com a IA
        prompt = "Dê uma dica rápida de como melhorar anúncios de manutenção residencial no Facebook."
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        print("\n--- DICA DA IA ---")
        print(completion.choices[0].message.content)
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    iniciar_conector()
