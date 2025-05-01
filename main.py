import cv2
import threading
import time
import pyaudio
import wave
import os
from datetime import datetime
import keyboard


RECORD_DURATION = 30  
recording = False


camera = cv2.VideoCapture(0)  

# Pyaudio postavke
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

video_folder = "videos"
audio_folder = "audio"
if not os.path.exists(video_folder):
    os.makedirs(video_folder)
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)


camera.set(cv2.CAP_PROP_FPS, 15)

def snimi_audio(trajanje=30):

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    start_time = time.time()
    while time.time() - start_time < trajanje:
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()


    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_filename = os.path.join(audio_folder, f"audio_{now}.wav")


    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def snimi_video(trajanje=30):
    global recording
    if recording:
        return
    recording = True
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = os.path.join(video_folder, f"video_{now}.avi")

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 15.0  
    frame_width = int(camera.get(3))
    frame_height = int(camera.get(4))
    out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))


    threading.Thread(target=snimi_audio, args=(trajanje,), daemon=True).start()

    start_time = time.time()
    while time.time() - start_time < trajanje:
        ret, frame = camera.read()
        if ret:
            out.write(frame)
        else:
            break

        time.sleep(0.05)

    out.release()
    recording = False


while True:
    if keyboard.is_pressed('F9'):
        if not recording:
            threading.Thread(target=snimi_video, args=(RECORD_DURATION,), daemon=True).start()

        time.sleep(0.5) 
