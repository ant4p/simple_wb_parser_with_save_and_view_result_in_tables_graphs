from rest_framework import routers


from api.views import ProductViewSet

app_name = "api"

router = routers.DefaultRouter()

router.register("products", ProductViewSet, basename='products')

urlpatterns = [
]




urlpatterns.extend(router.urls)
