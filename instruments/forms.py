from django.forms import ModelForm
from user.models import User
from django.contrib.auth.forms import UserCreationForm

# i pull the Original User Form and added to the Form my extensions 

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','age','City','Full_address','Postal_Code','Phonenumber')


 