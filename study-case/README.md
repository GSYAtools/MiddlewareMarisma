# Script de Ingestión de Incidentes - Caso de Estudio

## Descripción

Este script simula la ingestión de incidentes a lo largo de 24 horas de forma aleatoria, y luego genera un reporte HTML con los datos recuperados:

**FASE 1 - Ingestión:**
- **Selecciona aleatoriamente 10 de los 20 incidentes** disponibles en la carpeta
- **Distribuye su lanzamiento de forma aleatoria** a lo largo de 24 horas
- **Actualiza automáticamente el campo `detected_at`** con la fecha/hora actual de ingestión
- **Registra el progreso** en `ingest_incidents.log` y en la consola

**FASE 2 - Recuperación y Reporte:**
- **Recupera todos los incidentes ingestados** usando `/retrieve_incident`
- **Maneja estados `pending`** - reintentos automáticos hasta que estén `completed`
- **Genera un reporte HTML** con estadísticas, gráficos y tabla de incidentes

## Requisitos

- Python 3.7+
- Paquete `requests`: `pip install requests`
- El servidor FastAPI debe estar en ejecución en `http://localhost:8000`

## Instalación de Dependencias

```powershell
pip install requests
```

## Uso

### Modo Normal (24 horas)

```powershell
cd c:\Users\GSYA Lab 01\Documents\GitHub\MiddlewareMarisma\study-case
python ingest_incidents.py
```

El script:
1. Leerá los 20 archivos `request_*.json`
2. Seleccionará 10 aleatoriamente
3. Los distribuirá a lo largo de 24 horas en momentos aleatorios
4. Ingestará cada uno actualizando el timestamp a la hora actual
5. Recuperará todos los incidentes usando `/retrieve_incident` (con reintentos si están pending)
6. Generará un reporte HTML con los datos recuperados
7. Registrará todo en `ingest_incidents.log`

### Detener el Script

Presiona `Ctrl+C` para interrumpir en cualquier momento. El script guardará un registro de lo que se procesó hasta ese momento.

## Configuración (Editable)

Si deseas cambiar los parámetros, edita `ingest_incidents.py`:

```python
# Línea 28-32
API_ENDPOINT = "http://localhost:8000/new_incident"  # URL del endpoint
STUDY_CASE_DIR = Path(__file__).parent  # Carpeta de incidentes
DURATION_HOURS = 24  # Duración total en horas
NUM_INCIDENTS_TO_INGEST = 10  # Cuántos incidentes ingestar
MAX_INCIDENTS = 20  # Total de incidentes disponibles
```

### Ejemplos:

**Para ingestar solo 5 incidentes en 12 horas:**
```python
DURATION_HOURS = 12
NUM_INCIDENTS_TO_INGEST = 5
```

## Salida

### Fase 1: Ingestión
```
2025-10-16 10:30:45,123 - INFO - INICIANDO INGESTIÓN DE INCIDENTES (24 HORAS)
2025-10-16 10:30:45,124 - INFO - Se encontraron 20 archivos de incidentes
2025-10-16 10:30:45,125 - INFO - Se cargaron exitosamente 10 incidentes para ingestar
...
2025-10-16 10:30:50,456 - INFO - ✓ Incidente ingestado exitosamente: ID=uuid-xxx, Amenaza=T001, Tipo=Unauthorized access
```

### Fase 2: Recuperación y Reporte
```
2025-10-16 10:35:12,789 - INFO - INICIANDO FASE 2: RECUPERACIÓN Y REPORTE
2025-10-16 10:35:12,790 - INFO - RECUPERANDO 10 INCIDENTES
2025-10-16 10:35:12,791 - INFO - [1/10] Recuperando incidente: uuid-xxx
2025-10-16 10:35:13,100 - INFO - ✓ Incidente uuid-xxx recuperado (status: completed)
...
2025-10-16 10:35:30,456 - INFO - ✓ Reporte generado exitosamente: reporte_20251016_103530.html
2025-10-16 10:35:30,457 - INFO - Abre en tu navegador: file:///C:/Users/.../reporte_20251016_103530.html
```

### Archivo de Reporte HTML
Se genera automáticamente un reporte `reporte_YYYYMMDD_HHMMSS.html` con:
- **Estadísticas generales** (total de incidentes, tasa de éxito)
- **Resumen por severidad** (crítica, alta, media, leve)
- **Resumen por tipo de amenaza**
- **Resumen por estado** (pending, completed, in_progress, etc.)
- **Tabla detallada** de todos los incidentes con sus atributos

El reporte se genera en la carpeta `study-case/` y se puede abrir directamente en un navegador web.

## Estructura de Datos

Cada incidente se actualiza antes de ser ingestado:

```json
{
  "threat_id": "T001",
  "user_id": "admin",
  "device_id": "Cámara WiFi",
  "detected_at": "2025-10-16T10:30:45.123456Z",  ← ACTUALIZADO A HORA ACTUAL
  "threat_type": "Unauthorized access",
  "threat_description": "...",
  "severity": "alta",
  "actions_taken": "...",
  "status": "resolved",
  "project_name": "Di4SPDS",
  "subproject_name": "SmartHome",
  "cause": "...",
  "controls": "A.05.01;A.05.03;A.06.01"
}
```

## Manejo de Estados `pending`

El script automáticamente:
1. Intenta recuperar cada incidente con `/retrieve_incident/{incident_id}`
2. Si el status es `pending`, espera 2 segundos e intenta de nuevo
3. Realiza hasta 30 intentos antes de fallar
4. Una vez que está `completed`, lo incluye en el reporte

Esto ocurre automáticamente durante la **FASE 2**.

## Monitoreo Durante la Ejecución

**Mientras el script se ejecuta:**

### Dos terminales:
1. **Terminal 1**: Ejecuta el script de ingestión
2. **Terminal 2**: Consulta el estado de incidentes

```powershell
# Obtener UUIDs ingestados (Terminal 2)
Get-Content ingest_incidents.log | Select-String "ID="
```

### Ver el log en tiempo real (Terminal 2)
```powershell
Get-Content -Path ingest_incidents.log -Wait
```

## Resolución de Problemas

### "Error de conexión al ingestar"
- Verifica que el servidor FastAPI esté en ejecución en `http://localhost:8000`
- Ejecuta: `uvicorn app:app --reload --host 0.0.0.0 --port 8000`

### "Error al parsear request_XXX.json"
- Verifica que los JSON sean válidos
- Ejecuta: `python -m json.tool request_*.json`

### Script muy rápido
- El script respeta los tiempos aleatorios. Si todo termina rápido, es porque los tiempos aleatorios fueron cortos
- Para aumentar tiempos, edita `DURATION_HOURS`

### Reporte no se genera
- Verifica que `/retrieve_incident` esté disponible en el servidor
- Revisa `ingest_incidents.log` para más detalles
- Verifica que al menos un incidente fue ingestado exitosamente

## Notas

- Los timestamps se generan al momento de ingestión, no al del JSON original
- Cada ejecución selecciona un conjunto diferente y aleatorio de 10 incidentes
- El script es tolerante a errores: si falla un incidente, continúa con el siguiente
- Los UUIDs retornados por el API se registran en el log
- La recuperación de incidentes se realiza automáticamente después de la ingestión
- El reporte HTML es independiente y se puede compartir o consultar en cualquier momento
