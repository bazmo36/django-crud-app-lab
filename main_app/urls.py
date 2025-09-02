from django.urls import path
from .views import (
    HomeView,SignUpView,
    CatListView, CatCreateView, CatDetailView, CatUpdateView, CatDeleteView,
    FoodCreateView, FoodListView, FoodUpdateView, FoodDetailView, FoodDeleteView
)

urlpatterns = [
    path("auth/signup/",SignUpView.as_view(), name="signup"),

    path('', HomeView.as_view(), name='home'),

    # Cat URLs
    path("cats/", CatListView.as_view(), name="cat_list"),
    path("cats/new/", CatCreateView.as_view(), name="cat_create"),
    path("cats/<int:pk>/", CatDetailView.as_view(), name="cat_detail"),
    path("cats/<int:pk>/edit/", CatUpdateView.as_view(), name="cat_update"),
    path("cats/<int:pk>/delete/", CatDeleteView.as_view(), name="cat_delete"),

    # Food URLs
    path("foods/", FoodListView.as_view(), name='food_list'),
    path("foods/new/", FoodCreateView.as_view(), name='food_create'),
    path("foods/<int:pk>/", FoodDetailView.as_view(), name='food_detail'),
    path("foods/<int:pk>/update/", FoodUpdateView.as_view(), name='food_update'),
    path("foods/<int:pk>/delete/", FoodDeleteView.as_view(), name='food_delete'),
    
]
