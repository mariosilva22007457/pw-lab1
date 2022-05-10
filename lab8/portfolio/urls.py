from django.urls import path
from . import views


app_name = 'portfolio'
name = "home"

urlpatterns = [
    path('', views.home_view),
    path('home', views.home_view, name='home'),
    path('formacao', views.formacao_view, name= 'formacao'),
    path('contacto', views.contacto_view, name='contacto'),
    path('educacao', views.educacao_view, name='educacao'),
    path('projetos', views.projetos_view, name='projetos'),
    path('licenciatura', views.licenciatura_view, name='licenciatura'),
    path('blog',views.blog_view, name='blog'),
    path('web', views.web_view, name='web'),
    path('login',views.login_view, name='login')

]
