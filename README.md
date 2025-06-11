# AutoCheck API

Una API REST desarrollada con Django Rest Framework para la gestión de vehículos, clientes e inspecciones vehiculares.

## 🚀 Tecnologías Utilizadas

- **Django** - Framework web de Python
- **Django Rest Framework** - Toolkit para construir APIs REST
- **Simple JWT** - Autenticación JWT para Django REST Framework
- **SQLite** - Base de datos

## 📋 Requisitos Previos

- Python 3.8+
- pipenv

## 🔧 Instalación Local

### 1. Clonar el repositorio
```bash
git clone git@github.com:viniciusleon23/AutoCheckX_back.git
cd AutoCheckX_back
```

### 2. Instalar pipenv (si no lo tienes instalado)
```bash
pip install pipenv
```

### 3. Instalar dependencias y crear entorno virtual
```bash
pipenv install
```

### 4. Activar el entorno virtual
```bash
pipenv shell
```

### 5. Configurar variables de entorno
Crear un archivo `.env` en la raíz del proyecto:
```env
super_user_password = 0s90$SUDDTMj
super_user_name = leonjose
```

### 5. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```

La API estará disponible en: `http://localhost:8000/v1/`


## 🔐 Autenticación

La API utiliza JWT (JSON Web Tokens) para la autenticación.

### Obtener token de acceso
```bash
POST /v1/login/
Content-Type: application/json

{
    "username": "leonjose",
    "password": "0s90$SUDDTMj"
}
```

**Respuesta:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Renovar token
```bash
POST /v1/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Usar token en las peticiones
Incluir el token en el header de Authorization:
```bash
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## 📚 Endpoints de la API

### Base URL
```
http://localhost:8000/v1/
```

### Autenticación
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/login/` | Obtener tokens de acceso |
| POST | `/token/refresh/` | Renovar token de acceso |

### Vehículos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/vehiculos/` | Listar todos los vehículos |
| POST | `/vehiculos/` | Crear un nuevo vehículo |
| GET | `/vehiculos/{id}/` | Obtener vehículo específico |
| PUT | `/vehiculos/{id}/` | Actualizar vehículo completo |
| PATCH | `/vehiculos/{id}/` | Actualizar vehículo parcial |
| DELETE | `/vehiculos/{id}/` | Eliminar vehículo |

### Clientes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/clientes/` | Listar todos los clientes |
| POST | `/clientes/` | Crear un nuevo cliente |
| GET | `/clientes/{id}/` | Obtener cliente específico |
| PUT | `/clientes/{id}/` | Actualizar cliente completo |
| PATCH | `/clientes/{id}/` | Actualizar cliente parcial |
| DELETE | `/clientes/{id}/` | Eliminar cliente |

### Inspecciones
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/inspecciones/` | Listar todas las inspecciones |
| POST | `/inspecciones/` | Crear una nueva inspección |
| GET | `/inspecciones/{id}/` | Obtener inspección específica |
| PUT | `/inspecciones/{id}/` | Actualizar inspección completa |
| PATCH | `/inspecciones/{id}/` | Actualizar inspección parcial |
| DELETE | `/inspecciones/{id}/` | Eliminar inspección |

## 📝 Ejemplos de Uso

### Crear un cliente
```bash
curl -X POST http://localhost:8000/v1/clientes/ \
  -H "Authorization: Bearer tu_token_aqui" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Leon Alcantar",
    "email": "jose@jose.com",
    "telefono": "+1234567890"
  }'
```

### Obtener lista de vehículos
```bash
curl -X GET http://localhost:8000/v1/vehiculos/ \
  -H "Authorization: Bearer tu_token_aqui"
```

## 🗂️ Estructura del Proyecto

```
autocheckx-api/
├── autocheckxapi/          # Aplicación principal
│   ├── models.py           # Modelos de datos
│   ├── serializers.py      # Serializadores DRF
│   ├── views.py            # Vistas/ViewSets
│   └── urls.py             # URLs de la aplicación
│   ├── settings.py         # Configuraciones
│   └── urls.py             # URLs principales
├── requirements.txt        # Dependencias Python
├── docker-compose.yml      # Configuración Docker
├── Dockerfile             # Imagen Docker
└── README.md              # Este archivo
```



