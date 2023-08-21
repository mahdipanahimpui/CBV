from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from . forms import CarCreateForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, DeleteView, UpdateView, MonthArchiveView
from django.contrib.auth import views as auth_views
from . models import Car
from . serializers import CarSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView


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

# class Home(ListView):
#     template_name = 'home/home.html'
#     # model = Car # is available in template by <object_list>
#     # to change the name of <object_list>:
#     context_object_name = 'cars'
#     ordering = 'year' # a field in Car model
#     # allow_empty = False # True by default, eror 4XX if query is empty
 
#     # for specific query set use queryset, dont use model = Car
#     # queryset = Car.objects.filter(year__gte=2010)

#     # for complex queries use get_queryset
#     def get_queryset(self):
#         return Car.objects.filter(year__gte=2010)
    
    # adding more context using def_context_data
    # def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         ## adding data to context
#         context['username'] = 'jack'
#         return context

#-------------------------------------------------------


# class Home(ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'cars'
#     model = Car

# class CarDetailView(DetailView):
#     template_name = 'home/detail.html'
#     context_object_name = 'car'
#     model = Car
    # slug_field = 'name' # set slug for url in tempalte 'home:home' car.name, in url <slug:slug>
    # if <slug:my_slug_name> set the slug_rul_kwarg
    # slug_url_kwarg = 'my_slug_name'
    # change the pk in <int:pk> by pk_url_kwarg

    # set a specific queryset by queryset
    # queryset = Car.objects.filter(year__gte=2010)# returning obj from the queryset objects, if not found error


    # def get_queryset is available too, 

    # using specific parameters: override the get_object
    # ex) '<int:year>/<str:name>' in path
    # def get_object(self, queryset=None):
    #     return Car.objects.get(
    #         year=self.kwargs['year'],
    #         name=self.kwargs['name']
    #     )

#---------------------------------------------------



# class Home(ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'cars'
#     model = Car


# class CarCreateView(FormView):
#     template_name = 'home/create.html'
#     form_class = CarCreateForm
#     # success_url = 'home/home' # to use namespace use reverse_lazy
#     success_url = reverse_lazy('home:home')


#     # override the form_valid

#     def form_valid(self, form): 
#         self._create_car(form.cleaned_data)
#         # messages.success(self.request, 'created ', 'success') # request is available by self
#         return super().form_valid(form)

#     # _ means the method is for the class not use in out of class, as warning
#     def _create_car(self, data): 
#         Car.objects.create(name=data['name'], owner=data['owner'], year=data['year'])

# ------------------------------------------------------------------------------------


# createView is use to create object, form handling is charge of the createView
# class Home(ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'cars'
#     model = Car


# class CarCreateView(CreateView):
#     template_name = 'home/create.html'
#     model = Car
#     fields = ['name', 'year']
#     success_url = reverse_lazy('home:home')

#     # can use form valid
#     def form_valid(self, form):
#         car = form.save(commit=False)
#         car.owner = self.request.user.username if self.request.user.username else 'nothing'

#         car.save()
#         # messages.success(self.request, 'car created', 'success')
#         return super().form_valid(form)


#----------------------------------------------------



# class Home(ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'cars'
#     model = Car


# # just send a id
# class CarDeleteView(DeleteView):
#     model = Car
#     success_url = reverse_lazy('home:home')
#     template_name = 'home/delete.html' # ask to remove obj
#     # send the <object> to template_name


# class CarupdateView(UpdateView):
#     model = Car
#     fields = ['name']
#     success_url = reverse_lazy('home:home')
#     template_name = 'home/update.html'
#     # form is sent automatically to template_name

#     # template_name_suffix = '_update_form' # converted to car_update_form.html



# class UserLoginView(auth_views.LoginView):
#     template_name = 'home/login.html' # 'registration/login.html' is default
#     # AuthenticationForm is default

#     # after login
#     next_page = reverse_lazy('home:home') # or set the LOGIN_REDIRECR_URL = 'home:home' in settings.py, is used by other views




# class UserLogoutView(auth_views.LogoutView):
#     next_page = reverse_lazy('home:home') # or LOGOUT_REDIRECT_URL = 'home:home'





# class MonthCarView(MonthArchiveView):
#     model = Car
#     date_field = 'created'
#     template_name = 'home/home.html' # where to show data as form
#     context_object_name = 'cars'

#     # if using <int:month> use month_format
#     # by suing <str:month> month_format not need
#     month_format = '%m'

#     # result: localhost/2022/3/ filters the objects by date



# ------------------------------------------------------------------------





class Home(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()



class SingleCar(RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    # sent the <int:pk> by default but can change like <str:name>/ and change the lookup_field = name
    lookup_field = 'name'  # sensitive to capital/small letters



class DeleteCar(DestroyAPIView): # use delete mehtod in url
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    # sent the <int:pk>/ to change use:
    lookup_field = 'name' # field name to delete
    lookup_url_kwarg = 'car_name' # name of param in url





class CarCreate(CreateAPIView): # use delete mehtod in url
    serializer_class = CarSerializer
    queryset = Car.objects.all()




# put method: update the all fields, if not all, error occur
# patch method: update partial
class CarUpdate(UpdateAPIView):
        serializer_class = CarSerializer
        queryset = Car.objects.all()