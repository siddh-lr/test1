from django.db import models
from decimal import Decimal
from django.db.models import Func , Sum

# Create your models here.
class daily_sale(models.Model):
    cash = models.DecimalField(max_digits=8 , null=True,blank=True,decimal_places=3)
    online = models.DecimalField(max_digits=8 , null=True,blank=True,decimal_places=3)
    total_amount = models.DecimalField(max_digits=8 , null=True,blank=True,decimal_places=3)
    date = models.DateField(max_length=30,blank=True,null=True)    
    
    def __str__(self):
        return str(self.date)
    
    def save(self, *args, **kwargs):
        super(daily_sale, self).save(*args, **kwargs)
        
        self.total_amount = Decimal(self.cash + self.online)
        
        super(daily_sale, self).save(*args, **kwargs)
        
        
# class Month(Func):
#     function = 'EXTRACT'
#     template = '%(function)s(MONTH from %(expressions)s)'
#     output_field = models.IntegerField()
    
# summary = (daily_sale.objects
#             .annotate(m=Month('date'))
#             .values('m')
#             .annotate(total=Sum('total_amount'))
#             .order_by('month'))