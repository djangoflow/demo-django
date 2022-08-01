from django.apps import AppConfig


class NotesConfig(AppConfig):
    default_auto_field = "hashid_field.BigHashidAutoField"
    name = 'notes'
