from django.http import HttpResponse
from django.shortcuts import render

from store.models import StoreInfo


# Create your views here.

# 查下store全部信息
def select_store_list(request):
    store_list = StoreInfo.objects.all()
    print(type(store_list), store_list)
    return render(request, "store_list.html", {"content": store_list})


# 添加一条store信息
def add_store_info(request):
    name = request.POST['name']
    address = request.POST['address']
    create = StoreInfo.objects.create(name=name, address=address)
    print(type(create), create)
    return HttpResponse("Add Success")


# 删除一条store信息
def delete_store_info(request, pk):
    storeInfo = StoreInfo.objects.get(pk=pk)
    delete = storeInfo.delete()
    print(type(delete), delete)
    return HttpResponse("Delete Success")
