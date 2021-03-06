from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'index.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def add_points(request, point):
    request.user.score += point
    request.user.save()


@login_required
def profile(request):
    return render(request, "registration/profile.html")

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
