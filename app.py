import facebook
from groq import Groq

# --- CONFIGURACOES ---
FB_TOKEN = "EAANhJupL2y8BRXZCSEYzZBDqMq2xSE7RfeDd8Kcj4jZArG0DcBBPuqhF2sFQ8NuIx73QSH8z4TBZBexeym8XHi6W4yKqv31SDFAEYnVtwNd0PX5cduA7XHN669ZCbnM4pz96qICbWkwKpigNkuzF8CfgRSiCZAKztrc7iY4Xl8QM7yOHlnFnnwt6bjBqlogHlfH2fvIPc14xnrh2dmB9ZAZBO731HQrAmgXR2z9MAJr8qfguCPoFwPxg8OjKMwb7tN2zFHBR1z70MUcZACj3Cmm1RsiMZD"
GROQ_KEY = "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"

def iniciar_conector():
    try:
        # Conexao Facebook
        fb = facebook.GraphAPI(access_token=FB_TOKEN)
        user = fb.get_object('me')
        print(f"\n✅ SUCESSO: Conectado como {user['name']}!")
        
        # Conexao IA (Modelo Atualizado)
        ai = Groq(api_key=GROQ_KEY)
        
        # Teste de analise
        chat = ai.chat.completions.create(
            messages=[{"role": "user", "content": "Dê uma dica curta para anúncios de manutenção residencial no Facebook."}],
            model="llama-3.3-70b-versatile",
        )
        print(f"\n🤖 DICA DA IA: {chat.choices.message.content}")

    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    iniciar_conector()
