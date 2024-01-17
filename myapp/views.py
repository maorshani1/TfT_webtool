# myapp/views.py

from django.shortcuts import render

def download_template(request):
    context = {
        'message': "Hey teachers, we thought you would want to try our amazing social referent prevention! The first thing you need to do is to give us a list of all your students and their emails, which we will use to create personalized questionnaires. Please download the following excel template and make sure to have all details under the right column. When you're ready, click 'next' to upload the file with the requested details (don't worry, you don't have to do it right now, you can do it next time you log into the system)."
    }
    return render(request, 'download_template.html', context)
