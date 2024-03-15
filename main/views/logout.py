from django.contrib.auth import logout
def user_logout(request):
    logout(request)