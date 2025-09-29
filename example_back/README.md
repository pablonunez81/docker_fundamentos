# Proyecto de Ejemplo: Fundamentos de Docker

Este repositorio contiene un proyecto de ejemplo diseñado para ilustrar los conceptos fundamentales de Docker. A través de este proyecto, podrás aprender a:

- **Contenerizar aplicaciones:** Empaquetar tu aplicación y todas sus dependencias en un contenedor Docker.
- **Construir imágenes Docker:** Crear imágenes personalizadas a partir de un `Dockerfile`.
- **Ejecutar contenedores:** Iniciar y gestionar contenedores Docker.
- **Gestionar volúmenes:** Persistir datos generados por los contenedores.
- **Utilizar redes Docker:** Conectar contenedores entre sí.

## Contenido del Repositorio

El repositorio incluye los siguientes archivos y directorios:

- `Dockerfile`: Define cómo construir la imagen Docker de la aplicación.
- `app.py`: Un script Python de ejemplo que representa la aplicación.
- `requirements.txt`: Lista de dependencias de Python para la aplicación.
- `docker-compose.yml` (opcional): Archivo para definir y ejecutar aplicaciones Docker multi-contenedor.
- `README.md`: Este archivo de documentación.

## Requisitos Previos

Para ejecutar este proyecto, necesitarás tener Docker instalado en tu sistema. Puedes descargarlo desde el [sitio web oficial de Docker](https://www.docker.com/get-started).

## Cómo Empezar

Sigue estos pasos para construir y ejecutar la aplicación con Docker:

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Prueba en entorno local sin docker**
   ```      
   python -m venv venv
   .\venv\Scripts\activate
   pip install flask
   python -m flask run

   link: http://127.0.0.1:5000/getMyInfo
   ```

3. **Construye la imagen Docker:**
   ```bash
   docker build -t mi-aplicacion-docker .
   ```
   Este comando construirá una imagen llamada `mi-aplicacion-docker` a partir del `Dockerfile` en el directorio actual.

4. **Ejecuta el contenedor Docker:**
   ```bash
   docker run -p 5000:5000 mi-aplicacion-docker
   docker run -it --rm -d -p 5000:5000 --name web_app_python app_python
   
5. **Ejecutarlo valiendose del docker hub.**
   ```bash
   docker run -it --rm -d -p 5000:5000 --name web_app_python pablonunez81/app_python