from models import User


class EmailAuth(object):
    def authenticate(self, email=None, password=None):
        """
        get an instance of User using the supplied email and check itspassword
        """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None
