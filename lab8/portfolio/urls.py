from django.urls import path
from . import views


app_name = 'portfolio'
name = "home"

urlpatterns = [
    path('', views.home_view),
    path('home', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('apresentacao', views.apresentacao_view, name='apresentação'),
    path('competencias', views.competencias_view, name='competencias'),
    path('formacao', views.formacao_view, name='formação'),
    path('projetos', views.projetos_view, name='projetos'),
]