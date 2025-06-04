from django.shortcuts import render, redirect
from sympy import symbols, sympify, latex, lambdify
from .forms import FuncionForm
from .metodos.biseccion import metodo_biseccion

x = symbols('x')

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

        # Generar LaTeX si no viene del frontend
        latex_funcion = request.POST.get('latex_funcion', '').strip()
        if not latex_funcion:
            try:
                expr = sympify(funcion_original.replace('^', '**'))
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
                f_expr = sympify(funcion_original.replace('^', '**'))
                f_lambd = lambdify(x, f_expr, 'numpy')
                raiz, tabla, pasos = metodo_biseccion(f_lambd, float(a), float(b), tolerancia, max_iter)
                resultado['raiz'] = round(raiz, 6)
                resultado['tabla'] = tabla
                resultado['pasos'] = pasos
            except Exception as e:
                resultado['error'] = str(e)
                resultado['tabla'] = []
                resultado['pasos'] = [f"Error: {str(e)}"]
                resultado['raiz'] = 'No definida'

        if 'tabla' not in resultado:
            resultado['tabla'] = []
        if 'pasos' not in resultado:
            resultado['pasos'] = []

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
