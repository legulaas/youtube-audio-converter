"""
YouTube Audio Converter
=======================
Script para download e conversão de vídeos do YouTube para arquivos de áudio MP3.

Autor: Matheus Fragoso
Repositório: https://github.com/legulaas/youtube-audio-converter
"""

import yt_dlp
import os


def baixar_audio(url, pasta_destino='.'):
    """
    Baixa o áudio de um vídeo do YouTube e converte para MP3.
    
    Esta função utiliza yt-dlp para fazer o download do melhor stream de áudio
    disponível e FFmpeg para converter o arquivo para formato MP3 com qualidade
    máxima (320 kbps).
    
    Args:
        url (str): URL do vídeo do YouTube a ser baixado
        pasta_destino (str, optional): Diretório onde o arquivo será salvo.
                                       Padrão é o diretório atual ('.')
    
    Returns:
        None
    
    Raises:
        Exception: Se houver erro no download ou conversão do áudio
        
    Exemplo:
        >>> baixar_audio("https://www.youtube.com/watch?v=example")
        🔎 Processando vídeo...
        ✅ Áudio baixado com sucesso!
    """
    try:
        print("🔎 Processando vídeo...")

        # Configurações para o yt-dlp
        ydl_opts = {
            # Seleciona o melhor formato de áudio disponível
            'format': 'bestaudio/best',
            
            # Template para o nome do arquivo de saída
            # %(title)s = título do vídeo
            # %(ext)s = extensão do arquivo
            'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
            
            # Pós-processamento: extração e conversão do áudio
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',      # Usa FFmpeg para extrair áudio
                'preferredcodec': 'mp3',           # Converte para MP3
                'preferredquality': '320',         # Qualidade máxima (320 kbps)
            }],
            
            # Exibe informações durante o download
            'quiet': False
        }

        # Realiza o download usando as configurações definidas
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("✅ Áudio baixado com sucesso!")

    except Exception as e:
        # Captura e exibe erros que possam ocorrer
        print(f"❌ Erro: {e}")


def main():
    """
    Função principal que executa o programa.
    
    Solicita ao usuário a URL do vídeo e inicia o processo de download.
    """
    print("=" * 50)
    print("YouTube Audio Converter")
    print("=" * 50)
    print()
    
    # Solicita a URL do vídeo ao usuário
    url_video = input("Cole a URL do vídeo do YouTube: ")
    
    # Valida se o usuário inseriu alguma URL
    if not url_video.strip():
        print("❌ Erro: URL não pode estar vazia!")
        return
    
    # Inicia o processo de download
    baixar_audio(url_video)


if __name__ == "__main__":
    """
    Ponto de entrada do script.
    
    Este bloco garante que main() só será executado quando o script
    for rodado diretamente, não quando for importado como módulo.
    """
    main()
