import socket

# Configuración del receptor virtual (nuestro contenedor Docker)
HOST = '127.0.0.1'
PORT = 9000

def parse_gnss():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"🛰️ Conectado al flujo Galileo en el puerto {PORT}...")
        
        while True:
            data = s.recv(1024).decode('utf-8', errors='ignore')
            lines = data.split('\n')
            for line in lines:
                if '$GPGSV' in line or '$GAGSV' in line:
                    # $GAGSV son los mensajes específicos de GALILEO
                    print(f"📡 Señal detectada: {line.strip()}")

if __name__ == "__main__":
    parse_gnss()
