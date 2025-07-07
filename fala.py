import requests
from playsound import playsound
import tempfile
import os

# Chave da API ElevenLabs
ELEVEN_API_KEY = 'sk_045ca4d516963bb6b954ba580bf9d29d4cb93e02d5b6e1b1'

# Voice ID padrão da ElevenLabs (pode ser alterado)
# DEFAULT_VOICE_ID = 'cgSgspJ2msm6clMCkdW9'  # Geralmente "Rachel" ou "English". Troque se quiser outro.

VOICES = {
    "Aria": "9BWtsMINqrJLrRacOk9x",
    "Sarah": "EXAVITQu4vr4xnSDxMaL",
    "Laura": "FGY2WhTYpPnrIDTdsKH5",
    "Charlie": "IKne3meq5aSn9XLyUdCD",
    "George": "JBFqnCBsd6RMkjVDRZzb",
    "Callum": "N2lVS1w4EtoT3dr4eOWO",
    "River": "SAz9YHcvj6GT2YYXdXww",
    "Liam": "TX3LPaxmHKxFdv7VOQHJ",
    "Charlotte": "XB0fDUnXU5powFXDhCwa",
    "Alice": "Xb7hH8MSUJpSbSDYk0k2",
    "Matilda": "XrExE9yKIg1WjnnlVkGX",
    "Will": "bIHbv24MWmeRgasZH58o",
    "Jessica": "cgSgspJ2msm6clMCkdW9",
    "Eric": "cjVigY5qzO86Huf0OWal",
    "Chris": "iP95p4xoKVk53GoZ742B",
    "Brian": "nPczCjzI2devNBz1zQrb",
    "Daniel": "onwK4e9ZLuTAKqWW03F9",
    "Lily": "pFZP5JQG7iQjIQuC4Bku",
    "Bill": "pqHfZKP75CvOlQylNhV4",
}

DEFAULT_VOICE = 'Jessica'

def falar(texto, voice=DEFAULT_VOICE, model_id='eleven_multilingual_v2', lang='pt'):
    """
    Gera o áudio do texto usando ElevenLabs e toca automaticamente.
    :param texto: Texto a ser falado
    :param voice_id: ID da voz ElevenLabs
    :param model_id: Modelo ElevenLabs
    :param lang: Idioma (padrão: 'pt')
    """
    voice_id = VOICES[voice]
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    headers = {
        'xi-api-key': ELEVEN_API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
    }
    data = {
        'text': texto,
        'model_id': model_id,
        'voice_settings': {
            'stability': 0.5,
            'similarity_boost': 0.8
        }
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tf:
        tf.write(response.content)
        tf.close()
        try:
            playsound(tf.name)
        finally:
            os.remove(tf.name)


if __name__ == '__main__':
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Converte texto em fala usando ElevenLabs')
    parser.add_argument('-v', '--voice', default=DEFAULT_VOICE, 
                       choices=list(VOICES.keys()),
                       help=f'Voz a ser usada (padrão: {DEFAULT_VOICE})')
    parser.add_argument('texto', nargs='+', help='Texto a ser falado')
    
    args = parser.parse_args()
    
    texto = ' '.join(args.texto)
    falar(texto, voice=args.voice)
