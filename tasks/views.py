import os
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Task
import markdown2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def file_view(request):
    title_name = request.GET.get('file')
    if title_name:
        try:
            with open(os.path.join(BASE_DIR, title_name), 'r') as file:
                content = file.read()
                return HttpResponse(content, content_type="text/plain")
        except Exception as e:
            return HttpResponse(f"Error reading file: {e}", content_type="text/plain")
    else:
        return HttpResponse("No file specified.", content_type="text/plain")

def task_list(request):
    tasks = Task.objects.all()
    file_content = None
    error = None
    title_name = request.GET.get('title_name')
    
    if title_name:
        try:
            task = Task.objects.filter(title__iexact=title_name.strip()).first()
            if task:
                file_content = f"Project name: {task.title}, PM: {task.manager}, Description: {task.description}"
                file_content = task.description
            else:
                base_dir = 'tasks/' 
                full_path = os.path.join(base_dir, title_name)
                
                if os.path.exists(full_path):
                    with open(full_path, 'r') as file:
                        file_content = file.read()
                else:
                    file_content = "No matching Project found for the given name."
        except Exception as e:
            error = f"Error reading file: {str(e)}"

    context = {
        'tasks': tasks,
        'file_content': file_content,
        'error': error,
    }

    return render(request, 'tasks/task_list.html', context)