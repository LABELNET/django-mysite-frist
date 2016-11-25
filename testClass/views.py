# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from testClass.models import Food


class FoodList(ListView):
    """
    1.list第一种写法
    继承 listview ，指定model；
    context_object_name : 自定义模板上的 object名字,默认的是 object_list
    example:
      {% for food in foods %}
    """
    model = Food
    context_object_name = 'foods'


class FoodDetail(DetailView):
    """
    详情页 :
    slug_field 指定参数 pk
    """
    model = Food
    slug_field = 'pk'
    context_object_name = 'food'


class FoodListDef(ListView):
    """
    2.list 第二种写法
      context_object_name 就等于 foods_def
    """
    model = Food

    def get_context_data(self, **kwargs):
        context = super(FoodListDef, self).get_context_data(**kwargs)
        context['foods_def'] = Food.objects.all()
        return context


class FoodListQuery(ListView):
    """
     3.list 第三种写法
       需要指定 template_name
    """
    context_object_name = 'foods_query'
    queryset = Food.objects.all()
    template_name = 'testClass/food_list_query.html'
