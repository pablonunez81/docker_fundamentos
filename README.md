# Ejemplos de Docker y Docker Compose

Este directorio contiene dos proyectos de ejemplo para aprender a usar Docker y Docker Compose:

## 1. example_back

- Backend sencillo en Python (Flask).
- Incluye un `Dockerfile` para construir la imagen del backend.
- Permite ejecutar el servicio en un contenedor Docker.

## 2. example_back_front

- Proyecto con backend (Python/Flask) y frontend (HTML/JS).
- Utiliza `docker-compose.yml` para levantar ambos servicios en contenedores separados.
- Ideal para entender cómo orquestar múltiples servicios con Docker Compose.

### Estructura

```
example_back/
  app.py
  Dockerfile
  requirements.txt

example_back_front/
  docker-compose.yml
  backend/
    app.py
    Dockerfile
    requirements.txt
  frontend/
    Dockerfile
    sitio/
      linktree.html
      requests.js
```

### Uso rápido

Las imágenes de backend y frontend ya están publicadas en Docker Hub:

- Backend: [`pablonunez81/example_back_front_backend:latest`](https://hub.docker.com/r/pablonunez81/example_back_front_backend)
- Frontend: [`pablonunez81/example_back_front_frontend:latest`](https://hub.docker.com/r/pablonunez81/example_back_front_frontend)

Puedes usarlas directamente con Docker o Docker Compose, sin necesidad de construirlas localmente.

#### example_back
1. Construir la imagen:
   ```sh
   docker build -t example_back .
   ```
2. Ejecutar el contenedor:
   ```sh
   docker run -p 5000:5000 example_back
   ```

#### example_back_front
1. Levantar los servicios:
   ```sh
   docker-compose up --build
   ```
2. Acceder al backend y frontend según los puertos configurados en `docker-compose.yml`.

---

Estos ejemplos son útiles para comprender los conceptos básicos de Docker y Docker Compose, así como la separación de servicios en aplicaciones modernas.
