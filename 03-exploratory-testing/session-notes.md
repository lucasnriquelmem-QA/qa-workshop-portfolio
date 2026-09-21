# Sesión 1

## Charter
Explorar el comportamiento del carrito al iniciar sesión durante la compra — misión: descubrir si el carrito se pierde, se duplica o se mezcla al loguearse en distintos puntos del flujo.

## ÁREAS
Catálogo, Carrito de compras, Sign In / Sign Out. Navegador en modo incógnito, sitio: petstore.octoperf.com

## INICIO
12:00

## TESTER
Lucas

## DESGLOSE DE TAREAS
- Armado de carrito como usuario anónimo: [2 min]
- Login con carrito ya armado: [2 min]
- Login primero, luego armado de carrito: [2 min]
- Cierre de sesión con carrito activo: [2 min]
- Prueba con dos sesiones simultáneas: [2 min]

## ARCHIVOS DE DATOS
Usuario: j2ee / j2ee
Productos usados: Large Angelfish, Adult Male Chihuahua

## NOTAS DE PRUEBA
Agregué 2 productos al carrito (Large Angelfish y Adult Male Chihuahua) estando sin loguear. El carrito se mostraba vacío antes de iniciar sesión. Al loguearme con el carrito ya cargado, los productos se mantuvieron exactamente igual — sin pérdidas ni duplicados.

Repetí el flujo en orden inverso: inicié sesión primero y luego armé el carrito. El comportamiento fue similar al caso anterior — sin diferencias observables.

Al cerrar sesión con productos activos en el carrito, estos se pierden por completo. Esperaba que el carrito se mantuviera igual que al iniciar sesión (Paso 2), pero en este caso el carrito queda vacío sin ningún aviso previo al usuario.

Al probar con dos sesiones distintas del navegador (una anónima, otra logueada) usando el mismo usuario, los carritos de ambas sesiones se mezclaron entre sí, en vez de mantenerse independientes o sobrescribirse de forma predecible.

## LISTA DE RIESGOS
- El sistema podría perder el carrito del cliente si cierra sesión con productos activos, generando abandono de compra sin que el usuario entienda por qué.
- El sistema podría mezclar los carritos de dos sesiones abiertas con el mismo usuario, generando compras con productos que el cliente no agregó intencionalmente en esa sesión.

## DEFECTOS (BUGS)
**Bug 1 — Pérdida del carrito al cerrar sesión**
- Pasos para reproducir: agregar productos al carrito estando logueado → cerrar sesión (Sign Out)
- Resultado esperado: el carrito debería mantenerse o, como mínimo, avisar al usuario antes de vaciarse
- Resultado obtenido: el carrito se vacía sin aviso ni confirmación
- Reproducible: Sí

**Bug 2 — Mezcla de carritos entre sesiones simultáneas**
- Pasos para reproducir: abrir dos sesiones del navegador con el mismo usuario, armar carrito en ambas
- Resultado esperado: cada sesión debería mantener su propio carrito, o el sistema debería definir claramente cuál prevalece
- Resultado obtenido: los productos de ambos carritos se mezclan
- Reproducible: Sí

## INCIDENTES (ISSUES)
No quedó claro si existe algún mecanismo de aviso (modal, mensaje) antes de perder el carrito al cerrar sesión, o si esto es el comportamiento intencional del sistema. Tampoco quedó claro cómo el sistema resuelve conflictos cuando el mismo usuario tiene dos sesiones activas simultáneamente — no hay indicio de una regla de "última sesión gana" o similar.