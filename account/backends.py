# in models.py I created an email with normalize.
# All emails are lowercase for django. 
# But The user can type capital letters when writing an email.
# This shouldn't be an error.
# so, I write backens.py

# I get account model as get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

# document information. You can use this in all projects, email-username...etc.
# write AUTHENTICATION_BACKENDS = () in setting.py. I will say that, set this for all users.