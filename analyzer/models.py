from django.db import models


#new difs { label,lrg,dif_file,rti}

#gen_difs { label,lrg,dif_file,reason}

#RTI {label, rtino, owner, lrg, dif_file, symptom}

#exception_dif  { lrg, dif, symptom}
# Create your models here.





class Users(models.Model):

   username = models.CharField(max_length = 50)

   #new_difs = models.ForeignKey('New_difs',  on_delete=models.CASCADE )
   
 #  student = models.ForeignKey('Student', default = 1, null=True, on_delete=models.CASCADE )

   def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
      return "user name:"+str(self.username)

#       db_table = "trainer"

class New_difs(models.Model):
 	lrg_name = models.CharField(max_length = 20)
 	dif_name = models.CharField(max_length = 50)
 	rti_no = models.IntegerField()
 	#rti = models.ForeignKey(RTI, on_delete=models.CASCADE )
 	def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
 	    s="lrg name:"+self.lrg_name+" "+"dif name:"+self.dif_name+" "+"RTI no:"+self.rti_no
 	    return s



class RTI(models.Model):
   
   rti_no = models.IntegerField(null=True)
   rti_label = models.CharField(max_length = 50)
   
   rti_lrg = models.CharField(max_length = 50)
   rti_dif = models.CharField(max_length = 50)
   rti_symptom = models.CharField(max_length = 50)
   status = (
        ('A', 'Active'),
        ('I', 'IGNORE'),
        ('C', 'CRITICAL'),
    )
   rti_status = models.CharField(max_length = 50, choices=status,default = 'A')
   
   #New_difs=models.ForeignKey('New_difs',on_delete=models.CASCADE )
   
 #  student = models.ForeignKey('Student', default = 1, null=True, on_delete=models.CASCADE )

   def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
      return "RTI no:"+str(self.rti_no)+" LRG Name:"+self.rti_lrg+" DIF name:"+self.rti_dif+" SYMPTOM:"+self.rti_symptom
  # class Meta:
#       db_table = "trainer"

class Exception_difs(models.Model):
 	lrg_name = models.CharField(max_length = 20)
 	dif_name = models.CharField(max_length = 50)
 	symptom = models.CharField(max_length = 50)

 	def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
 	    s="lrg name:"+self.lrg_name+" "+"dif name:"+self.dif_name+" "+"symptom:"+self.symptom
 	    return s



class Gen_difs(models.Model):
 	lrg_name = models.CharField(max_length = 20)
 	dif_name = models.CharField(max_length = 50)
 	rti_no = models.IntegerField()
 	rti_owner= models.CharField(max_length = 20)
 	def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
 	    s="lrg name:"+self.lrg_name+" dif name:"+self.dif_name+" RTI no:"+self.rti_no+" RTI Owner:"+self.rti_owner
 	    return s


class signoff(models.Model):
   lrgs = (
        ('L', 'NETWORK_MAIN_LINUX.X64_210511'),
        ('W', 'NETWORK_MAIN_WINDOWS.X64_210509'),
        
   )
   
   label = models.CharField(max_length = 20,choices=lrgs,default = 'L')
   lrgs = (
        ('A', 'lrgngsm'),
        ('B', 'lrgnfptunnel'),
       
   )
   lrg = models.CharField(max_length = 50,choices=lrgs,default = 'A')
   difs = (
        ('A', 'a.dif'),
        ('B', 'b.dif'),
       
   )
   dif = models.CharField(max_length = 50,choices=difs,default = 'A')
   status = (
        ('A', 'Active'),
        ('I', 'IGNORE'),
        ('C', 'CRITICAL'),
   )
   status= models.CharField(max_length = 50,choices=status,default = 'A')

   def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
       s=" label:"+self.label+"lrg name:"+self.lrg+" dif name:"+self.dif+" Status:"+self.status
       return s


class LabelDrop(models.Model):
   rdbms_label = models.CharField(max_length = 20)
   dep_label = models.CharField(max_length = 50)
   farm_job = models.IntegerField()
   
   def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
       s="RDBMS Label:"+self.rdbms_label+" Dep Label:"+self.dep_label+" Farm Job:"+self.farm_job
       return s


class LabelStatus(models.Model):
   label = models.CharField(max_length = 20)
    
   def __str__(self): # What to be displayed when Dreamreal.objects.all() is called
       s="Label:"+self.label
       return s





