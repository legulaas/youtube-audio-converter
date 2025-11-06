@echo off
:: =============================================================================
:: YouTube Audio Converter - Build com Python Module
:: =============================================================================
:: Script que usa python -m PyInstaller para funcionar sem PATH
:: =============================================================================

title YouTube Audio Converter - Build Script

echo ===============================================================================
echo                     YouTube Audio Converter - Build
echo ===============================================================================
echo.

:: Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao esta instalado ou no PATH!
    pause
    exit /b 1
)

echo [INFO] Python encontrado!

:: Verificar se estamos no diretório correto
if not exist "gui.py" (
    echo [ERRO] Arquivo gui.py nao encontrado!
    pause
    exit /b 1
)

:: Instalar PyInstaller se necessário
echo [INFO] Verificando PyInstaller...
python -c "import PyInstaller" 2>nul
if %errorlevel% neq 0 (
    echo [INFO] Instalando PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo [ERRO] Falha ao instalar PyInstaller!
        pause
        exit /b 1
    )
)

:: Limpar builds anteriores
echo [INFO] Limpando builds anteriores...
if exist "build" rmdir /s /q "build" 2>nul
if exist "dist" rmdir /s /q "dist" 2>nul

:: Verificar se existe ícone
if exist "app_icon.ico" (
    echo [INFO] Icone encontrado: app_icon.ico
    set "ICON_PARAM=--icon=app_icon.ico"
) else (
    echo [WARNING] Icone nao encontrado, gerando sem icone
    set "ICON_PARAM="
)

:: Gerar executável usando python -m
echo [INFO] Gerando executavel...
echo [INFO] Comando: python -m PyInstaller --onefile --windowed --name="YouTube Audio Converter" %ICON_PARAM% gui.py

python -m PyInstaller --onefile --windowed --name="YouTube Audio Converter" %ICON_PARAM% gui.py

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Falha ao gerar executavel!
    echo.
    echo Detalhes do erro acima. Tente:
    echo 1. pip install --upgrade pyinstaller
    echo 2. Execute como administrador
    echo 3. Verifique se o FFmpeg esta no PATH
    echo.
    pause
    exit /b 1
)

:: Verificar resultado
if exist "dist\YouTube Audio Converter.exe" (
    echo.
    echo ===============================================================================
    echo [SUCESSO] Executavel gerado!
    echo ===============================================================================
    echo.
    echo Local: dist\YouTube Audio Converter.exe
    
    for %%I in ("dist\YouTube Audio Converter.exe") do (
        set /a "size_mb=%%~zI/1024/1024"
        echo Tamanho: %%~zI bytes (~!size_mb! MB)
    )
    
    echo.
    echo [INFO] Pronto para distribuicao!
    echo.
    
    :: Opções finais
    set /p "choice=Escolha: (1) Testar executavel (2) Abrir pasta (3) Sair: "
    
    if "!choice!"=="1" (
        echo [INFO] Testando executavel...
        start "" "dist\YouTube Audio Converter.exe"
    ) else if "!choice!"=="2" (
        echo [INFO] Abrindo pasta dist...
        explorer "dist"
    )
    
) else (
    echo [ERRO] Executavel nao encontrado!
)

echo.
pause