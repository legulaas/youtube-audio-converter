# YouTube Audio Converter v1.0.1 🎵

## 📥 Download Rápido

**Para usuários finais (recomendado):**
- Baixe: `YouTube-Audio-Converter-v1.0.1.exe` (18.5 MB)
- Execute diretamente - não precisa instalar Python!
- **Novo**: Ícone personalizado no executável

**Para desenvolvedores:**
- Baixe o código fonte completo
- Veja instruções de build no README.md

## 🚀 O que há de novo nesta versão

### ✨ Interface Gráfica Completa
- 🎯 Campo para URL do YouTube com validação automática
- 📁 Seletor de pasta de destino integrado
- 📊 Barra de progresso com status em tempo real
- 🔄 Botões para download, limpar e abrir pasta
- 📝 Área de log detalhada do processo

### 🛠️ Executável Standalone  
- ✅ **Não precisa instalar Python** no computador
- ✅ **Arquivo único** - fácil de distribuir
- ✅ **Todas as dependências incluídas** (exceto FFmpeg)
- ✅ **Interface moderna** e responsiva
- 🆕 **Ícone personalizado** no executável (nota musical + MP3)

## ⚙️ Requisitos do Sistema

### Obrigatório:
- **Windows 10/11** (64-bit)
- **FFmpeg** instalado no sistema ([Download aqui](https://ffmpeg.org/download.html))
- **Conexão com internet** para downloads

### Opcional (apenas para desenvolvedores):
- Python 3.11+
- Dependências: `pip install -r requirements.txt`

## 📋 Como usar

### Para Usuários Finais:
1. Baixe `YouTube-Audio-Converter-v1.0.1.exe`
2. Execute o arquivo (agora com ícone personalizado!)
3. Cole a URL do vídeo do YouTube
4. Escolha a pasta de destino
5. Clique em "Baixar Áudio"

### Para Desenvolvedores:
```bash
# Executar interface gráfica
python gui.py

# Executar linha de comando
python main.py

# Gerar novo executável
build.bat
```

## 🔧 Recursos Técnicos

- **Qualidade**: MP3 320 kbps (máxima qualidade)
- **Formatos suportados**: Todos os vídeos públicos do YouTube
- **Nomenclatura**: Automática baseada no título do vídeo
- **Interface**: Não trava durante downloads (threading)
- **Validação**: URLs e pastas de destino
- **Logs**: Detalhados para debug

## ❗ Importante

### Instalação do FFmpeg:
1. Baixe em: https://ffmpeg.org/download.html
2. Extraia e adicione ao PATH do Windows
3. Teste executando `ffmpeg -version` no cmd

### Uso Legal:
- ⚖️ Este software é apenas para **uso pessoal e educacional**
- ⚖️ Respeite os **direitos autorais** e termos do YouTube
- ⚖️ Não use para **distribuição não autorizada** de conteúdo

## 🐛 Relatando Problemas

Encontrou um bug? Abra uma issue em:
https://github.com/legulaas/youtube-audio-converter/issues

## 🙏 Créditos

- **yt-dlp**: Ferramenta poderosa para download de vídeos
- **FFmpeg**: Processamento de áudio/vídeo
- **tkinter**: Interface gráfica nativa do Python

---

**Autor:** Matheus Fragoso ([@legulaas](https://github.com/legulaas))  
**Repositório:** https://github.com/legulaas/youtube-audio-converter  
**Licença:** MIT