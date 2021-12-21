import form as form
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .forms import AddRecipeForm



class IngredientCategory:
    # Фильтер по инградиентам и категории блюда

    def get_ingredient(self):
        return Ingredient.objects.all()

    def get_meat(self):
        return Meat.objects.all()

    def get_vegetable(self):
        return Vegetable.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_user(self):
        return Avatar.objects.all()


class RecipeList(IngredientCategory, ListView):
    model = Recipe
    paginate_by = 1
    filter_backends = (DjangoFilterBackend,)


class PersonalAreaList(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe_app/personal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].filter(user=self.request.user)
        # ava = Avatar.objects.filter(user=self.request.user).first()
        # context['avatar'] = ava.image

        return context


class AuthorsList(IngredientCategory, ListView):
    model = Avatar
    context_object_name = 'authors'
    template_name = 'recipe_app/authors_list.html'


class RecipeDetailView(IngredientCategory, DetailView):
    model = Recipe
    template_name = 'recipe_app/recipe_detail.html'


# class AuthorListView(ListView):
#     model = Recipe
#     context_object_name = 'author'
#     template_name = 'recipe_app/author_detail.html'
#
#     def get_queryset(self):
#         # original qs
#         qs = super().get_queryset()
#         # filter by a variable captured from url, for example
#         return qs.filter(user=self.kwargs.pk)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author'] = Recipe.objects.filter(user=self.request.user)
    #     # ava = Avatar.objects.filter(user=self.request.user).first()
    #     # context['avatar'] = ava.image
    #
    #     return context
def author_recipes(request, pk):
    user = Recipe.objects.filter(user=pk)
    return render(request, 'recipe_app/author_detail.html', context={'user': user})

class Search(IngredientCategory, ListView):
    context_object_name = 'search'

    # paginate_by = 7 #кол-во выводимых записей
    def get_queryset(self):

        search = Recipe.objects.filter(
            title__iregex=self.request.GET.get("q"))

        return search

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, *kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'

        return context


class FilterRecipeView(IngredientCategory, ListView):
    # Фильтер рецептов
    def get_queryset(self):
        queryset = Recipe.objects.filter(
            Q(ingredient__in=self.request.GET.getlist("ingredient")) |
            Q(category__in=self.request.GET.getlist("category"))
        ).distinct()
        return queryset


class CustomLoginView(IngredientCategory, LoginView):
    template_name = 'recipe_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('personal_list')


class RegisterPage(IngredientCategory, FormView):
    template_name = 'recipe_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('personal_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('recipes')
        return super(RegisterPage, self).get(*args, **kwargs)


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = AddRecipeForm
    template_name = 'recipe_app/recipe_form.html'
    context_object_name = 'create'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect("personal_list")

    success_url = reverse_lazy('personal_list')


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description', 'video', 'image', 'number', 'ingredient', 'gram', 'cooking', 'category']
    success_url = reverse_lazy('personal_list')


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('personal_list')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


