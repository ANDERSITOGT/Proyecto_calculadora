function insertar(texto) {
    const input = document.getElementById("entrada_funcion");
    const cursorPos = input.selectionStart;
    const antes = input.value.substring(0, cursorPos);
    const despues = input.value.substring(cursorPos);
    input.value = antes + texto + despues;
    input.focus();
    input.setSelectionRange(cursorPos + texto.length, cursorPos + texto.length);
}

function borrar() {
    const input = document.getElementById("entrada_funcion");
    const cursorPos = input.selectionStart;
    if (cursorPos > 0) {
        const antes = input.value.substring(0, cursorPos - 1);
        const despues = input.value.substring(cursorPos);
        input.value = antes + despues;
        input.setSelectionRange(cursorPos - 1, cursorPos - 1);
    }
    input.focus();
}

function formatearNombreMetodo(metodo) {
    switch (metodo) {
        case "biseccion": return "Bisección";
        case "newton": return "Newton-Raphson";
        case "newton_mod": return "Newton-Raphson Modificado";
        default: return metodo;
    }
}

function mostrarPaso2() {
    const funcionOriginal = document.getElementById("entrada_funcion").value.trim();
    const metodo = document.getElementById("selector_metodo").value;

    if (!funcionOriginal || !metodo) {
        alert("Por favor ingresa una función válida y selecciona un método.");
        return;
    }

    const funcionPython = funcionOriginal.replace(/\^/g, '**');
    const esPolinomio = /^[0-9xX\^\+\-\*\/\.\s]+$/.test(funcionOriginal);
    const funcionVerificacion = funcionOriginal.replace(/\s+/g, '');

    let latex;
    try {
        latex = math.parse(funcionOriginal).toTex();
    } catch (error) {
        latex = "Error al convertir a LaTeX";
    }

    document.getElementById("funcion_mostrada").innerHTML = `\\[${latex}\\]`;
    document.getElementById("funcion_final").value = funcionPython;
    document.getElementById("metodo_final").value = metodo;
    document.getElementById("latex_funcion_final").value = latex;

    document.getElementById("mensaje_verificacion").innerText = esPolinomio ? "Polinomio válido" : "No es un polinomio válido";
    document.getElementById("verificacion_texto").innerText = funcionVerificacion;

    document.getElementById("subtitulo_metodo").innerText = `Completa los datos para el método ${formatearNombreMetodo(metodo)}:`;

    const camposContenedor = document.getElementById("campos_dinamicos");
    camposContenedor.innerHTML = "";

    if (metodo === "biseccion") {
        camposContenedor.innerHTML += `
            <div class="campo">
                <label for="a">Valor a:</label>
                <input type="number" step="any" name="a" required>
            </div>
            <div class="campo">
                <label for="b">Valor b:</label>
                <input type="number" step="any" name="b" required>
            </div>
        `;
    } else if (metodo === "newton" || metodo === "newton_mod") {
        camposContenedor.innerHTML += `
            <div class="campo">
                <label for="x0">Valor inicial x₀:</label>
                <input type="number" step="any" name="x0" required>
            </div>
        `;
    }

    MathJax.typeset();

    document.getElementById("contenedor_opciones").style.display = "block";
    document.querySelector(".teclado").style.display = "none";
    document.querySelector(".buscador").style.display = "none";
}

function regresarPaso1() {
    document.getElementById("contenedor_opciones").style.display = "none";
    document.querySelector(".teclado").style.display = "grid";
    document.querySelector(".buscador").style.display = "flex";
}

function validarFormulario(event) {
    const metodo = document.getElementById("metodo_final").value;
    const campos = document.querySelectorAll("#campos_dinamicos input");
    let validos = true;

    campos.forEach(input => {
        if (input.value.trim() === '') {
            validos = false;
        }
    });

    if (!validos) {
        event.preventDefault();
        alert("Por favor completa todos los campos requeridos antes de continuar.");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("form_datos");
    if (form) {
        form.addEventListener("submit", validarFormulario);
    }
});
