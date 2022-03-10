from django.contrib import admin
from django.urls import path
from employee import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', views.emp),  
    path('',views.index),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]
