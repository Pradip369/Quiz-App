from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

class Register(models.Model):
    name = models.CharField(max_length=30,unique=True)
    mobile_no = models.IntegerField(validators= [RegexValidator("^0?[5-9]{1}\d{9}$")],)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=40)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name_plural = "Registered Users"
        
    def __str__(self):
        return str(self.name)
    
class Question(models.Model):
    
    OPTION_CHOICES = [
        ('option1', 'option1'),
        ('option2', 'option2'),
        ('option3', 'option3'),
        ('option4', 'option4'),
    ]
    
    question = models.TextField(unique=True)
    option1 = models.CharField(max_length=200,help_text='Required')
    option2 = models.CharField(max_length=201,help_text='Required')
    option3 = models.CharField(max_length=202,null=True,blank=True,help_text='(Optional)')
    option4 = models.CharField(max_length=204,null=True,blank=True,help_text='(Optional)')
    answer = models.CharField(choices=OPTION_CHOICES,max_length=205,help_text='This answer must be match for given above option..')
    answer_hidden = models.CharField(max_length=206,null=True,blank=True,verbose_name='True Answer',help_text="Your selected option's answer",default='No select any ans. yet!!')
    point = models.IntegerField(default = 1,help_text='Student How many points will get for this given question?')
    solution = models.TextField(blank=True,null=True,help_text='(Optional) If possible! give the specific solution for this question..')
    cr_date = models.DateTimeField(auto_now=True,verbose_name='Created Date')
    
    class Meta:
        verbose_name_plural = "Questions"
        
    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)
        if self.answer == 'option1':
            self.answer_hidden = self.option1
            super(Question, self).save(*args, **kwargs)
        elif self.answer == 'option2':
            self.answer_hidden = self.option2
            super(Question, self).save(*args, **kwargs)
        elif self.answer == 'option3':
            self.answer_hidden = self.option3
            super(Question, self).save(*args, **kwargs)
        elif self.answer == 'option4':
            self.answer_hidden = self.option4
            super(Question, self).save(*args, **kwargs)
                        
    def __str__(self):
        return str(self.question)
    
class SubmitAnswer(models.Model):
    name = models.CharField(max_length=100,null=True)
    score = models.IntegerField(default=0)       
    cr_date = models.DateTimeField(auto_now = True,verbose_name='Submited Date')
    
    def __str__(self):
        return  '%s(%s)' %(self.name,self.score)
    
    class Meta:
        verbose_name_plural = "Submited Answer"