import facebook
from groq import Groq

# --- CONFIGURACOES ---
FB_TOKEN = "EAANhJupL2y8BRT36GD3JOUY5NJZAv33PllJDZCY6UzTPerfXyPP2RW5LEy0gqlXEQWnRA5DpCt4LbIUwnEiw1MnqDdZBdxiUgoOAM48PDUZAX9xDIV5JsAEoTTkOdHJysz5qevcwWKYZAr7hwhN3w5XwZBA0SlUJ0FwpQHefWcCe78a8K4VZCGxAKCZAgIW295t8FZAFJ8WWo8XpJIVPA7wUOvgMQkH3POk4dupOf7kcQGJBAaZAGlZBKEAZA4ZCTR5bdVNVsLepkZBto4XMTIsRrzAqYzXgcZD"
GROQ_KEY = "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"

def iniciar_conector():
    try:
        # Conexao Facebook
        fb = facebook.GraphAPI(access_token=FB_TOKEN)
        user = fb.get_object('me')
        print(f"\n✅ SUCESSO: Conectado como {user['name']}!")
        
        # Conexao IA (Modelo Atualizado)
        ai = Groq(api_key=GROQ_KEY)
        
        # Teste de conversa
        chat = ai.chat.completions.create(
            messages=[{"role": "user", "content": "Me dê uma dica rápida de marketing para a MS Manutenção residencial."}],
            model="llama-3.3-70b-versatile",
        )
        print(f"\n🤖 IA RESPONDE: {chat.choices.message.content}")

    except Exception as e:
        print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    iniciar_conector()
