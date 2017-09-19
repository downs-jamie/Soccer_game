import pygame
#from Soccer_player import Soccer_player
import random
from pygame.sprite import Sprite
from math import fabs, hypot
from random import randint
from Player import Player
from Ball import Ball
from Player2 import Player2 
from Player3 import Player3
from Player4 import Player4
import time

pygame.init()
pygame.mixer.init()

screen_size = (1295, 830)
screen = pygame.display.set_mode(screen_size)

background_image = pygame.image.load("field.png")
# player_image = pygame.image.load("soccer_player.png")
# player2_image = pygame.image.load("soccer_player2.png")
pygame.display.set_caption("Soccer Game!")
music = pygame.mixer.music.load("01 New Coat Of Paint.mp3")
# ball_image = pygame.image.load("soccer_ball.png")
pygame.mixer.music.play(-1, 0.0)


counter, text = 1, '1'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

player = Player(screen)
# player = {
#     "x": 200,
#     "y": 100,
#     "speed": 3
# }

player2 = Player2(screen)
# player2 = {
#     "x": 800,
#     "y": 100,
#     "speed": 1
# }

player3 = Player3(screen)

player4 = Player4(screen)

ball = Ball(screen)
# ball = {
#     "x": 490,
#     "y": 180,
#     'speed': 1
# }

keys = {
    "up": 273,
    "down": 274,
    "right": 275,
    "left": 276
}

keys_down = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}
# score = 0
# black = (0,0,0)
# def showScore(choice=1):
#     sFont = pygame.font.SysFont("monaco", 24)
#     Ssurf = sFont.render("Score: {0}" .format(score), True, black)
#     Srect = Ssurf.get_rect()
#     if choice == 1:
#         Srect.midtop = (80, 10)
#     else: 
#         Srect.midtop = (360, 120)
#     screen.blit(Ssurf, Srect)
#     pygame.display.flip()
clock = pygame.time.Clock()

game_on = True
while game_on:



