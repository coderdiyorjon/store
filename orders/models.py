from django.db import models

from products.models import Basket
from users.models import User

# Create your models here.


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Created'),
        (PAID, 'Paid'),
        (ON_WAY, 'On Way'),
        (DELIVERED, 'Delivered'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    statuses = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'#{self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        if baskets.exists():  # Basket mavjudligini tekshiramiz
            self.statuses = self.PAID  # O'zgaruvchini to‘g‘ri yangilash
            self.basket_history = {
                'purchased_items': [basket.de_json() for basket in baskets],
                'total_sum': float(baskets.total_sum())
            }
            self.save()  # Avval saqlash kerak
            baskets.delete()
