# Create your views here.
from django.views.generic import FormView

from testForm.form import AddFoodForm


class AddFoodView(FormView):
    template_name = 'testForm/food_add.html'
    form_class = AddFoodForm
    success_url = 'testForm/thanks.html'


    def form_valid(self, form):
        form.price_zero()
        return super(AddFoodView, self).form_valid(form)