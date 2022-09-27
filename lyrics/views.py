from rest_framework import viewsets, generics

from lyrics import serializers
from lyrics.models import Artist, Music


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by("id")
    serializer_class = serializers.ArtistSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by("id")
    serializer_class = serializers.MusicSerializer


class ListArtistMusics(generics.ListAPIView):
    serializer_class = serializers.MusicSerializer
    
    def get_queryset(self):
        queryset = Music.objects.filter(artista_id=self.kwargs["id"])
        return queryset
