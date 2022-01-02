from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')
        # https://www.google.com/recaptcha/api/siteverify
        # secret_key
        # resposta_captcha
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6Ld8aeQdAAAAAODzA3MUenrATqtaubnWvOT8ensg',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()
        print(recaptcha_result)
        if not recaptcha_result.get('success'):
            self.add_error(
                'texto_comentario',
                'Desculpe Mr. Robot, você não foi validado.'
            )
    #     nome = data.get('nome_comentario')
    #     email = data.get('email_comentario')
    #     comentario = data.get('texto_comentario')
    #     if not comentario:
    #         self.add_error('texto_comentario', 'O comentário precisa ter mais que 5 caracteres.')
    #     print(data)

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'texto_comentario')
