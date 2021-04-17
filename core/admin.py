from django.contrib import admin
from .models import Funcao, Exame, TipoRisco, TipoExame, Risco, Grupo


# Register your models here.
admin.site.register(Funcao)
admin.site.register(Exame)
admin.site.register(TipoRisco)
admin.site.register(TipoExame)
admin.site.register(Risco)
admin.site.register(Grupo)

