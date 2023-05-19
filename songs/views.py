from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView

from albums.models import Album
from .models import Song
from .serializers import SongSerializer


class CustomSongPaginationView(PageNumberPagination):
    page_size = 1


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = CustomSongPaginationView

    def perform_create(self, serializer):
        album_id = self.kwargs["pk"]
        album = get_object_or_404(Album, pk=album_id)

        serializer.save(album=album)
