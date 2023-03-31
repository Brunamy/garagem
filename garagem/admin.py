from django.contrib import admin

from .models import Categoria
from .models import Marca

admin.site.register(Categoria)
admin.site.register(Marca)
