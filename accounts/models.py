from django.db import models
from django.utils.translation import ugettext_lazy as _

#الربط بين البروفايل واليوزر
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.
type_of_person=(
    ('m','male'),
    ('f','female')
)

class profile(models.Model):
    spicialist={
        ("عظام","عظام"),
        ("قلب","قلب"),
        ("جلديه","جلديه"),
        ("اسنان","اسنان"),
        ("اوعيه","اوعيه" ), 
        ("كبد","كبد" ),
        ("باطنه","باطنه"),
        
    }
    
    #علاقة اليوزر بالبروفيل بمعنى كل يوزر له بروفايل واحد فقط
    #verbose_name فى صفحة الادمن كل فيلد بيبقى جنبه اسمه فبيهر عن طريقهوكمان للترجمه
    #on_deletمهمتها لو مسحت اليوزر يمسحى البروفايل تلقائى
    user= models.OneToOneField(User , verbose_name=_("user"),on_delete=models.CASCADE )
    name=models.CharField(_("الاسم :"), max_length=50, blank=True, null=True)
    dep=models.CharField(_("القسم"), max_length=100, blank=True, null=True)
    spicialist_doctor=models.CharField(_("متخصص فى"), max_length=100, blank=True, null=True)
    address=models.CharField(_("العنوان"), max_length=50, blank=True, null=True)
    address_details=models.CharField(_("الشارع"), max_length=50, blank=True, null=True)
    whating_time=models.IntegerField(_("وقت الانتظار"), blank=True, null=True)
    whating_hours=models.IntegerField(_("وقت العمل"), blank=True, null=True)
    number_phone=models.IntegerField(_("رقم الهاتف"), blank=True, null=True)
    who_i=models.TextField(_("من انا :"), max_length=100, blank=True, null=True)
    pric=models.IntegerField(_("سعرالكشف :"), blank=True, null=True)
    image=models.ImageField(_("الصوره"), upload_to='profile',blank=True, null=True)
    
    facebook=models.CharField(_("فيس بوك"), max_length=100,blank=True, null=True)
    google=models.CharField(_("جوجل"), max_length=100,blank=True, null=True)
    twitter=models.CharField(_("تويتر"), max_length=100,blank=True, null=True)
    slug=models.SlugField(_("slug"),blank=True, null=True)
    spicial=models.CharField(_("التخصص"),choices=spicialist, max_length=50)
    type_of_person=models.CharField(_("النوع"),choices=type_of_person, max_length=50)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
         
        super(profile, self).save(*args, **kwargs) # Call the real save() method
        
    
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        
    
        
    def __str__(self):
        return '%s' %(self.user.username)
    
    def creat_profile(sender,**kwargs):
        if kwargs['created']:
            profile.objects.create(user=kwargs['instance'])
            
    post_save.connect(creat_profile,sender=User)