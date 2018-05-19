from django.http import HttpResponseRedirect
def filt(func):
    def inter(request,*args,**kwargs):
        if request.session.get("uid"):
            return func(request,*args,**kwargs)
        else:
            re = HttpResponseRedirect("/reg/login/")
            re.set_cookie("url",request.get_full_path())
            return re
    return inter