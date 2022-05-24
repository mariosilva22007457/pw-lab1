from django import forms
from django.forms import ModelForm
from .models import Post, Quizz, UnidadesCurriculares, Noticias, Tecnologias, Padroes, Tecnicas
from .models import Pessoa, Projetos


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

            'pergunta3': 'Qual foi o primeiro album comercial de Jazz? ',  #

            'pergunta4': 'Quem é a rainha do Jazz?',  #

            'pergunta5': 'Que instrumento tocava Miles Davis? '

        }


help_texts = {

}


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

        labels = {

            'nome': 'Insira o seu nome',

            'linkedin': 'Insira Link Linkedin ',  #

        }


help_texts = {

}


class ProjetosForm(ModelForm):
    class Meta:
        model = Projetos
        fields = '__all__'

        labels = {

            'titulo': 'Insira titulo',

            'descricao': 'Insira descricao',

            'participantes': 'Insira participantes',

            'tecnologias': 'Insira tecnologias',
            'github': 'Insira github',

            'ano': 'Insira ano do projeto',

        }


help_texts = {

}


class UnidadesCurricularesForm(ModelForm):
    class Meta:
        model = UnidadesCurriculares
        fields = '__all__'

        labels = {

            'titulo': 'Insira titulo',

            'ano': 'Insira ano',
            'semestre' 'Insira semestre'

            'topicos': 'Insira topicos',

            'professores': 'Insira professores',

            'linkUC': 'Insira Link da UC',

            'projetosRealizados': 'insira  Projetos'

        }


help_texts = {

}


class NoticiasForm(ModelForm):
    class Meta:
        model = Noticias
        fields = '__all__'

        labels = {

            'titulo': 'Insira titulo',

            'descricao': 'Insira topicos',

            'imagem': 'Insira imagem',

            'link': 'Insira Link',

        }


help_texts = {

}


class TecnologiasForm(ModelForm):
    class Meta:
        model = Tecnologias

        fields = '__all__'

        labels = {
            'nome': 'Insira titulo',
            'acronimo': 'Insira acronimo',

            'ano': 'Insira ano',

            'criador': 'Insira o criador',
            'logotipo': 'Insira o logotipo',
            'link': 'Insira link',

            'caracteristicas': 'Insira as caracteristicas',
        }


help_texts = {

}


class PadroesForm(ModelForm):
    class Meta:
        model = Padroes

        fields = '__all__'

        labels = {
            'nome': 'Insira titulo',

            'link':'Insira o link',

            'descricao': 'Insira as caracteristicas',

            'imagem': 'Insira Imagem',
        }


help_texts = {

}



class TecnicasForm(ModelForm):
    class Meta:
        model = Tecnicas

        fields = '__all__'

        labels = {
            'nome': 'Insira titulo',
            'imagem': 'Insira Imagem',

            'link': 'Insira o link',
        }


help_texts = {

}

