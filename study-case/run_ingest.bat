@echo off
REM Script para ejecutar la ingestión de incidentes

setlocal enabledelayedexpansion

REM Colores para salida
for /F %%a in ('copy /Z "%~f0" nul') do set "BS=%%a"

echo.
echo ===============================================
echo   INGESTOR DE INCIDENTES - CASO DE ESTUDIO
echo ===============================================
echo.

REM Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo %BS%[91m[ERROR] Python no está instalado o no está en PATH%BS%[0m
    echo.
    pause
    exit /b 1
)

REM Verificar requests
python -c "import requests" >nul 2>&1
if %errorlevel% neq 0 (
    echo %BS%[93m[ADVERTENCIA] El paquete 'requests' no está instalado%BS%[0m
    echo Instalando requests...
    python -m pip install requests
    if %errorlevel% neq 0 (
        echo %BS%[91m[ERROR] No se pudo instalar requests%BS%[0m
        echo.
        pause
        exit /b 1
    )
)

REM Verificar que el archivo existe
if not exist "ingest_incidents.py" (
    echo %BS%[91m[ERROR] No se encontró ingest_incidents.py%BS%[0m
    echo.
    pause
    exit /b 1
)

echo %BS%[92m[OK] Verificaciones completadas%BS%[0m
echo.
echo Iniciando ingestión de incidentes...
echo.

REM Ejecutar script
python ingest_incidents.py

REM Mostrar resultado
if %errorlevel% equ 0 (
    echo.
    echo %BS%[92m[EXITOSO] La ingestión se completó correctamente%BS%[0m
) else (
    echo.
    echo %BS%[91m[ERROR] La ingestión terminó con errores%BS%[0m
)

echo.
echo El log se encuentra en: ingest_incidents.log
echo.
pause
