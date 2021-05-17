
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Python Functions
def hello_myapp(request):
   text="""<h1> Regression Dif Analysis Monitor for Label Drop </h1>"""
   return HttpResponse(text)

def hello_home(request):
   context={}
   text="""<h1> Regression Dif Analysis Monitor for Label Drop </h1>"""
   return render(request, 'home.html', context)


from analyzer.forms import LoginForm
from analyzer.forms import RTIForm
from analyzer.forms import RtiForm
def rti_add(request):
   context={}
   #form = RTIForm(request.POST or None)
   #context['form']=form
   #form.save()
   if request.method == "POST":
         form = RTIForm(request.POST)
        # rti_no = form.cleaned_data['rti_no']
         #print("RTI :",rti_no)
         context['form']=form
         form.save()
         print("data saved")
   else:
         #print("Validation failed")
         #rti_no="Invalid user name or not registered"
         form = RTIForm()
   context['form']=form
      
   return render(request, 'rti_create.html', context)

from analyzer.models import RTI

def crudops(request):
   #Creating an entry
    #Read ALL entries
   objects = RTI.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for obj in objects:
      obj.delete()
   
   r = RTI(
      rti_no = 1234, rti_lrg = "ABCD", rti_symptom="Connection failed",
      rti_label = "NETWOPK_MAIN_LINUX.X64", rti_dif = "a.dif"
   )
   
   r.save()
   print(r)

   #Read ALL entries
   rs = RTI.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for r in objects:
      res += r.rti_dif+"<br>"
   
   #Read a specific entry:
   r = RTI.objects.get(rti_no = 1234)
   print(r)
   res += 'Printing One entry <br>'
   res += r.rti_lrg
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   r.delete()
   
   #Update
   r = RTI(
      rti_no = 1234, rti_lrg = "ABCD", rti_symptom="Connection failed",
      rti_label = "NETWOPK_MAIN_LINUX.X64", rti_dif = "a.dif"
   )
   
   r.save()
   res += 'Updating entry<br>'
   
   r = RTI.objects.get(rti_no = 1234)
   r.rti_dif = 'b.dif'
   r.save()
   
   return HttpResponse(res)


from analyzer.forms import LoginForm

def login(request):
   username = "not logged in"
   print("Logging")
   # request.method: type of HTML action , GET or PUT or POST etc
   if request.method == "POST":
      #Get the posted form
	  # request.POST : gets the data from html page
      print("Get data from HTML")
      MyLoginForm = LoginForm(request.POST)
      username = MyLoginForm.data.get('username')
	  #Debugging
      #print( MyLoginForm.errors)
      print("Login user:",username, " ",MyLoginForm.is_valid())
     # MyLoginForm.clean_message()
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         print("Login user:",username)
      else:
         print("Validation failed")
         username="Invalid user name or not registered"
   else:
      print(" no POST")
      MyLoginForm = Loginform()
		
   return render(request, 'loggedin.html', {"username" : username})


   # Class based view
 
def my_view(request): # function based
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')

# For the above code equivalent class based code

from django.views import View
 
class MyView(View):   # Class based
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


from django.views.generic.edit import CreateView
from .models import RTI

 
class RtiCreate(CreateView): # Create view
 
    # specify the model for create view
    model =RTI
 
    # specify the fields to be displayed
 
    fields = ['rti_no', 'rti_label','rti_lrg','rti_dif','rti_symptom','rti_status']

    success_url = "/rti/about"

from django.views.generic.list import ListView
from .models import RTI
class RtiList(ListView):
   # specify the model for list view
   model = RTI


from django.views.generic.detail import DetailView
from .models import RTI

class RtiDetailView(DetailView):
   # specify the model to use
   model = RTI


from django.views.generic.edit import UpdateView

from .models import RTI
 
class RtiUpdateView(UpdateView):
 
    # specify the model for create view
    model =RTI
 
    # specify the fields to be displayed
 
    fields = ['rti_no', 'rti_label','rti_lrg','rti_dif','rti_symptom']

    success_url = "/rti/about"

from django.views.generic.edit import FormView
from .forms import RtiForm
 
class RtiFormView(FormView):
 
    # specify the model for create view
    model =RtiForm
 
    # sepcify name of template
    template_name = "rti_form.html"

    success_url = "/rti/about"

from django.views.generic.edit import FormView
from .forms import SignoffForm

