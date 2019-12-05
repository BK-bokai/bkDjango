from django.contrib import auth

def authenticate(func):
    def new_func(*args,**kwargs):
        