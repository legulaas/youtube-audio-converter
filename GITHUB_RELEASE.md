# 🚀 Instruções para Criar Release no GitHub

## 📋 Preparativos Concluídos

✅ **Projeto limpo e organizado**
✅ **Executável pronto**: `YouTube-Audio-Converter-v1.0.0.exe`
✅ **Documentação completa**
✅ **Arquivos de release criados**

## 🎯 Passos para Criar a Release

### 1. Commit e Push Final
```bash
git add .
git commit -m "Release v1.0.0: Interface gráfica e executável standalone"
git push origin main
```

### 2. Criar Tag da Versão
```bash
git tag -a v1.0.1 -m "YouTube Audio Converter v1.0.1 - Ícone personalizado"
git push origin v1.0.1
```

### 3. Criar Release no GitHub

1. **Acesse seu repositório** no GitHub
2. **Clique em "Releases"** (lado direito)
3. **Clique "Create a new release"**
4. **Preencha os dados**:

   **Tag version:** `v1.0.1`
   **Release title:** `🎵 YouTube Audio Converter v1.0.1 - Interface Gráfica + Executável com Ícone`
   
   **Description:** (copie o conteúdo de RELEASE_NOTES.md)

### 4. Upload do Executável

**Na seção "Attach binaries":**
- **Arquivo**: `dist/YouTube-Audio-Converter-v1.0.1.exe`
- **Nome sugerido**: `YouTube-Audio-Converter-v1.0.1-Windows.exe`

### 5. Configurações Recomendadas

- ✅ **Set as the latest release**
- ✅ **Create a discussion for this release** (opcional)
- ⚠️ **This is a pre-release** (deixar desmarcado)

## 📝 Texto Sugerido para Release

**Título:**
```
🎵 YouTube Audio Converter v1.0.0 - Interface Gráfica + Executável
```

**Descrição:** (use o conteúdo do arquivo RELEASE_NOTES.md)

## 📂 Arquivos para Upload

**Arquivo principal:**
- `YouTube-Audio-Converter-v1.0.0.exe` (18.5 MB)

**Arquivos opcionais (código fonte):**
- O GitHub automaticamente cria os arquivos .zip e .tar.gz do código fonte

## 🔍 Verificação Final

Antes de publicar, verifique:

- [ ] Executável funciona corretamente
- [ ] Documentação está atualizada  
- [ ] Tag da versão foi criada
- [ ] Commit final foi feito
- [ ] CHANGELOG.md está completo
- [ ] README.md tem instruções claras

## 🎉 Pós-Release

Após criar a release:

1. **Teste o download** do executável da release
2. **Compartilhe o link** da release
3. **Atualize** qualquer documentação externa
4. **Considere** criar uma branch `release/v1.0.0`

---

**Link da release será:**
`https://github.com/legulaas/youtube-audio-converter/releases/tag/v1.0.0`

**Download direto do executável será:**
`https://github.com/legulaas/youtube-audio-converter/releases/download/v1.0.0/YouTube-Audio-Converter-v1.0.0-Windows.exe`