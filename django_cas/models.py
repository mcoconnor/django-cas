from django.db import models
from django.contrib import auth

def get_user_model():
    '''
    For Django < 1.5 backward compatibility
    '''
    if hasattr(auth, 'get_user_model'):
        return auth.get_user_model()
    else:
        return auth.models.User

User = get_user_model()
