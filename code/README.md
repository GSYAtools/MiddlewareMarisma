# MiddlewareMarisma

Middleware para gestión automatizada de incidentes de seguridad con integración a eMarisma.

## Tabla de Contenidos

- [Características](#características)
- [Inicio Rápido con Docker](#-inicio-rápido-con-docker-recomendado)
- [Instalación Manual](#-instalación-manual)
- [Uso](#-uso)
- [Documentación](#-documentación)
- [API Endpoints](#-api-endpoints)

## Características

- ✅ Gestión automatizada de incidentes de seguridad
- ✅ Integración con eMarisma (gestión de riesgos)
- ✅ Base de datos MySQL para datos principales
- ✅ SQLite para registro interno de peticiones
- ✅ Auto-restart en caso de fallos (con Docker)
- ✅ Health checks integrados
- ✅ API REST con FastAPI
- ✅ Controles dinámicos basados en amenazas

## Inicio Rápido con Docker (Recomendado)

### Requisitos
- Docker 20.10+
- Docker Compose 2.0+

### 1. Configuración

```bash
# Copiar configuración de ejemplo
cp .env.example .env

# Editar config.json con tus credenciales
# (O usar variables de entorno en .env)
```

### 2. Levantar el Servicio

**Windows:**
```batch
docker-manage.bat start
```

**Linux/Mac:**
```bash
chmod +x docker-manage.sh
./docker-manage.sh start
```

**O directamente con Docker Compose:**
```bash
docker-compose up --build -d
```

### 3. Verificar Estado

```bash
# Windows
docker-manage.bat status

# Linux/Mac
./docker-manage.sh status

# O manualmente
curl http://localhost:8000/health
```

### 4. Ver Logs

```bash
# Windows
docker-manage.bat logs

# Linux/Mac
./docker-manage.sh logs
```

### 📚 Documentación Docker Completa

Ver [DOCKER.md](DOCKER.md) para documentación detallada sobre:
- Gestión avanzada de contenedores
- Troubleshooting
- Configuración de producción
- Health checks
- Backups
- Y más...

## Instalación Manual

### Requisitos
- Python 3.11+
- MySQL 5.7+ (servidor eMarisma)
- Acceso de red al servidor eMarisma

### 1. Crear Entorno Virtual

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar

Editar `config.json` con tus credenciales:
```json
{
    "username": "tu_usuario",
    "password": "tu_contraseña",
    "db_host": "172.20.48.129",
    "db_port": 3306,
    "db_user": "ar_marisma",
    "db_password": "contraseña_db",
    "db_name": "ar_marisma"
}
```

### 4. Ejecutar

**Desarrollo:**
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Producción:**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

## Uso

### Crear un Incidente

```bash
curl -X POST http://localhost:8000/new_incident \
  -H "Content-Type: application/json" \
  -d @request.json
```

### Ejemplo de Payload (request.json)

```json
{
  "threat_id": "T789012",
  "user_id": "user456",
  "device_id": "Protocolo Bluetooth",
  "detected_at": "2025-10-15T14:22:00Z",
  "threat_type": "Man in the middle",
  "threat_description": "Interceptación de comunicaciones",
  "severity": "leve",
  "actions_taken": "Bloquear enlace y alertar al usuario",
  "status": "resolved",
  "project_name": "Di4SPDS",
  "subproject_name": "SmartHome",
  "cause": "Causado por falta de actualización",
  "controls": "A.05.01;A.05.02"
}
```

**Campo `controls` (opcional):**
- Si está **vacío o no existe**: Se usa el primer control disponible para la amenaza
- Si está **presente**: Se validan y vinculan todos los controles especificados (separados por `;`)

## API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Health check del servicio |
| POST | `/new_incident` | Crear nuevo incidente |
| GET | `/docs` | Documentación interactiva (Swagger) |
| GET | `/redoc` | Documentación alternativa (ReDoc) |

## 📁 Estructura del Proyecto

```
code/
├── app.py                  # Aplicación principal FastAPI
├── config.json            # Configuración (credenciales, DB)
├── Dockerfile             # Imagen Docker
├── docker-compose.yml     # Orquestación Docker
├── docker-manage.sh       # Script de gestión (Linux/Mac)
├── docker-manage.bat      # Script de gestión (Windows)
├── requirements.txt       # Dependencias Python
├── client/               # Cliente HTTP para eMarisma
├── config/               # Carga de configuración
├── middleware/           # Middleware personalizado
├── routes/               # Endpoints de la API
└── services/             # Lógica de negocio
    ├── emarisma_db_service.py    # Consultas a MySQL
    ├── emarisma_http_service.py  # Flujos HTTP
    └── internal_db_service.py    # Base de datos interna
```

## Seguridad

- ✅ Todas las consultas SQL están parametrizadas (protección contra SQL injection)
- ✅ Uso de `json.dumps/loads` en lugar de `eval()` (prevención de ejecución de código)
- ✅ Sanitización de parámetros LIKE en consultas dinámicas
- ✅ Validación de entradas en endpoints
- ⚠️ **IMPORTANTE**: No versionar `config.json` ni `.env` con credenciales reales

## Auto-Restart y Alta Disponibilidad

Con Docker, el servicio:
- ✅ Se reinicia automáticamente si falla
- ✅ Se inicia automáticamente al arrancar el servidor
- ✅ Incluye health checks cada 30 segundos
- ✅ Se recupera de errores de red temporales

Ver [DOCKER.md](DOCKER.md) para configuración avanzada de producción.

## 📊 Monitoreo

### Health Check Manual
```bash
curl http://localhost:8000/health
```

Respuesta esperada:
```json
{"status": "healthy", "service": "MiddlewareMarisma"}
```

### Logs
```bash
# Con Docker
docker-compose logs -f

# Manual
# Los logs aparecen en la consola donde ejecutaste uvicorn
```

## 🐛 Troubleshooting

### El servicio no arranca

**Docker:**
```bash
docker-compose logs --tail=50
```

**Manual:**
Verificar:
1. Python 3.11+ instalado
2. Dependencias instaladas correctamente
3. `config.json` con credenciales válidas
4. Acceso de red a servidor MySQL

### Error de conexión a MySQL

Verificar:
```bash
# Probar conectividad
ping 172.20.48.129

# Verificar credenciales en config.json
```

### El contenedor se reinicia constantemente

```bash
# Ver logs
docker-compose logs --tail=100

# Ver health check
docker inspect middleware_marisma | grep -A 10 "Health"
```

## 📚 Documentación

- [DOCKER.md](DOCKER.md) - Guía completa de Docker
- `/docs` - Swagger UI (cuando el servicio está corriendo)
- `/redoc` - ReDoc (cuando el servicio está corriendo)

## 🤝 Contribuir

1. Fork del proyecto
2. Crear una rama de feature (`git checkout -b feature/AmazingFeature`)
3. Commit de cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Licencia

Este proyecto es propiedad de GSYA Lab.

## 📧 Contacto

Para soporte o preguntas, contactar al equipo de desarrollo de GSYA Lab.

---

**¿Nuevo en Docker?** Comienza con `docker-manage.bat start` (Windows) o `./docker-manage.sh start` (Linux/Mac)

**¿Prefieres instalación manual?** Sigue las instrucciones en [Instalación Manual](#-instalación-manual)

