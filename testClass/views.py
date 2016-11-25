# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from testClass.models import Food


class FoodList(ListView):
    """
    继承 listview ，指定model；
    context_object_name : 自定义模板上的 object名字,默认的是 object_list
    example:
      {% for food in foods %}
    """
    model = Food
    context_object_name = 'foods'


class FoodDetail(DetailView):
    """
    详情页
    """
    model = Food
    slug_field = 'pk'

    # def get_context_data(self, **kwargs):
    #     context = super(FoodDetail, self).get_context_data(**kwargs)
    #     context['food'] = Food.objects.all()
    #     return context
