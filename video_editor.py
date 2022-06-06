import os
from moviepy.editor import *


class VideoEditor(object):

    def __init__(self, video_path: str) -> None:
        self._video_path = video_path

        if not os.path.exists(self._video_path):
            raise ValueError(f"{self._video_path} not found")

        self._filename = os.path.basename(self._video_path)
        self._clip = VideoFileClip(self._video_path)
        self._audio = self._clip.audio



    def cropVideo(self):
        self._clip = self._clip.crop(x1=2, y1=2, x2=self._clip.w - 3, y2=self._clip.h - 3)

    def fadeinout(self):
        self._clip = self._clip.fadein(2).fadeout(2)

    def resizeVideo(self):
        self._clip = self._clip.resize(height=self._clip.h*1.1, width=self._clip.w*1.05)

    def reduceVol(self):
        self._clip = self._clip.volumex(0.9)

    def generate(self):
        self.cropVideo()
        self.fadeinout()
        self.resizeVideo()
        self.reduceVol()

        filename, file_extension = os.path.splitext(self._video_path)
        new_video_path = self._video_path.replace(file_extension, f"_regen{file_extension}")
        self._clip.write_videofile(new_video_path)



        

