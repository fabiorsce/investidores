from django.contrib.auth.models import User, check_password

class EmailAuthBackend(object):
    """
    Email Authentication Backend
    
    Allows a user to sign in using an {email or username}/password pair rather.
    """
    
    def authenticate(self, username=None, password=None):
        
        if '@' in username: 
            kwargs = {'email': username}
        else:
            kwargs={'username':username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None 

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None