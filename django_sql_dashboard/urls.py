from django.urls import path

from .views import (
    dashboard,
    dashboard_index,
    dashboard_json,
    dashboard_query,
    dashboard_query_csv,
    dashboard_query_json,
    dashboard_query_tsv,
)

urlpatterns = [
    path("", dashboard_index, name="django_sql_dashboard-index"),
    path("<slug>/", dashboard, name="django_sql_dashboard-dashboard"),
    path("<slug>.json", dashboard_json, name="django_sql_dashboard-dashboard_json"),
    path(
        "<slug>/<int:id>", dashboard_query, name="django_sql_dashboard-dashboard_query"
    ),
    path(
        "<slug>/<int:id>.json",
        dashboard_query_json,
        name="django_sql_dashboard-dashboard_query_json",
    ),
    path(
        "<slug>/<int:id>.csv",
        dashboard_query_csv,
        name="django_sql_dashboard-dashboard_query_csv",
    ),
    path(
        "<slug>/<int:id>.tsv",
        dashboard_query_tsv,
        name="django_sql_dashboard-dashboard_query_tsv",
    ),
]
