from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import User

from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home(request):
    print("HOME VIEW RUNNING")

    story = OurStory.objects.first()
    values = CoreValue.objects.all()
    programs = Program.objects.all()
    team = TeamMember.objects.all()
    mission_vision = MissionVision.objects.first()
    impacts = Impact.objects.all()

    print("VALUES:", values)

    return render(request, 'index.html', {
        'story': story,
        'values': values,
        'programs': programs,
        'team': team,
        'mission_vision': mission_vision,
        'impacts': impacts,
    })

def register(request):

    if request.method == "POST":

        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        User.objects.create(
            full_name = full_name,
            email = email,
            password_hash = password,
            role = role
        )

        return redirect('login')

    return render(request,'register.html')


def login_view(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password_hash):

            request.session['user_id'] = user.user_id
            request.session['role'] = user.role

            return redirect('dashboard')

        else:
            return render(request,'login.html',{'error':'Invalid credentials'})

    return render(request,'login.html')


def dashboard(request):

    if 'user_id' not in request.session:
        return redirect('login')

    return render(request,'dashboard.html')


def logout_view(request):

    request.session.flush()

    return redirect('login')


# Dashboard
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


# ---------------- CORE VALUES ----------------
def core_values_admin(request):
    if request.method == "POST":
        value = request.POST.get('value')
        CoreValue.objects.create(value=value)

    values = CoreValue.objects.all()
    return render(request, 'admin/core_values.html', {'values': values})

def delete_core_value(request, id):
    CoreValue.objects.get(id=id).delete()
    return redirect('core_values_admin')


# ---------------- PROGRAMS ----------------
def programs_admin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('description')
        Program.objects.create(name=name, description=desc)

    programs = Program.objects.all()
    return render(request, 'admin/programs.html', {'programs': programs})

def delete_program(request, id):
    Program.objects.get(id=id).delete()
    return redirect('programs_admin')


# ---------------- TEAM ----------------
def team_admin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        role = request.POST.get('role')
        TeamMember.objects.create(name=name, role=role)

    team = TeamMember.objects.all()
    return render(request, 'admin/team.html', {'team': team})

def delete_team(request, id):
    TeamMember.objects.get(id=id).delete()
    return redirect('team_admin')


# ---------------- IMPACT ----------------
def impact_admin(request):
    if request.method == "POST":
        title = request.POST.get('title')
        value = request.POST.get('value')
        Impact.objects.create(title=title, value=value)

    impacts = Impact.objects.all()
    return render(request, 'admin/impact.html', {'impacts': impacts})

def delete_impact(request, id):
    Impact.objects.get(id=id).delete()
    return redirect('impact_admin')


# ---------------- MISSION ----------------
def mission_admin(request):
    mv = MissionVision.objects.first()

    if request.method == "POST":
        mission = request.POST.get('mission')
        vision = request.POST.get('vision')

        if mv:
            mv.mission = mission
            mv.vision = vision
            mv.save()
        else:
            MissionVision.objects.create(mission=mission, vision=vision)

        return redirect('mission_admin')

    return render(request, 'admin/mission.html', {'mv': mv})


# ---------------- STORY ----------------
def story_admin(request):
    story = OurStory.objects.first()

    if request.method == "POST":
        content = request.POST.get('content')

        if story:
            story.content = content
            story.save()
        else:
            OurStory.objects.create(content=content)

        return redirect('story_admin')

    return render(request, 'admin/story.html', {'story': story})