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
![database_localhost](https://github.com/jesicat313-a11y/practica1/blob/33cf0cd2f286d5f16aaa49aa3ca152c31c11bb38/images/db_lh.png)
![local host](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/db_lh_por_usuario.png)

- POST/usuarios: permite registrar usuarios
![prueba curl local host](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/curl_lh.png)

- Validación de usuarios:
    -  Validación de datos (cedula de 10 digitos,entero, cedulas ya existentes)
    -  Manejo de errores 400, 404, 409
![prueba curl error](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/db_lh_iderror.png)
![prueba curl id ya registrado](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/db_lh_idyaregistrado.png)
    
    - Respuesta en formato JSON
 
Creatividad:
- Conexión con API externa telegram (@apiUIDEG4bot)
![Conexión Telegram](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/conexion_telegram.jpg) 
Uso de branches

![Branch dev](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/branch_dev.png)

Conenerización

![Docker](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/docker.png)

![creación de imagen y contenedor](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/le_docker.png)

Despliegue Cloud

![contenedor levantado](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/con_levantado.jpeg)
![url generada](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/ulr_publica.jpg)

https://tarjeta-servicio-665250288038.us-central1.run.app/usuarios

![pruebas curl url publica](https://github.com/jesicat313-a11y/practica1/blob/073092bfca3b78879f5616a3d420703fb3c043c4/images/pruebas_curl_up.jpeg)

![base de datos url publica](https://github.com/jesicat313-a11y/practica1/blob/86b70e7d929dafc8f3d2baa41b104615e3fa5fe1/images/db_up.jpg)
## SECCIÓN DE RESPUESTA A COMENTARIOS
1.	¿En su endpoint de usuarios, como protegerían la identidad de los mismos? ¿Ahora devuelvo una lista de usuarios, como harían que el endpoint se quede con una funcionalidad más segura?

Se pueden aplicar diferentes estrategias de protección de datos. Una opción es enmascarar la cédula, mostrando únicamente los últimos cuatro dígitos y ocultando el resto de la información sensible. De esta manera se reduce el riesgo de exposición de datos personales.
Adicionalmente, se puede implementar un identificador único interno (ID) para cada usuario dentro del sistema. Este identificador sería utilizado en las consultas y operaciones de la API, evitando el uso directo de la cédula

2.	¿Como conceptualizan una conexión para que se pueda no solo conocer el saldo, pero además transaccionar?

Incorporar endpoints específicos para operaciones financieras, como consulta de saldo, recarga, transferencia y consulta de historial de movimientos. Estas operaciones requieren mecanismos adicionales de seguridad debido a la sensibilidad de la información.
En primer lugar, sería necesario implementar procesos de autenticación y verificación de identidad, como el envío de códigos de verificación al correo electrónico o al número de teléfono registrado del usuario.
