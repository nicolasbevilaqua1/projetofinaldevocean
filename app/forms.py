from django.forms import ModelForm
from app.models import Produtos

# Create the form class.
class ProdutosForm(ModelForm):
     class Meta:
        model = Produtos
        fields = ['descricao', 'categoria', 'codigo', 'quantidade']