def signoffed(request):
   obj=None
  
   # request.method: type of HTML action , GET or PUT or POST etc
   if request.method == "POST":
      #Get the posted form
     # request.POST : gets the data from html page
      print("###############")
      print(request.POST)
      print("###############")
      obj = SignoffForm(request.POST)
      print(obj)
      print("is valid?:", obj.is_valid())
      print("lrg:",obj.cleaned_data)
      print("lrg:",obj.cleaned_data['lrg'])
     #username = obj.data.get('username')
     #Debugging
      #print( MyLoginForm.errors)
     # print("Login user:",username, " ",MyLoginForm.is_valid())
     # MyLoginForm.clean_message()
      if obj.is_valid():
         #username = MyLoginForm.cleaned_data['username']
         print("RTI No:",obj.cleaned_data['lrg'])
      else:
         print("Validation failed")
         #obj =  SignoffForm()
   else:
      print(" no POST")
      obj = SignoffForm()
      
   return render(request, 'signoff.html', {"form" : obj})



from .forms import SignoutForm

def signout(request):
   obj=None
  
   # request.method: type of HTML action , GET or PUT or POST etc
   if request.method == "POST":
      #Get the posted form
     # request.POST : gets the data from html page
      print("###############")
      print(request.POST)
      print("###############")
      obj = SignoutForm(request.POST)
      print(obj)
      print("is valid?:", obj.is_valid())
      print("lrg:",obj.cleaned_data)
      print("lrg:",obj.cleaned_data['lrg'])
     #username = obj.data.get('username')
     #Debugging
      #print( MyLoginForm.errors)
     # print("Login user:",username, " ",MyLoginForm.is_valid())
     # MyLoginForm.clean_message()
      if obj.is_valid():
         #username = MyLoginForm.cleaned_data['username']
         print("RTI No:",obj.cleaned_data['lrg'])
      else:
         print("Validation failed")
         #obj =  SignoffForm()
   else:
      print(" no POST")
      obj = SignoutForm()
      
   return render(request, 'signoff.html', {"form" : obj})

from .forms import LabelDropForm


def labeldrop(request):
   obj=None
  
   # request.method: type of HTML action , GET or PUT or POST etc
   if request.method == "POST":
      #Get the posted form
     # request.POST : gets the data from html page
      print("###############")
      print(request.POST)
      print("###############")
      obj = LabelDropForm(request.POST)
      print(obj)
      print("is valid?:", obj.is_valid())
      print("lrg:",obj.cleaned_data)
      print("dep label:",obj.cleaned_data['dep_label'])
     #username = obj.data.get('username')
     #Debugging
      #print( MyLoginForm.errors)
     # print("Login user:",username, " ",MyLoginForm.is_valid())
     # MyLoginForm.clean_message()
      if obj.is_valid():
         #username = MyLoginForm.cleaned_data['username']
         print("RDBMS label:",obj.cleaned_data['rdbms_label'])
      else:
         print("Validation failed")
         #obj =  SignoffForm()
   else:
      print(" no POST")
      obj = LabelDropForm()
      
   return render(request, 'signoff.html', {"form" : obj})

from .forms import LabelStatusForm


def labelstatus(request):
   obj=None
  
   # request.method: type of HTML action , GET or PUT or POST etc
   if request.method == "POST":
      #Get the posted form
     # request.POST : gets the data from html page
      print("###############")
      print(request.POST)
      print("###############")
      obj = LabelStatusForm(request.POST)
      print(obj)
      print("is valid?:", obj.is_valid())
      print("lrg:",obj.cleaned_data)
      print("dep label:",obj.cleaned_data['dep_label'])
     #username = obj.data.get('username')
     #Debugging
      #print( MyLoginForm.errors)
     # print("Login user:",username, " ",MyLoginForm.is_valid())
     # MyLoginForm.clean_message()
      if obj.is_valid():
         #username = MyLoginForm.cleaned_data['username']
         print("RDBMS label:",obj.cleaned_data['rdbms_label'])
      else:
         print("Validation failed")
         #obj =  SignoffForm()
   else:
      print(" no POST")
      obj = LabelStatusForm()
      
   return render(request, 'signoff.html', {"form" : obj})



# import generic FormView
from django.views.generic.edit import FormView
  




from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)
  
  
  
# delete view for details
def RtiDeleteView(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    obj = get_object_or_404(RTI, id = id)
  
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
  
    return render(request, "delete_view.html", context)

