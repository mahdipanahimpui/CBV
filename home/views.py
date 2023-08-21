from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView
from . models import Car


# class Home(View):
    ### methods:
    # setup()
    # dispatch()
    # http_method_not_allowed()
    # options()
    # http_method_names, witch methods are allowed
    
    # def get(self, request):
    #     return render(request, 'home/home.html')
    

    # def options(self, request, *args, **kwargs):
    #     response = super().options(request, *args, **kwargs)
    #     response.headers['host'] = 'localhost'
    #     response.headers['user'] = request.user
    #     return response
    
    # def http_method_not_allowed(self, request, *args, **kwargs):
    #     super().http_method_not_allowed(request, *args, **kwargs)
    #     return render(request, 'method_not_allowed.html')

#----------------------------------------------------------------------



# class Home(TemplateView):
#     # by TemplateView get mehod and return render the template name done automatically
#     template_name = 'home/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         ## adding data to context
#         context['cars'] = Car.objects.all()
#         return context
    

# class Two(RedirectView):
    # url = 'google.com' # needs, add the url end of the current url, 127.0.0.1/two/google.com
    # url = 'https://google.com'

    # note: url doesnt support url names, so use pattern_names
    # pattern_name = 'home:home'



    # permanent = False # True, used in seo, 

    # query_string = True # False by default, queries sent in redirect or not

    # do a process befor redirect
    # def get_redirect_url(self, *args, **kwargs):
    #     print('*'*90)
    #     print('befor redirect')
    #     print('*'*90)
    #     # print(kwargs['name'], kwargs['id']) # getting the parameters
    #     # kwargs.pop('name')
    #     # kwargs.pop('id')
    #     # popped because home:home dont need the params, or can use url(top) instead pop the kwargs
    #     return super().get_redirect_url(*args, **kwargs)


    # sending the params using url(top) without urlpatterns or get_redirect_url:
    # url = '/home/%(name)s/%(id)i/' # i: int, s: str



#-----------------------------------------------------------

class Home(ListView):
    template_name = 'home/home.html'
    # model = Car # is available in template by <object_list>
    # to change the name of <object_list>:
    context_object_name = 'cars'
    ordering = 'year' # a field in Car model
    # allow_empty = False # True by default, eror 4XX if query is empty

    # for specific query set use queryset, dont use model = Car
    # queryset = Car.objects.filter(year__gte=2010)

    # for complex queries use get_queryset
    def get_queryset(self):
        return Car.objects.filter(year__gte=2010)
    
    # adding more context using def_context_data
    # def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         ## adding data to context
#         context['username'] = 'jack'
#         return context