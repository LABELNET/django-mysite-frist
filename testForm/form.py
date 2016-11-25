from django import forms


class AddFoodForm(forms.Form):
    """
    先定义 form
    """
    name = forms.CharField()
    iis_code = forms.CharField()
    price = forms.IntegerField()

    # 价格不能小于等于0
    def price_zero(self):
        pass
