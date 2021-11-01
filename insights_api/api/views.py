from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from .serializers import TagSerializer, CardSerializer
from .models import Tag, Card
from .pagination import CardPagination

class TagList(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Tag.objects.all().order_by('nome')
    serializer_class = TagSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Tag.objects.all().order_by('nome')
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CardList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Card.objects.all().order_by('data_modificacao').reverse()
    serializer_class = CardSerializer
    pagination_class = CardPagination

    def get_queryset(self):
        queryset = Card.objects.all().order_by('data_modificacao').reverse()
        tags = self.request.query_params.get('tags')
        if tags is not None:
            tags = tags.split(',')
            queryset = queryset.filter(tags__nome__in=tags).distinct()
        return queryset

    tagParam = openapi.Parameter('tags', 
        in_=openapi.IN_QUERY, description='tags names to filter cards by tags', 
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_STRING)
    )
    @swagger_auto_schema(
        manual_parameters=[tagParam]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CardDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Card.objects.all().order_by('-data_modificacao')
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)