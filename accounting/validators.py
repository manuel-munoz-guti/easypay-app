from django.core.exceptions import ValidationError

def validar_bancarizacion(value):
    if value >= 50000:
        raise ValidationError(
            '%(value)s es un valor que debe registrarse en modulo bancarizacion',
            params={'value': value}
        )

def validar_monto_negativo(value):
     if value < 0:
        raise ValidationError(
            '%(value)s no es un monto valido de compra',
            params={'value': value}
        )

def validar_moneda_permitida(value):
     if value not in ['Bs', '$us', 'BS', '$US', '$']:
        raise ValidationError(
            '%(value)s no es una moneda aceptada',
            params={ 'value': value }
        )

def validar_code_CRM(value): 
    if "CRM" in value: 
        return value 
    else: 
        raise ValidationError(
            '%(value)s no contine un codigo correcto desde servicio CRM',
            params={ 'value': value }
        )

def validar_code_ERP(value): 
    if "ERP" in value: 
        return value 
    else: 
        raise ValidationError(
            '%(value)s no contine un codigo correcto desde servicio ERP',
            params={ 'value': value }
        )