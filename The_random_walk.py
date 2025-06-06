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
    """
    Dibuja una gráfica del trayecto del marinero.
    
    Parámetros:
    - trayecto (List[int]): lista de posiciones
    """
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