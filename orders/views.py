from django.views.generic import CreateView
from common.views import TitleMixin
from django.urls import reverse_lazy

from orders.forms import OrderForm

# Create your views here.


class OrderCreateView(TitleMixin ,CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
