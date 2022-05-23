from django.db import models


class Post(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    link = models.URLField(max_length=200, blank=True)

    def str(self):
        return f"{self.autor} no {self.data}, adicionou um {self.titulo} com a{self.descricao} e link {self.link}"


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField()

    def __str__(self):
        return f"{self.nome}  {self.pontuacao}"


class Quizz(models.Model):
    nome = models.CharField(max_length=50)

    pergunta1 = models.CharField(max_length=50)

    pergunta2 = models.CharField(max_length=50)

    pergunta3 = models.CharField(max_length=50)

    pergunta4 = models.CharField(max_length=50)

    pergunta5 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome}"


class Projetos(models.Model):
    titulo = models.CharField(max_length=200)

    descricao = models.CharField(max_length=500)

    participantes = models.ManyToManyField(Pessoa)

    tecnologias = models.CharField(max_length=100)

    github = models.URLField(max_length=200, blank=True)

    ano = models.IntegerField(default=0)

    imagem = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return f"{self.titulo}"


class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    link = models.URLField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return f"{self.titulo}"


