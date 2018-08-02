import json
from datetime import datetime

from django.db import models


class MemberInfo(object):
    def __init__(self, name, email, cpf=None):
        self.name = name
        self.email = email
        self.cpf = cpf

    def to_json(self):
        func = lambda o: {k: v for k, v in o.__dict__.items()
                          if v is not None}

        return json.dumps(self, default=func,
                          sort_keys=True)


class Event(models.Model):
    name = models.CharField(max_length=25)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.name


class EventCheck(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    member_name = models.CharField(max_length=300)
    member_email = models.EmailField(max_length=300)
    entrance_date = models.DateTimeField(auto_now_add=True)
    exit_date = models.DateTimeField(null=True)

    def checkout(self, date=datetime.now()):
        self.exit_date = date
        self.save()
