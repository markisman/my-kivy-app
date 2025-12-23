import cv2
import numpy as np

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.utils import platform


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        # دوربین Kivy (سازگار با اندروید)
        self.camera = Camera(play=True, resolution=(640, 480))
        self.camera.index = 0

        # ویجت نمایش تصویر پردازش‌شده
        self.img = Image()

        layout.add_widget(self.camera)
        layout.add_widget(self.img)

        Clock.schedule_interval(self.update, 1.0 / 15.0)
        return layout

    def update(self, dt):
        # گرفتن فریم از texture دوربین
        if not self.camera.texture:
            return

        texture = self.camera.texture
        w, h = texture.size

        # تبدیل texture به numpy array
        pixels = texture.pixels
        frame = np.frombuffer(pixels, dtype=np.uint8)
        frame = frame.reshape(h, w, 4)

        # RGBA → BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # پردازش تصویر (نمونه: شبیه‌سازی عمق ساده)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (15, 15), 0)

        depth = np.zeros_like(blur)
        depth[blur < 100] = 255   # نزدیک
        depth[blur >= 100] = 0   # دور

        # تبدیل به RGB برای Kivy
        depth_rgb = cv2.cvtColor(depth, cv2.COLOR_GRAY2RGB)

        # ساخت Texture جدید
        tex = Texture.create(size=(w, h), colorfmt="rgb")
        tex.blit_buffer(depth_rgb.tobytes(), colorfmt="rgb", bufferfmt="ubyte")
        tex.flip_vertical()

        self.img.texture = tex


if __name__ == "__main__":
    CameraApp().run()
