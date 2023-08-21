from django.shortcuts import render
from django.views import View


class Home(View):
    ### methods:
    # setup()
    # dispatch()
    # http_method_not_allowed()
    # options()
    # http_method_names, witch methods are allowed
    
    # def get(self, request):
    #     return render(request, 'home/home.html')
    

    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers['host'] = 'localhost'
        response.headers['user'] = request.user
        return response
    
    def http_method_not_allowed(self, request, *args, **kwargs):
        super().http_method_not_allowed(request, *args, **kwargs)
        return render(request, 'method_not_allowed.html')


