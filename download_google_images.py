#!/usr/bin/env python3
"""
Script para baixar imagens do Google Images e garantir que só imagens válidas sejam salvas.
"""
import requests
import os
import argparse
import re
from pathlib import Path
from urllib.parse import urlparse, quote_plus
from PIL import Image
import hashlib

def download_image(url, folder, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, stream=True, timeout=10)
        response.raise_for_status()
        filepath = os.path.join(folder, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return filepath
    except Exception as e:
        print(f"Erro ao baixar {filename}: {e}")
        return None

def is_valid_image(filepath):
    try:
        with Image.open(filepath) as img:
            img.verify()
        return True
    except Exception:
        return False

def search_google_images(search_term, count=20):
    print(f"🔍 Buscando imagens de '{search_term}' no Google...")
    search_url = f"https://www.google.com/search?q={quote_plus(search_term)}&tbm=isch&tbs=isz:l"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        image_urls = []
        patterns = [
            r'https://[^"\s]*\.(?:jpg|jpeg|png|webp)',
            r'https://[^"\s]*\.googleusercontent\.com[^"\s]*',
            r'https://[^"\s]*\.gstatic\.com[^"\s]*'
        ]
        for pattern in patterns:
            matches = re.findall(pattern, response.text, re.IGNORECASE)
            image_urls.extend(matches)
        unique_urls = list(dict.fromkeys(image_urls))[:count]
        print(f"✅ Encontradas {len(unique_urls)} URLs de imagens")
        return unique_urls
    except Exception as e:
        print(f"❌ Erro ao buscar imagens: {e}")
        return []

def download_and_validate_images(urls, search_term, folder="downloaded_images", count=20):
    Path(folder).mkdir(exist_ok=True)
    downloaded = 0
    i = 3  # Ignorar as 3 primeiras imagens
    total_urls = len(urls)
    hashes = set()
    while downloaded < count and i < total_urls:
        url = urls[i]
        ext = 'jpg'
        if '.png' in url: ext = 'png'
        elif '.webp' in url: ext = 'webp'
        filename = f"{search_term}_{downloaded+1:03d}.{ext}"
        print(f"📥 Baixando {filename}")
        filepath = download_image(url, folder, filename)
        if filepath and is_valid_image(filepath):
            # Verificar duplicidade por hash
            with open(filepath, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in hashes:
                os.remove(filepath)
                print(f"⚠️ Imagem duplicada, deletada!")
            else:
                hashes.add(file_hash)
                downloaded += 1
                print(f"✅ Imagem válida!")
        else:
            if filepath:
                os.remove(filepath)
            print(f"❌ Imagem inválida, deletada!")
        i += 1
    print(f"\n🎉 Download concluído! {downloaded} imagens válidas e únicas em '{folder}'")

def main():
    parser = argparse.ArgumentParser(description="Baixa imagens do Google Images e salva só as válidas.")
    parser.add_argument("search_term", help="Termo para buscar imagens")
    parser.add_argument("-c", "--count", type=int, default=20, help="Número de imagens para baixar (padrão: 20)")
    parser.add_argument("-f", "--folder", default="downloaded_images", help="Pasta para salvar as imagens (padrão: downloaded_images)")
    args = parser.parse_args()
    print(f"🚀 Iniciando download de {args.count} imagens de '{args.search_term}'")
    urls = search_google_images(args.search_term, args.count * 3)  # Buscar mais URLs para compensar inválidas
    if urls:
        download_and_validate_images(urls, args.search_term, args.folder, args.count)
    else:
        print("❌ Nenhuma imagem encontrada")

if __name__ == "__main__":
    main() 