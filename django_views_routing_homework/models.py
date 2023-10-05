from django.db import models
from django import forms
from django_views_routing_homework.validators import validate_min_length_full_name


class User(models.Model):
    class Meta:
        db_table = 'users_info'
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    full_name = models.CharField(max_length=256, validators=[validate_min_length_full_name])
    email = models.EmailField()
    registered_from = models.CharField(
        max_length=2,
        choices=[('wb', 'website'),('ma', 'mobile_app')],
        default='wb'
    )
    age = models.PositiveSmallIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'registered_from', 'age')