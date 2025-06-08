from django.shortcuts import render, redirect
from sympy import symbols, sympify, latex, lambdify
from .forms import FuncionForm
from .metodos.biseccion import metodo_biseccion
from .utils.graficador import graficar_funcion  # ✅ nuevo import
import re

x = symbols('x')

def insertar_multiplicaciones(expr):
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z])\(', r'\1*(', expr)
    expr = re.sub(r'\)([a-zA-Z])', r')*\1', expr)
    expr = re.sub(r'\)\(', r')*(', expr)
    return expr

def calcular_raiz(request):
    if (
        request.method == 'POST'
        and request.POST.get('fase') == 'final'
        and request.POST.get('funcion')
        and request.POST.get('metodo')
    ):
        funcion_original = request.POST.get('funcion', '').strip()
        metodo = request.POST.get('metodo', '')
        max_iter = int(request.POST.get('max_iter', '50'))
        a = request.POST.get('a', '')
        b = request.POST.get('b', '')
        x0 = request.POST.get('x0', '')

        # Procesar tolerancia
        try:
            tolerancia = float(request.POST.get('tolerancia', ''))
            if tolerancia <= 0:
                tolerancia = 1e-5
        except:
            tolerancia = 1e-5

        # Procesar función
        funcion_preparada = insertar_multiplicaciones(funcion_original.replace('^', '**'))

        # Generar LaTeX si no viene del frontend
        latex_funcion = request.POST.get('latex_funcion', '').strip()
        if not latex_funcion:
            try:
                expr = sympify(funcion_preparada)
                latex_funcion = latex(expr)
            except:
                latex_funcion = funcion_original

        resultado = {
            'funcion': funcion_original,
            'latex_funcion': latex_funcion,
            'metodo': metodo,
            'a': a,
            'b': b,
            'x0': x0,
            'tolerancia': tolerancia,
            'max_iter': max_iter,
        }

        if metodo == 'biseccion':
            try:
                f_expr = sympify(funcion_preparada)
                f_lambd = lambdify(x, f_expr, 'numpy')
                raiz, tabla, pasos = metodo_biseccion(f_lambd, float(a), float(b), tolerancia, max_iter)
                resultado['raiz'] = round(raiz, 6)
                resultado['tabla'] = tabla
                resultado['pasos'] = pasos

                # ✅ Generar gráfica del ajuste
                nombre_imagen = "grafico_biseccion.png"
                graficar_funcion(f_lambd, a, b, raiz, nombre_imagen)
                resultado['grafica'] = nombre_imagen

            except Exception as e:
                resultado['error'] = str(e)
                resultado['tabla'] = []
                resultado['pasos'] = [f"Error: {str(e)}"]
                resultado['raiz'] = 'No definida'
                resultado['grafica'] = None  # en caso de error, no hay gráfica

        if 'tabla' not in resultado:
            resultado['tabla'] = []
        if 'pasos' not in resultado:
            resultado['pasos'] = []
        if 'grafica' not in resultado:
            resultado['grafica'] = None

        request.session['resultado'] = resultado
        return redirect('ver_resultado')

    return render(request, 'raiz/calculadora.html', {
        'form': FuncionForm(),
        'errores': []
    })

def ver_resultado(request):
    resultado = request.session.get('resultado')
    if not resultado:
        return redirect('calculadora')
    return render(request, 'raiz/resultados.html', {'resultado': resultado, 'estilo_tiger': True})
