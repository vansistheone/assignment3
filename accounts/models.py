from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):

    ROLE_CHOICES = (
        ('admin','Admin'),
        ('staff','Staff'),
        ('volunteer','Volunteer'),
    )

    STATUS_CHOICES = (
        ('active','Active'),
        ('inactive','Inactive'),
    )

    user_id = models.AutoField(primary_key=True)

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password_hash = models.CharField(max_length=255)

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.password_hash.startswith('pbkdf2'):
            self.password_hash = make_password(self.password_hash)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email



# 1. Our Story
class OurStory(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Our Story"


# 2. Core Values
class CoreValue(models.Model):
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value


# 3. Programs
class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 4. Team Members
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 5. Mission & Vision
class MissionVision(models.Model):
    mission = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return "Mission & Vision"


# 6. Impact
class Impact(models.Model):
    title = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return self.title