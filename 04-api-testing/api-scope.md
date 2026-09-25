# API Testing - Alcance

## API
Swagger Petstore

## Alcance funcional
Gestión de mascotas (pet).

## Operaciones seleccionadas

| Método HTTP | Endpoint | Propósito |
|---|---|---|
| POST | /v2/pet | Agregar una nueva mascota a la tienda |
| GET | /v2/pet/{petId} | Buscar una mascota específica por su ID |
| PUT | /v2/pet | Actualizar los datos de una mascota existente |
| DELETE | /v2/pet/{petId} | Eliminar una mascota del sistema por su ID |

## Justificación
Se seleccionaron estas cuatro operaciones porque representan el ciclo de vida CRUD completo (Crear, Leer, Actualizar y Borrar) del recurso principal de la API (`pet`). Probar estas operaciones principales permite validar de manera integral la integridad y persistencia de los datos del negocio dentro del alcance funcional establecido.

## Condiciones de prueba identificadas
* **Escenarios Positivos:**
  * Creación exitosa de un recurso enviando un JSON válido estructurado con los campos obligatorios.
  * Recuperación y visualización correcta del recurso previamente creado utilizando su identificador único.
  * Modificación exitosa del recurso asegurando que los cambios impacten correctamente el backend.
  * Remoción completa y exitosa del recurso mediante su ID.
* **Escenarios Negativos:**
  * Búsqueda de recursos inexistentes empleando un identificador aleatorio o inválido para comprobar el manejo controlado de errores del servidor.

## Fuera de alcance
Se excluyen las operaciones de carga de archivos (`POST /v2/pet/{petId}/uploadImage`) y búsquedas masivas por estado (`GET /v2/pet/findByStatus`) o etiquetas (`GET /v2/pet/findByTags`), ya que el enfoque primordial radica en garantizar la consistencia y estabilidad transaccional de los flujos individuales sobre el recurso `pet`.
