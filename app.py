import facebook
from groq import Groq

# --- CONFIGURAÇÕES ---
# 1. Gere um NOVO Token no Facebook e cole aqui entre as aspas
FB_TOKEN = "EAANhJupL2y8BRXZCSEYzZBDqMq2xSE7RfeDd8Kcj4jZArG0DcBBPuqhF2sFQ8NuIx73QSH8z4TBZBexeym8XHi6W4yKqv31SDFAEYnVtwNd0PX5cduA7XHN669ZCbnM4pz96qICbWkwKpigNkuzF8CfgRSiCZAKztrc7iY4Xl8QM7yOHlnFnnwt6bjBqlogHlfH2fvIPc14xnrh2dmB9ZAZBO731HQrAmgXR2z9MAJr8qfguCPoFwPxg8OjKMwb7tN2zFHBR1z70MUcZACj3Cmm1RsiMZD"
GROQ_KEY = "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"

def analisar_ads():
    try:
        # Conecta ao Facebook
        fb = facebook.GraphAPI(access_token=FB_TOKEN)
        
        # Busca suas campanhas reais
        contas = fb.get_connections('me', 'adaccounts')
        if not contas['data']:
            print("❌ Erro: Nenhuma conta de anúncios encontrada.")
            return
            
        id_conta = contas['data'][0]['id']
        campanhas = fb.get_connections(id_conta, 'campaigns', fields='name,status,objective')
        
        # Conecta à IA para analisar os dados
        ai = Groq(api_key=GROQ_KEY)
        prompt = f"Como especialista em Ads, analise estas campanhas da MS Manutenção e sugira 3 melhorias: {campanhas['data']}"
        
        resposta = ai.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )

        print(f"\n✅ CONECTADO À CONTA: {id_conta}")
        print("\n--- ANÁLISE ESTRATÉGICA DA IA ---")
        print(resposta.choices.message.content)

    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    analisar_ads()
