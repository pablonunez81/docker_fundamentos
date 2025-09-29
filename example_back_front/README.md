# Ejemplo de Docker y Docker compose: Fundamentos
    docker compose build
    docker compose up
    ```

    Si deseas ejecutar los servicios en segundo plano, puedes usar:

    ```bash
    docker compose up -d
    ```

## Acceso al Sitio Web Frontend

   Una vez que los servicios estén en ejecución, puedes acceder al sitio web frontend abriendo tu navegador web y navegando a la siguiente dirección:

1. **Desde el host vía navegador web**
   ```
   http://localhost:8080/linktree.html


2. **Desde dentro del contenedor de frontend**
   ```
   > curl --location http://example_back_front-backend-1:5000/getMyInfo

   curl --location http://example_back_front-backend-1:5000/getMyInfo         
   {"author":"Juan Perez","blog":"https://juanperez.com","lastname":"Perez","name":"Juan","socialMedia":{"facebookUser":"juaniperez","githubUser":"juaniperez","instagramUser":"juaniperez","linkedin":"juan-perez","xUser":"juaniperez"}}