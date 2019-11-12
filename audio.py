import pygame
from time import sleep

def ping(sound):
    audio_length = pygame.mixer.Sound.get_length(sound)
    channel = sound.play()
    channel.set_volume(1,1)
    sleep(audio_length)

def echo(distance,direction,sound):
    volume_to_distance = [1,.7,.1]
    time_delay_to_distance = [0,.5,1]
    volume = volume_to_distance[distance - 1]
    time_delay = time_delay_to_distance[distance -1]
    audio_length = pygame.mixer.Sound.get_length(sound)

    if direction == 'front' or direction == 'back':
        sleep(time_delay)
        channel = sound.play()
        channel.set_volume(volume,volume)
        sleep(audio_length*3)
    elif direction == 'right':
        sleep(time_delay)
        channel = sound.play()
        channel.set_volume(0,volume)
        sleep(audio_length*3)
    elif direction == 'left':
        sleep(time_delay)
        channel = sound.play()
        channel.set_volume(volume,0)
        sleep(audio_length*3)








if __name__ == "__main__":
    pygame.mixer.init()

## Walking Audio
    ping_sound = pygame.mixer.Sound("Sounds/ping_2.wav")
    hollow_sound = pygame.mixer.Sound("Sounds/drop.wav")
    stone_step = []
    for i in range(1,7):
        stone_step.append(pygame.mixer.Sound("Sounds/stoneSteps/stone"+str(i)+".ogg"))

    ping(ping_sound)
    echo(3,'left',hollow_sound)
    ping(ping_sound)
    echo(2,'right',hollow_sound)
    ping(ping_sound)
    echo(1,'front',hollow_sound)

    # i = 0
    # while i < 6:
    #     #step = random.choice(stone_step)
    #     step = stone_step[i]
    #     step.play()
    #     sleep(.2)
    #     i+=1