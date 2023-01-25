import datetime

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Order(models.Model):
    STATUSES = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered')
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Customer')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUSES[0][0], verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    closed_at = models.DateTimeField(null=True, blank=True, verbose_name='Closed At')

    class Meta:
        order_by = ('-created_at',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'#{self.pk}> by {self.customer}'
