##🏗️ Fase 1: El Proyecto "Virtual" (Coste 0€)

En lugar de usar un sensor propio, vamos a "secuestrar" (con permiso) los datos de estaciones GNSS profesionales. La red IGS y la EUSPA ofrecen flujos de datos en tiempo real (NTRIP) de estaciones repartidas por toda España.
Pasos para empezar hoy mismo:

    Registro en el GSC: Regístrate en el European GNSS Service Centre. Es gratis y te dará acceso a datos de Galileo que no cualquiera tiene.

    El "SysAdmin" Pipeline (Docker):

        Monta un contenedor con RTKLIB (concretamente el comando str2str).

        Este contenedor se conectará por red a una estación de la red IGS (ej. una en Madrid o Barcelona).

        Recibirás datos RTCM (mensajes comprimidos de satélites).

    Investigación: Tu misión será crear un script que procese esos mensajes y extraiga cuántos satélites Galileo está viendo esa estación profesional en comparación con GPS.

Componente,Recomendación,Precio aprox.,¿Dónde comprar?
Módulo GNSS,u-blox NEO-M9N o M10,25€ - 40€,AliExpress / Amazon / Tiendas de robótica (p. ej. Ro-Botica)
Antena,Antena activa de cerámica (mínimo 25dB),10€ - 15€,Viene a veces con el módulo
Microcontrolador,Arduino (Uno/ESP32),Ya lo tienes,-
Adaptador USB-TTL,Para conectar el módulo directo al PC y depurar,5€,Amazon
TOTAL,,~40€ - 55€,
