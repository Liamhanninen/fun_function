from django.db import models

TIME_TYPES = (
    ('Hours', 'Hours'),
    ('Minutes', 'Minutes'),
)

class BasicModelFields(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True, blank=True)  

    class Meta:
        abstract = True

class TriangleArea(BasicModelFields):
    base = models.DecimalField(max_digits=10, decimal_places=2,blank=False,verbose_name = 'Base')
    height = models.DecimalField(max_digits=10, decimal_places=2,blank=False,verbose_name = 'Height')
    area = models.DecimalField(max_digits=20, decimal_places=2, editable=False,verbose_name = 'Area')

    def save(self, *args, **kwargs):
        self.area = (self.base * self.height) / 2
        super(TriangleArea, self).save(*args, **kwargs)

class MaximumEdge(BasicModelFields):
    first_side = models.IntegerField(verbose_name = 'First Side',blank=False)
    second_side = models.IntegerField(verbose_name = 'Second Side',blank=False)
    calculated_side = models.IntegerField(verbose_name = 'Maximum Edge',editable=False)

    def save(self, *args, **kwargs):
        self.calculated_side = self.first_side + self.second_side - 1
        super(MaximumEdge, self).save(*args, **kwargs)

class SecondsConversion(BasicModelFields):
    time_type = models.CharField(max_length=200, blank=False, choices = TIME_TYPES,verbose_name = 'Unit of Time')
    amount = models.IntegerField(blank=False,verbose_name = 'Amount')
    seconds = models.IntegerField(editable=False,verbose_name = 'Seconds')

    def save(self, *args, **kwargs):
        if self.time_type == 'Hours':
            multiply_by = 60 * 60
        else:
            multiply_by = 60
        self.seconds = multiply_by * self.amount
        super(SecondsConversion, self).save(*args, **kwargs)    

class RepeatingFunction(BasicModelFields):
    string_to_repeat = models.CharField(max_length=200, blank=False,verbose_name = 'String to Repeat')
    repeat_n_times = models.IntegerField(blank=False,verbose_name = 'Repeat n Times')
    repeated_string = models.CharField(max_length=2000, blank=False,verbose_name = 'Repeated String')

    def save(self, *args, **kwargs):
        self.repeated_string = ''
        for iter_string in range(self.repeat_n_times):
            self.repeated_string = self.repeated_string + self.string_to_repeat
        super(RepeatingFunction, self).save(*args, **kwargs)


