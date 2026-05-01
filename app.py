import facebook
from groq import Groq

# --- CONFIGURACOES ---
FB_TOKEN = "EAANhJupL2y8BRbcIkwRPE3pmmLWeFHpTaHiy0Jofl4ve3jYj1YxGEoUrCaQjK0q9xDhoE5GDeiMmfzKX4dxPAlxdIHZBNZBj4b9DEr342YXeztYudkZA20vKb3EyIlXCgvNyZAnCkaBFPkgRKJuqWZA7nS0mjxRcJZCLYv5TX7GX0MGINTw0pEN4PCAByRgpOjJIIzCoWO8yLyA63fOVg0LWwCdosTwYWvAQMfx0v2vdWXN1MCcTT178CVlRAvbontUMv9IuJCMK5jab6nZAbho2MoZD"
GROQ_KEY = "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"

def iniciar_conector():
    try:
        # 1. Conexao Facebook
        fb = facebook.GraphAPI(access_token=FB_TOKEN)
        user = fb.get_object('me')
        print(f"\n✅ SUCESSO: Conectado como {user['name']}!")
        
        # 2. Conexao IA
        ai = Groq(api_key=GROQ_KEY)
        
        chat = ai.chat.completions.create(
            messages=[{"role": "user", "content": "Me dê uma dica rápida de marketing para a MS Manutenção residencial no Facebook."}],
            model="llama-3.3-70b-versatile",
        )
        
        # --- CORREÇÃO AQUI: Adicionado o [0] para acessar a resposta corretamente ---
        resposta_ia = chat.choices[0].message.content
        print(f"\n🤖 IA RESPONDE: {resposta_ia}")

    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    iniciar_conector()
