from django.urls import path
from .views import SignUpView, UserEditForm, ShowProfilePageView, EditProfilePageView, CreateProfilePageView, AccountShowView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/account_page/', AccountShowView.as_view(), name='account_page'),
    path('edit_account/', UserEditForm.as_view(), name='edit_account'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='user_profile'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page'),
]