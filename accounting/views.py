from django.shortcuts import render
from rest_framework import viewsets
from .models import Client
from .models import Bank
from .models import Purchase
from .models import Account
from .models import Payment
from .serializers import ClientSerializer
from .serializers import BankSerializer
from .serializers import PurchaseSerializer
from .serializers import AccountSerializer
from .serializers import PaymentSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

