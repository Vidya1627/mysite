from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', views.CompanyView)
router.register('user', views.UserView)
router.register('product', views.ProductView)

urlpatterns = [
    path('', include(router.urls))
]
