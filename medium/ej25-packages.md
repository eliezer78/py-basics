## **Enunciados de Ejercicios: Python y Librerías**

### **Ejercicio 1: Analizador de Temperaturas Aleatorias**

Crea una función que genere un *array* de 200 temperaturas (flotantes) aleatorias entre 10.0 y 40.0 grados Celsius. Utilizando **numpy** y **math**, calcula y muestra el promedio, la desviación estándar, el valor mínimo y el máximo.

### **Ejercicio 2: Gestor de Tareas y Fechas**

Crea una clase llamada Tarea que tenga como atributos: nombre (string), fecha\_limite (dt.date) y estado (string: 'pendiente', 'completada'). La clase debe tener un método que calcule y retorne los días restantes (o pasados) hasta la fecha límite. Luego, crea una lista de 5 instancias de esta clase con fechas límite aleatorias (usando **random** y **datetime**) y muestra la información de cada tarea.

### **Ejercicio 3: Analizador de Datos de Ventas**

Crea una clase llamada AnalizadorVentas que, al inicializarse, genere un DataFrame de **pandas** con 100 filas y las columnas: 'Fecha' (fechas aleatorias), 'Producto' (elegido al azar) y 'Monto' (números aleatorios). La clase debe tener métodos para:

1. Calcular el total de ventas por producto.  
2. Obtener el promedio de ventas por día.  
3. Filtrar las ventas que superen un monto mínimo dado.

### **Ejercicio 4: Simulación de Inversión Financiera**

Simula el valor de una inversión inicial de $10,000 durante un año (252 días hábiles). Utiliza **numpy** para generar 252 rendimientos diarios aleatorios con una distribución normal y **pandas** para gestionar el valor de la inversión. Muestra el valor final de la inversión y el rendimiento total.

### **Ejercicio 5: Simulador de Población Crecimiento Exponencial**

Crea una clase llamada SimuladorPoblacion que simule el crecimiento de una población a lo largo de los años. La clase debe tener un método que utilice **numpy** para generar una serie de **pandas** que represente la población a lo largo del tiempo, aplicando la fórmula de crecimiento exponencial. La clase también debe tener un método para retornar la población final.

### **Ejercicio 6: Generador de Contraseñas Seguras**

Utiliza la librería **random** para crear una función que genere una contraseña aleatoria y segura. La contraseña debe tener una longitud aleatoria entre 12 y 16 caracteres y debe incluir al menos una letra mayúscula, una minúscula, un dígito y un símbolo.

### **Ejercicio 7: Analizador de Encuestas**

Crea una clase llamada AnalizadorEncuesta que genere un DataFrame de **pandas** con 500 filas de datos de encuestas aleatorias. Las columnas deben ser: 'ID\_Encuesta', 'Edad' y 'Nivel\_Satisfaccion' (de 1 a 5). La clase debe tener métodos para:

1. Retornar un resumen estadístico de la columna 'Edad'.  
2. Calcular el nivel de satisfacción promedio para rangos de edad definidos.

### **Ejercicio 8: Cálculo de Propiedades de un Círculo**

Crea una clase llamada Circulo que tenga como atributo radio (número). El constructor debe recibir el radio como un array de tipo flotante ('f') de la librería **array**. La clase debe tener dos métodos:

1. area(): que calcule y retorne el área del círculo utilizando **math.pi**.  
2. circunferencia(): que calcule y retorne la circunferencia.

### **Ejercicio 9: Generador y Analizador de Fechas Históricas**

Genera una lista de 200 fechas aleatorias en un rango de 100 años. Utiliza las librerías **datetime** y **random**. Luego, usando **pandas**, crea un DataFrame con las fechas y muestra el año más antiguo, el más reciente, el mes más frecuente y el día de la semana con más ocurrencias.

### **Ejercicio 10: Clasificador de Números Aleatorios**

Crea una clase ClasificadorNumeros que genere un *array* de **numpy** con 100 números enteros aleatorios entre \-100 y 100\. La clase debe tener métodos para contar los números positivos, negativos y ceros. También debe tener un método para calcular el promedio de los números positivos y retornar el logaritmo natural de ese promedio.