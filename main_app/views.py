from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView, FormView
from django.contrib.auth.models import User
from .models import Cat, Food
from .forms import CatForm, FoodForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'


class HomeView(TemplateView):
    template_name = "home.html"


class CatListView(LoginRequiredMixin,ListView): 
    model = Cat
    template_name = "cats/cat_list.html"
    context_object_name = "cats"

class CatDetailView(LoginRequiredMixin,DetailView):
    model = Cat
    template_name = "cats/cat_detail.html"
    context_object_name = "cat"

class CatCreateView(LoginRequiredMixin,CreateView):  
    model = Cat
    form_class = CatForm
    template_name = "cats/cat_form.html"

    def get_success_url(self):
        return reverse("cat_detail", kwargs={"pk": self.object.pk})

class CatUpdateView(LoginRequiredMixin,UpdateView):
    model = Cat
    form_class = CatForm
    template_name = "cats/cat_form.html"

    def get_success_url(self):
        return reverse("cat_detail", kwargs={"pk": self.object.pk})

class CatDeleteView(LoginRequiredMixin,DeleteView):
    model = Cat
    success_url = reverse_lazy("cat_list")


# Food Views
class FoodCreateView(LoginRequiredMixin,CreateView):
    model = Food
    template_name = 'foods/food_form.html'
    form_class = FoodForm

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})  # Fix: use 'pk'

class FoodListView(LoginRequiredMixin,ListView):
    model = Food
    template_name = 'foods/food_list.html'
    context_object_name = 'foods'

class FoodUpdateView(LoginRequiredMixin,UpdateView):
    model = Food
    template_name = 'foods/food_form.html' 
    form_class = FoodForm
    pk_url_kwarg = 'pk'  
    
    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})

class FoodDetailView(LoginRequiredMixin,DetailView):
    model = Food
    template_name = 'foods/food_detail.html'
    context_object_name = 'food'
    pk_url_kwarg = 'pk'  

class FoodDeleteView(LoginRequiredMixin,DeleteView):
    model = Food
    success_url = reverse_lazy("food_list")

