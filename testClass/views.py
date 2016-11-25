# Create your views here.
from django.views.generic import ListView

from testClass.models import Food


class FoodList(ListView):
    model = Food
