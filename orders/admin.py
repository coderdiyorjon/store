from django.contrib import admin

from orders.models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'statuses')
    fields = ('id', 'created',
              ('first_name', 'last_name',),
              ('email', 'address',),
              'basket_history', 'initiator',)
    readonly_fields = ('id', 'created')
