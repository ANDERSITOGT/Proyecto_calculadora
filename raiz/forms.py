from django import forms

class FuncionForm(forms.Form):
    funcion = forms.CharField(
        label="Función polinómica",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: x**3 - 2*x - 5'})
    )

    metodo = forms.ChoiceField(
        label="Método numérico",
        choices=[
            ('biseccion', 'Bisección'),
            ('newton', 'Newton-Raphson'),
            ('newton_mod', 'Newton-Raphson Modificado')
        ]
    )

    a = forms.FloatField(label="Extremo a", required=False)
    b = forms.FloatField(label="Extremo b", required=False)
    x0 = forms.FloatField(label="Valor inicial x₀", required=False)

    tolerancia = forms.FloatField(label="Tolerancia", initial=0.0001)
    max_iter = forms.IntegerField(label="Máx. iteraciones", initial=100)
