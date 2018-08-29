from django.contrib.auth import get_backends, get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login as auth_login


@user_passes_test(lambda u: u.is_superuser and u.is_active)
def login_as(request, id):
    backend = get_backends()[0]
    user = get_user_model().objects.get(id=id)
    user.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
    if user.is_active:
        auth_login(request, user)
        return HttpResponseRedirect('/')
    # TODO
    return HttpResponse("500 error", status=500)
