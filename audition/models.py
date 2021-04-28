from django.db import models

# Create your models here.



ASTAT = (
    ('Pending', 'Pending'),
    ('Selected', 'Selected'),
    ('Rejected', 'Rejected')
)

QTYPE = (
    ('LONG', 'LONG'),
    ('SMALL', 'SMALL'),
    ('MCQ','MCQ')
)

class Candidates(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=15, choices=ASTAT, default='Selected')

    class Meta:
        ordering = ['-status', 'name']

    def __str__(self):
        return "{} : status {}".format(self.name, self.status)

class auditionRounds(models.Model):
    roundno = models.IntegerField(default=1)
    round_status = models.BooleanField(default=False)
    #candidate = models.ForeignKey(Candidates, on_delete=models.CASCADE, related_name='candidates', blank=True, null=True)
    candidate = models.ManyToManyField(Candidates, related_name='candidates', blank=True, null=True)

    def __str__(self):
        return "Round: {}".format(self.roundno)

class auditionQuestions(models.Model):
    roundno = models.IntegerField(default=1)
    serialno = models.IntegerField(default=1)
    question = models.CharField(max_length=5000)
    round = models.ForeignKey(auditionRounds, on_delete=models.CASCADE, related_name='round')
    qtype = models.CharField(max_length=15, choices=QTYPE, default='LONG', null=True, blank=True)
    op1 = models.CharField(max_length=5000, null=True, blank=True)
    op2 = models.CharField(max_length=5000, null=True, blank=True)
    op3 = models.CharField(max_length=5000, null=True, blank=True)
    op4 = models.CharField(max_length=5000, null=True, blank=True)

    class Meta:
        unique_together = ('roundno', 'serialno',)
        ordering = ['roundno', 'serialno']

    def __str__(self):
        return "Round {}, qno {} : {}".format(self.roundno, self.serialno, self.question)

class auditionAnswers(models.Model):
    roundno = models.IntegerField(default=1)
    q = models.ForeignKey(auditionQuestions, on_delete=models.CASCADE, related_name='problem')
    ans = models.CharField(max_length=800)
    ansby = models.ForeignKey(Candidates, on_delete=models.CASCADE, related_name='candidate')
    anstime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Round {} q: {}, answered by {}".format(self.q.roundno , self.q.serialno, self.ansby.name)