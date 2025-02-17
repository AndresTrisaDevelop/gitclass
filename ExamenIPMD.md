# Preguntas y Respuestas sobre Big Data

## Preguntas Tipo Test

### 1. Los mensajes que una aplicación productora envía a Kafka:
**A.** Se almacenan en el clúster de Kafka de forma indefinida y sólo se pueden borrar de forma manual.  
**B.** Se almacenan en memoria del clúster de Kakfa hasta que los lee el primer consumidor, y una vez leído se borran de memoria.  
**C.** Se almacenan en almacenamiento persistente del clúster de Kafka hasta que los lee el primer consumidor, y una vez leído se eliminan.  
**D.** Se almacenan en el clúster de Kafka y se eliminan tras cierto tiempo en el clúster o cuando el volumen de mensajes alcanza cierto umbral, según configuración.  
**Respuesta correcta:** D  

### 2. Cuando un consumidor lee mensajes de Kafka:
**A.** Lee los mensajes en orden dentro de cada partición.  
**B.** Lee los mensajes en orden dentro de cada topic.  
**C.** Lee los mensajes en orden dentro de cada bróker.  
**D.** Kafka no garantiza ningún tipo de orden al consumir los mensajes.  
**Respuesta correcta:** A  

### 3. ¿Qué implica una transformación narrow en Spark?
**A.** Movimientos de datos entre nodos  
**B.** Uso intensivo de la memoria RAM  
**C.** Replicación de particiones  
**D.** Cada partición da lugar a otra en el mismo nodo  
**Respuesta correcta:** D  

### 4. Se quiere desplegar un producto Big Data en una plataforma de cloud computing. Por requisitos del producto, se requiere tener el mayor control posible del servidor o servidores donde se despliegue dicho producto. ¿Qué solución de las disponibles elegiría?
**A.** IaaS  
**B.** PaaS  
**C.** FaaS  
**D.** SaaS  
**Respuesta correcta:** A  

### 5. Para utilizar una cola de Kafka desde el lenguaje de programación Java...
**A.** Basta descargar e importar la librería de Kafka para Java, y tener previamente Kafka instalado y corriendo en un cluster  
**B.** Es necesario tener instalado Spark en el mismo cluster además de Kafka  
**C.** Es necesario tener instalado HDFS en el mismo cluster además de Kafka  
**D.** No es posible utilizar Kafka desde Java; es necesario hacerlo desde Python  
**Respuesta correcta:** A  

### 6. ¿Cuál de las siguientes tecnologías es más similar a BigQuery?
**A.** Apache Hive  
**B.** Apache Kafka  
**C.** Apache Spark  
**D.** HDFS  
**Respuesta correcta:** A  

### 7. En el contexto de MapReduce, la fase "reduce" se utiliza para:
**A.** Dividir los datos en bloques  
**B.** Ordenar los datos alfabéticamente  
**C.** Agrupar y agregar datos por clave  
**D.** Transformar los datos en pares (clave, valor)  
**Respuesta correcta:** C  

### 8. ¿Por qué actualmente no se utilizan los RDDs en Spark?
**A.** Porque el código es menos intuitivo y más propenso a errores por parte del programador, además de no estar optimizados, a diferencia de los DataFrames  
**B.** Porque los RDDs escriben los resultados en disco el resultado intermedio de los cálculos  
**C.** Porque no están disponibles en Python (pyspark), sino sólo en lenguaje Scala  
**D.** Las respuestas A y B son correctas  
**Respuesta correcta:** D  

### 9. ¿Cuál de las siguientes situaciones no es habitual en Spark Structured Streaming?
**A.** Entrenar un modelo predictivo en tiempo real  
**B.** Refrescar una agregación que estamos guardando en una tabla  
**C.** Comprobar y consolidar datos recibidos en tiempo real antes de guardarlos  
**D.** Todas las respuestas anteriores son habituales con Spark Structured Streaming  
**Respuesta correcta:** A  

### 10. ¿Cómo almacena la información Kafka para ser consumida?
**A.** En ficheros en formato binario  
**B.** En el metastore  
**C.** En HDFS  
**D.** Ninguna de las respuestas anteriores es cierta  
**Respuesta correcta:** A  

