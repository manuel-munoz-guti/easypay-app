# Project Fullstack for Python module USIP Diploma

## Integrantes:
1. Jose Manuel Munoz Gutierrez
2. Marianela Munoz Gutierrez

```
ADMIN:
username: manuelinux@gmail.com
pass: holacasaagua
```

## Contenido del Proyecto
- Proyecto en Django con una Aplicación llamada: accounting (Es el modulo de pagos que maneja EASYPAY APP)

- La aplicación tiene un diagrama ER de las 5 tablas Disenadas
    Client, Bank, Purchase, Account, Payment

- Creamos 5 validaciones:
    validar_bancarizacion,
    validar_monto_negativo,
    validar_moneda_permitida,
    validar_code_CRM,
    validar_code_ERP

- Registramos 5 Models en nuestro Admin de Django: Client, Bank, Purchase, Account, Payment

- Creamos 5 ModelViewSet<br>
    ROOT: http://127.0.0.1:8000/accounting/<br>
        "clients": "http://127.0.0.1:8000/accounting/clients/",<br>
        "banks": "http://127.0.0.1:8000/accounting/banks/",<br>
        "purchases": "http://127.0.0.1:8000/accounting/purchases/",<br>
        "accounts": "http://127.0.0.1:8000/accounting/accounts/",<br>
        "payments": "http://127.0.0.1:8000/accounting/payments/"
     
- Creamos un Custom API para sacar un reporte de pagos completados<br>
    -SWAGGER: http://127.0.0.1:8000/swagger/<br>
       -API: http://127.0.0.1:8000/swagger/payments/completed_list<br>

- El proyecto incluye el archivo requirements.txt en la raíz del repositorio