# PRACTICA1G4
Integrantes 
- Fausto Almeida
- Angel Toapanta
- Jessica Tipantuña

CONSTRUCCIÓN DE API 
- Código fuente del API(app.py)
- Base de datos  SQLite( Basedatos.py)
Funcionalidades Implementadas
- GET/usuarios: consulta total de usuarios registrados.
![base de datos local host] db_lh.png
![local host](db_lh_por_usuario.png)
- POST/usuarios: permite registrar usuarios
![prueba curl local host](curl_lh.png)
- Validación de usuarios:
    -  Validación de datos (cedula de 10 digitos,entero, cedulas ya existentes)
    -  Manejo de errores 400, 404, 409
![prueba curl error](db_lh_iderror.png)
![prueba curl id ya registrado](db_lh_idyaregistrado.png)  
    -  Respuesta en formato JSON
Creatividad:
- Conexión con API externa telegram (@apiUIDEG4bot)
![Conexión Telegram](conexion_telegram.jpg) 
Uso de branches
![Branch dev](branch_dev.png)
Conenerización
![Docker](docker.png)
![creación de imagen y contenedor](le_docker.png)
Despliegue Cloud
![contenedor levantado](con_levantado.jpg)
![url generada](url.publica.jpg)
https://tarjeta-servicio-665250288038.us-central1.run.app/usuarios
![pruebas curl url publica](pruebas_curl_up.png)
![base de datos url publica](db_up.png)
## SECCIÓN DE RESPUESTA A COMENTARIOS
1.	¿En su endpoint de usuarios, como protegerían la identidad de los mismos? ¿Ahora devuelvo una lista de usuarios, como harían que el endpoint se quede con una funcionalidad más segura?

Se pueden aplicar diferentes estrategias de protección de datos. Una opción es enmascarar la cédula, mostrando únicamente los últimos cuatro dígitos y ocultando el resto de la información sensible. De esta manera se reduce el riesgo de exposición de datos personales.
Adicionalmente, se puede implementar un identificador único interno (ID) para cada usuario dentro del sistema. Este identificador sería utilizado en las consultas y operaciones de la API, evitando el uso directo de la cédula

2.	¿Como conceptualizan una conexión para que se pueda no solo conocer el saldo, pero además transaccionar?

Incorporar endpoints específicos para operaciones financieras, como consulta de saldo, recarga, transferencia y consulta de historial de movimientos. Estas operaciones requieren mecanismos adicionales de seguridad debido a la sensibilidad de la información.
En primer lugar, sería necesario implementar procesos de autenticación y verificación de identidad, como el envío de códigos de verificación al correo electrónico o al número de teléfono registrado del usuario.
