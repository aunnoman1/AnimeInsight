from django.db import models

class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    english_name = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    genres = models.CharField(max_length=255)
    synopsis = models.TextField()
    type = models.CharField(max_length=50)
    episodes = models.IntegerField()
    aired = models.CharField(max_length=50)
    premiered = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    producers = models.CharField(max_length=255)
    licensors = models.CharField(max_length=255)
    studios = models.CharField(max_length=255)
    source = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    rank = models.IntegerField()
    popularity = models.IntegerField()
    favorites = models.IntegerField()
    scored_by = models.IntegerField()
    members = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name


class User(models.Model):
    userID = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.user_name
    

    
class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username} - {self.anime.name}"
    
        
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username} - {self.anime.name}"
