from django.http import HttpResponseRedirect
from django.shortcuts import render

import datetime

# Create your views here.
from django.urls import reverse

from portfolio.forms import PostForm
from portfolio.models import Post,  Noticias, Tecnologias, Tecnicas, Padroes
from .models import Quizz
from .forms import QuizzForm
from .funcQuizz import draw_graph
from .forms import Projetos
from .models import Projetos
from .models import UnidadesCurriculares
from .forms import UnidadesCurricularesForm


def index_view(request):
    return render(request, 'portfolio/layout.html')


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


def educacao_view(request):
    return render(request, 'portfolio/educacao.html')


def projetos_view(request):
    context = {'projetos': Projetos.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def licenciatura_view(reuqest):
    context = {'unidades_curriculars': UnidadesCurriculares.objects.all()}
    return render(reuqest, 'portfolio/licenciatura.html', context)


def blog_view(request):
    context = {'blog_posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)



def web_view(reuqest):
    context = {'noticias': Noticias.objects.all(),'tecnologias': Tecnologias.objects.all(),'tecnicas': Tecnicas.objects.all(),'padroes': Padroes.objects.all()}
    return render(reuqest, 'portfolio/web.html', context)


def login_view(request):
    return render(request, 'portfolio/login.html')


def formacao_view(request):
    return render(request, 'portfolio/formação.html')


def nova_post_view(request):
    form = PostForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)


def edita_post_view(request, blog_post_id):
    post = Post.objects.get(id=blog_post_id)
    form = PostForm(request.POST or None, request.FILES, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'blog_post_id': blog_post_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_post_view(request, blog_post_id):
    Post.objects.get(id=blog_post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def quizz_view(request):
    draw_graph(Quizz.objects.all())

    form = QuizzForm(request.POST, use_required_attribute=False)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)

    context = {
        'form': form,
    }

    return render(request, 'portfolio/quizz.html', context)
