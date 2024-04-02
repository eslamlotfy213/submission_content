import openai
import os 
from pydub import AudioSegment

API_KEY =   "Your API Key" 

openai.api_key = API_KEY
#transcrib_audio
def transcribe_audio(audio_file_path):
    with open(audio_file_path,'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1",audio_file)
       
        #save transcription to .txt file ....
    with open("transcription.txt",'w') as f:
     f.write(transcription['text'])
    return transcription['text']

