from django import forms
from bilets.models import Proverka


class ProverkaForm(forms.Form):
    invoiceId_Vvod = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))

    class Meta:
        model = Proverka
        fields = ('invoiceId_Vvod',)


