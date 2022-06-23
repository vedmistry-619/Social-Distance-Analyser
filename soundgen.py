from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from os import path
speech = gTTS(text = "Alert! Please Maintain Social Distancing.")
speech.save('Ronaldo.mp3')
playsound('Ronaldo.mp3')

#src = "Ronaldo.mp3"
#dst = "test.wav"
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")