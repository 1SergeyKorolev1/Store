from django.shortcuts import render
import os
import json


# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        data = {
            'User': email,
            'Textarea': textarea
        }

        json_f = 'data.json'

        with open(json_f, 'a') as f:
            if os.stat(json_f).st_size == 0:
                json.dump([data], f)
            else:
                with open(json_f) as f_:
                    list_ = json.load(f_)
                    list_.append(data)
                with open(json_f, 'w') as f_1:
                    json.dump(list_, f_1)

    return render(request, 'catalog/contact.html')
