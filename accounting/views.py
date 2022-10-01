from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
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
from .serializers import ReportePaymentsSerializer

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

@api_view(["GET"])
def payments_completed(request):
    """
     Reporte de Pagos Completados
    """
    try:
        payments = Payment.objects.filter(status='COM')
        cantidad = payments.count()

        return JsonResponse(
            ReportePaymentsSerializer({
                "cantidad": cantidad,
                "payments": payments
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)