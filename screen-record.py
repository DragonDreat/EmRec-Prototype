import pyautogui
import cv2
import numpy as np
import pyaudio
import wave
import time
from datetime import datetime
import os
import threading


video_folder = "videos"
audio_folder = "audio"
if not os.path.exists(video_folder):
    os.makedirs(video_folder)
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)


screen_width, screen_height = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 15.0
now = datetime.now().strftime("%Y%m%d_%H%M%S")
video_filename = os.path.join(video_folder, f"screen_{now}.avi")


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


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


    audio_filename = os.path.join(audio_folder, f"audio_{now}.wav")
    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



def snimi_ekran(trajanje=30):
    out = cv2.VideoWriter(video_filename, fourcc, fps, (screen_width, screen_height))

    start_time = time.time()
    while time.time() - start_time < trajanje:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timestamp, (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Upisuj frame u video fajl
        out.write(frame)

    out.release()


if __name__ == "__main__":
    # Postavlja trajanje snimanja
    record_duration = 30

    audio_thread = threading.Thread(target=snimi_audio, args=(record_duration,))
    screen_thread = threading.Thread(target=snimi_ekran, args=(record_duration,))

    audio_thread.start()
    screen_thread.start()

    audio_thread.join()
    screen_thread.join()

