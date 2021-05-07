'''
Faça um programa em Python que abra e reproduza
o áudio de um arquivo MP3.
'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

'''Esse é o código que deveria funcionar se o pygame pudesse ser importado nesta versão do Python.'''
''' Código do Guanabara:
import pygame
pygame.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
pygame.event.wait()

Bom dia!

DEpois de muita pesquisa eu achei duas maneiras de ser feita. isso é um dos Bugs do pygame

uma dica tenta colocar nome das músicas sem espaço, sem caracteres e tudo minúscula.

O meu arquivo  mp3 também aparecia interrogação, mas assim que eu executei esse código, 

o arquivo mp3 foi reconhecido.

 

from pygame import mixer

mixer.init() mixer.music.load('suamusica.mp3')

mixer.music.play()

import time

time.sleep(360)

__________________

from pygame import mixer

mixer.init() mixer.music.load('suamusica.mp3')

mixer.music.play()

parar = input('Digite algo para parar...')
 

espero ter ajudado... valeu bom domingo a todos 
'''