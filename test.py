
import moviepy.editor as mpe

sound = "mysound.mp3"
img = 'mypic.jpg'
clips = mpe.ImageClip(img).set_duration(306)
clips.write_videofile("test.mp4", fps=24)

clip = mpe.VideoFileClip("test.mp4")
audio_bg = mpe.AudioFileClip(sound)
final_clip = clip.set_audio(audio_bg)
final_clip.write_videofile("test2.mp4")

# concat_clip = concatenate_videoclips(clips, method="compose")
# concat_clip.write_videofile("test.mp4", fps=24)

