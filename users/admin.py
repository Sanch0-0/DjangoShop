from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from cart.models import Cart


admin.site.unregister(Group)


class CartInline(admin.StackedInline):
    model = Cart
    show_change_link = True


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'fullname', 'last_login']
    list_display_links = ['id', 'email', 'fullname', 'last_login']
    search_fields = ['email', 'fullname']
    list_filter = ['is_active', 'is_staff']
    fieldsets = [
        (
            None,
            {
                "fields": ['email', 'fullname', 'date_joined', 'last_login', 'is_active']
            }
        )
    ]
    inlines = [CartInline]
