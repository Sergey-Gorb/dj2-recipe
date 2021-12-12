from django.urls import path, include
from .views import recipe


urlpatterns = [
    path('', recipe, name='index')
    # здесь зарегистрируйте вашу view-функцию
]
# urlpatterns = [
#     path('', include('recipes.urls')),
# ]