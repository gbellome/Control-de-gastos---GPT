# **Controla - App de Gestión de Gastos**

**Controla** es una aplicación web que permite a los usuarios gestionar sus gastos personales de manera eficiente. La app ofrece la posibilidad de cargar resúmenes de movimientos financieros, categorizarlos automáticamente, establecer objetivos de gastos mensuales y generar reportes detallados. Con un diseño moderno y fácil de usar, **Controla** ayuda a tomar el control de las finanzas personales.

---

## **Características Principales**

- **Cargar resúmenes de movimientos**: Los usuarios pueden cargar sus resúmenes financieros en formato PDF o CSV, donde la aplicación identificará automáticamente el banco y tipo de resumen (tarjeta de crédito, tarjeta de débito, o caja de ahorro).
- **Categorización automática de movimientos**: Los movimientos cargados se categorizan automáticamente con reglas predefinidas o personalizables.
- **Establecimiento de objetivos de gasto**: Los usuarios pueden definir objetivos mensuales vinculados a su sueldo y recibir alertas si exceden los límites establecidos.
- **Generación de reportes detallados**: Se generan reportes mensuales que resumen los gastos categorizados, los totales por categoría, y comparaciones con los límites definidos. Los reportes se pueden exportar en formato CSV.
- **Interfaz moderna y responsiva**: Diseñada con **Material UI** para ofrecer una experiencia de usuario fluida en todos los dispositivos.

---

## **Tecnologías Usadas**

- **Backend**:

  - **Flask**: Framework en Python para crear la API RESTful.
  - **pdfplumber**: Para extraer datos de PDFs de los resúmenes financieros.
  - **Pandas**: Para procesar y limpiar los datos extraídos de los archivos.
  - **Flask-CORS**: Para permitir la comunicación entre el backend y el frontend.
  - **SQLAlchemy**: ORM para interactuar con la base de datos.
  - **SQLite** (desarrollo) / **PostgreSQL** (producción): Base de datos para almacenar las transacciones y demás datos de los usuarios.
  - **Gunicorn**: Servidor de producción para la app Flask.

- **Frontend**:

  - **React**: Framework de JavaScript para construir la interfaz de usuario.
  - **Material UI**: Biblioteca de componentes de UI para diseñar una interfaz moderna y accesible.
  - **react-dropzone**: Para permitir la carga de archivos PDF y CSV de forma sencilla.
  - **Axios**: Para realizar las solicitudes HTTP desde el frontend al backend.

- **Despliegue**:
  - **Heroku**: Plataforma en la nube para el despliegue de la aplicación.
  - **PostgreSQL en Heroku**: Para la base de datos en producción.

---

## **Estructura del Proyecto**

### **Backend**

backend/
├── app/
│ ├── init.py
│ ├── models/
│ │ ├── transaccion.py # Clase para manejar movimientos
│ │ ├── categoria.py # Clase para manejar categorías
│ │ ├── objetivo.py # Clase para manejar objetivos
│ │ └── auditoria.py # Clase para registrar acciones
│ ├── controllers/
│ │ ├── transacciones.py # Rutas relacionadas con movimientos
│ │ ├── categorias.py # Rutas relacionadas con categorías
│ │ ├── objetivos.py # Rutas relacionadas con objetivos
│ │ └── reportes.py # Rutas relacionadas con reportes
│ ├── services/
│ │ ├── reglas.py # Categorización automática
│ │ ├── alertas.py # Generación de alertas
│ │ └── exportacion.py # Generación de archivos CSV
│ ├── config.py # Configuración del entorno
│ ├── config_dev.py # Configuración para desarrollo
│ ├── config_prd.py # Configuración para producción
│ └── init.py
├── run.py # Archivo principal para ejecutar el servidor
├── requirements.txt # Dependencias de Python
└── .env # Variables de entorno
