from django import forms


class TFIDFForm(forms.Form):
    file = forms.FileField(label="Выберите текстовый файл")
