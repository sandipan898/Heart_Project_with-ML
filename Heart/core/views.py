from django.shortcuts import render,HttpResponse

# Create your views here.
def form_view(request):
    return render(request ,template_name='Mainapp/index.html')


def resault_view(request):
    return render(request ,template_name='Mainapp/resault.html')