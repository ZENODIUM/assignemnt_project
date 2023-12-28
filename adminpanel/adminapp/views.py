from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from google.cloud import firestore  # Import Firestore

# Initialize Firestore client
db = firestore.Client()

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            auth.login(request, user)
            # Create or get the user profile
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

@login_required(login_url='login')  # Decorator to ensure the user is logged in
def dashboard(request):
    user_profile = request.user.userprofile  # Assuming you have a UserProfile related to the User model

    if request.method == 'POST':
        country = request.POST['country']
        language = request.POST['language']

        # Update user profile in Firestore
        update_user_profile_firestore(user_profile.user.username, country, language)

        # Update user profile in Django
        user_profile.country = country
        user_profile.language = language
        user_profile.save()

    return render(request, 'dashboard.html', {'user_profile': user_profile})

def update_user_profile_firestore(username, country, language):
    # Reference to Firestore collection
    collection_ref = db.collection('sigaram_test_collection')

    # Create or update document
    doc_ref = collection_ref.document(username)
    doc_ref.set({
        'country': country,
        'language': language,
        'timestamp': firestore.SERVER_TIMESTAMP
    }, merge=True)
