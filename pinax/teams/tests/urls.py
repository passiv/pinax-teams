from django.urls import include, path

urlpatterns = [
    path('account/', include("account.urls")),
    path('', include("pinax.teams.urls", namespace="pinax_teams")),
]
