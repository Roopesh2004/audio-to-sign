import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string


def func():
    r = sr.Recognizer()

    # List of phrases mapped to video filenames
    video_phrases = {
        'are you free today': 'Are you free today.mp4',
        'are you hiding something': 'Are you hiding something.mp4',
        'bring water for me': 'bring water for me.mp4',
        'can help you': 'can help you.mp4',
        'comb your hair': 'Comb your hair.mp4',
        'congratulations': 'Congratulations.mp4',
        'do me a favour': 'Do me a favour.mp4',
        'do not hurt me': 'Do not hurt me.mp4',
        'do not worry': 'Do not worry.mp4',
        'do you need something': 'Do you need something.mp4',
        'do not abuse him': 'donotabusehim.mp4',
        'do not make me angry': 'Donotmakemeangry.mp4',
        'from now he won’t hurt you': 'fromnowhewonthurtyou.mp4',
        'had your food': 'Had your food.mp4',
        'he is on the way': 'He is on the way.mp4',
        'he would be coming today': 'He would be coming today.mp4',
        'he came by train': 'Hecamebytrain.mp4',
        'help me': 'help me.mp4',
        'how are things': 'How are things.mp4',
        'how are you': 'how are you.mp4',
        'how dare you': 'How dare you.mp4',
        'how old are you': 'Howoldareyou.mp4',
        'i am afraid of that': 'I am afraid of that.mp4',
        'i am crying': 'i am crying.mp4',
        'i am feeling cold': 'i am feeling cold.mp4',
        'i am in dilemma what to do': 'I am in dilam what to do.mp4',
        'i am not really sure': 'I am not really sure.mp4',
        'i am really grateful': 'I am really grateful.mp4',
        'i am fine thank you': 'iamfinethankyou.mp4',
        'i am sitting in the class': 'Iamsittingintheclass.mp4',
        'i am suffering from fever': 'iamsufferingfromfever.mp4',
        'i am tired': 'iamtired.mp4',
        'i am very happy': 'iamveryhappy.mp4',
        'i cannot help you': 'icannothelpyou.mp4',
        'i do not agree': 'idonotagree.mp4',
        'i enjoyed a lot': 'ienjoyedalot.mp4',
        'i got hurt': 'igothurt.mp4',
        'i like you i love you': 'ilikeyouiloveyou.mp4',
        'i need water': 'ineedwater.mp4',
        'i promise': 'ipromise.mp4',
        'i really appreciate': 'Ireallyappreciate.mp4',
        'is she is my friend': 'issheismyfriend.mp4',
        'it does not make any difference': 'itdoesnotmakeanydifference.mp4',
        'it was nice meeting you': 'itwasnicemeetingyou.mp4',
        'it was nice chatting with you': 'iwasnicexhattingwithyou.mp4',
        'i was stopped by someone': 'iwasstoppedbysomeone.mp4',
        'let him take time': 'lethimtaketime.mp4',
        'my name is': 'mynameis.mp4',
        'pour some more water': 'poursomemorewater.mp4',
        'prepare the bed': 'preparethebed.mp4',
        'serve the food': 'servethefood.mp4',
        'shall we go outside': 'shallwegooutside.mp4',
        'somehow got to know': 'somehowgottoknow.mp4',
        'speak softly': 'speeksoftly.mp4',
        'take care of yourself': 'tackcareofyourself.mp4',
        'tell me the truth': 'tellmethetruth.mp4',
        'thank you so much': 'thankyousomuch.mp4',
        'that is so kind of you': 'thatssokindofyou.mp4',
        'the place is beautiful': 'theplaceisbutifull.mp4',
        'try to understand': 'trytounderstand.mp4',
        'turn on light': 'turnonlight.mp4',
        'we are all with you': 'weareallwithyou.mp4',
        'what is your phone number': "what'syourphonenumber.mp4",
        'what are you doing': 'whatareyoudoing.mp4',
        'what did you tell him': 'whatdidyoutellhim.mp4',
        'what do you do': 'whatdoyoudo.mp4',
        'what do you think': 'whatdoyouthink.mp4',
        'what do you want to become': 'whatdoyouwanttobecome.mp4',
        'what happened': 'whathappened.mp4',
        'what have you planned': 'whathaveyouplanned.mp4',
        'what you want': 'whatyouwant.mp4',
        'when will the train leave': 'whenwillthetrainleave.mp4',
        'where are you from': 'whereareyoufrom.mp4',
        'wear the shirt': 'wheretheshirt.mp4',
        'which college are you from': 'whichcollegeareyoufrom.mp4',
        'who are you': 'whoareyou.mp4',
        'why are you angry': 'whyareyouangry.mp4',
        'why are you crying': 'whyareyoucrying.mp4',
        'why are you disappointed': 'whyareyoudisappointed.mp4',
        'you are bad': 'youarebade.mp4',
        'you are good': 'youaregood.mp4',
        'you are welcome': 'youarewelcome.mp4',
        'you can do anything': 'youcandoanything.mp4',
        'you can do it': 'youcandoit.mp4',
        'you need to take the medicine': 'youneedtotakethemedicine.mp4'
    }

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            print("Say something:")
            audio = r.listen(source)
            try:
                a = r.recognize_google(audio).lower()
                print("You said:", a)

                # Check for exit condition
                if a in ["goodbye", "good bye", "bye"]:
                    print("Goodbye!")
                    break

                # Check for video playback
                if a in video_phrases:
                    video_path = r"C:\Users\HP\Downloads\Automatic-Indian-Sign-Language-Translator-ISL-master\Automatic-Indian-Sign-Language-Translator-ISL-master\AI_DATASET\\" + video_phrases[a]
# Path to videos folder

                    # Play video using OpenCV
                    cap = cv2.VideoCapture(video_path)
                    if not cap.isOpened():
                        print("Error: Could not open video.")
                        continue

                    while cap.isOpened():
                        ret, frame = cap.read()
                        if not ret:
                            break
                        cv2.imshow('Video', frame)

                        # Press 'q' to quit video playback
                        fps = cap.get(cv2.CAP_PROP_FPS)
                        delay = int(1000 / fps)  # Convert FPS to milliseconds
                        if cv2.waitKey(delay) & 0xFF == ord('q'):
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                else:
                    print("Phrase not recognized or video not available.")

            except Exception as e:
                print("Error recognizing speech:", str(e))


# GUI for the main menu
while True:
    image = "signlang.png"
    msg = "HEARING IMPAIRMENT ASSISTANT"
    choices = ["Live Voice", "All Done!"]
    reply = buttonbox(msg, image=image, choices=choices)

    if reply == choices[0]:
        func()
    if reply == choices[1]:
        quit()
