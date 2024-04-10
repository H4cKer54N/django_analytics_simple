=======================
Django Analytics simple
=======================

**Ver documentación en :** [Español](README_es.md) | [English](README.md)

Django Analytics simple es un paquete de Django diseñado para facilitar el seguimiento y análisis de datos de usuario en aplicaciones web. Proporciona middleware que registra información sobre los usuarios, incluidos detalles como el navegador, el sistema operativo, el dispositivo y la ubicación geográfica. Los datos recopilados se almacenan en una nueva tabla de base de datos, lo que permite realizar análisis detallados para mejorar la experiencia del usuario y tomar decisiones informadas en el desarrollo y mantenimiento de aplicaciones.

Instalación
-----------

Puedes instalar Django Analytics simple usando pip:

.. code-block:: bash

    pip install django_analytics_simple

Luego agrega 'django_analytics_simple' a tus aplicaciones instaladas en tu archivo settings.py de tu proyecto django:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'django_analytics_simple',
        ...
    ]

Lo siguiente es incluir el middleware en tus middlewares, en el mismo archivo que hiciste lo de installed apps, (settings.py):

.. code-block:: python

    MIDDLEWARE = [
        ...
        'django_analytics_simple.middleware.AnalyticsMiddleware',
        ...
    ]

Configuración
-------------

Django Analytics simple requiere el archivo GeoLite2-City.mmdb para la geolocalización por IP que ya debería venir incluido en el paquete, el mismo lo iré actualizando mensualmente.

Además, puedes establecer la variable ANALYTICS_LANGUAGE en el archivo settings.py de tu proyecto de Django para especificar el idioma para la recuperación de datos de ubicación.

.. code-block:: python

    ANALYTICS_LANGUAGE = 'en'  # Especifica el idioma para la recuperación de datos de ubicación.

Ten en cuenta que es posible que necesites revisar los idiomas admitidos por MaxMindDB para una configuración adecuada.

Dependencias
------------

Django Analytics simple depende de las siguientes bibliotecas externas:

`MaxMindDB <https://pypi.org/project/maxminddb/>`__
`User-agents <https://pypi.org/project/user-agents/>`__

Asegúrate de que estas dependencias estén instaladas antes de usar Django Analytics.

Uso
---

Después de configurar Django Analytics simple, ejecuta los siguientes comandos para aplicar las migraciones:

.. code-block:: bash

    python manage.py makemigrations django_analytics_simple
    python manage.py migrate

Licencia
--------

Este proyecto está licenciado bajo la Licencia Internacional de Creative Commons Atribución-NoComercial-SinDerivadas 4.0. Consulta el archivo LICENSE para más detalles.

Autor
-----

`Santiago Nestor Britos <mailto:s.britos@hotmail.com>`__ - s.britos@hotmail.com
