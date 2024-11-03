import pygame
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Vaibhav N\Desktop\Piper\piper\welcome1.wav")
pygame.mixer.music.play()

# Keep the script running while the sound plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
