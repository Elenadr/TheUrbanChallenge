
# 🛰️ Galileo Sentinel: GNSS Real-Time Monitor

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)](https://github.com/tu-usuario/galileo-sentinel)
[![Galileo Constellation](https://img.shields.io/badge/Constellation-Galileo-blue.svg)](https://www.gsc-europa.eu/)

Este proyecto es una infraestructura de monitorización de la constelación europea **Galileo** en tiempo real. Utiliza microservicios (Docker) para procesar flujos de datos GNSS profesionales (NTRIP) y analizar la disponibilidad y precisión de los satélites.

## 🏗️ Arquitectura de Sistemas
- **Ingesta:** RTKLIB (str2str) en contenedor Docker.
- **Procesado:** Python 3.x con análisis de sentencias NMEA/RTCM.
- **Fuentes de datos:** EUSPA GSC & IGN España (NTRIP Casters).

## 🚀 Cómo empezar
1. Asegúrate de tener **Docker** instalado.
2. Levanta el puente de datos:
   ```bash
   docker-compose up -d
```

3. Ejectura el monitor
```bash
python src/main.py
```
---
Proyecto en desarrollo para fomentar el uso de la soberanía tecnológica europea (Galileo).



----
## Troubleshooting

| -- | -- | -- |
| Desafío | Diagnóstico del errpr | Solución |
| -- | -- | -- |
|Docker Daemon Error | Docker motor was not installed by default on Kali | Install docker.io, manage services with systemctl and configuration of group permisions|
| -- | -- | -- |
| 401 Unauthorized | Error de autenticación en los servidores NTRIP.  | Depuración de credenciales y validación de sintaxis en la cadena de conexión de str2str. |
| -- | -- | -- |
| Binary Output (Garbage) | Los datos llegaban en binario RTCM3, ilegibles para un parser de texto estándar. | Implementación de un decodificador avanzado con la librería pyrtcm para interpretar los frames binarios directamente.|
| -- | -- | -- |
