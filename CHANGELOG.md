# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [1.0.0] - 2025-11-06

### ✨ Adicionado
- **Interface gráfica completa** usando tkinter
- **Executável standalone** (.exe) que não requer Python instalado
- **Barra de progresso** com status em tempo real do download
- **Seletor de pasta** para escolher destino dos arquivos
- **Validação de URL** automática do YouTube
- **Tratamento de erros** robusto e amigável
- **Botões de ação**: Download, Limpar campos, Abrir pasta
- **Área de log** detalhada com informações do processo
- **Script de build** automatizado (`build.bat`)
- **Documentação completa** com instruções de uso

### 🔧 Melhorado
- **Função de download** refatorada para suportar callbacks de status
- **Qualidade de áudio** mantida em 320 kbps (máxima qualidade)
- **Interface responsiva** que não trava durante downloads
- **Nomenclatura automática** baseada no título do vídeo

### 📋 Características Técnicas
- **Linguagem**: Python 3.11+
- **Interface**: tkinter (nativa do Python)
- **Bibliotecas**: yt-dlp, PyInstaller
- **Tamanho do executável**: ~18.5 MB
- **Compatibilidade**: Windows 10/11
- **Dependências externas**: FFmpeg (obrigatório)

### 🎯 Para Usuários Finais
- Baixe apenas o arquivo `YouTube-Audio-Converter.exe`
- Não é necessário instalar Python ou outras dependências
- Interface amigável e intuitiva
- Funciona offline (após download inicial)

### 👨‍💻 Para Desenvolvedores  
- Código fonte completo disponível
- Script de build automatizado
- Documentação técnica detalhada
- Estrutura de projeto organizada