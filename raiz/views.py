from django.shortcuts import render, redirect
from sympy import symbols, sympify
from .forms import FuncionForm

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
        tolerancia = request.POST.get('tolerancia', '')
        max_iter = request.POST.get('max_iter', '')
        a = request.POST.get('a', '')
        b = request.POST.get('b', '')
        x0 = request.POST.get('x0', '')

        # Convertir a LaTeX con sympy
        try:
            expr = sympify(funcion_original)
            latex_funcion = expr._repr_latex_()[2:-2]  # eliminar $$
        except:
            latex_funcion = funcion_original

        resultado = {
            'funcion': funcion_original,
            'latex_funcion': latex_funcion,
            'metodo': metodo,
            'raiz': 1.0,
            'a': a,
            'b': b,
            'x0': x0,
            'tolerancia': tolerancia,
            'max_iter': max_iter,
            'tabla': [
                {'iteracion': 1, 'a': a or -10, 'b': b or 10, 'c': 1.0, 'fc': 0.5, 'error': 1.0},
                {'iteracion': 2, 'a': 1.0, 'b': 2, 'c': 1.5, 'fc': -0.2, 'error': 0.5},
            ]
        }

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
    return render(request, 'raiz/resultados.html', {'resultado': resultado})

def mostrar_resultado_ejemplo(request):
    resultado = {
        'funcion': '2x^2 + 4x - 2',
        'latex_funcion': '2x^2 + 4x - 2',
        'metodo': 'biseccion',
        'raiz': 1.0,
        'a': 0,
        'b': 2,
        'x0': '',
        'tolerancia': '0.001',
        'max_iter': '20',
        'tabla': [
            {'iteracion': 1, 'a': 0, 'b': 2, 'c': 1.0, 'fc': 0.5, 'error': 1.0},
            {'iteracion': 2, 'a': 1.0, 'b': 2, 'c': 1.5, 'fc': -0.2, 'error': 0.5},
        ]
    }

    return render(request, 'raiz/resultados.html', {'resultado': resultado})
