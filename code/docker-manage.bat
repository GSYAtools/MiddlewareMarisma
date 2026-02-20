@echo off
REM Script de gestión del contenedor MiddlewareMarisma para Windows
REM Uso: docker-manage.bat [comando]

setlocal enabledelayedexpansion

REM Verificar que Docker está instalado
where docker >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker no está instalado
    exit /b 1
)

where docker-compose >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker Compose no está instalado
    exit /b 1
)

REM Procesar comandos
if "%1"=="" goto :help
if "%1"=="start" goto :start
if "%1"=="stop" goto :stop
if "%1"=="restart" goto :restart
if "%1"=="logs" goto :logs
if "%1"=="status" goto :status
if "%1"=="shell" goto :shell
if "%1"=="clean" goto :clean
if "%1"=="rebuild" goto :rebuild
if "%1"=="backup" goto :backup
if "%1"=="help" goto :help
goto :help

:start
echo [INFO] Construyendo y levantando el servicio...
docker-compose up --build -d
if %errorlevel% equ 0 (
    echo [INFO] Servicio iniciado correctamente
    call :status
) else (
    echo [ERROR] Error al iniciar el servicio
)
exit /b 0

:stop
echo [INFO] Deteniendo el servicio...
docker-compose stop
echo [INFO] Servicio detenido
exit /b 0

:restart
echo [INFO] Reiniciando el servicio...
docker-compose restart
echo [INFO] Servicio reiniciado
call :status
exit /b 0

:logs
echo [INFO] Mostrando logs (Ctrl+C para salir)...
docker-compose logs -f --tail=100
exit /b 0

:status
echo [INFO] Estado del servicio:
docker-compose ps
echo.
echo [INFO] Health check:
curl -s http://localhost:8000/health
echo.
exit /b 0

:shell
echo [INFO] Accediendo al contenedor...
docker exec -it middleware_marisma bash
exit /b 0

:clean
echo [WARN] Esto eliminará el contenedor y las redes (los volúmenes persisten)
set /p confirm="¿Continuar? (S/N): "
if /i "%confirm%"=="S" (
    echo [INFO] Limpiando...
    docker-compose down
    echo [INFO] Limpieza completada
) else (
    echo [INFO] Operación cancelada
)
exit /b 0

:rebuild
echo [INFO] Reconstruyendo desde cero (sin cache)...
docker-compose down
docker-compose build --no-cache
docker-compose up -d
echo [INFO] Reconstrucción completada
call :status
exit /b 0

:backup
echo [INFO] Creando backup de datos...
set BACKUP_DIR=backups\%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set BACKUP_DIR=%BACKUP_DIR: =0%
mkdir "%BACKUP_DIR%" 2>nul

if exist "internal.db" (
    copy /Y "internal.db" "%BACKUP_DIR%\" >nul
    echo [INFO] ✓ internal.db respaldado
)

if exist "session.json" (
    copy /Y "session.json" "%BACKUP_DIR%\" >nul
    echo [INFO] ✓ session.json respaldado
)

if exist "config.json" (
    copy /Y "config.json" "%BACKUP_DIR%\" >nul
    echo [INFO] ✓ config.json respaldado
)

echo [INFO] Backup completado en: %BACKUP_DIR%
exit /b 0

:help
echo MiddlewareMarisma - Script de Gestión Docker
echo.
echo Uso:
echo     docker-manage.bat [comando]
echo.
echo Comandos disponibles:
echo     start       Construir y levantar el servicio
echo     stop        Detener el servicio
echo     restart     Reiniciar el servicio
echo     logs        Ver logs en tiempo real
echo     status      Ver estado del servicio
echo     shell       Acceder al shell del contenedor
echo     clean       Eliminar contenedor y redes (mantiene volúmenes)
echo     rebuild     Reconstruir desde cero sin cache
echo     backup      Crear backup de datos importantes
echo     help        Mostrar esta ayuda
echo.
echo Ejemplos:
echo     docker-manage.bat start
echo     docker-manage.bat logs
echo     docker-manage.bat backup
echo.
echo Más información:
echo     Ver DOCKER.md para documentación completa
exit /b 0
