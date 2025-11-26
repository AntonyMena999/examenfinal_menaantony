# IMAGEN BASE
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto (80)
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]