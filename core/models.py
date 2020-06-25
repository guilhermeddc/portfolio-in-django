from django.db import models
from random import randint
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = randint(1, 9999)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'projects/{new_filename}/{final_filename}'


class Locality(models.Model):
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('UF', max_length=2)

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'

    def __str__(self):
        return f'{self.city} - {self.state}'


class Profile(models.Model):
    name = models.CharField('Nome Completo', max_length=30)
    email = models.EmailField('E-mail', max_length=100)
    phone = models.CharField('Telefone', max_length=15)
    image = models.ImageField('Foto de perfil', upload_to=upload_image_path)
    title = models.CharField('Título do perfil', max_length=50)
    sub_title = models.CharField('Subtítulo do perfil', max_length=150)
    description = models.TextField('Descrição do projeto', max_length=1000)
    locality = models.ForeignKey('Locality', verbose_name='Localização', on_delete=models.CASCADE)
    country = models.CharField('País', max_length=20)
    site_url = models.CharField('URL do site', max_length=100)
    facebook_url = models.CharField('URL do facebook', max_length=100)
    linkedin_url = models.CharField('URL do linkedin', max_length=100)
    instagram_url = models.CharField('URL do instagram', max_length=100)
    github_url = models.CharField('URL do github', max_length=100)
    gitlab_url = models.CharField('URL do gitlab', max_length=100)


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfil'

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField('Título do projeto', max_length=50)
    image = models.ImageField('Foto do projeto', upload_to=upload_image_path)
    description = models.TextField('Descrição do projeto', max_length=1000)
    link = models.CharField('Link para o projeto', max_length=250, null=True, blank=True)

    created = models.DateTimeField('Criado em ', auto_now_add=True)
    modified = models.DateTimeField('Modificado em ', auto_now=True)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-created']

    def __str__(self):
        return self.title

