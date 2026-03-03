# Índice
- [Fase 1](#fase-1)
- [Fase 2](#fase-2)
- [Fase 3](#fase-1)
- [Fase 4](#fase-2)


## Fase 1: 
### La Infrastructura (SysAdmin Puro) 🏗️

* Antes de mirar los satélites, monta el "laboratorio".

    Configurar un Stack de Observabilidad: Instalar Docker y desplegar un contenedor con InfluxDB (base de datos de series temporales) y Grafana.

    Seguridad: Configurar un firewall y, si usas varios nodos, una VPN ligera (como WireGuard) para que los datos viajen seguros desde el sensor al servidor central.

## Fase 2:
### Ingesta de Datos (El Corazón de Galileo) 🛰️

* Aquí es donde entra la investigación técnica.

    Instalar RTKLIB (un software open-source de referencia en el sector espacial) en tu servidor.

    Configurar un servicio que "escuche" al satélite y separe los mensajes: los de GPS (Constelación G) de los de Galileo (Constelación E).

    El reto técnico: Implementar la captura de mensajes OSNMA (Open Service Navigation Message Authentication). Esto es lo que hace a Galileo único: es la primera constelación que "firma" sus mensajes para evitar hackeos de posición. Objetivo: Lograr Galileo Message Authenticated: TRUE.

  ## Fase 3:
  ### El Algoritmo de "Duelo" (Investigación) 🧮

* Crea un script en Python que haga lo siguiente:

    - Calcule la posición solo usando satélites GPS.
    - Calcule la posición solo usando satélites Galileo.
    - Compare ambas con un "Ground Truth" (tu posición real en Google Maps/OpenStreetMap).
    - Exporte la diferencia (el error en metros) a tu base de datos cada segundo.
 
## Fase 4: 
### Visualización y Divulgación (El Click-Bait) 🎨

* Crea el Dashboard de Grafana que el público de a pie pueda entender:

    - "Ranking de Precisión": Un marcador tipo partido de fútbol (Galileo 0.8m vs GPS 2.1m).
    - "Mapa de Calor de Confianza": Un mapa de tu calle donde se vea dónde la señal europea es más sólida.
    - Estado de la Constelación: Cuántos satélites Galileo ves ahora mismo (ej. "GSAT-0220 activo").
