from django.shortcuts import render

import datetime


# Create your views here.
def index_view(request):
    return render(request, 'portfolio/layout.html')


def about_view(request):
    return render(request, 'portfolio/about.html')


def home_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']
    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'portfolio/home.html', context)


def apresentacao_view(request):
    return render(request, 'portfolio/apresentação.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def educação_view(request):
    return render(request, 'portfolio/educação.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')


def licenciatura_view(reuqest):
    return render(reuqest, 'portfolio/licenciatura.html'

                  )


def blog_view(request):
    return render(request, 'portfolio/blog.html')

def web_view(reuqest):
    return render(reuqest, 'portfolio/web.html')
