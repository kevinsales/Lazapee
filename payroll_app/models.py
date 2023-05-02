from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=300)
    id_number = models.CharField(max_length=300)
    rate = models.FloatField(max_length=300)
    overtime_pay = models.FloatField(max_length=300, null=True, blank=True, default=0)
    allowance = models.FloatField(max_length=300, null=True, blank=True, default=0)

    def getName(self):
        return self.name
    
    def getID(self):
        return self.id_number

    def getRate(self):
        return self.rate

    def getOvertime(self):
        return self.overtime_pay
    
    def resetOvertime(self):
        Employee.objects.update(overtime_pay=0)
        
        

    def getAllowance(self):
        return self.allowance
    
    def __str__(self):
        return f"{self.id_number}, rate: {self.rate}"
    
class Payslip(models.Model):
    id_number = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=300)
    date_range = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    pay_cycle = models.IntegerField()
    rate = models.FloatField(max_length=300)
    earnings_allowance = models.FloatField(max_length=300)
    deductions_tax = models.FloatField(max_length=300)
    deductions_health = models.FloatField(max_length=300)
    pag_ibig = models.FloatField(max_length=300)
    sss = models.FloatField(max_length=300)
    overtime = models.FloatField(max_length=300)
    total_pay = models.FloatField(max_length=300)

    def getIDNumber(self):
        return self.id_number
    
    def getMonth(self):
        return self.month
    
    def getDate_range(self):
        return self.date_range
    
    def getYear(self):
        return self.year
    
    def getPay_cycle(self):
        return self.pay_cycle
    
    def getRate(self):
        return self.rate
    
    def getCycleRate(self):
        cycleRate = self.rate/2
        return cycleRate
    
    def getEarnings_allowance(self):
        return self.earnings_allowance
    
    def getDeductions_tax(self):
        return self.deductions_tax

    def getDeductions_health(self):
        return self.deductions_health
    
    def getPag_ibig(self):
        return self.pag_ibig
    
    def getSSS(self):
        return self.sss
    
    def getOvertime(self):
        return self.overtime

    def getTotal_pay(self):
        return self.total_pay
    
    def __str__(self):
        return f"pk: {self.pk}, Employee: {self.id_number}, Period: {self.date_range}, {self.year}, Cycle: {self.pay_cycle}, Total Pay: {self.total_pay}"