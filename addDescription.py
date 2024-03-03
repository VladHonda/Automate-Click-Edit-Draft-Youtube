import pyautogui
from time import sleep
import random
import keyboard  # Import the keyboard module

from random import choices
def trial():
    return 2000 <= sorted(choices(range(6666), k=8))[1] < 6666

z = sum(trial() for i in range(6666)) / 6666

# Number of times to repeat the process
# Loop until 'edit_draft.png' is no longer detected or max_repeats is reached
while True:
    # Sleep for a few seconds to give time to switch to the desired window or tab
    sleep(z)

    # Check if the Esc key is pressed
    if keyboard.is_pressed('esc'):
        print("Esc key pressed. Exiting the loop.")
        break

    # Locate and click on the 'edit_draft.png'
    edit_draft_location = pyautogui.locateOnScreen('edit_draft.png', confidence=0.8)
    if edit_draft_location:
        pyautogui.click(edit_draft_location)
        sleep(z*4)

        # Locate and click on 'description.png'
        description_location = pyautogui.locateOnScreen('description.png', confidence=0.8)
        if description_location:
            pyautogui.click(description_location)
            sleep(z)  # Adjust this sleep duration based on the time it takes for the description field to become active
            pyautogui.hotkey('ctrl', 'a')
            # Type the text
            text_to_paste = "Please don't forget to subscribe.\n\n#stableDiffusion #Deforum #shorts Stable Diffusion\n\nprompt:\n   t3/4 view of a cat with 13 rings Neptune has at least five main rings and four prominent ring arcs Moon Neutron Star, explosions, sci-fi, cyberpunk, dystopia, trending on artstation, cinematic lighting, hyper realism, 64k, 32k, 16k, 12k, 8k, [high contrast], hyper detailed, unreal, udk 5, unreal engine 5\npos:\n beautiful, high resolution, artstation, vivid explosion, Hypnotic, Detail, Finetuned Diffusion, MaskGit, Redshift Renderer (Cinema 4d),  Mech, StyleGan-T\n\nneg:\n ugly, line drawing, eye, text, EasyNegative, text"

            pyautogui.write(text_to_paste)
            print("Text written successfully.")

            # Move to 'next.png' and click 4 times with a random interval
            next_location = pyautogui.locateOnScreen('next.png', confidence=0.8)
            if next_location:
                print("Located 'next.png'. Clicking 4 times.")
                pyautogui.moveTo(next_location.left + next_location.width / 2, next_location.top + next_location.height / 2)
                for _ in range(4):
                    pyautogui.click()
                    sleep(z)  # Adjust the range based on your preference
                    print("Click.")

                                                    
                sleep(z*20)
                # Press 'Tab' and then 'Enter'
                pyautogui.press('tab')
                sleep(z)  # Adjust the sleep duration based on your system's responsiveness
                pyautogui.press('enter')
                print("Pressed 'Tab' and 'Enter'.")
            else:
                print("Error: 'next.png' not found.")
               
            
        
    else:
        print("Error: 'edit_draft.png' not found.")
        break  # Break out of the loop if 'edit_draft.png' is not found
