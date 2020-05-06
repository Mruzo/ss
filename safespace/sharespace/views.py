from django.shortcuts import render, get_object_or_404
from .forms import RoomForm, SearchForm
from .models import Room, Post
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.views.generic import View, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm
from django.template.loader import render_to_string

# Create your views here.


def shared_view(request):
    tmpl_vars = {
        'rooms': Room.objects.all(),
        # 'form': PostForm(),
    }
    return render(request, 'sharespace/main.html', tmpl_vars)


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            rooms = list(Room.objects.all().values())
            data['html_room_list'] = render_to_string('sharespace/includes/partial_room_form.html',
                                                      {'rooms': rooms})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request)
    return JsonResponse(data)


def create_post(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
    else:
        form = RoomForm()
    return save_book_form(request, form, 'sharespace/shareform.html')


def update_post(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
    else:
        form = RoomForm(instance=room)
    return save_book_form(request, form, 'sharespace/updateform.html')


def delete_post(request, pk):
    room = get_object_or_404(Room, pk)
    data = dict()
    if request.method == 'POST':
        room.delete()
        data['form_is_valid'] = True
        rooms = Room.objects.all()
        data['html_room_list'] = render_to_string('sharespace/includes/partial_room_list.html', {'rooms': rooms})
    else:
        context = {'room': room}
        data['html_form'] = render_to_string('sharespace/deleteform.html', context, request=request,)
    return JsonResponse(data)


class RoomDetail(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        data = dict()
        data['room'] = model_to_dict(room)
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class RoomCreate(CreateView):
    def post(self, request):
        data = dict()
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)

        else:
            data['error'] = "form not valid!"
        return JsonResponse(data)




