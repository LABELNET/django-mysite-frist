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
        print(self.price)
        if self.price <= 0:
            print("价格不可以小于0")
        pass
