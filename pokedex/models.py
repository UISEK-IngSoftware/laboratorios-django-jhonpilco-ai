from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    
    picture = models.ImageField(upload_to="trainer_images")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pokemon(models.Model):

    POKEMON_TYPES = [
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Electrico'),
        ('L', 'Lagartija'),
        ('S', 'Psíquico')
    ]

    name = models.CharField(max_length=30, null=False)

    type = models.CharField(
        max_length=30,
        choices=POKEMON_TYPES,
        null=False
    )

    height = models.FloatField()
    weight = models.FloatField()
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to="pokemons_images")

    def __str__(self):
        return self.name
    
