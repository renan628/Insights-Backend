from rest_framework.routers import DefaultRouter
from .views import TagList, TagDetail, CardList, CardDetail
from django.urls import path, re_path, include

app_name = 'api'

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),
    path('cards/', CardList.as_view()),
    path('cards/<int:pk>/', CardDetail.as_view()),
]

urlpatterns = urlpatterns + router.urls