# Calculadora Web de Raíces de Polinomios con Métodos Numéricos

Esta aplicación web permite calcular raíces reales de polinomios utilizando tres métodos numéricos: Bisección, Newton-Raphson y Newton-Raphson Modificado. Desarrollada con Django y Python, está orientada a fines educativos y prácticos.

## 🚀 Funcionalidades Principales

- Ingreso de funciones polinómicas vía formulario.
- Selección de método numérico:  
  - Bisección  
  - Newton-Raphson  
  - Newton-Raphson Modificado  
- Formulario dinámico con parámetros según el método.
- Tabla detallada de iteraciones.
- Visualización paso a paso del cálculo.
- Gráfica interactiva del polinomio.
- Exportación de resultados en `.txt` y `.csv`.

## 🧮 Métodos Implementados

### Método de Bisección
Iterativamente reduce un intervalo `[a, b]` donde hay cambio de signo hasta hallar la raíz.

### Newton-Raphson
Utiliza la derivada para aproximarse rápidamente a la raíz a partir de un valor inicial.

### Newton-Raphson Modificado
Versión optimizada para raíces múltiples o para evitar recalcular la derivada.

## 🛠 Tecnologías

- **Backend:** Python + Django  
- **Frontend:** HTML + CSS  
- **Librerías:** SymPy, NumPy, Matplotlib

## 📂 Estructura del Proyecto

Proyecto_calculadora/
├── raiz/
│ ├── templates/
│ ├── static/
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── metodos/
│ ├── biseccion.py
│ ├── newton.py
│ └── newton_modificado.py
├── utils/
│ └── graficador.py
├── calculadora_raices/
│ └── urls.py
├── manage.py




## 🔗 Enlaces Útiles

- 📹 [Video del proyecto](https://enlace-video.com)
- 📁 [Repositorio en GitHub](https://github.com/tu_usuario/nombre_proyecto)

## 📄 Licencia

Este proyecto se desarrolló como trabajo académico. Uso libre para fines educativos.
