# 🎵 YouTube Audio Converter

Conversor simples e eficiente de vídeos do YouTube para arquivos MP3 de alta qualidade, com **interface gráfica** e **executável standalone**.

## 📋 Descrição

Este projeto permite baixar o áudio de vídeos do YouTube e salvá-los como arquivos MP3 com qualidade máxima (320 kbps). Oferece duas interfaces: linha de comando e interface gráfica intuitiva. Utiliza as bibliotecas `yt-dlp` para download e `FFmpeg` para conversão de áudio.

## ✨ Funcionalidades

- ✅ **Interface gráfica amigável** com tkinter
- ✅ **Executável standalone** (não precisa instalar Python)
- ✅ Download de áudio em alta qualidade (320 kbps)
- ✅ Conversão automática para MP3
- ✅ Interface via linha de comando (modo clássico)
- ✅ Seletor de pasta de destino
- ✅ Barra de progresso e status em tempo real
- ✅ Suporte a diversos formatos de URL do YouTube
- ✅ Nomenclatura automática baseada no título do vídeo
- ✅ Validação de entrada e tratamento de erros

## 🔧 Requisitos

### Dependências Python
- Python 3.6 ou superior
- yt-dlp
- FFmpeg (instalado no sistema)

### Instalação do FFmpeg

#### Windows
1. Baixe o FFmpeg em: https://ffmpeg.org/download.html
2. Extraia o arquivo e adicione a pasta `bin` ao PATH do sistema

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS
```bash
brew install ffmpeg
```

## 📦 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/legulaas/youtube-audio-converter.git
cd youtube-audio-converter
```

2. Instale as dependências Python:
```bash
pip install yt-dlp
```

## 🚀 Uso

### 🖥️ Interface Gráfica (Recomendado)

**Usando o executável (mais simples):**
1. Baixe o arquivo `YouTube Audio Converter.exe` da seção Releases
2. Execute o arquivo (não é necessário instalar Python)
3. Cole a URL do vídeo do YouTube
4. Escolha a pasta de destino
5. Clique em "Baixar Áudio"

**Executando o código Python:**
```bash
python gui.py
```

### 💻 Linha de Comando (Modo Clássico)

Execute o script:
```bash
python main.py
```

Em seguida, cole a URL do vídeo do YouTube quando solicitado:
```
Cole a URL do vídeo do YouTube: https://www.youtube.com/watch?v=exemplo
```

O arquivo MP3 será salvo no mesmo diretório do script com o nome do vídeo.

### 🔧 Uso Programático

Você também pode importar e usar a função em seus próprios scripts:

```python
from main import baixar_audio

# Baixar para o diretório atual
baixar_audio("https://www.youtube.com/watch?v=exemplo")

# Baixar para um diretório específico
baixar_audio("https://www.youtube.com/watch?v=exemplo", pasta_destino="./musicas")

# Com callback de status para interface personalizada
def meu_callback(status):
    print(f"Status: {status}")

baixar_audio(
    "https://www.youtube.com/watch?v=exemplo", 
    pasta_destino="./musicas",
    callback_status=meu_callback
)
```

## 🖼️ Screenshots

### Interface Gráfica
- Campo para URL do YouTube
- Seletor de pasta de destino  
- Barra de progresso com status em tempo real
- Botões para limpar campos e abrir pasta
- Área de log com informações detalhadas

### Recursos da GUI
- ✅ Validação automática de URLs
- ✅ Progresso visual do download
- ✅ Integração com explorador de arquivos
- ✅ Interface responsiva e intuitiva
- ✅ Tratamento de erros amigável

## � Gerar Executável

Para gerar seu próprio executável:

### Método Simples
```bash
# Execute o script de build (instala dependências automaticamente)
build.bat
```

### Método Manual
```bash
# Instale as dependências
pip install -r requirements.txt

# Gere o executável
python -m PyInstaller --onefile --windowed --name="YouTube Audio Converter" gui.py
```

O executável será gerado na pasta `dist/`.

## �📂 Estrutura do Projeto

```
youtube-audio-converter/
│
├── main.py                        # Script principal (linha de comando)
├── gui.py                         # Interface gráfica
├── README.md                      # Documentação
├── requirements.txt               # Dependências Python
├── youtube-audio-converter.spec   # Configuração PyInstaller
├── version_info.txt              # Informações da versão
├── build.bat                     # Script de build automático
├── quick_build.bat              # Script de build rápido
└── .gitignore                   # Arquivos ignorados pelo Git
```

## ⚙️ Configurações

Você pode modificar as configurações no arquivo `main.py`:

- **Qualidade do áudio**: Altere `'preferredquality': '320'` (valores: 0-9 ou 128, 192, 256, 320)
- **Formato de saída**: Altere `'preferredcodec': 'mp3'` (opções: mp3, m4a, wav, etc.)
- **Diretório padrão**: Modifique o parâmetro `pasta_destino` na função

## 🛡️ Tratamento de Erros

O script inclui tratamento de erros para:
- URLs inválidas ou vazias
- Problemas de conexão com a internet
- Vídeos indisponíveis ou privados
- Erros de conversão de áudio

## ⚠️ Avisos Legais

- Este script é apenas para uso educacional e pessoal
- Respeite os direitos autorais e os Termos de Serviço do YouTube
- Não utilize para distribuição não autorizada de conteúdo protegido por direitos autorais

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 👤 Autor

**Matheus Fragoso**

- GitHub: [@legulaas](https://github.com/legulaas)

## 🙏 Agradecimentos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Ferramenta poderosa para download de vídeos
- [FFmpeg](https://ffmpeg.org/) - Solução completa para processamento de áudio/vídeo

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!

