README del Backend

# 🎬 API Servidor - Cine Daslegacy

Este es el backend del sistema de gestión de cine, desarrollado con **Django REST Framework**. Se encarga de la gestión de la base de datos, autenticación segura con OAuth 2.0 y el almacenamiento de imágenes multimedia.

## 👨‍💻 Autores
* **Andrés Tulcanaza**
* **David Puga**

## 🚀 Tecnologías Usadas
* **Python 3.10+**
* **Django 4.2**
* **Django REST Framework** (API)
* **Django OAuth Toolkit** (Autenticación profesional)
* **Pillow** (Gestión de imágenes)
* **CORS Headers** (Seguridad de conexión)

## ⚙️ Instalación y Configuración

### 1. Clonar y preparar entorno
```bash
# Entrar a la carpeta
cd backend

# Crear entorno virtual (Mac/Linux)
python3 -m venv venv
source venv/bin/activate

# Crear entorno virtual (Windows)
python -m venv venv
venv\Scripts\activate
2. Instalar dependencias
Bash
pip install django djangorestframework django-oauth-toolkit django-cors-headers Pillow
3. Base de Datos
Bash
python manage.py makemigrations
python manage.py migrate
4. Crear Superusuario (Admin)
Bash
python manage.py createsuperuser
# Sigue las instrucciones para crear tu usuario 'admin'
5. Configuración OAuth 2.0
Inicia el servidor: python manage.py runserver

Ve a: http://127.0.0.1:8000/admin/

Entra a Django OAuth Toolkit > Applications.

Crea una nueva aplicación:

Client Type: Confidential

Authorization Grant Type: Resource owner password-based

IMPORTANTE: Copia el Client ID y Client Secret para usarlos en el Frontend.

6. Ejecutar Servidor
Bash
python manage.py runserver
La API estará disponible en http://127.0.0.1:8000/api/