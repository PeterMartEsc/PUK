# Actividad 1.1 - Pruebas software

<center>
    <img src="https://aqua-cloud.io/wp-content/uploads/2025/07/software_testing_pyramid.webp" width=400/>
</center>

## Índice

- [Pruebas Funcionales](#pruebas-funcionales)

- [Pruebas No Funcionales](#pruebas-no-funcionales)


## Pruebas Funcionales

Las __pruebas funcionales__ son aquellos tests que verifican que el software cumple con los requisitos especificados, es decir, realiza la función para la que fue creado.

- __Pruebas unitarias:__ test que verifican el funcionamiento de una pequeña parte de un programa, de forma aislada. Por ejemplo una función o una clase específica.

- __Pruebas de integración:__ tests en los que se juntan varias partes de un programa para comprobar el intercambio de datos entre ellas, que interactúen correctamente entre si. Por ejemplo, si la capa _repository_ obtiene los datos correctamente de una bbdd, si la _service_ recibe correctamente la información administrada por los repository, etc.

- __Pruebas de regresión:__ tests que se suelen realizar para la actualización de un programa. Estos comprueban que las nuevas implementaciones no rompan el funcionamiento del software existente.

- __Pruebas de humo:__ tests rapidos que verifican funcionalidades básicas del software tras recibir una actualización. Se realizan antes que las unitarias y las de integración, como medida de seguirdad para ahorrar tiempo. Si no cumple estas funcionalidades básicas, no tiene sentido testear todo el programa.

- __Pruebas de aceptación:__ son pruebas de caja negra (se analiza la funcionalidad externa, sin conocer su estructura interna) donde el cliente, usuarios objetivo, o quien fuera que solicitara la aplicación, comprueba que hace exactamente lo que quiere.


## Pruebas No Funcionales

Las __pruebas no funcionales__ se centran en verificar el comportamiento del software sin entrar en aspectos de funcionalidad: rendimiento, escalabilidad, usabilidad, etc.


- __Pruebas de carga:__ consiste en simular una demanda de datos masiva a una bbdd, api o aplicación en general, para comprobar su respuesta y cuando se empieza a ralentizar.

- __Pruebas de estrés:__ parecidas a las de carga, pero en estas se busca someterlo a una carga mayor a la que se espera que soporte de normal, para encontrar en que punto se rompe y como reacciona a ese colapso. 

- __Pruebas de compatibilidad:__ aquí se busca verificar el funcionamiento correcto de una aplicación en diferentes entornos. Hardware, sistemas operativos, redes, navegadores, etc.

- __Pruebas de usabilidad:__ van relacionadas con el diseño ux/ui. Se busca evaluar que tan intuitiva y cómoda es una aplicación para los usuarios reales.

- __Pruebas de escalabilidad:__ la escalabilidad va relacionada con la capacidad de crecimiento de una aplicación. Estas pruebas se encargan de comprobar esto mismo, como necesita escalar la aplicación dependiendo de su crecimiento. Si tiene más usuarios, cuanto servidores más se necesitan, cuantos recursos más hay que destinarle, etc.

- __Pruebas de seguridad:__ como su propio nombre indica, se encarga de comprobar las vulnerabilidades, riesgos y/o amenazas del software, para garantizar la protección de los datos sensibles que pueda manejar este y que nadie pueda saltarse las reglas de acceso. 
