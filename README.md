# NV-Tracking

Aplicación web en Django para registrar el ingreso de camiones, los informes de control de calidad del alimento y las salidas de barcos hacia los criaderos.

## Funciones

- Registro de camiones (patente, chofer, carga y horarios).
- Informes de control de calidad: tipo de alimento, almacenamiento y temperatura, con aprobación o rechazo.
- Registro de barcos y lugar de destino del despacho.

## Requisitos

- Python 3.10 o superior

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # y cambia SECRET_KEY
python manage.py migrate
python manage.py runserver
```

## Pruebas

```bash
python manage.py test
```

Las pruebas también corren en GitHub Actions en cada pull request.
