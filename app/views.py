from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
import numpy as np
import joblib
from django.shortcuts import render
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tensorflow import keras
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm
from django.contrib import messages
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import numpy as np
import joblib
from . import forms
from django.shortcuts import render
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tensorflow import keras
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm
from django.contrib import messages
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import numpy as np
import joblib
from . import forms
import numpy as np
import joblib

model = joblib.load('G:/JAYASURYA/OWN/price prediction regreesion/deploy1/app/rfc1.pkl')

# Create your views here.
def index(request):
    return render(request, 'index.html')







def predict(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features).astype(float)]
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        return render(request, 'test.html', {'prediction_text':f'The vechicle estimation price is {output}'})
    return render(request, 'test.html')

def home(request):
    return render(request, 'test.html')


def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'registration/login.html', context)

def logoutusers(request):
    logout(request)
    return redirect('login')


