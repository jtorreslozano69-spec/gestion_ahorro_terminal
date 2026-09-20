# GESTIÓN DE AHORROS AUTOMATIZADO (Versión CLI)

Este es mi proyecto automatizado e interactivo. Este código lo hice por problemas de gestionar mis ahorros, lo usé por un tiempo y tuve la genial idea de subirlo a mi portafolio para demostrar mi habilidad en **Arquitectura de Software, Lógica de Control de Flujos y Automatización**. Desarrollado en código Python puro.

---

### ¿Cómo funciona el motor?
Mi programa simula una gestión de cuentas de ahorros inteligentes con una automatización en tiempo real:

* **Lo Principal:** El usuario tiene que ingresar un monto y el código lo suma directamente a la cuenta `losahorros`.
* **Vuelto Automático:** A la misma vez, el 10% de ese monto, con la lógica que puse, se va de forma independiente a la segunda cuenta llamada `Vueltos`.
  * *Ejemplo:* Si el monto ingresado es de 100 dólares, el 10% de ese monto (que es 10) se calcula y se desvía automáticamente a la cuenta `Vueltos`.
* **Historial Dinámico:** Mi código procesa y renderiza mediante los bucles un desglose detallado de cada movimiento usando formato dinámico (`f-strings`).

---

### Habilidades y Técnicas Demostradas
Cuando revises mi archivo `gestion_ahorro.py`, podrás ver todas las herramientas que implementé:

* **Control de Flujos:** Uso avanzado del comando `while True` coordinado de forma indestructible con comandos de escape (`break`).
* **Matemática Aplicada:** Operaciones matemáticas en cadena y acumulación independiente de variables directamente en la memoria RAM.
* **Estructuras Dinámicas:** Manipulación precisa de las listas nativas (`[]`) e inyección de hilos con formato (`f-strings`) para el historial de transacciones.

---

### Aviso importante antes de usar mi programa (Código)
**Información para Visitantes y Desarrolladores:**

* **Naturaleza Volátil:** Esta es la versión *Demostrativa*. Está diseñada para ejecutarse directamente en la terminal y de forma volátil en la memoria RAM. Esto significa que todos los datos que se pongan en esta versión **se eliminarán permanentemente** después de cerrar la terminal o salirse de la aplicación.
* **Derechos de Autor:** Queda prohibida la redistribución, copia o uso de este código para creaciones de aplicaciones (programas) comerciales ajenas sin mi permiso o autorización expresa.

---

### ¿Buscas la versión completa llamada AutoAhorro?
Si te llega a interesar la versión definitiva para usarla en tu día a día, el producto comercial completo incluye:

* **Interfaz Virtual Interactiva (GUI):** Ventanas modernas, colores y botones minimalistas creados con la librería CustomTkinter.
* **Base de Datos Local Permanente (JSON):** Los saldos y el historial completo que tienen las cuentas se quedan grabados para siempre en un archivo JSON en tu computadora mes tras mes.

---

### Contáctame para Propuestas de Desarrollo o Licencias
Si eres un cliente interesado en adquirir una licencia comercial de la versión Pro, o una empresa/emprendedor que busca hacerme una propuesta de desarrollo a medida para tu negocio, ¡escríbeme directo aquí!:

* **Correo Electrónico:** [jorreslozano69@gmail.com](mailto:jorreslozano69@gmail.com)