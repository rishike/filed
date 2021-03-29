from django.urls import path
from .views import CreateViewSet, SongDetail, PodcastDetail, AudiobookDetail, SongListView, PodcastListView, AudiobookListView

urlpatterns = [
    path('create', CreateViewSet().as_view()),
    path('song/', SongListView().as_view()),
    path('song/<int:pk>', SongDetail().as_view()),
    path('podcast/', PodcastListView().as_view()),
    path('podcast/<int:pk>', PodcastDetail().as_view()),
    path('audiobook/', AudiobookListView().as_view()),
    path('audiobook/<int:pk>', AudiobookDetail().as_view())
]