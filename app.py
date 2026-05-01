import facebook
from groq import Groq

# --- CONFIGURACOES ---
FB_TOKEN = "EAANhJupL2y8BRXZCSEYzZBDqMq2xSE7RfeDd8Kcj4jZArG0DcBBPuqhF2sFQ8NuIx73QSH8z4TBZBexeym8XHi6W4yKqv31SDFAEYnVtwNd0PX5cduA7XHN669ZCbnM4pz96qICbWkwKpigNkuzF8CfgRSiCZAKztrc7iY4Xl8QM7yOHlnFnnwt6bjBqlogHlfH2fvIPc14xnrh2dmB9ZAZBO731HQrAmgXR2z9MAJr8qfguCPoFwPxg8OjKMwb7tN2zFHBR1z70MUcZACj3Cmm1RsiMZD"
GROQ_KEY = "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"

def iniciar_conector():
    try:
        # Conecta ao Facebook
        fb = facebook.GraphAPI(access_token=FB_TOKEN)
        usuario = fb.get_object('me')
        
        # Conecta à IA (Groq)
        ai = Groq(api_key=GROQ_KEY)
        
        print(f"\n✅ SUCESSO: Conectado como {usuario['name']}")
        
        # Pergunta de teste para a IA analisar seus anúncios
        chat = ai.chat.completions.create(
            messages=[{"role": "user", "content": "Dê uma dica estratégica para anúncios de manutenção residencial no Facebook Ads."}],
            model="llama3-8b-8192",
        )
        print(f"\n🤖 IA: {chat.choices.message.content}")

    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    iniciar_conector()
