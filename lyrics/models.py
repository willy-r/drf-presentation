from django.db import models


class Artist(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    nacionalidade = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome.title()


class Music(models.Model):
    titulo = models.CharField(max_length=200)
    genero_musical = models.CharField(max_length=200)
    duracao_seg = models.IntegerField()
    artista = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo.title()
