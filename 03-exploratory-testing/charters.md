# Charters

## Charter 1

**Título:** Explorar el proceso de checkout ante interrupciones de conexión

**Misión:** Explorar el flujo de pago (agregar producto → carrito → checkout) usando confirmaciones de compra, cortes de conexión simulados en distintos puntos del proceso, y reintentos de pago, para descubrir si el sistema puede registrar un pago como aprobado sin confirmar el pedido, o generar cobros/pedidos duplicados.

**Área principal explorada:** Checkout y confirmación de pedido

---

## Charter 2

**Título:** Explorar el comportamiento del carrito al iniciar sesión durante la compra

**Misión:** Explorar el flujo de armar un carrito como usuario no registrado y luego iniciar sesión o registrarse en distintos puntos del checkout, usando variaciones de orden (loguearse antes/después de agregar productos, cerrar y reabrir sesión), para descubrir si el carrito se pierde, se duplica o se mezcla con el de otra sesión.

**Área principal explorada:** Carrito de compras y transición de sesión (anónimo → autenticado)