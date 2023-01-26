from pydub.audio_segment import AudioSegment as aseg

filename = "mysound.mp3"
a = aseg.from_mp3(filename)
fin = 5.09

print(len(a))


