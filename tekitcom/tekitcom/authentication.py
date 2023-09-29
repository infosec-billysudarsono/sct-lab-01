from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserAuthBackend:
    def authenticate(self, request, username=None, password=None, login_type=None):
        try:
            user = User.objects.get(username=username)
            
            if request.POST['login_type'] not in ["PASSWORD", "DEFAULT", "GOJEK_OTP", "BLIBLI"]:
                raise ValidationError('login_type is not one of the values accepted ["PASSWORD", "DEFAULT", "GOJEK_OTP", "BLIBLI_OAUTH"]')
            
            if request.POST['login_type'] == "GOJEK_OTP":
                return user
            
            if user.check_password(password):
                return user
            
            return None
        
        except User.DoesNotExist:
            raise ValidationError('User does not exists!')

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError('User does not exists!')