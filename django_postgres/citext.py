from django.db.models import fields


class CaseInsensitiveTextField(fields.TextField):

    def db_type(self, connection):
        return "citext"
