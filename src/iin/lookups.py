from django.db.models import CharField, TextField
from django.db.models.lookups import In


@CharField.register_lookup
@TextField.register_lookup
class IIn(In):
    """
    Case-insensitive version of the __in lookup
    Usage: field_name__iin=[...]
    """

    lookup_name = "iin"

    def process_lhs(self, compiler, connection, lhs=None):
        lhs, params = super().process_lhs(compiler, connection, lhs=lhs)
        return f"LOWER({lhs})", params

    def process_rhs(self, compiler, connection):
        rhs, params = super().process_rhs(compiler, connection)
        return rhs, tuple(p.lower() if isinstance(p, str) else p for p in params)
