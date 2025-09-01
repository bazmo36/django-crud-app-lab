from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView
from .models import Cat, Food
from .forms import CatForm, FoodForm


class HomeView(TemplateView):
    template_name = "home.html"


class CatListView(ListView): 
    model = Cat
    template_name = "cats/cat_list.html"
    context_object_name = "cats"

class CatDetailView(DetailView):
    model = Cat
    template_name = "cats/cat_detail.html"
    context_object_name = "cat"

class CatCreateView(CreateView):  
    model = Cat
    form_class = CatForm
    template_name = "cats/cat_form.html"

    def get_success_url(self):
        return reverse("cat_detail", kwargs={"pk": self.object.pk})

class CatUpdateView(UpdateView):
    model = Cat
    form_class = CatForm
    template_name = "cats/cat_form.html"

    def get_success_url(self):
        return reverse("cat_detail", kwargs={"pk": self.object.pk})

class CatDeleteView(DeleteView):
    model = Cat
    success_url = reverse_lazy("cat_list")


# Food Views
class FoodCreateView(CreateView):
    model = Food
    template_name = 'foods/food_form.html'
    form_class = FoodForm

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})  # Fix: use 'pk'

class FoodListView(ListView):
    model = Food
    template_name = 'foods/food_list.html'
    context_object_name = 'foods'

class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'foods/food_form.html' 
    form_class = FoodForm
    pk_url_kwarg = 'pk'  
    
    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})

class FoodDetailView(DetailView):
    model = Food
    template_name = 'foods/food_detail.html'
    context_object_name = 'food'
    pk_url_kwarg = 'pk'  

class FoodDeleteView(DeleteView):
    model = Food
    # success_url = '/foods/'
    # def get_success_url(self):
    #     return reverse('food_list', kwargs={'pk': self.object.pk})

    success_url = reverse_lazy("food_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
