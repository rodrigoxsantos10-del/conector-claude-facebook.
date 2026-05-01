import facebook
from groq import Groq

# --- CONFIGURACOES ---
# 1. Pegue o token novo no Facebook e cole entre as aspas abaixo
FB_TOKEN = "EAANhJupL2y8BRewFFtDQ7Ucky0pCjJXby5ZAlMfG3Us1N2qTljpufnyzZCfQWmwB8vhDckZBUS2ARGei1B0V5DhneZB4kFt2mZBZBqlONZCECQvSlBb2y3Knf41OgXj0PV49YNjZAiycF3CSdkBXJzU8iabBBIB97NA5jqkanCk7yNZBNI7v7QHeyotI5d5aUTbdDDlFJwlV1BsiFcCSlk2Yh43gQHXSNAfXFrOsqdgMk2m9Igza6HZAfbL0yaZBLQFMX8GJ43quoD3qGsvKclSZCGWcFQZDZD"
GROQ_KEY = "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"

def iniciar_conector():
    try:
        # Conexao Facebook
        fb = facebook.GraphAPI(access_token=FB_TOKEN)
        user = fb.get_object('me')
        print(f"\n✅ SUCESSO: Conectado como {user['name']}!")
        
        # Conexao IA
        ai = Groq(api_key=GROQ_KEY)
        
        chat = ai.chat.completions.create(
            messages=[{"role": "user", "content": "Dê uma dica de marketing para a MS Manutenção residencial."}],
            model="llama-3.3-70b-versatile",
        )
        
        # --- CORREÇÃO AQUI: Acessando o item zero da lista ---
        resposta_ia = chat.choices[0].message.content
        print(f"\n🤖 IA RESPONDE: {resposta_ia}")

    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    iniciar_conector()
