from django.db import models

class Industry(models.Model):
    
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="industry_icon/")
    short_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 

class Projects(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField()
    client_name = models.CharField(max_length=255)
    client_statement = models.TextField()
    client_picture = models.ImageField(upload_to= "client_pic/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
   
class ProjectImage(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_pic/")  
    
    
class Services(models.Model):
    icon = models.ImageField(upload_to="service_icon/")
    name = models.CharField(max_length=255)
    describtion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServiceProduct(models.Model):
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

   
class Technologies(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="tech_icon/")
    picture = models.ImageField(upload_to="tech_pic/")
    short_describtion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TechnologiesProduct(models.Model):
    tech_id = models.ForeignKey(Technologies,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    
    
class Fields(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class FieldsProduct(models.Model):
    field_id = models.ForeignKey(Fields,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to="team_member/")
