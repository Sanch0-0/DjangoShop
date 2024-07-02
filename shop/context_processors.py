from .models import Category


def active_categories(requests):
    categories = Category.objects.exclude(clothes=None)

    return {"active_categories": categories}
