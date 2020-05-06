from django.shortcuts import render, get_object_or_404, redirect
from .models import Photos
from .forms import PhotoForm
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.


def book_list(request):
    books = Photos.objects.all()
    form = PhotoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = PhotoForm
        return redirect('/viewspace')
    context = {
        'books': books,
        'form': form
    }
    return render(request, 'viewspace/view_list.html', context)


def photo_create(request):

    form = PhotoForm()
    context = {'form': form}
    return render(request, 'viewspace/includes/photo_form.html', context)


def photo_delete(request, pk):
    obj = get_object_or_404(Photos, pk=pk)
    template_name = 'viewspace/photo_delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/viewspace")
    return render(request, template_name, {'obj': obj})

