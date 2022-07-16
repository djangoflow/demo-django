import tablib
from import_export.admin import ImportExportMixin
from import_export.formats import base_formats
from import_export.widgets import ForeignKeyWidget


class EnsureForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if value:
            return self.get_queryset(value, row, *args, **kwargs).get_or_create(
                **{self.field: value}
            )[0]
        else:
            return None


class SCSV(base_formats.CSV):
    def get_title(self):
        return "scsv"

    def create_dataset(self, in_stream, **kwargs):
        kwargs["delimiter"] = ";"
        kwargs["format"] = "csv"
        return tablib.import_set(in_stream, **kwargs)


class SCSVAdminMixin(ImportExportMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formats += [SCSV]

    def get_import_formats(self):
        return [f for f in self.formats if f().can_import()]
