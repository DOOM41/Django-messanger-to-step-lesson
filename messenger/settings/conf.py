# from django.conf import settings

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration


# # Sentry
# if not settings.DEBUG:
#     sentry_sdk.init(
#         dsn="https://cebc4b414ade4f69a4cc6ee94788ddac@o4505120608944128.ingest.sentry.io/4505120612220928",  # noqa
#         integrations=[
#             DjangoIntegration(),
#         ],

#         # Set traces_sample_rate to 1.0 to capture 100%
#         # of transactions for performance monitoring.
#         # We recommend adjusting this value in production.
#         traces_sample_rate=1.0,

#         # If you wish to associate users to errors (assuming you are using
#         # django.contrib.auth) you may enable sending PII data.
#         send_default_pii=True
#     )
