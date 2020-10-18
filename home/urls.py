from django.urls import path,include
from .views import (index
)

app_name = 'home'


urlpatterns = [
    path('',index,name='index'),
    # path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    # path('category/<slug>/', ItemDetailViewCategory.as_view(), name='category'),
    # path('newproducts/', NewProduct.as_view(), name='newproducts'),
    # path('featuredproducts/', FeaturedProducts.as_view(), name='featured'),
    
]
