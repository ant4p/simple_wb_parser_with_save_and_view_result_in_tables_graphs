import django_filters
from products.models import Product


class ProductFilterAPI(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    min_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="gte")
    max_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="lte")
    min_reviews = django_filters.NumberFilter(field_name="reviews", lookup_expr="gte")
    max_reviews = django_filters.NumberFilter(field_name="reviews", lookup_expr="lte")

    class Meta:
        model = Product
        fields = [
            "price",
            "rating",
            "min_price",
            "max_price",
            "min_rating",
            "max_rating",
            "min_reviews",
            "max_reviews",
        ]
