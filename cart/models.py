from django.db import models
from users.models import User
from shop.models import Clothes



class Cart(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="products")
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name="products")
    quantity = models.SmallIntegerField(verbose_name="quantity", default=1)
