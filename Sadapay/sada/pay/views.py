from django.shortcuts import render

# Create your views here.

def heading(request):
    m = {"name":"Hey! it's Tashfeen Mehmood"}
    return render(request,'index.html',m)
def about(request):
    d = {'details': 'Graduate in Computer Science From FJWU'}
    return render(request,'index.html', d)





