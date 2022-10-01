from django.contrib import admin
from .models import Client
from .models import Bank
from .models import Account
from .models import Purchase
from .models import Payment

class ClientAdmin(admin.ModelAdmin):
    list_display = ("owner","firstName","lastName","displayName","created","updated");

class BankAdmin(admin.ModelAdmin):
    list_display = ("code","name","nit","created","updated");

class AccountAdmin(admin.ModelAdmin):
    list_display = ("client","bank","balance","balanceCredit","currency","status","created","updated");

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("owner","amount","currency","credit","status");

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("purchase","account","pay","balance","currency","status");

# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Payment, PaymentAdmin)