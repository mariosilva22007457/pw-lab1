

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Post
from .models import PontuacaoQuizz
from .models import Quizz
from .models import Pessoa
from .models import Projetos

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
admin.site.register(Quizz)
admin.site.register(Pessoa)
admin.site.register(Projetos)
