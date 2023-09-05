from django.db import models

from uploader.models import Image
from garagem.models import Modelo, Cor, Acessorio


class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
        )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descricao = models.CharField(max_length=100)
    acessorios = models.ManyToManyField(Acessorio, related_name="acessorios")
    capa = models.ManyToManyField(
        Image,
        related_name="+",
    )

    def __str__(self):
        return f"{self.modelo} (Modelo: {self.modelo} - Ano: {self.ano} - Cor: {self.cor})"

    class Meta:
        verbose_name = "veículo"