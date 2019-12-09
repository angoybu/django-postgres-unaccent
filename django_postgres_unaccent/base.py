# -*- coding: utf-8 -*-
# Found in
# https://stackoverflow.com/questions/5619848/how-to-have-accent-insensitive-filter-in-django-with-postgres/5787198#5787198
# parts of credits comes to clarisys.fr
from django.db.backends.postgresql.base import *


class DatabaseOperations(DatabaseOperations):
    def lookup_cast(self, lookup_type, internal_type=None):
        if lookup_type in('icontains', 'istartswith'):
            return "UPPER(unaccent(%s::text))"
        else:
            return super(DatabaseOperations, self).lookup_cast(lookup_type, internal_type)


class DatabaseWrapper(DatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.operators['icontains'] = 'LIKE UPPER(unaccent(%s))'
        self.operators['istartswith'] = 'LIKE UPPER(unaccent(%s))'
        self.ops = DatabaseOperations(self)
