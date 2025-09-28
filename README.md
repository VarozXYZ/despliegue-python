# Generador de Contraseñas

Aplicación web para generar contraseñas seguras con Flask.

## Características

- Generación segura con módulo `secrets`
- Personalizable: longitud (4-128) y tipos de caracteres
- Interfaz moderna y responsive
- API REST para integración

## Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

Accede a: `http://localhost:5000`

## Estructura

```
├── app.py              # Aplicación Flask
├── requirements.txt    # Dependencias
└── templates/
    └── index.html     # Interfaz web
```

## Despliegue

**Aplicación desplegada en Render:**
🌐 **URL:** https://despliegue-python-1.onrender.com/

**Para desplegar en Render:**
1. Conecta tu repositorio a Render
2. Configura el build command: `pip install -r requirements.txt`
3. Configura el start command: `gunicorn app:app`
4. La aplicación se desplegará automáticamente
