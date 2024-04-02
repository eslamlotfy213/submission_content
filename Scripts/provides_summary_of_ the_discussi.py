import openai
import os 
from pydub import AudioSegment

API_KEY =  "Your API Key" 

openai.api_key = API_KEY


#t ranscrib_audio
def transcribe_audio(audio_file_path):
    with open(audio_file_path,'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1",audio_file)
       
        #save transcription to .txt file ....
    with open("transcription.txt",'w') as f:
     f.write(transcription['text'])
    return transcription['text']


def abstract_summary_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']




def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    return {
        'abstract_summary': abstract_summary,
    }


# save the returned dict to nicly formated .md file
def save_to_md(meeting_minutes_dict, file_name):
    with open(file_name,'w') as f:
        f.write(f"# Main Topic Coversation 2024\n\n")
        f.write(f"## Abstract Summary\n\n")


audio_file_path ="Your File audio"

transcription = transcribe_audio(audio_file_path)

minutes = meeting_minutes(transcription)

print(minutes)

save_to_md(minutes,"results.md")





