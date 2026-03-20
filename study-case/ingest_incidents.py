#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para ingestar incidentes de forma aleatoria durante 24 horas.
Selecciona 10 de 20 incidentes y los ingesta en momentos aleatorios.
Actualiza el campo 'detected_at' con la fecha/hora actual antes de enviar.
"""

import json
import random
import time
import os
import threading
from datetime import datetime, timedelta
from pathlib import Path
import requests
import logging
import sys

# Asegurar UTF-8 en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configurar logging con UTF-8
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ingest_incidents.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuración
API_ENDPOINT = "http://localhost:8000/new_incident"
STUDY_CASE_DIR = Path(__file__).parent
DURATION_HOURS = 0.05
NUM_INCIDENTS_TO_INGEST = 2
MAX_INCIDENTS = 20

class IncidentIngester:
    def __init__(self):
        self.study_case_dir = STUDY_CASE_DIR
        self.api_endpoint = API_ENDPOINT
        self.incidents_to_ingest = []
        self.ingested_incident_ids = []  # Guardar IDs de incidentes ingestados
        self.retrieved_incidents = []    # Guardar incidentes recuperados
        self.ingested_count = 0
        self.failed_count = 0
        self.count_lock = threading.Lock()  # Lock para sincronización de contadores
        self.active_threads = []  # Guardar referencias a hilos activos
        
    def load_incidents(self):
        """Carga todos los archivos de incidentes disponibles."""
        incident_files = sorted(self.study_case_dir.glob("request_*.json"))
        
        if not incident_files:
            logger.error(f"No se encontraron archivos de incidentes en {self.study_case_dir}")
            return False
        
        logger.info(f"Se encontraron {len(incident_files)} archivos de incidentes")
        
        # Seleccionar 10 aleatorios de los 20
        selected_files = random.sample(incident_files, min(NUM_INCIDENTS_TO_INGEST, len(incident_files)))
        
        for file_path in selected_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    incident = json.load(f)
                    self.incidents_to_ingest.append(incident)
                    logger.info(f"Incidente cargado: {file_path.name}")
            except json.JSONDecodeError as e:
                logger.error(f"Error al parsear {file_path.name}: {e}")
            except Exception as e:
                logger.error(f"Error al cargar {file_path.name}: {e}")
        
        if self.incidents_to_ingest:
            logger.info(f"Se cargaron exitosamente {len(self.incidents_to_ingest)} incidentes para ingestar")
            return True
        else:
            logger.error("No se pudo cargar ningún incidente")
            return False
    
    def shuffle_incidents(self):
        """Baraja la lista de incidentes."""
        random.shuffle(self.incidents_to_ingest)
        logger.info(f"Incidentes barajeados. Orden de ingestión:")
        for idx, incident in enumerate(self.incidents_to_ingest, 1):
            logger.info(f"  {idx}. {incident.get('threat_id', 'Unknown')} - {incident.get('threat_type', 'Unknown')}")
    
    def generate_random_timestamps(self):
        """
        Genera timestamps aleatorios distribuidos a lo largo de 24 horas.
        Retorna una lista de (delay_en_segundos, incidente) ordenada por delay.
        """
        now = datetime.now()
        end_time = now + timedelta(hours=DURATION_HOURS)
        total_seconds = DURATION_HOURS * 3600
        
        # Generar valores aleatorios de delay entre 0 y total_seconds
        delays = sorted([random.uniform(0, total_seconds) for _ in range(len(self.incidents_to_ingest))])
        
        result = []
        for delay, incident in zip(delays, self.incidents_to_ingest):
            result.append((delay, incident))
        
        logger.info(f"\nDistribución de incidentes en 24 horas:")
        for idx, (delay, incident) in enumerate(result, 1):
            scheduled_time = now + timedelta(seconds=delay)
            logger.info(f"  {idx}. {incident.get('threat_id')} - Programado para: {scheduled_time.strftime('%H:%M:%S')}")
        
        return result
    
    def ingest_incident(self, incident):
        """
        Ingesta un incidente actualizando el campo 'detected_at' con la hora actual.
        """
        try:
            # Actualizar 'detected_at' con la fecha/hora actual en formato ISO
            incident['detected_at'] = datetime.now().isoformat() + 'Z'
            
            # Realizar POST request
            response = requests.post(
                self.api_endpoint,
                json=incident,
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    incident_id = response_data.get('request_id', 'Unknown')
                    # Guardar el ID para recuperarlo luego
                    if incident_id != 'Unknown':
                        with self.count_lock:
                            self.ingested_incident_ids.append(incident_id)
                except:
                    incident_id = 'Unknown'
                
                logger.info(
                    f"✓ Incidente ingestado exitosamente: "
                    f"ID={incident_id}, "
                    f"Amenaza={incident.get('threat_id')}, "
                    f"Tipo={incident.get('threat_type')}"
                )
        
                with self.count_lock:
                    self.ingested_count += 1
                return True
            else:
                logger.error(
                    f"✗ Error al ingestar incidente {incident.get('threat_id')}: "
                    f"Status {response.status_code} - {response.text}"
                )
                with self.count_lock:
                    self.failed_count += 1
                return False
                
        except requests.exceptions.ConnectionError:
            logger.error(
                f"✗ Error de conexión al ingestar {incident.get('threat_id')}: "
                f"No se puede conectar a {self.api_endpoint}"
            )
            with self.count_lock:
                self.failed_count += 1
            return False
        except requests.exceptions.Timeout:
            logger.error(
                f"✗ Timeout al ingestar {incident.get('threat_id')}: "
                f"Solicitud tardó demasiado"
            )
            with self.count_lock:
                self.failed_count += 1
            return False
        except Exception as e:
            logger.error(
                f"✗ Error inesperado al ingestar {incident.get('threat_id')}: {e}"
            )
            with self.count_lock:
                self.failed_count += 1
            return False
    
    def _ingest_incident_scheduled(self, delay_seconds, incident, idx, total):
        """
        Función para ser ejecutada en un hilo: espera delay_seconds y luego ingesta el incidente.
        Se ejecuta de forma asíncrona sin bloquear el hilo principal.
        """
        threat_id = incident.get('threat_id', 'Unknown')
        
        try:
            # Esperar el tiempo programado
            logger.info(f"[{idx}/{total}] ⏱️  Hilo iniciado: {threat_id} se lanzará en {delay_seconds:.1f}s")
            time.sleep(delay_seconds)
            
            # Ingestar en el momento programado
            logger.info(f"[{idx}/{total}] 🚀 Lanzando incidente: {threat_id}")
            self.ingest_incident(incident)
            
        except Exception as e:
            logger.error(f"Error en hilo de ingestión para {threat_id}: {e}")
    
    def retrieve_incident_with_retry(self, incident_id, max_retries=30, retry_delay=2):
        """
        Recupera un incidente usando /retrieve_incident.
        Si está en estado 'pending', reintentas hasta que esté 'completed'.
        """
        retrieve_endpoint = f"http://localhost:8000/retrive_incident/{incident_id}"
        retries = 0
        
        while retries < max_retries:
            try:
                response = requests.get(retrieve_endpoint, timeout=10)
                
                if response.status_code == 200:
                    incident_data = response.json()
                    status = incident_data.get('status', 'unknown')
                    
                    if status == 'completed':
                        logger.info(f"✓ Incidente {incident_id} recuperado (status: completed)")
                        return incident_data
                    elif status == 'pending':
                        retries += 1
                        logger.debug(f"  Incidente {incident_id} aún en estado 'pending' (intento {retries}/{max_retries})...")
                        time.sleep(retry_delay)
                        continue
                    else:
                        logger.warning(f"⚠ Incidente {incident_id} tiene status desconocido: {status}")
                        return incident_data
                else:
                    retries += 1
                    logger.debug(f"  Error al recuperar {incident_id}: Status {response.status_code} (intento {retries}/{max_retries})")
                    if retries < max_retries:
                        time.sleep(retry_delay)
                    continue
                    
            except requests.exceptions.ConnectionError:
                retries += 1
                logger.debug(f"  Error de conexión al recuperar {incident_id} (intento {retries}/{max_retries})")
                if retries < max_retries:
                    time.sleep(retry_delay)
                continue
            except Exception as e:
                retries += 1
                logger.debug(f"  Error al recuperar {incident_id}: {e} (intento {retries}/{max_retries})")
                if retries < max_retries:
                    time.sleep(retry_delay)
                continue
        
        logger.error(f"✗ No se pudo recuperar el incidente {incident_id} después de {max_retries} intentos")
        return None
    
    def retrieve_all_incidents(self):
        """Recupera todos los incidentes ingestados."""
        if not self.ingested_incident_ids:
            logger.warning("No hay incidentes para recuperar")
            return False
        
        logger.info("\n" + "=" * 70)
        logger.info(f"RECUPERANDO {len(self.ingested_incident_ids)} INCIDENTES")
        logger.info("=" * 70)
        
        for idx, incident_id in enumerate(self.ingested_incident_ids, 1):
            logger.info(f"\n[{idx}/{len(self.ingested_incident_ids)}] Recuperando incidente: {incident_id}")
            incident_data = self.retrieve_incident_with_retry(incident_id)
            
            if incident_data:
                self.retrieved_incidents.append(incident_data)
            else:
                logger.error(f"No se pudo recuperar el incidente {incident_id}")
        
        logger.info(f"\nRecuperados {len(self.retrieved_incidents)} de {len(self.ingested_incident_ids)} incidentes")
        return len(self.retrieved_incidents) > 0
    
    def generate_report(self):
        """Genera un reporte HTML con los incidentes recuperados."""
        if not self.retrieved_incidents:
            logger.warning("No hay incidentes para generar reporte")
            return
        
        logger.info("\n" + "=" * 70)
        logger.info("GENERANDO REPORTE")
        logger.info("=" * 70)
        
        # Calcular estadísticas
        total_incidents = len(self.retrieved_incidents)
        severities = {}
        threat_types = {}
        statuses = {}
        
        for incident in self.retrieved_incidents:
            severity = incident.get('severity', 'unknown')
            threat_type = incident.get('threat_type', 'unknown')
            status = incident.get('status', 'unknown')
            
            severities[severity] = severities.get(severity, 0) + 1
            threat_types[threat_type] = threat_types.get(threat_type, 0) + 1
            statuses[status] = statuses.get(status, 0) + 1
        
        # Generar HTML
        html_report = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Caso de Estudio - Middleware Marisma</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid #667eea;
        }}
        .stat-card h3 {{
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        .stat-card .value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #333;
        }}
        .summary-section {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-section h2 {{
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}
        .summary-item {{
            background: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            border-left: 3px solid #667eea;
        }}
        .summary-item h4 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .summary-item ul {{
            list-style-position: inside;
        }}
        .summary-item li {{
            padding: 5px 0;
        }}
        .incidents-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        .incidents-table th {{
            background-color: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        .incidents-table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
        }}
        .incidents-table tbody tr:hover {{
            background-color: #f9f9f9;
        }}
        .severity-critica {{
            background-color: #fee;
            color: #c00;
            padding: 5px 10px;
            border-radius: 3px;
            font-weight: bold;
        }}
        .severity-alta {{
            background-color: #fef3cd;
            color: #856404;
            padding: 5px 10px;
            border-radius: 3px;
            font-weight: bold;
        }}
        .severity-media {{
            background-color: #d1ecf1;
            color: #0c5460;
            padding: 5px 10px;
            border-radius: 3px;
            font-weight: bold;
        }}
        .severity-leve {{
            background-color: #d4edda;
            color: #155724;
            padding: 5px 10px;
            border-radius: 3px;
            font-weight: bold;
        }}
        .status-completed {{
            color: #28a745;
            font-weight: bold;
        }}
        .status-pending {{
            color: #ffc107;
            font-weight: bold;
        }}
        .status-in_progress {{
            color: #007bff;
            font-weight: bold;
        }}
        footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Reporte de Caso de Estudio</h1>
            <p>Middleware Marisma - Ingestión de Incidentes Automatizada</p>
            <p>Generado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </header>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>✓ Incidentes Totales</h3>
                <div class="value">{total_incidents}</div>
            </div>
            <div class="stat-card">
                <h3>📍 Incidentes Ingestados</h3>
                <div class="value">{self.ingested_count}</div>
            </div>
            <div class="stat-card">
                <h3>❌ Errores</h3>
                <div class="value">{self.failed_count}</div>
            </div>
            <div class="stat-card">
                <h3>📈 Tasa de Éxito</h3>
                <div class="value">{(self.ingested_count / (self.ingested_count + self.failed_count) * 100):.1f}%</div>
            </div>
        </div>
        
        <div class="summary-section">
            <h2>📋 Resumen de Incidentes</h2>
            <div class="summary-grid">
                <div class="summary-item">
                    <h4>Por Severidad</h4>
                    <ul>
                        {''.join([f"<li><strong>{sev}</strong>: {count} incidentes</li>" for sev, count in sorted(severities.items())])}
                    </ul>
                </div>
                <div class="summary-item">
                    <h4>Por Tipo de Amenaza</h4>
                    <ul>
                        {''.join([f"<li><strong>{ttype}</strong>: {count} incidentes</li>" for ttype, count in sorted(threat_types.items(), key=lambda x: -x[1])[:10]])}
                    </ul>
                </div>
                <div class="summary-item">
                    <h4>Por Estado</h4>
                    <ul>
                        {''.join([f"<li><strong>{st}</strong>: {count} incidentes</li>" for st, count in sorted(statuses.items())])}
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="summary-section">
            <h2>📄 Detalle de Incidentes</h2>
            <table class="incidents-table">
                <thead>
                    <tr>
                        <th>ID Incidente</th>
                        <th>Amenaza</th>
                        <th>Tipo</th>
                        <th>Severidad</th>
                        <th>Estado</th>
                        <th>Detectado</th>
                        <th>Subproyecto</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join([f"""
                    <tr>
                        <td>{incident.get('incident_id', 'N/A')}</td>
                        <td>{incident.get('threat_id', 'N/A')}</td>
                        <td>{incident.get('threat_type', 'N/A')}</td>
                        <td><div class="severity-{incident.get('severity', 'unknown')}">{incident.get('severity', 'N/A')}</div></td>
                        <td><span class="status-{incident.get('status', 'unknown').lower().replace(' ', '_')}">{incident.get('status', 'N/A')}</span></td>
                        <td>{incident.get('detected_at', 'N/A')}</td>
                        <td>{incident.get('subproject_name', 'N/A')}</td>
                    </tr>
                    """ for incident in self.retrieved_incidents])}
                </tbody>
            </table>
        </div>
        
        <footer>
            <p>Reporte generado automáticamente por el Sistema de Ingestión de Incidentes</p>
            <p>Archivos de log: ingest_incidents.log</p>
        </footer>
    </div>
</body>
</html>
        """
        
        # Guardar reporte
        report_path = self.study_case_dir / f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(html_report)
            logger.info(f"✓ Reporte generado exitosamente: {report_path.name}")
            logger.info(f"  Abre en tu navegador: file:///{report_path.absolute()}")
            return str(report_path)
        except Exception as e:
            logger.error(f"✗ Error al generar reporte: {e}")
            return None
    
    def run(self):
        """Ejecuta el ciclo de ingestión usando hilos para no bloquear."""
        logger.info("=" * 70)
        logger.info("INICIANDO INGESTIÓN DE INCIDENTES (MULTIHILO)")
        logger.info("=" * 70)
        
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=DURATION_HOURS)
        
        logger.info(f"Hora de inicio: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"Hora de fin esperada: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("")
        
        # Cargar incidentes
        if not self.load_incidents():
            logger.error("No se pudieron cargar los incidentes. Abortando.")
            return False
        
        # Barajar y distribuir
        self.shuffle_incidents()
        logger.info("")
        
        scheduled_incidents = self.generate_random_timestamps()
        logger.info("")
        
        # Ingestar incidentes usando hilos
        logger.info("Creando hilos para lanzar incidentes en el momento programado...")
        logger.info("-" * 70)
        
        try:
            # Crear un hilo para cada incidente
            threads = []
            for idx, (delay, incident) in enumerate(scheduled_incidents, 1):
                thread = threading.Thread(
                    target=self._ingest_incident_scheduled,
                    args=(delay, incident, idx, len(scheduled_incidents)),
                    name=f"ingestion-{idx}-{incident.get('threat_id', 'unknown')}"
                )
                thread.daemon = False  # No es daemon para que espere a terminar
                thread.start()
                threads.append(thread)
                logger.info(f"[{idx}/{len(scheduled_incidents)}] Hilo creado para: {incident.get('threat_id', 'Unknown')}")
            
            logger.info("\n" + "-" * 70)
            logger.info(f"Se crearon {len(threads)} hilos. Esperando a que terminen...")
            logger.info("-" * 70 + "\n")
            
            # Esperar a que todos los hilos terminen
            for thread in threads:
                thread.join()
            
            logger.info("\n" + "=" * 70)
            logger.info("Todos los hilos han terminado.")
            logger.info("=" * 70)
            logger.info(f"Incidentes ingestados exitosamente: {self.ingested_count}")
            logger.info(f"Incidentes con error: {self.failed_count}")
            logger.info(f"Total procesado: {self.ingested_count + self.failed_count}")
            logger.info(f"Hora de finalización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            if self.failed_count > 0:
                logger.warning(f"\n⚠ Se encontraron {self.failed_count} errores durante la ingestión.")
            else:
                logger.info("\n✓ Todos los incidentes fueron ingestados exitosamente.")
            
            # FASE 2: Recuperar incidentes y generar reporte
            logger.info("\n" + "=" * 70)
            logger.info("INICIANDO FASE 2: RECUPERACIÓN Y REPORTE")
            logger.info("=" * 70)
            
            if self.retrieve_all_incidents():
                self.generate_report()
                logger.info("\n✓ Proceso completado: Incidentes recuperados y reporte generado")
            else:
                logger.error("\n✗ No se pudieron recuperar los incidentes para generar el reporte")
            
            return True
            
        except KeyboardInterrupt:
            logger.warning("\n\n⚠ Ingestión interrumpida por el usuario")
            logger.info(f"Incidentes ingestados: {self.ingested_count}")
            logger.info(f"Incidentes con error: {self.failed_count}")
            return False
        except Exception as e:
            logger.error(f"\n✗ Error fatal durante la ejecución: {e}")
            return False

def main():
    """Función principal."""
    ingester = IncidentIngester()
    success = ingester.run()
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
