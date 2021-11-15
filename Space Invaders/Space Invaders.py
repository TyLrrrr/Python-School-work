def main():
    import turtle
    import os
    import math
    import random
    import platform
    #import pygame


    #determine the platform
    if platform.system() == "Windows":
        try:
            import winsound
            # use the below code for sounds in windows.
            # winsound.PlaySound("wavfile.wav", winsound.SND_ASYNC)
        except:
            print("Winsound module not available")

    # set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Space Invaders")
    screen.bgpic("space_invaders_background.gif")
    screen.tracer(0)

    # Register the shapes
    screen.register_shape("invader.gif")
    screen.register_shape("player.gif")

    # Draw a border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    # set the score
    score = 0

    # Draw the score
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290,275)
    scorestring = "Score: {}".format(score)
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()

    # Restart option
    retry = turtle.Turtle()
    retry.speed(0)
    retry.color("white")
    retry.penup()
    retry.setposition(-50,-50)
    retry_string = "Retry? Y or N".format()
    retry.hideturtle()


    #game over
    game_over = turtle.Turtle()
    game_over.speed(0)
    game_over.color("white")
    game_over.penup()
    game_over.setposition(-70,0)
    game_over_string = "- GAME OVER! -".format()
    game_over.hideturtle()

    
    # Create the player turtle
    player = turtle.Turtle()
    player.color("blue")
    player.shape("player.gif")
    player.penup()
    player.speed(0)
    player.setposition(0,-250)
    player.setheading(90)
    player.speed = 0

    # Choose the number of enemies
    number_of_enemies = 30
    # Create an empty list of enemies
    enemies = []
    # add enemies to the list
    for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())

    enemy_start_x = -225
    enemy_start_y = 250
    enemy_number = 0

    for enemy in enemies:
        enemy.color("red")
        enemy.shape("invader.gif")
        enemy.penup()
        enemy.speed(0)
        x = enemy_start_x + (50 * enemy_number)
        y = enemy_start_y
        enemy.setposition(x,y)
        enemy_number += 1
        if enemy_number == 10:
            enemy_start_y -= 50
            enemy_number = 0


    #create bullet
    bullet = turtle.Turtle()
    bullet.color("green")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setposition(0,-300)
    bullet.setheading(90)
    bullet.shapesize(0.5,0.5)
    bullet.hideturtle()

    # speed variables
    enemyspeed = 0.1
    bulletspeed = 1.5

    # bullet states
    # ready to fire
    # fired
    bulletstate = "ready"

    #Cross platform sound files
    def play_sound(sound_file, time = 0):
        #windows
        if platform.system() == "Windows":
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)
        #linux
        elif platform.system() == "Linux":
            os.system("aplay -q {}&".format(sound_file))
        #mac
        else:
            os.system("afplay {}&".format(sound_file))

        if time > 0:
            turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))
            
    # Move player left and right and fire
    def move_left():
        player.speed = -0.5
        
    def move_right():
        player.speed = 0.5

    def move_stop():
        player.speed = 0

    def move_player():
        x = player.xcor()
        x += player.speed
        if x < -280:
            x = -280
        if x > 280:
            x = 280
        player.setx(x)

    def fire_bullet():
        # declare bulletstate as a global if it needs change
        nonlocal bulletstate
        if bulletstate == "ready":
            play_sound("laser.wav")
            bulletstate = "fire"
            # Move the bullet position to jsut above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x,y)
            bullet.showturtle()

    #Restart and exit the game
    def restart():
        turtle.clearscreen()
        main()
        
    def close():
        exit()
    
    # collision function
    def isCollision(t1,t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 15:
            return True
        else:
            return False

    # key board bindings
    screen.listen()
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(move_stop, "Down")
    screen.onkeypress(fire_bullet, "space")
    screen.onkeypress(fire_bullet, "Up")
    screen.onkeypress(restart, "y")
    screen.onkeypress(close, "n")

    #Play Background music
    #pygame.mixer.init()
    #pygame.mixer.music.load("bgm.wav")
    #pygame.mixer.music.play(-1)


    run_game = True
    # Main game loop
    while run_game == True:
        screen.update()
        move_player()

        for enemy in enemies:
            # move the enemy
            x = enemy.xcor()
            x += enemyspeed    
            enemy.setx(x)

            # move enemy back and down
            if enemy.xcor() > 280:
                # moves all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # change direction
                enemyspeed *= -1

            if enemy.xcor() < -280:
                # moves all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # change direction
                enemyspeed *= -1
                
            # game over if enemy reached bottom
            if enemy.ycor() < -250:
                # game over
                game_over.write(game_over_string, False, align="left", font=("Arial", 14, "normal"))
                retry.write(retry_string, False, align="left", font=("Arial", 14, "normal"))
                run_game = False


            # check for collision between bullet and enemy
            if isCollision(bullet, enemy):
                # explosion sound
                play_sound("explosion.wav")
                # reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)
                # reset the enemy
                enemy.setposition(0,5000)
                # update the score
                score += 10
                scorestring = "Score: {}".format(score)
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            # Check for collision between enemy and player
            if isCollision(enemy, player):
                # explosion sound
                play_sound("explosion.wav")
                player.hideturtle()
                enemy.hideturtle()
                # game over
                # Restart?
                retry.write(retry_string, False, align="left", font=("Arial", 14, "normal"))
                game_over.write(game_over_string, False, align="left", font=("Arial", 14, "normal"))
                run_game = False
                    
            
        # check to see if bullet reached top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

        # move the bullet
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

main()
