# urls.py
from django.urls import path
from .views import AlergenListCreateView, PancakeListCreateView, CreateYourOwnListCreateView, DrinkListCreateView, FeaturedGameListCreateView

urlpatterns = [
    path('alergeni/', AlergenListCreateView.as_view(), name='alergen-list-create'),
    path('palacinke/', PancakeListCreateView.as_view(), name='pancake-list-create'),
    path('kreiraj-svoju/', CreateYourOwnListCreateView.as_view(), name='createyourown-list-create'),
    path('pica/', DrinkListCreateView.as_view(), name='drink-list-create'),
    path('featured-igre/', FeaturedGameListCreateView.as_view(), name='featuredgame-list-create'),
]
