from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import (
    AgilePrinciples,
    AgileValues,
)

# Register your models here.

@admin.register(AgilePrinciples)
class AgilePrinciplesAdmin(SimpleHistoryAdmin):
    pass


@admin.register(AgileValues)
class AgileValuesAdmin(SimpleHistoryAdmin):
    pass