from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    # def clean(self):
    #     data = self.cleaned_data
    #     nome = data.get('nome_comentario')
    #     email = data.get('email_comentario')
    #     comentario = data.get('texto_comentario')
    #     if not comentario:
    #         self.add_error('texto_comentario', 'O comentário precisa ter mais que 5 caracteres.')
    #     print(data)

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'texto_comentario')
