from mutagen.mp3 import MP3
audio = MP3("dhruva.mp3")
mp3len = audio.info.length
print mp3len
