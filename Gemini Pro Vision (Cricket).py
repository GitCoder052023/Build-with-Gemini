import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
import cv2
import pyttsx3


engine = pyttsx3.init()
rate = 200  # Adjust as needed (150 is faster than the default)
engine.setProperty('rate', rate)
# Set the pause duration in seconds:


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="REPLACE WITH YOUR OWN API KEY")
model = genai.GenerativeModel('gemini-pro-vision')

# Local video file path
video_path = 'Videos/Cricket.mp4'  # Replace with your local video path

# Open the local video
cap = cv2.VideoCapture(video_path)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break  # End of video

    # Save the frame as a JPEG image
    frame_name = f"frame_{cap.get(cv2.CAP_PROP_POS_FRAMES)}.jpg"
    frame_path_full = pathlib.Path('C:/Users/Hamdan/PycharmProjects/Gemini/Frames') / frame_name #REPLACE FOLDER PATH WITH YOUR OWN PATH
    cv2.imwrite(str(frame_path_full), frame)

    # Load the saved image
    img = PIL.Image.open(frame_path_full)

    # Generate cricket commentary query
    query = ("write commentary for the cricket action happening in this image, and write only commentary for cricket image,"
             "do not write any any other thing. and write commentary like humans way,"
             "and take the actual names of players in commentary")

    # Generate response from Gemini Pro Vision
    response = model.generate_content([query, img], stream=True)
    response.resolve()
    commentary = response.text

    # Print or display the commentary
    print(commentary)
    engine.say(commentary)
    engine.runAndWait()

    # Optional: Speak the commentary using a text-to-speech library
    # (Add necessary libraries and code for text-to-speech functionality)

# Release video capture
cap.release()
