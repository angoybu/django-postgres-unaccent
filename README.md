## Django Postgres Unaccent

In your settings file change the database engine to `django_postgres_unaccent`.

```
DATABASES = {
    "default": {
        "ENGINE": "django_postgres_unaccent",
        ...
    }
}
