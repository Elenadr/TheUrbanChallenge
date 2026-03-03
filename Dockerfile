# Imagen base ligera de Debian
FROM debian:bookworm-slim

# Instalar dependencias para compilar RTKLIB
RUN apt-get update && apt-get install -y \
    git \
    make \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Clonar y compilar RTKLIB (versión demo5 que es excelente para Galileo)
RUN git clone https://github.com/rtklibexplorer/RTKLIB.git /opt/rtklib \
    && cd /opt/rtklib/app/consapp/str2str/gcc \
    && make

# Añadir el binario al PATH
ENV PATH="/opt/rtklib/app/consapp/str2str/gcc:${PATH}"

EXPOSE 9000

# Comando por defecto
CMD ["str2str"]
