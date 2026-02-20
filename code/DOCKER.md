# 🐳 Guía de Dockerización - MiddlewareMarisma

## 📋 Requisitos Previos

- Docker instalado (versión 20.10 o superior)
- Docker Compose instalado (versión 2.0 o superior)

Para verificar la instalación:
```bash
docker --version
docker-compose --version
```

## 🚀 Inicio Rápido

### 1. Construir y Levantar el Servicio

Desde el directorio `code/`:

```bash
docker-compose up --build -d
```

- `--build`: Construye la imagen desde cero
- `-d`: Ejecuta en modo detached (background)

### 2. Verificar el Estado

```bash
docker-compose ps
```

Deberías ver:
```
NAME                  COMMAND                  SERVICE       STATUS
middleware_marisma    "uvicorn app:app --h…"   middleware    Up (healthy)
```

### 3. Ver Logs

```bash
# Logs en tiempo real
docker-compose logs -f

# Últimas 100 líneas
docker-compose logs --tail=100
```

### 4. Probar el Servicio

```bash
curl http://localhost:8000/health
```

Respuesta esperada:
```json
{"status": "healthy", "service": "MiddlewareMarisma"}
```

## 🔄 Auto-Restart

El sistema está configurado con `restart: unless-stopped`, esto significa:

✅ **Se reiniciará automáticamente si:**
- La aplicación falla o se cierra inesperadamente
- El servidor se reinicia
- Docker se reinicia

❌ **NO se reiniciará si:**
- Detienes manualmente el contenedor con `docker-compose stop` o `docker stop`

### Políticas de Restart Disponibles

Si necesitas cambiar el comportamiento, edita `docker-compose.yml`:

```yaml
restart: always           # Siempre reinicia, incluso si se detiene manualmente
restart: unless-stopped   # Reinicia excepto detención manual (ACTUAL)
restart: on-failure       # Solo reinicia si falla
restart: "no"            # Nunca reinicia
```

## 🏥 Health Checks

El sistema incluye dos niveles de health checks:

### 1. Health Check de Docker (Dockerfile)
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3
```

### 2. Health Check de Docker Compose
```yaml
healthcheck:
  test: ["CMD", "python", "-c", "..."]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

**Comportamiento:**
- Verifica cada 30 segundos
- Espera 40 segundos antes de empezar a verificar (startup)
- Reinicia automáticamente después de 3 fallos consecutivos

## 📦 Gestión de Datos

### Volúmenes Persistentes

El sistema monta estos archivos como volúmenes:

```yaml
volumes:
  - ./internal.db:/app/internal.db      # Base de datos SQLite
  - ./session.json:/app/session.json    # Sesión HTTP
  - ./config.json:/app/config.json      # Configuración
```

**Ventajas:**
- Los datos persisten aunque se borre el contenedor
- Puedes editar `config.json` sin reconstruir la imagen
- Los logs y datos se guardan fuera del contenedor

## 🔧 Comandos Útiles

### Gestión del Servicio

```bash
# Iniciar (si está detenido)
docker-compose start

# Detener (sin borrar contenedor)
docker-compose stop

# Reiniciar
docker-compose restart

# Parar y eliminar contenedores
docker-compose down

# Parar y eliminar todo (contenedores, redes, volúmenes)
docker-compose down -v
```

### Construcción y Actualización

```bash
# Reconstruir solo si hay cambios
docker-compose up -d

# Forzar reconstrucción completa
docker-compose up --build -d

# Reconstruir sin cache
docker-compose build --no-cache
```

### Debugging

```bash
# Acceder al contenedor
docker exec -it middleware_marisma bash

# Ver logs con timestamps
docker-compose logs -f --timestamps

# Ver solo errores
docker-compose logs | grep ERROR

# Inspeccionar el contenedor
docker inspect middleware_marisma

# Ver recursos usados
docker stats middleware_marisma
```

### Limpieza

```bash
# Limpiar contenedores detenidos
docker container prune

# Limpiar imágenes no usadas
docker image prune

# Limpiar todo (cuidado!)
docker system prune -a
```

## 🌐 Configuración de Red

### Acceso desde Otros Contenedores

Si necesitas que otros contenedores se comuniquen con este:

```yaml
services:
  otro_servicio:
    networks:
      - marisma_network
    environment:
      - MIDDLEWARE_URL=http://middleware:8000
```

### Cambiar Puerto

Edita `docker-compose.yml`:
```yaml
ports:
  - "9000:8000"  # Puerto externo:Puerto interno
```

## 🔐 Variables de Entorno

### Opción 1: Archivo `.env`

Crea un archivo `.env` en el mismo directorio:
```env
DB_HOST=172.20.48.129
DB_PORT=3306
DB_USER=ar_marisma
DB_PASSWORD=M33aarIsmmmA
LOG_LEVEL=info
```

### Opción 2: En docker-compose.yml

```yaml
environment:
  - DB_HOST=172.20.48.129
  - DB_PORT=3306
```

## 📊 Monitoreo de Recursos

### Límites Configurados

```yaml
deploy:
  resources:
    limits:
      cpus: '1'          # Máximo 1 CPU
      memory: 512M       # Máximo 512MB RAM
    reservations:
      cpus: '0.25'       # Mínimo garantizado
      memory: 128M
```

### Ajustar Límites

Si la aplicación necesita más recursos, edita estos valores en `docker-compose.yml`.

## 🚨 Troubleshooting

### El contenedor se reinicia constantemente

```bash
# Ver por qué falla
docker-compose logs --tail=50

# Ver el estado detallado
docker inspect middleware_marisma | grep -A 10 "Health"
```

### La aplicación no responde al health check

```bash
# Probar manualmente dentro del contenedor
docker exec middleware_marisma curl http://localhost:8000/health

# Ver si el puerto está escuchando
docker exec middleware_marisma netstat -tlnp
```

### Error de conexión a MySQL

Verifica que:
1. El servidor MySQL es accesible desde el contenedor
2. Las credenciales en `config.json` son correctas
3. La red de Docker permite la conexión

```bash
# Probar conexión desde el contenedor
docker exec middleware_marisma ping 172.20.48.129
```

### Problemas de permisos con volúmenes

```bash
# En el host, ajustar permisos
chmod 666 internal.db session.json config.json
```

## 🔄 Actualización del Código

### Método 1: Con Rebuild
```bash
git pull origin feature/db_integration
docker-compose up --build -d
```

### Método 2: Sin Downtime (con Docker Swarm)
```bash
docker stack deploy -c docker-compose.yml marisma
```

## 📈 Producción

### Recomendaciones

1. **Usar Docker Swarm o Kubernetes** para alta disponibilidad
2. **Configurar logging centralizado** (ELK, Splunk, etc.)
3. **Implementar alertas** basadas en health checks
4. **Usar secrets** en lugar de variables de entorno para credenciales
5. **Configurar backups automáticos** de `internal.db`

### Ejemplo con Docker Swarm

```bash
# Inicializar swarm
docker swarm init

# Deploy con 3 réplicas
docker stack deploy -c docker-compose.yml marisma

# Escalar
docker service scale marisma_middleware=5
```

## 📚 Referencias

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Health Check Best Practices](https://docs.docker.com/engine/reference/builder/#healthcheck)
- [Container Restart Policies](https://docs.docker.com/config/containers/start-containers-automatically/)
