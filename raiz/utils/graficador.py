import matplotlib.pyplot as plt
import numpy as np
import os

def graficar_funcion(f_lambd, a, b, raiz_aprox, nombre_archivo):
    x_vals = np.linspace(float(a) - 1, float(b) + 1, 500)
    y_vals = f_lambd(x_vals)

    plt.figure(figsize=(8, 4))
    plt.axhline(0, color='black', linewidth=1)
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axvline(x=raiz_aprox, color='red', linestyle='--', label='Raíz aproximada')
    plt.title('Gráfica del ajuste')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)

    ruta = os.path.join("raiz", "static", "raiz", "img", nombre_archivo)
    plt.savefig(ruta)
    plt.close()
