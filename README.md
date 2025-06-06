# 🥴 Caminata Aleatoria del Marinero Borracho

Este proyecto implementa una sencilla simulación en Python de la caminata aleatoria unidimensional, también conocida como el problema del "marinero borracho". Utiliza gráficos de Matplotlib para visualizar el trayecto del marinero.

## 📜 Descripción

La caminata aleatoria es un modelo estocástico en el cual un "marinero" da pasos hacia adelante o hacia atrás con igual probabilidad. Esta simulación ilustra cómo puede evolucionar la posición del marinero después de una cantidad determinada de pasos.

## 🧠 Cómo funciona

El archivo contiene dos funciones principales:

- `marinero_borracho_v1(n)`:
  - Simula la caminata aleatoria de un marinero durante `n` pasos.
  - En cada paso, el marinero se mueve a la izquierda o derecha con una probabilidad del 50%.

- `graficar_trayecto(trayecto)`:
  - Dibuja el recorrido del marinero usando Matplotlib.
  - Muestra la evolución de la posición paso a paso.

## 📈 Ejemplo de uso

```python
import random
import matplotlib.pyplot as plt

def marinero_borracho_v1(n):
    posicion = 0
    trayecto = []
    for i in range(n):
        if random.random() < 0.5: 
            paso = -1
        else:
            paso = +1
        posicion = posicion + paso
        trayecto.append(posicion)
    return(trayecto)

def graficar_trayecto(trayecto):
    pasos = list(range(1, len(trayecto) + 1))
    plt.plot(pasos, trayecto, marker='o', linestyle='-', color='blue', label='Trayecto')
    plt.axhline(0, color='gray', linestyle='--')  # línea base en 0
    plt.title("Simulación: Caminata Aleatoria del Marinero Borracho")
    plt.xlabel("Paso")
    plt.ylabel("Posición")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

random.seed(123)
trayecto = marinero_borracho_v1(10)
graficar_trayecto(trayecto)

