import requests
import json

# Chave da API ElevenLabs (mesma do fala.py)
ELEVEN_API_KEY = 'sk_045ca4d516963bb6b954ba580bf9d29d4cb93e02d5b6e1b1'

def listar_vozes():
    """
    Lista todas as vozes disponíveis na ElevenLabs e salva em vozes.txt
    """
    url = 'https://api.elevenlabs.io/v1/voices'
    headers = {
        'xi-api-key': ELEVEN_API_KEY,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        vozes = response.json()
        
        # Salvar em arquivo
        with open('vozes.txt', 'w', encoding='utf-8') as f:
            f.write("=== VOZES DISPONÍVEIS NA ELEVENLABS ===\n\n")
            f.write(f"Total de vozes encontradas: {len(vozes['voices'])}\n\n")
            
            for i, voz in enumerate(vozes['voices'], 1):
                f.write(f"{i}. Nome: {voz['name']}\n")
                f.write(f"   ID: {voz['voice_id']}\n")
                f.write(f"   Categoria: {voz.get('category', 'N/A')}\n")
                f.write(f"   Descrição: {voz.get('description', 'Sem descrição')}\n")
                f.write(f"   Labels: {voz.get('labels', {})}\n")
                f.write(f"   Disponível para: {voz.get('available_for_tiers', [])}\n")
                f.write("-" * 50 + "\n")
        
        print(f"✅ {len(vozes['voices'])} vozes listadas e salvas em 'vozes.txt'")
        
        # Mostrar algumas vozes no terminal também
        print("\n📋 Primeiras 10 vozes:")
        for i, voz in enumerate(vozes['voices'][:100], 1):
            print(f"{i}. {voz['name']} (ID: {voz['voice_id']})")
        
        return vozes['voices']
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar com a API: {e}")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

if __name__ == '__main__':
    print("🔍 Buscando vozes disponíveis na ElevenLabs...")
    vozes = listar_vozes()
    
    if vozes:
        print(f"\n✅ Arquivo 'vozes.txt' criado com sucesso!")
        print("📁 Abra o arquivo para ver todas as vozes disponíveis.") 