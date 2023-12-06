
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserData

def user_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_data')
    else:
        form = UserForm()

    users = UserData.objects.all()
    return render(request, 'index.html', {'form': form, 'users': users})













































# from django.shortcuts import render
# from app.models import data
# # Create your views here.  
# def index(request):
#     dt = data.objects.all()
#     dict = {'d':dt}
#     return render(request,'index.html',dict)

# def about(request):
#     return render(request, 'about.html')
# def blogsingle(request):
#     return render(request, 'blog-single.html')
# def blog(request):
#     return render(request, 'blog.html')
# def contact(request):
#     return render(request, 'contact.html')
# def portfolio(request):
#     return render(request, 'portfolio.html')