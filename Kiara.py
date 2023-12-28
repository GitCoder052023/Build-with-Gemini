import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

try:
    print("Text Model: Kiara TLDR")
    print("Text + Vision Model: Kiara VITA")
    print("Voice Model: Kiara VLDR")
    print("Voice + Vision Model: Kiara VIVA")
    print("")
    choice = input('Choose the model to chat from above: ')


    if choice == "Kiara TLDR":
        def to_markdown(text):
            text = text.replace('•', '  *')
            return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


        genai.configure(api_key="AIzaSyAm_r0GQ6GdUqZvAOHCgSB15jLgl6yjT84")

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

    if choice == "Kiara VITA":

        def to_markdown(text):
            text = text.replace('•', '  *')
            return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


        genai.configure(api_key="AIzaSyAm_r0GQ6GdUqZvAOHCgSB15jLgl6yjT84")

        model = genai.GenerativeModel('gemini-pro-vision')
        img = PIL.Image.open("images/test2.jpg")

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

    if choice == "Kiara VLDR":
        def to_markdown(text):
            text = text.replace('•', '  *')
            return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


        genai.configure(api_key="AIzaSyAm_r0GQ6GdUqZvAOHCgSB15jLgl6yjT84")

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

    if choice == "Kiara VIVA":
        def to_markdown(text):
            text = text.replace('•', '  *')
            return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


        genai.configure(api_key="AIzaSyAm_r0GQ6GdUqZvAOHCgSB15jLgl6yjT84")

        model = genai.GenerativeModel('gemini-pro-vision')
        img = PIL.Image.open("images/test2.jpg")

        messages = []

        while True:
            message = input("You: ")
            engine.say("Recognizing sir, Please wait")
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

except FileNotFoundError:
    # Handle the error if the file is not found
    print("Error: Image file not found. Please check the file name and path.")

except Exception as e:
    # Handle any other technical errors
    print("An unexpected technical error occurred:", e)