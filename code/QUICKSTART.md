# 🚀 Inicio Rápido - MiddlewareMarisma Dockerizado

## ⚡ Para Empezar en 3 Pasos

### 1️⃣ Editar Configuración (Opcional)
```bash
# Copiar ejemplo de variables de entorno
cp .env.example .env

# O editar config.json directamente
notepad config.json  # Windows
nano config.json     # Linux/Mac
```

### 2️⃣ Levantar el Servicio

**Windows:**
```batch
docker-manage.bat start
```

**Linux/Mac:**
```bash
chmod +x docker-manage.sh
./docker-manage.sh start
```

### 3️⃣ Verificar que Funciona
```bash
curl http://localhost:8000/health
```

**Respuesta esperada:**
```json
{"status":"healthy","service":"MiddlewareMarisma"}
```

## 🎯 Comandos Esenciales

### Gestión Básica

| Acción | Windows | Linux/Mac |
|--------|---------|-----------|
| Iniciar | `docker-manage.bat start` | `./docker-manage.sh start` |
| Detener | `docker-manage.bat stop` | `./docker-manage.sh stop` |
| Ver logs | `docker-manage.bat logs` | `./docker-manage.sh logs` |
| Estado | `docker-manage.bat status` | `./docker-manage.sh status` |
| Backup | `docker-manage.bat backup` | `./docker-manage.sh backup` |

### Sin Scripts

```bash
# Iniciar
docker-compose up -d

# Detener
docker-compose stop

# Ver logs
docker-compose logs -f

# Estado
docker-compose ps
```

## 🧪 Probar la API

### Health Check
```bash
curl http://localhost:8000/health
```

### Crear Incidente
```bash
curl -X POST http://localhost:8000/new_incident \
  -H "Content-Type: application/json" \
  -d @request.json
```

### Documentación Interactiva
Abrir en navegador: http://localhost:8000/docs

## 🔄 Auto-Restart Configurado

El servicio **SE REINICIARÁ AUTOMÁTICAMENTE** si:
- ✅ La aplicación falla o crashea
- ✅ El servidor se reinicia
- ✅ Docker se reinicia
- ✅ El health check falla 3 veces consecutivas

El servicio **NO se reiniciará** si:
- ❌ Lo detienes manualmente con `docker-compose stop`

## 📊 Monitoreo

### Ver Logs en Tiempo Real
```bash
docker-compose logs -f --tail=100
```

### Ver Estado del Heath Check
```bash
docker inspect middleware_marisma | grep -A 20 "Health"
```

### Ver Estadísticas de Recursos
```bash
docker stats middleware_marisma
```

## 🆘 Solución Rápida de Problemas

### El servicio no arranca
```bash
# Ver qué pasó
docker-compose logs --tail=50
```

### Reiniciar desde cero
```bash
docker-compose down
docker-compose up --build -d
```

### Acceder al contenedor
```bash
docker exec -it middleware_marisma bash
```

### Limpiar y empezar de nuevo
```bash
# ⚠️ Esto borra TODOS los datos
docker-compose down -v
docker-compose up --build -d
```

## 📚 Más Información

- **Documentación completa de Docker**: Ver [DOCKER.md](DOCKER.md)
- **README principal**: Ver [README.md](README.md)
- **API Docs**: http://localhost:8000/docs (cuando el servicio esté corriendo)

## ✅ Checklist de Verificación

- [ ] Docker y Docker Compose instalados
- [ ] Archivo `config.json` configurado con credenciales
- [ ] Servicio iniciado: `docker-compose up -d`
- [ ] Health check responde: `curl http://localhost:8000/health`
- [ ] Logs sin errores: `docker-compose logs`

## 💡 Tips

1. **Backups automáticos**: Ejecuta `docker-manage.bat backup` antes de cambios importantes
2. **Ver logs filtrados**: `docker-compose logs | grep ERROR`
3. **Reinicio rápido**: `docker-compose restart`
4. **Puerto ocupado**: Edita `docker-compose.yml` y cambia `"8000:8000"` a `"9000:8000"`

---

**¿Problemas?** Consulta [DOCKER.md](DOCKER.md) o los logs: `docker-compose logs -f`
