import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
import pyttsx3
import cv2

key = "REPLACE WITH YOUR OWN GEMINI API KEY"

engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def Activate_KiaraTLDR():
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro')
    messages = []

    while True:
        user_input = input("You: ")
        messages.append({
            "role": "user",
            "parts": [user_input],
        })

        response = model.generate_content(messages)

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        print("Kiara:", response.text)

def Activate_KiaraVITA():
    genai.configure(api_key=key)

    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open("images/zenLq.jpg")

    messages = []

    while True:
        message = input("You: ")
        print("Recognizing...")
        messages.append({
            "role": "user",
            "parts": [message, [img]],
        })

        response = model.generate_content([message, img], stream=True)
        response.resolve()

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        print("Kiara: " + response.text)

def Activate_KiaraVLDR():
    genai.configure(api_key=key)

    model = genai.GenerativeModel('gemini-pro')

    messages = []

    while True:
        message = input("You: ")
        messages.append({
            "role": "user",
            "parts": [message],
        })

        response = model.generate_content(messages)

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        print("Kiara: " + response.text)
        engine.say(response.text)
        engine.runAndWait()

def Activate_KiaraVIVA():
    genai.configure(api_key=key)

    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open("images/R.jpg")

    messages = []

    while True:
        message = input("You: ")
        engine.say("Generating Answer sir, Please wait")
        engine.runAndWait()
        messages.append({
            "role": "user",
            "parts": [message, [img]],
        })

        response = model.generate_content([message, img], stream=True)
        response.resolve()

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        print("Kiara: " + response.text)
        engine.say(response.text)
        engine.runAndWait()

def Activate_KiaraVITA_Video():
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro-vision')

    # Define video path and frame saving path
    video_path = "Videos/MyMP4.mp4"
    frame_path = 'C:/Users/Hamdan/PycharmProjects/Gemini/Frames'  # Ensure this directory exists

    # Open the video capture
    cap = cv2.VideoCapture(video_path)

    messages = []

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break  # End of video

        # Save the frame as a JPEG image
        frame_name = f"frame_{cap.get(cv2.CAP_PROP_POS_FRAMES)}.jpg"
        frame_path_full = pathlib.Path(frame_path) / frame_name
        cv2.imwrite(str(frame_path_full), frame)

        # Load the saved image
        img = PIL.Image.open(frame_path_full)

        # Get query from user
        message = input("You: ")
        print("Generating Answer sir, Please wait")
        messages.append({
            "role": "user",
            "parts": [message, [img]],
        })

        response = model.generate_content([message, img], stream=True)
        response.resolve()

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        print("Kiara: " + response.text)

    # Release video capture
    cap.release()

def Activate_Kiara_VIVA_Video():
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro-vision')

    # Define video path and frame saving path
    video_path = "Videos/MyMP4.mp4"
    frame_path = 'C:/Users/Hamdan/PycharmProjects/Gemini/Frames'  # Ensure this directory exists

    # Open the video capture
    cap = cv2.VideoCapture(video_path)

    messages = []

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break  # End of video

        # Save the frame as a JPEG image
        frame_name = f"frame_{cap.get(cv2.CAP_PROP_POS_FRAMES)}.jpg"
        frame_path_full = pathlib.Path(frame_path) / frame_name
        cv2.imwrite(str(frame_path_full), frame)

        # Load the saved image
        img = PIL.Image.open(frame_path_full)

        # Get query from user
        message = input("You: ")
        engine.say("Generating Answer sir, Please wait")
        engine.runAndWait()
        messages.append({
            "role": "user",
            "parts": [message, [img]],
        })

        response = model.generate_content([message, img], stream=True)
        response.resolve()

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        print("Kiara: " + response.text)
        engine.say(response.text)
        engine.runAndWait()

    # Release video capture
    cap.release()

try:
    print("Text Model: Kiara TLDR\n")
    print("Text + Vision Model(IMG): Kiara VITA \nText + Vision Model(VID): Kiara VITA (V)\n")
    print("Voice Model: Kiara VLDR\n")
    print("Voice + Vision Model(IMG): Kiara VIVA \nVoice + Vision Model(VID): Kiara VIVA (V)\n")
    choice = input('Choose the model to chat from above: ')

    if choice == "Kiara TLDR":
        Activate_KiaraTLDR()

    if choice == "Kiara VITA":
        Activate_KiaraVITA()

    if choice == "Kiara VLDR":
        Activate_KiaraVLDR()

    if choice == "Kiara VIVA":
        Activate_KiaraVIVA()

    if choice == "Kiara VITA (V)":
        Activate_KiaraVITA_Video()

    if choice == "Kiara VIVA (V)":
        Activate_Kiara_VIVA_Video()

except FileNotFoundError:
    # Handle the error if the file is not found
    print("Error: Image file not found. Please check the file name and path.")

except Exception as e:
    # Handle any other technical errors
    print("An unexpected technical error occurred:", e)