## Preguntas de Ensayo Corto

### 1. Una entidad bancaria solía utilizar una herramienta de Business Intelligence conectada a una base de datos relacional. No obstante, su volumen de datos ahora es tan ingente que los cuadros de mando sobre agregaciones calculadas al vuelo en SQL han dejado de responder, por lo que se ha decidido reemplazar la base de datos por HDFS para almacenar toda la información. Explica en tres líneas cómo conseguir que los cuadros de mando sigan funcionando, detallando todas las modificaciones que habría que llevar a cabo. (Responder en 4 líneas) 
### ¿Cómo conseguir que los cuadros de mando sigan funcionando tras reemplazar la base de datos por HDFS?
Se debe utilizar una capa de consulta sobre HDFS, como Apache Hive o Impala, para ejecutar consultas SQL sobre los datos. Además, hay que modificar la herramienta de Business Intelligence para conectarla a esta nueva capa y optimizar las consultas con particionamiento y almacenamiento en formatos columnar como Parquet.  

### 2. Una empresa multinacional de comercio electrónico pretende predecir si un usuario que entra en su web y ha hecho click en un producto, estará o no interesado en otro producto de la tienda, relacionado con el primero, y con qué probabilidad ocurrirá esto. El objetivo es decidir si se incluirá ese segundo producto o no en la lista de "sugerencias relacionadas" que aparecen en la página del primer producto en el que hizo click. Para ello, desea construir un modelo predictivo. Justifique con dos frases por apartado la respuesta a las siguientes preguntas: (a) ¿En qué parte de la solución Spark Structured Streaming SÍ sería útil? (b) ¿En qué parte de la solución NO sería útil? (Responder en 5 líneas) 
### Uso de Spark Structured Streaming en una empresa de comercio electrónico:
(a) **Sí sería útil** para procesar en tiempo real los clics del usuario y actualizar dinámicamente los modelos de recomendación.  
(b) **No sería útil** para el entrenamiento completo del modelo, ya que esto requiere procesar grandes volúmenes de datos históricos y no flujos de datos en tiempo real.  

### 3. Explique en menos de 5 líneas por qué existen en Spark MLlib piezas que son entrenables sin ser modelos predictivos, y ponga algún ejemplo indicando qué es lo que se entrena. No se puntuará el ejemplo sin la explicación. (Responder en 7 líneas) 
### ¿Por qué existen en Spark MLlib piezas que son entrenables sin ser modelos predictivos? Ejemplo:
Algunas transformaciones como la normalización o reducción de dimensionalidad requieren entrenamiento para calcular estadísticas sobre los datos. Un ejemplo es PCA (Análisis de Componentes Principales), que aprende las combinaciones óptimas de atributos para reducir la dimensionalidad de los datos.  

### 4. Enumerar los tres orígenes de los datos que se están generando masivamente en la actualidad y poner un ejemplo de cada uno. (Responder en 4 líneas) 
### Orígenes de datos masivos y ejemplos:
1. **Redes sociales** (ejemplo: publicaciones en Twitter).  
2. **Sensores IoT** (ejemplo: datos de temperatura en fábricas).  
3. **Transacciones financieras** (ejemplo: pagos con tarjeta en tiempo real).  

### 5. En una gran entidad bancaria de ámbito internacional, JUSTIFICAR (no basta mencionar), en dos líneas de texto cada una, la tecnología que se debería utilizar (y por qué) para (a) enviar al sistema los datos de una transacción realizada desde un cajero, y (b) ajustar un modelo predictivo de la cantidad de dinero que va a sacar un usuario, utilizando el histórico completo de transacciones realizadas en el pasado por los clientes de un país. No mencionar nada sobre almacenamiento. (Responder en 4 líneas) 
### Tecnologías recomendadas en una entidad bancaria:
(a) **Para enviar datos de una transacción en un cajero**, se recomienda Kafka, ya que permite procesar eventos en tiempo real con baja latencia.  
(b) **Para ajustar un modelo predictivo de retiro de dinero**, se recomienda Spark MLlib, ya que permite procesar y entrenar modelos con grandes volúmenes de datos históricos de transacciones bancarias.  
