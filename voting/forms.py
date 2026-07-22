from django import forms
from .models import *
from account.forms import FormSettings


class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = []  # No voter-specific fields needed (OTP/phone removed)


class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ['name', 'max_vote']


class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ['fullname', 'bio', 'position', 'photo']
