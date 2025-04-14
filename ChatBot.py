import speech_recognition as sr
import openai
import tkinter as tk
from tkinter import Label

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening for a question...")
            audio = recognizer.listen(source)
            question = recognizer.recognize_google(audio)
            print(f"Question: {question}")
            answer = get_answer(question)
            display_answer(answer)
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")

def transcribe_audio_from_file(audio_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            print("Processing audio file...")
            audio = recognizer.record(source)
            question = recognizer.recognize_google(audio)
            print(f"Question: {question}")
            answer = get_answer(question)
            display_answer(answer)
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")

def get_answer(question):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer this interview question: {question}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I couldn't generate an answer."

def display_answer(answer):
    # Create a transparent window
    root = tk.Tk()
    root.attributes('-alpha', 0.8)  # Set transparency
    root.attributes('-topmost', True)  # Keep window on top
    root.configure(bg='black')
    root.geometry("800x200")
    
    label = Label(root, text=answer, font=("Arial", 16), fg="white", bg="black", wraplength=750)
    label.pack(expand=True)
    
    root.after(10000, root.destroy)  # Auto-close after 10 seconds
    root.mainloop()

if __name__ == "__main__":
    print("Provide the path to an audio file for transcription.")
    audio_file_path = input("Enter the audio file path: ").strip()
    transcribe_audio_from_file(audio_file_path)