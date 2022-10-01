# Project Fullstack for Python module USIP Diploma

## Integrantes:
1. Jose Manuel Munoz Gutierrez
2. Marianela Munoz Gutierrez

username:manuelinux@gmail.com
pass: holacasaagua

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

- Creamos 5 ModelViewSet
    ROOT: http://127.0.0.1:8000/accounting/
        "clients": "http://127.0.0.1:8000/accounting/clients/",
        "banks": "http://127.0.0.1:8000/accounting/banks/",
        "purchases": "http://127.0.0.1:8000/accounting/purchases/",
        "accounts": "http://127.0.0.1:8000/accounting/accounts/",
        "payments": "http://127.0.0.1:8000/accounting/payments/"
     
- Utilice Django Rest Framework para crear al menos 1 Custom API
- Debe incluir el archivo requirements.txt en la raíz del repositorio