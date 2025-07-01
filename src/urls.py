from django.urls import path


from src.views import ShowMainPage, ShowResult

app_name = 'src'

urlpatterns = [
    path('', ShowMainPage.as_view(), name='main'),
    path('result/', ShowResult.as_view(), name='result'),
]
