# 📌 Proyecto de Gestión de Clientes

Este proyecto es un sistema de gestión de clientes y compras desarrollado con **Django**, diseñado para facilitar la administración de clientes y sus transacciones. A continuación, se describen las funcionalidades y componentes clave del sistema.

## 🚀 Tecnologías Utilizadas

- **Backend**: Django, un framework de alto nivel para el desarrollo web en Python que promueve el desarrollo rápido y el diseño limpio.
- **Base de Datos**: SQLite, una base de datos ligera y fácil de usar que se utiliza para el desarrollo y pruebas locales.
- **Frontend**: HTML y JavaScript (Fetch API) para la interacción del usuario y la comunicación con el backend.
- **Otros**: Pandas y OpenPyXL, bibliotecas de Python utilizadas para la manipulación y exportación de datos en formatos Excel y CSV.

## 🛠 Instalación y Configuración

### 🔹 Requisitos Previos

Antes de comenzar, asegúrate de tener instalados:

- **Python 3.x**: El lenguaje de programación utilizado para desarrollar el proyecto.
- **pip**: El administrador de paquetes de Python, necesario para instalar las dependencias del proyecto.
- **Git**: Opcional, pero recomendado para clonar el repositorio y gestionar el control de versiones.

### 🔹 Instalación

1️⃣ **Clonar el Repositorio**

Clona el repositorio del proyecto en tu máquina local y navega al directorio del proyecto.

```bash
git clone https://github.com/Alejandroclaro1227/Desarrollo_Back
```

2️⃣ **Crear y Activar un Entorno Virtual**

Crea un entorno virtual para aislar las dependencias del proyecto y actívalo.

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

3️⃣ **Instalar Dependencias**

Instala las dependencias necesarias para ejecutar el proyecto.

```bash
pip install -r requirements.txt
```

4️⃣ **Configurar la Base de Datos**

Realiza las migraciones necesarias para configurar la base de datos.

```bash
python manage.py makemigrations clientes
python manage.py migrate
```

5️⃣ **Crear un Superusuario**

Crea un superusuario para acceder al panel de administración de Django.

```bash
python manage.py createsuperuser
```

- Ingresa un nombre de usuario, correo y contraseña.


![Lista de Compras](https://raw.githubusercontent.com/Alejandroclaro1227/Desarrollo_Back/main/imagenes_prueba/Data.jfif)

----------------------------------------------------------------------------------------------------------------------------------

![Formulario](https://raw.githubusercontent.com/Alejandroclaro1227/Desarrollo_Back/refs/heads/main/imagenes_prueba/html.jfif)

----------------------------------------------------------------------------------------------------------------------------------

![JSON](https://github.com/Alejandroclaro1227/Desarrollo_Back/blob/main/imagenes_prueba/JSON.jfif)

---------------------------------------------------------------------------------------------------------------------------------

![Info](https://raw.githubusercontent.com/Alejandroclaro1227/Desarrollo_Back/refs/heads/main/imagenes_prueba/info.jfif)




6️⃣ **Ejecutar el Servidor**

Inicia el servidor de desarrollo de Django.

```bash
python manage.py runserver
```

- La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 🎯 Funcionalidades Clave

### 🔹 📋 **Gestión de Clientes**

- **Crear, actualizar y eliminar clientes**: Gestiona los datos de los clientes desde el panel de administración.
- **Datos básicos de los clientes**: Incluye tipo de documento, número de documento, nombre, apellido, correo y teléfono.

### 🔹 🛍 **Gestión de Compras**

- **Registrar compras**: Asocia compras a cada cliente, almacenando la fecha, cantidad y monto de cada compra.

### 🔹 🔎 **Búsqueda de Clientes**

- **Consultar clientes**: Busca clientes por número de documento a través de una API, con respuesta en formato JSON.

### 🔹 📤 **Exportación de Datos**

- **Exportar cliente individual**: Genera un archivo Excel o CSV con los datos del cliente.
- **Exportar reporte de fidelización**: Crea un informe en Excel con clientes que superen $5'000.000 COP en compras en el último mes.

## 🔗 Endpoints de la API

| Método | URL                                          | Descripción                                 |
| ------ | -------------------------------------------- | ------------------------------------------- |
| `GET`  | `/api/clientes/<numero_documento>/`          | Busca un cliente por su número de documento |
| `GET`  | `/api/clientes/<numero_documento>/exportar/` | Exporta los datos del cliente en Excel      |
| `GET`  | `/api/reporte-fidelizacion/`                 | Genera un reporte de clientes fidelizados   |

## 🎨 Interfaz de Usuario

- **Frontend Simple**: Un formulario HTML y JavaScript para realizar búsquedas de clientes.
- **Panel de Administración**: Accesible en `http://127.0.0.1:8000/admin` para la gestión de clientes y compras.

## 📂 Estructura del Proyecto

```
/cliente_compras
│── backend/
│   ├── clientes/
│   │   ├── migrations/         # Migraciones de la base de datos
│   │   ├── models.py           # Definición de modelos (Cliente, Compra)
│   │   ├── views.py            # Lógica de API y exportación de datos
│   │   ├── serializers.py      # Serialización de datos
│   │   ├── urls.py             # Rutas de la API
│   ├── settings.py             # Configuración del proyecto Django
│   ├── urls.py                 # Rutas principales
│   ├── wsgi.py                 # Configuración WSGI
│── frontend/
│   ├── index.html              # Página web principal
│   ├── styles.css              # Estilos básicos
│── requirements.txt            # Dependencias del proyecto
│── manage.py                   # Comando para ejecutar Django
```

## 📌 Consideraciones

- **Seguridad**: No se han agregado permisos o autenticación en la API. Se recomienda integrar Django REST Framework con Token Authentication si se expone públicamente.
- **Base de Datos**: Se usa **SQLite** por defecto, pero se puede cambiar a **PostgreSQL o MySQL** en `settings.py`.
- **Despliegue**: Puede desplegarse en **Heroku, Render, Railway** o cualquier servidor con soporte para Django.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para colaborar:

1. Haz un **fork** del repositorio.
2. Crea una **rama** (`feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz **commit** (`git commit -m "Añadir nueva funcionalidad"`).
4. Envía un **pull request**.

## 📜 Licencia

Este proyecto está bajo la Licencia **MIT**. Puedes usarlo, modificarlo y distribuirlo libremente.

---

🚀 **¡Gracias por usar el Proyecto de Gestión de Clientes!** 🎯
