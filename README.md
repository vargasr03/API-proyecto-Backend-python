# ProyectoAPI 
Este proyecto implementa una API RESTful utilizando FastAPI para gestionar recetas culinarias. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre las recetas almacenadas en una base de datos SQLite. 
## Instalación 
1. Clona el repositorio: https://github.com/codingwthisa/fastapi-recipes-api.git
2. Accede al directorio del proyecto: cd fastapi-recipes-api
3. Instala las dependencias utilizando pip (se recomienda usar un entorno virtual): pip install -r requirements.txt

## Ejecución 
1. Una vez instaladas las dependencias, se puede ejecutar la aplicación utilizando uvicorn: uvicorn main:app --reload
2. La aplicación estará disponible en http://localhost:8000 en el navegador o cliente de API.

## Endpoints 
### Crear una receta 
- **URL:** `/recipes/` 
- **Método HTTP:** POST 
- **Body:** JSON con los datos de la receta (title, description, ingredients, instructions) 
- **Respuesta:** JSON con los datos de la receta creada 

### Leer una receta 
- **URL:** `/recipes/{recipe_id}` - }
- **Método HTTP:** GET 
- **Parámetro de ruta:** `recipe_id` (ID de la receta) 
- **Respuesta:** JSON con los datos de la receta solicitada

### Leer todas las recetas 
- **URL:** `/recipes/`
- **Método HTTP:** GET
- **Parámetros de consulta opcionales:** `skip` (número de registros a omitir), `limit` (número máximo de registros a devolver)
- **Respuesta:** JSON con una lista de todas las recetas
- 
### Actualizar una receta 
- **URL:** `/recipes/{recipe_id}` 
- **Método HTTP:** PUT - **Parámetro de ruta:** `recipe_id` (ID de la receta a actualizar)
- **Body:** JSON con los datos actualizados de la receta (title, description, ingredients, instructions)
- **Respuesta:** JSON con los datos de la receta actualizada ### Borrar una receta
- **URL:** `/recipes/{recipe_id}`
- **Método HTTP:** DELETE
- **Parámetro de ruta:** `recipe_id` (ID de la receta a borrar)
- **Respuesta:** JSON con los datos de la receta borrada
