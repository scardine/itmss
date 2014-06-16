# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
from stdimage import StdImageField


class Secao(models.Model):
    ALIGN = (
        ('right', 'Direita'),
        ('left', 'Esquerda'),
    )
    titulo = models.CharField(u'Título', max_length=250)
    conteudo = HTMLField(u'Conteúdo')
    ordem = models.IntegerField(default=1)
    imagem = StdImageField(upload_to='imagens', blank=True, null=True, variations={
        'icone': (128, 128, True),
    })
    cor = models.CharField(max_length=30, default='#0ea4b8')
    alinhamento = models.CharField(max_length=20, choices=ALIGN)

    class Meta:
        verbose_name = 'Seção'
        verbose_name_plural = 'Seções'

    def __unicode__(self):
        return self.titulo


class Servico(models.Model):

    titulo = models.CharField(u'Título', max_length=250)
    conteudo = HTMLField(u'Conteúdo')
    ordem = models.IntegerField(default=1)
    imagem = StdImageField(upload_to='imagens', blank=True, null=True, variations={
        'icone': (128, 128, True),
    })
    cor = models.CharField(max_length=30, default='#0ea4b8')

    class Meta:
        verbose_name = 'Serviço'

    def __unicode__(self):
        return self.titulo

class Contato(models.Model):

    titulo = models.CharField(u'Título', max_length=250)
    mapa = models.CharField(max_length=500)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    ordem = models.IntegerField(default=1)