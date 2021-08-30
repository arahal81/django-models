from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack

# Create your views here.
def home(request):
    return render(request,'home.html')


class SnackListPageView(ListView):
    template_name = "snack_list.html"
    model = Snack


class SnackListDetailView(DetailView):
    template_name = "snack_list_detail.html"
    model = Snack