import django_filters

from products.models import Product


class ProductFitlter(django_filters.FilterSet):

    ordering_price_disc = django_filters.OrderingFilter(
        fields=("discounted_price", "discounted_price")
    )
    ordering_price = django_filters.OrderingFilter(fields=("price", "price"))
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    range_price_disc = django_filters.RangeFilter(field_name="discounted_price")
    range_price = django_filters.RangeFilter(field_name="price")
    min_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="gte")
    max_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="lte")
    ordering_rating = django_filters.OrderingFilter(fields=("rating", "rating"))
    min_reviews = django_filters.NumberFilter(field_name="reviews", lookup_expr="gte")
    max_reviews = django_filters.NumberFilter(field_name="reviews", lookup_expr="lte")
    ordering_reviews = django_filters.OrderingFilter(fields=("reviews", "reviews"))

    class Meta:
        model = Product
        fields = [
            # "price",
            # "rating",
            "ordering_price_disc",
            "ordering_price",
            "min_price",
            "max_price",
            "range_price_disc",
            "range_price",
            "min_rating",
            "max_rating",
            "ordering_rating",
            "min_reviews",
            "max_reviews",
            "ordering_reviews",
        ]
