import socket
from pyrtcm import RTCMReader

def monitor_galileo_binario():
    # Conectamos al flujo de "caracteres raros"
    stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stream.connect(('127.0.0.1', 9000))
    
    print("🛰️ Decodificador RTCM3 iniciado. Escuchando constelaciones...")

    # El RTCMReader se encarga de limpiar la "basura" y buscar mensajes reales
    rtr = RTCMReader(stream)

    for (raw_data, parsed_data) in rtr:
        msg_id = parsed_data.identity
        
        # Los mensajes 1045 y 1046 son EXCLUSIVOS de Galileo
        if msg_id in ['1045', '1046']:
            print(f"🇪🇺 [GALILEO] Mensaje detectado: {msg_id} - Efemérides recibidas")
        
        # Mensajes de observación (donde están los satélites)
        elif msg_id.startswith('107'): # 107x = GPS
            print(f"🇺🇸 [GPS] Datos de observación: {msg_id}")
        elif msg_id.startswith('109'): # 109x = Galileo MSM
            print(f"🇪🇺 [GALILEO] Datos de observación MSM: {msg_id}")

if __name__ == "__main__":
    monitor_galileo_binario()
