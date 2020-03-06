from django.db import models

class GCN_notice(models.Model):
    NOTICE_ID = models.IntegerField(primary_key=True)
    NOTICE_TYPE = models.IntegerField()
    NOTICE_TEL_ID = models.IntegerField()
    TRIGGER_NUM = models.IntegerField()
    
    GRB_DATE = models.DateField()
    GRB_TIME = models.TimeField()
    GRB_RA = models.FloatField()
    GRB_RA_hms = models.CharField(max_length=45)
    GRB_DEC = models.FloatField()
    GRB_RA_dms = models.CharField(max_length=45)
    GRB_ERROR = models.FloatField()

    TRIGGER_SIGNIF = models.FloatField()
    TRIGGER_DUR = models.FloatField()

    def __str__(self):
        return str(self.NOTICE_ID)

