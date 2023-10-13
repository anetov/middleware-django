from django.urls import path
from .views import CreateIceCream, IceList, TasteList, TypeList

urlpatterns = [
    path('', IceList.as_view(), name='list'),
    path('icecream/', CreateIceCream.as_view(), name='add_ice'),
    path('taste/', TasteList.as_view(), name='taste'),
    path('type/', TypeList.as_view(), name='type'),
]
