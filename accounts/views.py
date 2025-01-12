from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser, Message
from .forms import CustomUserCreationForm, ProfileForm

# Home
def home(request):
    return render(request, 'home.html')

# Admin dashboard
@login_required 
def admin_dashboard(request):
    if request.user.profile.user_type == 1:  # Only admins
        users = CustomUser.objects.all()
        return render(request, 'registration/admin_dashboard.html', {'users': users})
    return redirect('course_list')

# Register
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#profile
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige l'utilisateur vers la page de profil après la mise à jour
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'registration/update_profile.html', {'form': form})

# message
@login_required
def chat_page(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        receiver_id = request.POST.get('receiver')
        try:
            receiver = CustomUser.objects.get(id=receiver_id)
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
        except CustomUser.DoesNotExist:
            # Handle the case where the receiver does not exist
            messages.error(request, 'The selected user does not exist.')
        return redirect('chat_page')

    messages = Message.objects.filter(receiver=request.user) | Message.objects.filter(sender=request.user)
    messages = messages.order_by('timestamp')
    users = CustomUser.objects.all()

    return render(request, 'registration/chat_page.html', {'mes': messages, 'users': users})