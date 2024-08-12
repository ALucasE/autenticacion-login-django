# Autenticacion y Login

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)
![Django](https://img.shields.io/badge/Django-4.2.x-blue)
![Boostrap](https://img.shields.io/badge/Boostrap-5.x-yellow)
![HTML](https://img.shields.io/badge/HTML-5-violet)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.x-orange)
![MySQL](https://img.shields.io/badge/MySQL-5.x-blue)

## Descripción
Mejorá la seguridad de tu sitio web con esta implementación de un sistema de inicio de sesión simple en Django 4.2 con Phyton 3.10

## Dependencias
crispy-bootstrap5==2024.2
Django==4.2
django-crispy-forms==2.3
python-decouple==3.8

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ALucasE/autenticacion-login-django.git
    cd autenticacion-login-django
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the requirements:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Esta app usa Crispy forms bootstrap5

[GitHub](https://github.com/django-crispy-forms/crispy-bootstrap5)

settings.py
```bash
pip install crispy-bootstrap5
```


settings.py
```py
INSTALLED_APPS = (
    'crispy_forms',
    'crispy_bootstrap5',
)

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

Template
```html
{% load crispy_forms_tags %}

{{ form | crispy }}
```

## License

This project is licensed under the MIT License.

## Contacto

- **Correo Electrónico**: alucase@gmail.com
- **LinkedIn**: [Lucas Acosta](https://www.linkedin.com/in/alucase/)
- **GitHub**: [ALucasE](https://github.com/ALucasE)
- **Web**: [alucase.github.io](https://alucase.github.io/)

---

¡Gracias por visitar mi github! Espero que disfrutes explorando mis proyectos.
