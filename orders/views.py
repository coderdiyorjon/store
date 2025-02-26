from django.views.generic import CreateView
from django.views.generic.base import TemplateView

# Create your views here.

class OrderCreateView(TemplateView):
    template_name = 'orders/order-create.html'