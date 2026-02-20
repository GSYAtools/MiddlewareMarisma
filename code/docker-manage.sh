#!/bin/bash
# Script de gestión del contenedor MiddlewareMarisma
# Uso: ./docker-manage.sh [comando]

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para imprimir mensajes
info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Función para verificar que Docker está instalado
check_docker() {
    if ! command -v docker &> /dev/null; then
        error "Docker no está instalado"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        error "Docker Compose no está instalado"
        exit 1
    fi
    
    info "Docker y Docker Compose están instalados"
}

# Función para construir y levantar
start() {
    info "Construyendo y levantando el servicio..."
    docker-compose up --build -d
    info "Servicio iniciado correctamente"
    status
}

# Función para detener
stop() {
    info "Deteniendo el servicio..."
    docker-compose stop
    info "Servicio detenido"
}

# Función para reiniciar
restart() {
    info "Reiniciando el servicio..."
    docker-compose restart
    info "Servicio reiniciado"
    status
}

# Función para ver logs
logs() {
    info "Mostrando logs (Ctrl+C para salir)..."
    docker-compose logs -f --tail=100
}

# Función para ver estado
status() {
    info "Estado del servicio:"
    docker-compose ps
    echo ""
    info "Health check:"
    curl -s http://localhost:8000/health | python3 -m json.tool 2>/dev/null || warn "El servicio no responde al health check"
}

# Función para acceder al shell del contenedor
shell() {
    info "Accediendo al contenedor..."
    docker exec -it middleware_marisma bash
}

# Función para limpiar
clean() {
    warn "Esto eliminará el contenedor y las redes (los volúmenes persisten)"
    read -p "¿Continuar? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        info "Limpiando..."
        docker-compose down
        info "Limpieza completada"
    else
        info "Operación cancelada"
    fi
}

# Función para limpieza completa
clean_all() {
    error "¡ADVERTENCIA! Esto eliminará contenedores, redes Y VOLÚMENES (se perderán datos)"
    read -p "¿Estás SEGURO? Escribe 'SI' para confirmar: " -r
    echo
    if [[ $REPLY == "SI" ]]; then
        info "Eliminando todo..."
        docker-compose down -v
        info "Limpieza completa realizada"
    else
        info "Operación cancelada"
    fi
}

# Función para reconstruir desde cero
rebuild() {
    info "Reconstruyendo desde cero (sin cache)..."
    docker-compose down
    docker-compose build --no-cache
    docker-compose up -d
    info "Reconstrucción completada"
    status
}

# Función para backup
backup() {
    info "Creando backup de datos..."
    BACKUP_DIR="backups/$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    
    if [ -f "internal.db" ]; then
        cp internal.db "$BACKUP_DIR/"
        info "✓ internal.db respaldado"
    fi
    
    if [ -f "session.json" ]; then
        cp session.json "$BACKUP_DIR/"
        info "✓ session.json respaldado"
    fi
    
    if [ -f "config.json" ]; then
        cp config.json "$BACKUP_DIR/"
        info "✓ config.json respaldado"
    fi
    
    info "Backup completado en: $BACKUP_DIR"
}

# Función para mostrar ayuda
help() {
    cat << EOF
${GREEN}MiddlewareMarisma - Script de Gestión Docker${NC}

${YELLOW}Uso:${NC}
    ./docker-manage.sh [comando]

${YELLOW}Comandos disponibles:${NC}
    start       Construir y levantar el servicio
    stop        Detener el servicio
    restart     Reiniciar el servicio
    logs        Ver logs en tiempo real
    status      Ver estado del servicio
    shell       Acceder al shell del contenedor
    clean       Eliminar contenedor y redes (mantiene volúmenes)
    clean-all   Eliminar TODO incluyendo volúmenes (¡PELIGROSO!)
    rebuild     Reconstruir desde cero sin cache
    backup      Crear backup de datos importantes
    help        Mostrar esta ayuda

${YELLOW}Ejemplos:${NC}
    ./docker-manage.sh start
    ./docker-manage.sh logs
    ./docker-manage.sh backup

${YELLOW}Más información:${NC}
    Ver DOCKER.md para documentación completa
EOF
}

# Main
check_docker

case "${1:-help}" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    logs)
        logs
        ;;
    status)
        status
        ;;
    shell)
        shell
        ;;
    clean)
        clean
        ;;
    clean-all)
        clean_all
        ;;
    rebuild)
        rebuild
        ;;
    backup)
        backup
        ;;
    help|*)
        help
        ;;
esac