#loop through all pygame events
#this is how to exit game
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            # the user clicked the red x in the top left
            game_on = False
        elif event.type == pygame.KEYDOWN:
            # print "User pressed a key!"
            if event.key == keys['up']:
                # user pressed up!!
                # hero['y'] -= hero['speed']
                keys_down['up'] = True
            elif event.key == keys['down']:
                # hero['y'] += hero['speed']
                keys_down['down'] = True
            elif event.key == keys['left']:
                # hero['x'] -= hero['speed']
                keys_down['left'] = True
            elif event.key == keys['right']:
                # hero['x'] += hero['speed']
                keys_down['right'] = True
        elif event.type == pygame.KEYUP:
            # the user let go of a key. See if it's one that matters
            if event.key == keys['up']:
                # user let go of the upkey. Flip the bool
                keys_down['up'] = False
            if event.key == keys['down']:
                keys_down['down'] = False
            if event.key == keys['right']:
                keys_down['right'] = False
            if event.key == keys['left']:
                keys_down['left'] = False

    if keys_down['up']:
        if player.y > 0:
            player.y -= player.speed
    elif keys_down['down']:
        if player.y < 744:
            player.y += player.speed
    if keys_down['left']:
        if player.x > 0:
            player.x -= player.speed
    elif keys_down['right']:
        if player.x < 1247:
            player.x += player.speed

    # if keys_down['up']:
    #     if player['y'] > 0:
    #         player['y'] -= player['speed']
    # elif keys_down['down']:
    #     if player['y'] < 440:
    #         player['y'] += player['speed']
    # if keys_down['left']:
    #     if player['x'] > 0:
    #         player['x'] -= player['speed']
    # elif keys_down['right']:
    #     if player['x'] < 960:
    #         player['x'] += player['speed']


    # if ball.y > 0:
    #     ball.y -= ball.speed
    # if ball.y < 496:
    #     ball.y += ball.speed
    # if ball.x > 0:
    #     ball.x -= ball.speed
    # if ball.x < 976:
    #     ball.x += ball.speed
    
    # if ball['y'] > 0:
    #     ball['y'] -= ball['speed']
    # if ball['y'] < 496:
    #     ball['y'] += ball['speed']
    # if ball['x'] > 0:
    #     ball['x'] -= ball['speed']
    # if ball['x'] < 976:
    #     ball['x'] += ball['speed']

    if player2.y > 0:
        player2.y -= player2.speed
    if player2.y < 744:
        player2.y += player2.speed
    if player2.x > 0:
        player2.x -= player2.speed
    if player2.x < 1247:
        player2.x += player2.speed
    

    if player3.y > 0:
        player3.y -= player3.speed
    if player3.y < 744:
        player3.y += player3.speed
    if player3.x > 0:
        player3.x -= player3.speed
    if player3.x < 1247:
        player3.x += player3.speed

    if player4.y > 0:
        player4.y -= player4.speed
    if player4.y < 744:
        player4.y += player4.speed
    if player4.x > 0:
        player4.x -= player4.speed
    if player4.x < 1247:
        player4.x += player4.speed
    
    #     player2['y'] -= player2['speed']
    # if player2['y'] < 440:
    #     player2['y'] += player2['speed']
    # if player2['x'] > 0:
    #     player2['x'] -= player2['speed']
    # if player2['x'] < 960:
    #     player2['x'] += player2['speed']


    # dx = ball.x - player.x
    # dy = ball.y - player.y
    # dist = hypot(dx,dy)

    # dx = dx / dist
    # dy = dy / dist

    # ball.x += dx * ball.speed
    # ball.y += dy * ball.speed




    # dx = player2.x - ball.x
    # dy = player2.y - ball.y
    # dist = hypot(dx,dy)

    # dx = dx / dist
    # dy = dy / dist

    # player2.x -= dx * player2.speed
    # player2.y -= dy * player2.speed






    
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         game_on = False
    #     elif event.type == pygame.KEYDOWN:
    #         #print "User pressed a key!"
    #         if event.key == keys["up"]: 
    #               273 is the up arrow key
    #             #player['y'] -= player['speed']
    #             #print "key is pressed"
    #             keys_down["up"] == True
    #         elif event.key == keys["down"]:
    #             #player ['y'] += player ["speed"]
    #             keys_down["down"] == True
    #         elif event.key == keys["right"]:
    #             #player ['x'] += player['speed']
    #             keys_down["right"] == True
    #         elif event.key == keys["left"]:
    #             #player['x'] -= player['speed']
    #             keys_down["left"] == True


    #     elif event.type == pygame.KEYUP:
    #         if event.key == keys["up"]:
    #             keys_down["up"] = False
    #         if event.key == keys["down"]:
    #             keys_down["down"] = False
    #         if event.key == keys["right"]:
    #             keys_down["right"] = False
    #         if event.key == keys["left"]:
    #             keys_down["left"] = False

    # if keys_down["up"]:
    #     player["y"] -= player["speed"]
    # elif keys_down["down"]:
    #     player["y"] += player["speed"]
    # if keys_down["left"]:
    #     player["x"] -= player["speed"]
    # elif keys_down["right"]:
    #     player["x"] += player["speed"]

    distance_between = fabs(player.x - ball.x) + fabs(player.y - ball.y)
    if distance_between < 32:
        (ball.x,ball.y) = (player.x, player.y)
        player2.has_ball =False
        player3.has_ball =False 
        player4.has_ball =False
    distance_between = fabs(player2.x - ball.x) + fabs(player2.y - ball.y)
    if distance_between < 32:
        (ball.x,ball.y) = (player2.x, player2.y)
        player2.has_ball = True
    # distance_between = fabs(player3.x - ball.x) + fabs(player3.y - ball.y)
    # if distance_between < 32:
    #     (ball.x,ball.y) = (player3.x, player3.y)
    #     player3.has_ball = True

    # elif distance_between == 0:
    #     (player2.x,player2.y) -= (player.x,player.y)
        
        dx = player2.x - player.x
        dy = player2.y - player.y
        dist = hypot(dx,dy)

        dx = dx / dist
        dy = dy / dist

        if player2.has_ball == True:
            player2.x += dx * player2.speed
            player2.y += dy * player2.speed 
        else:
            player2.x -= dx * player2.speed
            player2.y -= dy * player2.speed


    if player2.has_ball == False:
        dx = player2.x - ball.x
        dy = player2.y - ball.y
        dist = hypot(dx,dy)

        dx = dx / dist 
        dy = dy / dist

        player2.x -= dx * player2.speed
        player2.y -= dy * player2.speed

    distance_between = fabs(player3.x - ball.x) + fabs(player3.y - ball.y)
    if distance_between < 32:
        (ball.x,ball.y) = (player3.x, player3.y)
        player3.has_ball = True

        dx = player3.x - player.x
        dy = player3.y - player.y
        dist = hypot(dx,dy)

        dx = dx / dist
        dy = dy / dist

        if player3.has_ball == True:
            player3.x += dx * player3.speed
            player3.y += dy * player3.speed 
        else:
            player3.x -= dx * player3.speed
            player3.y -= dy * player3.speed


    if player3.has_ball == False:
        dx = player3.x - ball.x
        dy = player3.y - ball.y
        dist = hypot(dx,dy)

        dx = dx / dist 
        dy = dy / dist

        player3.x -= dx * player3.speed
        player3.y -= dy * player3.speed


    distance_between = fabs(player4.x - ball.x) + fabs(player4.y - ball.y)
    if distance_between < 32:
        (ball.x,ball.y) = (player4.x, player4.y)
        player4.has_ball = True

        dx = player4.x - player.x
        dy = player4.y - player.y
        dist = hypot(dx,dy)

        dx = dx / dist
        dy = dy / dist

        if player4.has_ball == True:
            player4.x += dx * player4.speed
            player4.y += dy * player4.speed 
        else:
            player4.x -= dx * player4.speed
            player4.y -= dy * player4.speed


    if player4.has_ball == False:
        dx = player4.x - ball.x
        dy = player4.y - ball.y
        dist = hypot(dx,dy)

        dx = dx / dist 
        dy = dy / dist

        player4.x -= dx * player4.speed
        player4.y -= dy * player4.speed

    game_on = True
    while game_on: 
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                counter += 1
                text = str(counter).rjust(3) if counter < 10 else 'GGGGGOOOAAAAALLLLL!'
            if e.type == pygame.QUIT: break
        else:
            # screen.fill((255, 255, 255))
            screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
            pygame.display.flip()
            clock.tick(60)
            continue
        break 
        # print "collision!"
    # screen.blit(clock)
    screen.blit(background_image, [0,0])
    # screen.blit(player_image, [player["x"], player["y"]])
    player2.draw_me()
    player3.draw_me()
    player4.draw_me()
    player.draw_me()

    ball.draw_me()
    # screen.blit(player2_image, [player2["x"], player2["y"]])
    # screen.blit(ball_image, [ball["x"], ball["y"]])
    
    # showScore()
    pygame.display.flip()

# counter, text = 1, '1'.rjust(3)
# pygame.time.set_timer(pygame.USEREVENT, 1000)
# font = pygame.font.SysFont('Consolas', 30)

# while game_on = True:
#     for e in pygame.event.get():
#         if e.type == pygame.USEREVENT: 
#             counter += 1
#             text = str(counter).rjust(3) if counter < 10 else 'GGGGGOOOAAAAALLLLL!'
#         if e.type == pygame.QUIT: break
#     else:
#         screen.fill((255, 255, 255))
#         screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
#         pygame.display.flip()
#         clock.tick(60)
#         continue
#     break