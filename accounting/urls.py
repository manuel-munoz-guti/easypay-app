from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"clients", views.ClientViewSet)
router.register(r"banks", views.BankViewSet)
router.register(r"purchases", views.PurchaseViewSet)
router.register(r"accounts", views.AccountViewSet)
router.register(r"payments", views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
