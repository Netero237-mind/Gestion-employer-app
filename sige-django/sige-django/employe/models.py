from django.db import models


class Employe(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(unique=True, verbose_name="Email")
    poste = models.CharField(max_length=100, verbose_name="Poste")
    salaire = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Salaire (FCFA)"
    )

    class Meta:
        verbose_name = "Employé"
        verbose_name_plural = "Employés"
        ordering = ['nom']

    def __str__(self):
        return f"{self.nom} — {self.poste}"
