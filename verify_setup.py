import os

import cv2
import faiss
import numpy as np
import whisper
from dotenv import load_dotenv

load_dotenv()

print('[OK] OpenCV:', cv2.__version__)
print('[OK] Whisper: loaded')
print('[OK] FAISS: loaded')
print('[OK] NumPy:', np.__version__)
print('[OK] Gemini Key set:', bool(os.getenv('GOOGLE_API_KEY')))
print('[OK] FFmpeg path:', os.getenv('FFMPEG_PATH'))
print('\nSetup complete. Ready to build.')