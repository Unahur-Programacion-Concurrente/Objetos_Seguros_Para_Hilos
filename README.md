# Objetos Seguros para Hilos

## Cola FIFO compartida

El siguiente archivo python contiene la definición de la clase *ColaFIFO* que implementa una cola First In, First Out.
```
colaFIFO.py
```
El contenido de la cola se almacena en una atributo lista llamado “*elementos*”

La clase contiene 7 métodos

***Constructor*** : inicializa la lista “elementos” para el contenido de la cola

***insertar(dato)*** : inserta un elemento en la cola

***extraer(dato)*** extrae un elemento en la cola

***ultimo()*** : muestra el último elemento de la cola

***primero()*** : muestra el primer elemento de la cola (próximo a salir)

***cola_vacia()*** : devuelve Verdadero si la cola está vacia

***cantidad_elementos()*** : retorna la cantidad de elementos en la cola

El script incluye una función ***main()*** cuyo propósito es probar los métodos.

## Ejercicio

1. Leer y analizar que hace el código de este programa. 
**Analizar hasta comprender todas las líneas del código**

2. En un archivo python separado, importar la clase ColaFIFO, instanciar una cola de ésta clase y luego implementar un programa que ejecute las siguientes threads:

	 - Una thread (productor) que ejecute un loop infinito que en cada iteración inserte en la cola un valor numérico generado aleatoriamente (con valores entre 0 y 100), imprima un mensaje de logging indicando que se realizó la inserción y espere (sleep) dos segundos.
	
	  **Esta thread debe recibir como argumentos un objeto ColaFIFO y un valor numérico (retardo), inicialmente de 2 segundos.**
		  Por ejemplo:
      ````
        # a partir de una clase derivada de Thread
        c1 = Cons(cola, 2) 
      
        # directamente desde el módulo threading 
        c1 = threading.Thread(target=cons, args=(cola, 2))
      ````
  
   - Una thread (consumidor) que ejecute un loop infinito que en cada iteración extraiga un elemento de la cola, genere un mensaje de logging con el valor del elemento extraído y luego espere (sleep) dos segundos.  

	  **Esta thread debe recibir como argumentos un objeto ColaFIFO y un valor numérico (retardo), inicialmente de 2 segundos.**
    
    Ejemplos: 
    ```
      # a partir de una clase derivada de Thread
      p1 = Prod(cola, 2) 
     
      # directamente desde el módulo threading 
      p1 = threading.Thread(target=prod, args=(cola, 2))  
    ```

    **Implementar estas threads a partir de clases derivadas de Thread que reciban como argumento el objeto de clase ColaFIFO instanciado y el valor numérico de retardo**

    **Las threads deben permanecer ejecutándose indefinidamente, no debe terminar el programa después de lanzarlas. Coloque todo el código que sea necesario para esto.**

3. Ejecute el programa y analice los resultados. Obtiene en alguna de las ejecuciones datos inconsistentes o errores? En caso afirmativo, analice los resultados identificando las causas de las inconsistencias o errores.
4. Modifique el programa anterior de modo que los hilos tengan en cuenta los casos en que la cola está vacía.
6. Modifique el programa anterior modificando la clase ColaFIFO de modo que sus métodos tengan en cuenta los casos en que la cola está vacía.
8. Repita el primer ejercicio utilizando la clase ColaFIFOmax para instanciar una cola de tamaño (size) 10 y modifique los retardos de productor y consumidor de modo que queden los dos iguales (1 segundo).
9. Ejecute el programa y observe los resultados explicando lo que observa.
11. Repetir el ejercicio anterior modificando la clase ColaFIFOmax de modo que considere los casos de cola llena y cola vacía.
13. Es segura para hilos la clase del ejercicio anterior? Por que?
14. Modificar el ejercicio anterior de modo que se puedan lanzar un número cualquiera de hilos productor y consumidor y observe los resultados al ejecutarlo.
15. Modificar el ejercicio anterior utilizando locks cada vez que se accede al objeto compartido cola dentro de los hilos (sin modificar la clase). Ejecute el programa y observe los resultados.
16. Que errores observa? Hay condiciones de carrera?
17. Modificar la clase ColaFIFOmax de modo que sea Segura para Hilos.
18. Volver a escribir el ejercicio anterior comprobando que no se producen condiciones de carrera ni bloqueos.






