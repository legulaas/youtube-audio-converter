"""
YouTube Audio Converter
=======================
Script para download e conversão de vídeos do YouTube para arquivos de áudio MP3.

Autor: Matheus Fragoso
Repositório: https://github.com/legulaas/youtube-audio-converter
"""

import yt_dlp
import os


def baixar_audio(url, pasta_destino='.', callback_status=None):
    """
    Baixa o áudio de um vídeo do YouTube e converte para MP3.
    
    Esta função utiliza yt-dlp para fazer o download do melhor stream de áudio
    disponível e FFmpeg para converter o arquivo para formato MP3 com qualidade
    máxima (320 kbps).
    
    Args:
        url (str): URL do vídeo do YouTube a ser baixado
        pasta_destino (str, optional): Diretório onde o arquivo será salvo.
                                       Padrão é o diretório atual ('.')
        callback_status (function, optional): Função de callback para atualizações de status
    
    Returns:
        None
    
    Raises:
        Exception: Se houver erro no download ou conversão do áudio
        
    Exemplo:
        >>> baixar_audio("https://www.youtube.com/watch?v=example")
        🔎 Processando vídeo...
        ✅ Áudio baixado com sucesso!
    """
    def update_status(message):
        """Helper para atualizar status."""
        if callback_status:
            callback_status(message)
        else:
            print(message)
    
    try:
        update_status("🔎 Processando vídeo...")

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
            
            # Controla verbosidade baseado se há callback
            'quiet': callback_status is not None,
            
            # Hook para progresso personalizado quando há callback
            'progress_hooks': [lambda d: progress_hook(d, update_status)] if callback_status else [],
        }

        # Realiza o download usando as configurações definidas
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            update_status("✅ Áudio baixado com sucesso!")

    except Exception as e:
        # Captura e exibe erros que possam ocorrer
        update_status(f"❌ Erro: {e}")
        raise  # Re-levanta a exceção para tratamento na GUI


def progress_hook(d, callback):
    """
    Hook de progresso para yt-dlp.
    
    Args:
        d (dict): Dados do progresso do yt-dlp
        callback (function): Função para atualizar status
    """
    if d['status'] == 'downloading':
        if 'total_bytes' in d and d['total_bytes']:
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            callback(f"📥 Baixando: {percent:.1f}% ({d['downloaded_bytes']} / {d['total_bytes']} bytes)")
        elif '_percent_str' in d:
            callback(f"📥 Baixando: {d['_percent_str']}")
        else:
            callback("📥 Baixando...")
    elif d['status'] == 'finished':
        callback(f"🔄 Convertendo para MP3: {os.path.basename(d['filename'])}")
    elif d['status'] == 'error':
        callback(f"❌ Erro no download: {d.get('error', 'Erro desconhecido')}")


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
