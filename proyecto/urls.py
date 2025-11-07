
from django.contrib import admin
from django.urls import path
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('pasteles/', views.pasteles, name='pasteles'),
    path('cakes/', views.cakes, name='cakes'),
    path('minitortas/', views.minitortas, name='minitortas'),
    path('bocaditos/', views.bocaditos, name='bocaditos'),

]
