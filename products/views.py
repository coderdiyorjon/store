from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory

# Create your views here.


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = self.title  # Set the title from the class attribute
        context['categories'] = ProductCategory.objects.all()
        return context

# def index(request):
#     context = {'is_promotion': True, 'title': 'Store', }
#     return render(request, 'products/index.html', context)


# def products(request, category_id=None, page_number=1):
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     per_page=3
#     context = {'title': 'Store - Каталог',
#     'products':(Paginator(products, per_page)).page(page_number),
#     'categories': ProductCategory.objects.all(), }
#     return render(request, 'products/products.html', context)

class BasketCreateView(CreateView):
    model = Basket

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=self.kwargs.get('product_id'))
        baskets = Basket.objects.filter(product=product, user=request.user)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
