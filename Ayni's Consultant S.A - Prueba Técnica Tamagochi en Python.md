**Objetivo:** Crear un programa que simule una mascota virtual, aplicando funciones, bucles, condicionales, variables globales y eventos aleatorios.

**Requisitos:**

1. **Entrada del usuario**
    
    - Pedir el nombre de la mascota con `input()`.
        
2. **Variables de estado**
    
    - `energia`, `felicidad`, `hambre`, `acciones`.
        
    - Inicializa con valores aleatorios entre 3 y 5 para que sea mas dinámico.
        
3. **Funciones**
    
    - `mostrar_estado()` → imprime todos los estados actuales.
	    - imprime: ❤️ Felicidad: ⚡ Energía: 🍖 Hambre:
        
    - `comer()` → reduce hambre en 3, aumenta felicidad en 1, reduce energía en 1.
	    - imprime: está comiendo 🍗
        
    - `dormir()` → aumenta energía en 4 y felicidad en 1.
		 imprime: está durmiendo 😴
        
    - `jugar()` → aumenta felicidad en 2, reduce energía en 2 y aumenta hambre en 1.
		 imprime: está jugando 🎾
        
    - `aburrirse()` → reduce felicidad en 2 (evento aleatorio).
	     imprime: se aburre... 💤"
        
4. **Bucle principal**
    
    - Mostrar estado.
        
    - Preguntar acción: comer, dormir, jugar.
        
    - Aplicar cambios en variables según la acción.
        
    - Cada acción aumenta la variable `acciones` y el hambre natural.
        
    - Incluir eventos aleatorios (`aburrirse`) con `random` 20% de prob.
        
    - Usar `time.sleep()` 3 segundos para pausas.
        
5. **Límites y condiciones de fin**
    
    - Limitar valores de variables con `min()` y `max()`.
	    - max hambre: 10
		- max felicidad: 10
		- min energía: 0
        
    - Terminar el juego si:
        
        - `hambre >= 10` → muere de hambre.
            
        - `energia <= 0` → muere de cansancio.
            
        - Número aleatorio de acciones (5–10) → muere de “vejez”. (mínimo 5, máximo 10)
