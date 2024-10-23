# Clasificación de Imágenes de Perros y Gatos

Este proyecto es una aplicación que utiliza un backend en Flask, donde se entrena un modelo con TensorFlow para clasificar imágenes de perros y gatos. El frontend está desarrollado en Angular y realiza solicitudes al backend para obtener predicciones.


## Requisitos

Tener instalado Python, pip y Node.js. 

    git clone https://github.com/Xonazo/PetClassifier.git

    cd PetClassifier

### Backend (Flask)

1. **Crea un entorno virtual:**

   ```bash
   python -m venv venv


2. **Activar el entorno virtual:**

- En Windows:

  ```
  venv\Scripts\activate
  ```

- En macOS y Linux:

  ```
  source venv/bin/activate
  ```


3. **Instalar las dependencias desde `requirements.txt`:**

        pip install -r requirements.txt


### Frontend (Angular)

1. **Instalar Angular CLI**:

        npm install -g @angular/cli


2. **Navegar a la carpeta del frontend:**

        cd /frontend


3. **Instalar las dependencias del proyecto Angular:**

        npm install


## Entrenamiento del Modelo

Para entrenar el modelo, ejecuta el archivo `predict.py`. Asegúrate de que la carpeta `images` contenga dos subcarpetas: `dogs` y `cats`, donde cada una debe tener imágenes de perros y gatos. Puedes descargar el dataset desde el siguiente enlace:

[Stanford Dogs Dataset](https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset)

### Ejecutar el archivo `predict.py`
Este comando entrenará el modelo y generará un archivo con el modelo entrenado.

        python predict.py



## Ejecutando el Servidor

Después de entrenar el modelo, ejecuta el archivo `server.py` para iniciar el servidor Flask.

        python server.py


El servidor estará disponible en la ruta `/predict`, donde podrás enviar imágenes para recibir predicciones.


```http
  POST /predict/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `file`      | `file` | **Required**. Imagen a clasificar (formato: jpg, jpeg, png) |

Esto devolvera si la imagen enviada corresponde a un perro o un gato.



## Frontend

1. **Navegar a la carpeta del proyecto Angular:**

        cd /frontend


2. **Instalar las dependencias del proyecto Angular:**

        npm install

3. **Abrir el navegador y acceder a:**

        http://localhost:4200

4. **Interacción con la Página Principal:**

Al iniciar el frontend, se te dirigirá a la página principal donde se encontrara un formulario para cargar una imagen.

#### Cargar Imágenes:

Usa el formulario para seleccionar una imagen .
Una vez que la imagen se suba, se enviará al backend mediante una solicitud POST a la ruta /predict.
#### Recibir Predicciones:

Después de enviar la imagen, el backend procesará la solicitud y devolverá si la imagen corresponde a un perro o un gato.


## Contribuciones

Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.


