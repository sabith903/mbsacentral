from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from .models import Category, Image, Program, Stage, Student, Team


def search(request):
    query = request.GET.get('q')
    students = Student.objects.filter(Q(name__icontains=query)) if query else []
    teams = Team.objects.filter(Q(name__icontains=query)) if query else []
    programs = Program.objects.filter(Q(name__icontains=query)) if query else []

    context = {
        'query': query,
        'students': students,
        'teams': teams,
        'programs': programs,
    }
    return render(request, 'core/search.html', context)

def home(request):
    students = Student.objects.all()
    return render(request, 'core/home.html', {'students': students})

def students_list(request):
    students = Student.objects.all()
    return render(request, 'core/students_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'core/student_detail.html', {'student': student})

def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'core/teams_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'core/team_detail.html', {'team': team})

def programs_list(request):
    programs = Program.objects.all()
    return render(request, 'core/programs_list.html', {'programs': programs})

def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    stages = Stage.objects.filter(program=program)
    students = Student.objects.filter(program=program)

    return render(request, 'core/program_detail.html', {
        'programs': program,
        'stages': stages,
        'students': students,
    })


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'core/category.html',{'categories':categories})

def stage_list(request):
    stages = Stage.objects.all()
    return render(request, 'core/stages_list.html', {'stages': stages})

def stage_detail(request, stage_id):
    stage = get_object_or_404(Stage, id=stage_id)
    return render(request, 'core/stage_detail.html', {'stage': stage})


def display_images(request):
    images =Image.objects.all()
    return render(request, 'core/display_images.html', {'images': images})

