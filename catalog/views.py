import json
import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category


# Create your views here.
class ProductListView(ListView):
    model = Product
    extra_context = {'title_name': 'Store',}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.all()
        category = Category.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            activity = versions.filter(attribute_bul=True)
            if activity:
                product.activ_version = activity.last().name
            else:
                product.activ_version = '... версии отсутствуют'

        context['product_list'] = products
        context['category_list'] = category
        return context


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'category', 'price', 'image')
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=0)
        versions = Version.objects.filter(product=self.object)
        if self.request.method == 'POST':
            context['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = VersionFormset(instance=self.object)
        context['versions'] = len(versions)
        return context
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']

        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'category', 'price', 'image')
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        versions = Version.objects.filter(product=self.object)
        context['version'] = len(versions)

        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

class VersionCreateView(CreateView, LoginRequiredMixin):
    model = Version
    form_class = VersionForm
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
