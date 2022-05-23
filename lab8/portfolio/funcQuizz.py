from .models import Quizz
import matplotlib.pyplot as plt


def info_user(objetos):
    dados = {}
    for quizz in objetos:
        dados[quizz.nome] = QuizzPontuacao(quizz)

    return dados


def desenha_grafico_resultados(objetos):
    # creating the dataset
    dados = info_user(objetos)

    user = list(dados.keys())
    pontuacao = list(dados.values())

    figuraOutput = plt.figure(figsize=(5, 5))

    # creating the bar plot
    plt.bar(user, pontuacao, color='blue',
            width=0.9)

    plt.ylabel("Nome dos participantes")
    plt.xlabel("Pontuação")
    plt.title("Pontuação dos participantes!")
    plt.savefig('portfolio/static/portfolio/images/grafico_final.png')


def QuizzPontuacao(input):
    pontuacaoDaPessoa = 0

    if input.pergunta1 == "New Orleans":
        pontuacaoDaPessoa += 5

    if input.pergunta2 == "Jogador de basebol":
        pontuacaoDaPessoa += 5

    if input.pergunta3 == "Livery Stable Blues":
        pontuacaoDaPessoa += 5

    if input.pergunta4 == "Ella Fitzgerald":
        pontuacaoDaPessoa += 5

    if input.pergunta5 == "Trompete":
        pontuacaoDaPessoa += 5

    return pontuacaoDaPessoa
