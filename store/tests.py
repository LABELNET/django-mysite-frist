from django.test import TestCase

from store.models import StoreInfo


# Create your tests here.
class StoreTestCase(TestCase):
    # insert store info
    def test_insert(self):
        store_info = StoreInfo.objects.create(name='捞乐', address='南京东路')
        print(type(store_info), store_info)