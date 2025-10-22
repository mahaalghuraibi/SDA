from django.urls import path
# import Home view from the views file
from .views import Home, Cats, CatsIndex, CatDetail ,FeedingsIndex, PhotoDetail, ToyIndex, ToyDetail
from . import views

urlpatterns = [
  path('', Home.as_view(), name='home'),
  #path('cats/', Cats.as_view(), name='cat-index'),
  path('cats/', CatsIndex.as_view(), name='cat-index'),
  path('cats/<int:cat_id>/', CatDetail.as_view(), name='cat-detail'),
  path('cats/<int:cat_id>/feedings/', FeedingsIndex.as_view(), name='feeding-create'),
  path('cats/<int:cat_id>/add-photo/', PhotoDetail.as_view(), name='add-photo'),
  path('toys/', ToyIndex.as_view(), name='toy-index'),
  path('toys/<int:toy_id>/', ToyDetail.as_view(), name='toy-detail'),

  
]


