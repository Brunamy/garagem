from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from garagem.serializers import MarcaSerializer
# class AcessorioVieSet(ModelViewSet):
#     queryset = Acessorio.objects.all()
#     serializer_class = AcessorioSerializer

# class CategoriaVieSet(ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer

# class CorVieSet(ModelViewSet):
#     queryset = Cor.objects.all()
#     serializer_class = CorSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

# class VeiculoViewSet(ModelViewSet):
#     queryset = Veiculo.objects.all()
#     # serializer_class = VeiculoSerializer

#     def get_serializer_class(self):
#         if self.action in ["list", "retrieve"]:
#             return VeiculoDetailSerializer
#         return VeiculoSerializer