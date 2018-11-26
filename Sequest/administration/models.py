from django.db import models
from django.contrib.auth.models import User

from marketplace.models import Request


# The administration classes ###########################################################################################
class ReportedRequest(models.Model):
    reason = models.TextField(max_length=500)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='reportedrequests')
    is_solved = models.BooleanField(default=False)
    is_solved_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
