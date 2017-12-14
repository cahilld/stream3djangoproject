from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import TodoItem
from .forms import TodoItemForm
import json

# Create your views here.
def get_index(request):
    if request.user.is_authenticated:
        results = TodoItem.objects.filter(owner=request.user)
        return render(request, "index.html", {'items': results})
    else:
        return render(request, "index.html")

def add_item(request):
    if request.method == "POST":
        # Get the details from the request
        form = TodoItemForm(request.POST)
        # Handle Saving to DB
        if form.is_valid():
            item=form.save(commit=False)
            item.owner=request.user
            item.save()
            return redirect(get_index)
    else:
        # GET Request so just give them a blank form
        form = TodoItemForm()    
    
    return render(request, "item_form.html", { 'form': form })
    
def edit_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    
    if request.method =="POST":
        form=TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_index)
    else:
        form = TodoItemForm(instance=item)
    
    return render(request, "item_form.html", {"form":form})
    
def toggle_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.status = not item.status
    item.save()
    return redirect(get_index)

def delete_item(request, id):
    item=get_object_or_404(TodoItem, pk=id)
    item.delete()
    return redirect('home')
    
def move_item(request):
    # if request.POST and request.is_ajax:
    id = int(request.POST.get('id'))
    status = request.POST.get('status')
    item = get_object_or_404(TodoItem, pk=id)
    item.status = status
    item.save()
    
    resp = {
        'id': id,
        'status': status
    }
    
    return HttpResponse(json.dumps(resp))