

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Post
from .models import PontuacaoQuizz
from .models import Quizz

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
admin.site.register(Quizz)