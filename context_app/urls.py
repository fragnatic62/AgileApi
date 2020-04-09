from django.urls import path

from .views import (
    AgileValuesViewset,
    AgilePrincipleViewset,
)

urlpatterns = [
    path("agile_values/", AgileValuesViewset.as_view(), name="agile_value_list"),
    path("agile_principles/", AgilePrincipleViewset.as_view(), name="agile_principle_list")
]