from django.conf import settings

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from decouple import config


# Sentry
if not settings.DEBUG:
    sentry_sdk.init(
        dsn="https://cebc4b414ade4f69a4cc6ee94788ddac@o4505120608944128.ingest.sentry.io/4505120612220928",  # noqa
        integrations=[
            DjangoIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )

# Main host
MAIN_HOST = 'http://localhost:8000'

# Email-host
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = config('EMAIL_HOST', cast=str)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', cast=str)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', cast=str)

# Celery
CELERY_BROKER_URL = config('REDIS_URL', cast=str) + "/0"
CELERY_RESULT_BACKEND = config('REDIS_URL', cast=str) + "/1"
CELERY_CACHE_BACKEND = 'default'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': config('REDIS_URL', cast=str) + "/2",
    }
}
