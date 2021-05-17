from django import forms
from analyzer.models import Users

from django.forms import ValidationError

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_username(self):
      username = self.cleaned_data.get("username")
      print("user :",username)
      user1 = Users.objects.filter(username = username)
      if(user1):
         print("Valid user name")
      else:
         print("not valid anme")
      if user1:
         print("Valid user")         
      else:
         raise ValidationError("User does not exist in our db!")
      return username


class RtiForm(forms.Form):
   rti_no = forms.IntegerField()
   rti_label = forms.CharField(max_length = 100)
   rti_lrg = forms.CharField(max_length = 100)
   rti_dif = forms.CharField(max_length = 100)
   rti_symptom = forms.CharField(max_length = 100)


# import GeeksModel from models.py
from .models import RTI
  
# create a ModelForm
class RTIForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = RTI
        fields = "__all__"


# import GeeksModel from models.py
from .models import RTI,signoff,LabelDrop,LabelStatus
  
# create a ModelForm
class SignoutForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = signoff
        fields = "__all__"

# create a ModelForm
class LabelDropForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = LabelDrop
        fields = "__all__"

# create a ModelForm
class LabelStatusForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = LabelStatus
        fields = "__all__"



# import GeeksModel from models.py
from .models import signoff
  
# create a ModelForm
class SignoffForm(forms.Form):
    # specify the name of model to use
    label = forms.CharField(max_length = 100)
    lrg = forms.CharField(max_length = 100)
    dif = forms.CharField(max_length = 100)


    # iterable
    status_CHOICES =(
    ("1", "Critical"),
    ("2", "Ignorable"),
    ("3", "No SS"),)
   
    status= forms.ChoiceField(choices = status_CHOICES)

    #def clean_username(self):
    # this function will be used for the validation
    
    def clean(self):
 
        # data from the form is fetched using super function
        super(SignoffForm, self).clean()
         
        # extract the username and text field from the data
        label = self.cleaned_data.get('label')
        lrg = self.cleaned_data.get('lrg')
        dif = self.cleaned_data.get('dif')
        status = self.cleaned_data.get('status')
        print("clean data", self.cleaned_data)
        # conditions to be met for the username length
        #if len(username) < 5:
         #   self._errors['username'] = self.error_class([
          #      'Minimum 5 characters required'])
       # if len(text) <10:
        #    self._errors['text'] = self.error_class([
 #               'Post Should Contain a minimum of 10 characters'])
 
        # return any errors if found
        #return self.cleaned_data

        
   


