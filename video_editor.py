import os
from moviepy.editor import *


class VideoEditor(object):

    def __init__(self, video_path: str) -> None:
        self._video_path = video_path

        if not os.path.exists(self._video_path):
            raise ValueError(f"{self._video_path} not found")

        self._filename = os.path.basename(self._video_path)
        self._clip = VideoFileClip(self._video_path)
        self._audio = AudioFileClip(self._video_path)




    def cropVideo(self):
        self._clip = self._clip.crop(x1=10, y1=15, x2=self._clip.w - 10, y2=self._clip.h - 15)

    def fadeout(self):
        self._clip = self._clip.fadeout(2)

    def resizeVideo(self):
        self._clip = self._clip.resize(height=self._clip.h*1.1, width=self._clip.w*1.05)

    def reduceVol(self):
        self._clip = self._clip.volumex(1.1)


    def flipHorizoltal(self):
        self._clip = self._clip.fx(vfx.mirror_x)

    def cutHead(self):
        self._clip = self._clip.subclip(1,-1)

    def generate(self):
        self.flipHorizoltal()
        self.cutHead();
        # self.cropVideo()
        self.fadeout()
        # self.resizeVideo()
        self.reduceVol()

        filename, file_extension = os.path.splitext(self._video_path)
        new_video_path = self._video_path.replace(file_extension, f"_regen{file_extension}")
        self._clip.write_videofile(new_video_path, temp_audiofile='temp-audio.m4a', remove_temp=True, codec='libx264', audio_codec="aac")
        self._clip.close()
        self._audio.close()



        


