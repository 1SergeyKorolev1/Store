import json
import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.forms import ProductForm
from catalog.models import Product, Version


# Create your views here.
class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            activity = versions.filter(attribute_bul=True)
            if activity:
                product.activ_version = activity.last().name
            else:
                product.activ_version = '...'

        context['product_list'] = products
        context['title_name'] = 'Store'
        return context


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'category', 'price', 'image')
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'category', 'price', 'image')
    success_url = reverse_lazy('catalog:home')


class ContactView(View):
    @staticmethod
    def get(request):
        context = {
            'title_name': 'Контакты',
        }

        return render(request, 'catalog/contact.html', context)

    def post(self, request):
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        data = {
            'User': email,
            'Textarea': textarea
        }

        json_f = 'data.json'

        with open(json_f, 'a') as f:
            if os.stat(json_f).st_size == 0:
                json.dump([data], f)
            else:
                with open(json_f) as f_:
                    list_ = json.load(f_)
                    list_.append(data)
                with open(json_f, 'w') as f_1:
                    json.dump(list_, f_1)

        return self.get(request)

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     print(product)
#     context = {
#         'product': product,
#         'title_name': product.name,
#     }
#
#     return render(request, 'catalog/product_detail.html', context)

# def contact(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         textarea = request.POST.get('textarea')
#         data = {
#             'User': email,
#             'Textarea': textarea
#         }
#
#         json_f = 'data.json'
#
#         with open(json_f, 'a') as f:
#             if os.stat(json_f).st_size == 0:
#                 json.dump([data], f)
#             else:
#                 with open(json_f) as f_:
#                     list_ = json.load(f_)
#                     list_.append(data)
#                 with open(json_f, 'w') as f_1:
#                     json.dump(list_, f_1)
#
#     context = {
#         'title_name': 'Контакты',
#     }
#
#     return render(request, 'catalog/contact.html', context)
