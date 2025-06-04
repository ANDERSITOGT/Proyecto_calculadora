def metodo_biseccion(f, a, b, tolerancia, max_iter):
    pasos = []
    tabla = []
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("No se cumple el criterio de cambio de signo en el intervalo [a, b].")

    pasos.append(f"Se inicia el método de bisección con a = {a}, b = {b}, tolerancia = {tolerancia}, máximo de iteraciones = {max_iter}.")

    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)

        error = abs(b - a) / 2.0

        pasos.append(
            f"Iteración {i}: a = {a}, b = {b}, c = (a+b)/2 = {c}, f(c) = {fc}, error = {error}"
        )

        tabla.append({
            'iteracion': i,
            'a': round(a, 6),
            'b': round(b, 6),
            'c': round(c, 6),
            'fc': round(fc, 6),
            'error': round(error, 6),
        })

        if abs(fc) < 1e-12 or error < tolerancia:
            pasos.append(f"Criterio de paro alcanzado: error < tolerancia o f(c) ≈ 0. Raíz aproximada = {c}.")
            return c, tabla, pasos

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    pasos.append(f"Se alcanzó el máximo número de iteraciones. Última aproximación = {c}.")
    return c, tabla, pasos
