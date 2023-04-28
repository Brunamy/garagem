from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaVieSet, CorVieSet, MarcaViewSet

router = DefaultRouter()
# router.register(r"acessorios", AcessorioVieSet)
router.register(r"categorias", CategoriaVieSet)
router.register(r"cores", CorVieSet)
router.register(r"marcas", MarcaViewSet)
# router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]