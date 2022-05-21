from django.db import models


class Post(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    link = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='media/', blank=True)

    def str(self):
        return f"{self.autor} no {self.data}, adicionou um {self.titulo} com a{self.descricao} e imagem {self.imagem}"


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField()

    def __str__(self):
        return f"{self.nome}  {self.pontuacao}"
