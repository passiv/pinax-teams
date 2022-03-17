# include these urls instead of urls.py if you are using the WSGI + Django middlewares
# to set request.team, manually hooking up List/Create views as well as the accept/reject

from django.urls import path

from . import views

app_name = "pinax_teams"


urlpatterns = [
    # team specific
    path('detail/', views.team_detail, name="team_detail"),
    path('join/', views.team_join, name="team_join"),
    path('leave/', views.team_leave, name="team_leave"),
    path('apply/', views.team_apply, name="team_apply"),
    path('edit/', views.team_update, name="team_edit"),
    path('manage/', views.TeamManageView.as_view(), name="team_manage"),
    path('ac/users-to-invite/', views.autocomplete_users, name="team_autocomplete_users"),  # noqa
    path('invite-user/', views.TeamInviteView.as_view(), name="team_invite"),
    path('members/<int:pk>/revoke-invite/', views.team_member_revoke_invite, name="team_member_revoke_invite"),  # noqa
    path('members/<int:pk>/resend-invite/', views.team_member_resend_invite, name="team_member_resend_invite"),  # noqa
    path('members/<int:pk>/promote/', views.team_member_promote, name="team_member_promote"),  # noqa
    path('members/<int:pk>/demote/', views.team_member_demote, name="team_member_demote"),  # noqa
    path('members/<int:pk>/remove/', views.team_member_remove, name="team_member_remove"),  # noqa
]
