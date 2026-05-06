from django.shortcuts import render
from django.contrib import messages
from .models import ContactMessage
from activities.models import Activity
from members.models import Member, Membership
from partners.models import Partner

def home(request):
    activities = Activity.objects.all()
    members = Member.objects.all()
    partners = Partner.objects.all()

    return render(request, 'core/home.html', {
        'activities': activities,
        'members': members,
        'partners': partners
    })

def members_page(request):
    from members.models import Member
    members = Member.objects.all()

    return render(request, 'core/members.html', {
        'members': members
    })

from django.shortcuts import render, get_object_or_404
from activities.models import Activity   # adapte si ton app s'appelle autrement

def activity_detail(request, id):
    activity = get_object_or_404(Activity, id=id)

    return render(request, 'activity_detail.html', {
        'activity': activity
    })

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )

        messages.success(request, "Message envoyé avec succès !")

    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')


def partners_page(request):
    partners = Partner.objects.all()

    return render(request, 'core/partners.html', {
        'partners': partners
    })



def join(request):
    success = False

    if request.method == 'POST':
        Membership.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            motivation=request.POST.get('motivation'),
        )

        success = True

    return render(request, 'core/join.html', {
        'success': success
    })