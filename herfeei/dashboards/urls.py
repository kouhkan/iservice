from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView

from herfeei.dashboards.apis.contacts import ContactView
from herfeei.dashboards.apis.faqs import FaqView, FaqCategoriesView, FaqDetailView
from herfeei.dashboards.apis.rules import GetRulesView
from herfeei.dashboards.apis.users import UpdateUserAvatarView, UpdateUserProfileView
from herfeei.users.apis.addresses import CreateUserAddressView, GetUserAddressesListView, GetUserAddressView, \
    UpdateUserAddressView, DeleteUserAddressView, ChangeDefaultUserAddressView

urlpatterns = [
    path("", include([
        path("users/", include([
            path("avatar/", UpdateUserAvatarView.as_view(), name="avatar"),
            path("profile/", UpdateUserProfileView.as_view(), name="profile"),
        ])),
        path("logout/", TokenBlacklistView.as_view(), name="logout"),
        path("addresses/", include([
            path("", CreateUserAddressView.as_view(), name="create-address"),
            path("<int:id>/", GetUserAddressView.as_view(), name="get-user-address"),
            path("list/", GetUserAddressesListView.as_view(), name="get-user-addresses"),
            path("update/<int:id>/", UpdateUserAddressView.as_view(), name="update-user-addresses"),
            path("delete/<int:id>/", DeleteUserAddressView.as_view(), name="delete-user-addresses"),
            path("default/<int:id>/", ChangeDefaultUserAddressView.as_view(), name="change-default-user-addresses"),
        ])),
        path("rules/", GetRulesView.as_view(), name="get-rules"),
        path("faqs/", include([
            path("", FaqView.as_view(), name="get-faqs"),
            path("<slug:slug>/", FaqDetailView.as_view(), name="faq-details"),
            path("categories/", FaqCategoriesView.as_view(), name="get-faq-categories"),
        ]), name="faqs"),
        path("contacts/", ContactView.as_view(), name="contacts")
    ]))
]
