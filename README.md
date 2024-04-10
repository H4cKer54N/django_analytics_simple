# Django Analytics

**See documentation at :** [Español](README_es.md) | [English](README.md)

Django Analytics is a Django package designed to facilitate tracking and analysis of user data in web applications. It provides middleware that records information about users, including details such as browser, operating system, device, and geographical location. The collected data is stored in a new database table, enabling detailed analytics to improve user experience and make informed decisions in application development and maintenance.

## Installation

You can install Django Analytics using pip:

```bash
pip install django-analytics
```

Then, add 'django_analytics' to your Django project's installed apps in the settings.py file:

```python
INSTALLED_APPS = [
    ...
    'django_analytics',
    ...
]
```

Next, include the provided middleware in your project's middleware stack in the same settings.py file:

```python
MIDDLEWARE = [
    ...
    'django_analytics.middleware.AnalyticsMiddleware',
    ...
]
```

## Configuration
Django Analytics requires the GeoLite2-City.mmdb file for IP geolocation, which should already be included in the package, and it will be updated monthly.

Additionally, you can set the ANALYTICS_LANGUAGE variable in your Django project's settings.py file to specify the language for location data retrieval.


```python
ANALYTICS_LANGUAGE = 'en'  # Specify the language for location data retrieval
```

Please note that you may need to review the languages supported by MaxMindDB for proper configuration.


## Dependencies

Django Analytics relies on the following external libraries:

[MaxMindDB] https://pypi.org/project/maxminddb/
[User-agents] https://pypi.org/project/user-agents/
Ensure that these dependencies are installed before using Django Analytics.

## Usage

After configuring Django Analytics, run the following commands to apply migrations:

```bash
python manage.py makemigrations django_analytics
python manage.py migrate
```

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. See the LICENSE file for details.

## Author

[Santiago Nestor Britos](mailto:s.britos@hotmail.com) - s.britos@hotmail.com