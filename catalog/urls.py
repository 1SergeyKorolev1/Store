from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, \
    ProductCreateView, ContactView, VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact', ContactView.as_view(), name='contact'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('create_version/', VersionCreateView.as_view(), name='create_version')


]
