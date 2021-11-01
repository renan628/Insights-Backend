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
    queryset = Card.objects.all().order_by('data_modificacao')
    serializer_class = CardSerializer
    pagination_class = CardPagination

    def get_queryset(self):
        queryset = Card.objects.all().order_by('data_modificacao')
        tags = self.request.query_params.get('tags')
        print(tags)
        if tags is not None:
            tags = tags.split(',')
            queryset = queryset.filter(tags__pk__in=tags)
        return queryset

    tagParam = openapi.Parameter('tags', 
        in_=openapi.IN_QUERY, description='description', 
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_INTEGER)
    )
    @swagger_auto_schema(
        operation_description="description from swagger_auto_schema via method_decorator",
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