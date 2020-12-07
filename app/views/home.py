import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from faker import Faker

from app.models.Message import Message
from app.models.Discussion import Discussion


def home(request):
    return render(request, 'index.html')


def seed(request):
    Message.objects.all().delete()
    Discussion.objects.all().delete()
    User.objects.all().exclude(username="a").delete()
    fake = Faker()
    for i in range(5):
        User.objects.create(
            username=fake.profile()['username'],
            password=make_password('a'),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            is_superuser=True
        )
    users = User.objects.all()
    for i in range(10):
        owner = random.choice(users),
        partner = random.choice(users.exclude(pk=owner[0].pk))
        d = Discussion.objects.create(
            title=fake.sentence(),
            description=fake.paragraph(),
        )
        d.users.add(owner[0])
        d.users.add(partner)

    discussions = Discussion.objects.all()

    for i in range(100):
        discuss = random.choice(discussions)
        sender = random.choice(discuss.users.all())
        receiver = random.choice(discuss.users.all().exclude(pk=sender.pk))
        Message.objects.create(
            content=fake.sentence(),
            message_sender=sender,
            message_receiver=receiver,
            discussion=discuss
        )
    return redirect('/chat')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
