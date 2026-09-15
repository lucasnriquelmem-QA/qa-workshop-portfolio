# Coverage Decisions

## Riesgos que se probarán primero
R1 — Pago registrado como aprobado pero pedido no confirmado tras corte de conexión en el checkout
R2 — Pérdida del carrito al loguearse un usuario no registrado durante el checkout
R4 — Un cliente registrado podría acceder al historial de pedidos de otro usuario

## ¿Por qué esos riesgos son prioridad?
R1 y R4 tienen impacto Alto: comprometen directamente dinero del cliente (cobro sin pedido confirmado) o exponen datos personales de otro usuario — ambos son daños difíciles de revertir y con consecuencia legal/reputacional. R2, aunque de impacto medio, tiene probabilidad Alta y ataca directamente la conversión de ventas — es el flujo más transitado de la app (navegar sin login antes de comprar), así que un fallo ahí afecta a muchos usuarios con frecuencia. Los tres coinciden con el criterio usado en ejercicios anteriores: priorizar donde el Nivel de riesgo (Impacto × Probabilidad) es más alto, y donde el fallo toca dinero, datos o conversión — no cosmética.

## Qué se probará menos o quedará fuera por ahora
R5 — Navegación/búsqueda de catálogo con resultados incorrectos o vacíos
R6 — Validación de formato en registro de cuenta (email mal formado, campos vacíos)
R3 — Subtotal desactualizado al editar cantidad en el carrito antes de avanzar

## Justificación de exclusiones
R5 y R6 tienen Nivel Bajo/Medio y no comprometen dinero ni datos — su peor consecuencia es una mala experiencia de búsqueda o una cuenta mal registrada, ambos corregibles sin urgencia y de bajo costo de reparación. R3 tiene Nivel Medio, pero depende de una secuencia de acciones específica del usuario (editar cantidad justo antes de avanzar), lo que reduce su probabilidad real de ocurrencia frente a los riesgos priorizados. Con tiempo de testing limitado, el esfuerzo se concentra en los riesgos que combinan mayor impacto de negocio con mayor probabilidad, dejando estos para una segunda ronda de cobertura si el tiempo lo permite.