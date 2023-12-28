import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image
import cv2

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="REPLACE WITH YOUR OWN API KEY")
model = genai.GenerativeModel('gemini-pro-vision')

# Define video path and frame saving path
video_path = "Videos/MyMP4.mp4"
frame_path = 'C:/Users/Hamdan/PycharmProjects/Gemini/Frames'  # Ensure this directory exists

# Open the video capture
cap = cv2.VideoCapture(video_path)

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
    Input = input("Enter query for this frame: ")

    # Generate response from Gemini Pro Vision
    response = model.generate_content([Input, img], stream=True)
    response.resolve()
    print(response.text)

# Release video capture
cap.release()
