from django.urls import path
from .views import Home, CatsIndex, CatDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('cats/', CatsIndex.as_view(), name='cat-index'), 
  path('cats/<int:cat_id>/', CatDetail.as_view(), name='cat-detail'),
 
]
