from django.db import models


class User(models.Model):

    class Meta:
        db_table = 'users_info'
        get_latest_by = 'created_at'
        ordering = ['-created_at']
        constraints = [models.CheckConstraint(check=models.Q(full_name__gte=5), name='full_name_gte_5')]

    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    registered_from = models.CharField(max_length=120, choices=[('wb', 'website'),('m_ap', 'mobile_app')], default='wb')
    age = models.PositiveSmallIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)