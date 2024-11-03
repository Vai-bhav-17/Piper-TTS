import subprocess
import pygame
import time

# Define the path to the piper executable and the output file
piper_executable = r"C:\Users\Vaibhav N\Desktop\Piper\piper\piper.exe"
output_file = "new.wav"
message = "Welcome to the fascinating world of chess, a game that has captivated minds for centuries. Chess, known as the 'Game of Kings,' is not merely a board game but a profound exercise in strategy, foresight, and patience. Each player commands an army of sixteen pieces, including pawns, knights, bishops, rooks, a queen, and a king. The ultimate goal is to place the opponent's king under direct threat of capture, known as checkmate."

# Command to create the audio file
command = f'echo "{message}" | "{piper_executable}" --model en_US-kathleen-low.onnx --output_file {output_file}'

# Run the command to create the audio file
subprocess.run(command, shell=True, check=True)

# Initialize pygame mixer and play the audio file
pygame.mixer.init()
pygame.mixer.music.load(output_file)
pygame.mixer.music.play()

# Keep the script running while the sound plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
