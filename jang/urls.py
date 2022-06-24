from . import views
from django.urls import path

urlpatterns = [
     path('', views.load_addproducts, name='addproducts'),
     path('add_product_details',views.add_product_details,name='add_product_details'),
     path('showproducts',views.showproducts,name='showproducts'),
     
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('edit_productdetails/<int:pk>',views.edit_productdetails,name='edit_productdetails'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product')
]