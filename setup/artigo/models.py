from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    texto = models.TextField(blank=True)
    avatar = models.CharField(max_length=255)

    def __str__(self):
        return  self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    texto = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    texto = models.TextField(blank=True)
    img_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(default=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"