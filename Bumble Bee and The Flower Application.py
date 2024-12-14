import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 600

Score = 0
Gameover = 0 
bumble_bee = Actor("bumble bee")
bumble_bee.pos = 100,100
flower = Actor("flower")
flower.pos = 200,0