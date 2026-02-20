# Makefile para MiddlewareMarisma
# Facilita la gestión del proyecto con comandos cortos

.PHONY: help build start stop restart logs status shell clean backup test health

# Variables
COMPOSE := docker-compose
COMPOSE_PROD := docker-compose -f docker-compose.prod.yml
CONTAINER := middleware_marisma

# Configuración de colores para output
GREEN := \033[0;32m
YELLOW := \033[1;33m
NC := \033[0m # No Color

help: ## Mostrar esta ayuda
	@echo "$(GREEN)MiddlewareMarisma - Comandos disponibles:$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "Ejemplos:"
	@echo "  make start    - Iniciar el servicio"
	@echo "  make logs     - Ver logs en tiempo real"
	@echo "  make backup   - Crear backup de datos"

build: ## Construir la imagen Docker
	@echo "$(GREEN)Construyendo imagen...$(NC)"
	$(COMPOSE) build --no-cache

start: ## Levantar el servicio
	@echo "$(GREEN)Iniciando servicio...$(NC)"
	$(COMPOSE) up -d
	@sleep 2
	@$(MAKE) health

stop: ## Detener el servicio
	@echo "$(YELLOW)Deteniendo servicio...$(NC)"
	$(COMPOSE) stop

down: ## Detener y eliminar contenedores
	@echo "$(YELLOW)Deteniendo y eliminando contenedores...$(NC)"
	$(COMPOSE) down

restart: ## Reiniciar el servicio
	@echo "$(GREEN)Reiniciando servicio...$(NC)"
	$(COMPOSE) restart
	@sleep 2
	@$(MAKE) health

logs: ## Ver logs en tiempo real
	$(COMPOSE) logs -f --tail=100

logs-errors: ## Ver solo errores en los logs
	$(COMPOSE) logs | grep -i error

status: ## Ver estado del servicio
	@echo "$(GREEN)Estado del servicio:$(NC)"
	@$(COMPOSE) ps
	@echo ""
	@$(MAKE) health

health: ## Verificar health check
	@echo "$(GREEN)Health check:$(NC)"
	@curl -s http://localhost:8000/health | python3 -m json.tool 2>/dev/null || echo "$(YELLOW)⚠ Servicio no responde$(NC)"

shell: ## Acceder al shell del contenedor
	@echo "$(GREEN)Accediendo al contenedor...$(NC)"
	docker exec -it $(CONTAINER) bash

clean: ## Limpiar contenedores y redes (mantiene volúmenes)
	@echo "$(YELLOW)Limpiando contenedores y redes...$(NC)"
	$(COMPOSE) down
	@echo "$(GREEN)Limpieza completada$(NC)"

clean-all: ## Limpiar TODO incluyendo volúmenes (¡CUIDADO!)
	@echo "$(YELLOW)⚠ ADVERTENCIA: Esto eliminará todos los datos$(NC)"
	@read -p "¿Continuar? [y/N]: " confirm && [ "$$confirm" = "y" ] || exit 1
	$(COMPOSE) down -v
	@echo "$(GREEN)Limpieza completa realizada$(NC)"

backup: ## Crear backup de datos importantes
	@echo "$(GREEN)Creando backup...$(NC)"
	@mkdir -p backups/$$(date +%Y%m%d_%H%M%S)
	@cp -v internal.db backups/$$(date +%Y%m%d_%H%M%S)/ 2>/dev/null || echo "No internal.db"
	@cp -v session.json backups/$$(date +%Y%m%d_%H%M%S)/ 2>/dev/null || echo "No session.json"
	@cp -v config.json backups/$$(date +%Y%m%d_%H%M%S)/ 2>/dev/null || echo "No config.json"
	@echo "$(GREEN)Backup completado en backups/$$(date +%Y%m%d_%H%M%S)$(NC)"

rebuild: ## Reconstruir desde cero sin cache
	@echo "$(GREEN)Reconstruyendo desde cero...$(NC)"
	$(COMPOSE) down
	$(COMPOSE) build --no-cache
	$(COMPOSE) up -d
	@sleep 2
	@$(MAKE) health

test: ## Probar la API
	@echo "$(GREEN)Probando endpoints...$(NC)"
	@echo "Health check:"
	@curl -s http://localhost:8000/health | python3 -m json.tool
	@echo ""
	@echo "Docs disponibles en: http://localhost:8000/docs"

stats: ## Ver estadísticas de recursos del contenedor
	docker stats $(CONTAINER) --no-stream

inspect: ## Inspeccionar el contenedor
	docker inspect $(CONTAINER)

# Comandos de producción
prod-start: ## Iniciar en modo producción
	@echo "$(GREEN)Iniciando en modo PRODUCCIÓN...$(NC)"
	$(COMPOSE_PROD) up -d

prod-stop: ## Detener modo producción
	@echo "$(YELLOW)Deteniendo modo PRODUCCIÓN...$(NC)"
	$(COMPOSE_PROD) down

prod-logs: ## Ver logs de producción
	$(COMPOSE_PROD) logs -f --tail=100

# Comandos de desarrollo
dev: ## Modo desarrollo (sin Docker)
	@echo "$(GREEN)Iniciando en modo desarrollo...$(NC)"
	uvicorn app:app --reload --host 0.0.0.0 --port 8000

install: ## Instalar dependencias de Python
	pip install -r requirements.txt

venv: ## Crear entorno virtual
	python3 -m venv .venv
	@echo "$(GREEN)Entorno virtual creado. Actívalo con:$(NC)"
	@echo "  source .venv/bin/activate  (Linux/Mac)"
	@echo "  .venv\\Scripts\\Activate.ps1  (Windows)"

# Comandos de Docker
docker-prune: ## Limpiar Docker (imágenes, contenedores, etc.)
	docker system prune -a -f

docker-logs: ## Ver logs de Docker
	journalctl -u docker -f

# Por defecto mostrar ayuda
.DEFAULT_GOAL := help
