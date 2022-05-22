from django import forms
from django.forms import ModelForm
from .models import Post, Quizz


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao...'}),

            'date': forms.DateInput(format='%m/%d/%Y'),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Author',
            'date': 'Data',
            'titulo': 'Title',
            'descricao': 'Description',
            'image': 'Image',
        }


    # texto auxiliar a um determinado campo do formulário
        help_texts = {

        }

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        labels = {

            'nome': 'Qual o seu nome?',

            'pergunta1': 'Que cidade é considerada o berço do Jazz?',

            'pergunta2': 'Que profissão usou o termo "Jazz" pela primeira vez? ',  #

            'pergunta3': 'Qual foi o primeiro album de Jazz? comercial', #

            'pergunta4': 'Quem é a rainha do Jazz?', #

            'pergunta5': 'Que instrumento tocava Miles Davis? '



        }

