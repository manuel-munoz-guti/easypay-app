from django.contrib import admin
from .models import Client
from .models import Bank
from .models import Account
from .models import Purchase
from .models import Payment

# Register your models here.
admin.site.register(Client)
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(Purchase)
admin.site.register(Payment)