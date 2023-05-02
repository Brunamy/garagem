from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Marca, Veiculo
from garagem.serializers import AcessorioSerializer, CategoriaSerializer, CorSerializer, MarcaSerializer, VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class AcessorioVieSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CategoriaVieSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CorVieSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class MarcaVieSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class VeiculoVieSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    # serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer