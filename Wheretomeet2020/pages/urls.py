from django.urls import path
from .import views

app_name = "pages"

urlpatterns = [
    path('', views.index, name='index'),
    # path('maps', views.maps, name='maps'),
    path('<int:people>', views.search, name='search'),
    
]
