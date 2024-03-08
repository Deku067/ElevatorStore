from django.db import models

# Create your models here.
    
class User(models.Model):
    username = models.CharField(max_length=50, unique=True, primary_key = True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, unique=True)
    email_address = models.EmailField(unique=True)
    # add()
    # delete()
    # update()
    # request_per_visit()
    # request_canselling()
    # online_canselling()
    # show_call_data()
    # Show_education()
    # show_collectedpackage()
    # co_work()
    # add_login()
    # read_login_users()
    # login()

class Manager(models.Model):
    M_username = models.CharField(max_length=50, unique=True, primary_key = True)
    M_password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, unique=True)
    email_address = models.EmailField(unique=True)
    # add()
    # delete()
    # catch_data()
    # create_new_off()
    # create_collectedPackage()
    # create_education()

class Comment(models.Model):
    username = models.CharField(max_length=50, unique=True, primary_key = True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    # read_comment()
    # insert_new_comment()
    # delete_comment()
    # publish()
    
    