import cv2
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.graphics.texture import Texture


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.camera = Camera(play=True, resolution=(640, 480), index=0)
        self.img = Image()

        layout.add_widget(self.camera)
        layout.add_widget(self.img)

        Clock.schedule_interval(self.update, 1 / 15)
        return layout

    def update(self, dt):
        if not self.camera.texture:
            return

        texture = self.camera.texture
        w, h = texture.size

        frame = np.frombuffer(texture.pixels, dtype=np.uint8)
        frame = frame.reshape(h, w, 4)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (15, 15), 0)

        depth = np.zeros_like(blur)
        depth[blur < 100] = 255

        rgb = cv2.cvtColor(depth, cv2.COLOR_GRAY2RGB)

        tex = Texture.create(size=(w, h), colorfmt="rgb")
        tex.blit_buffer(rgb.tobytes(), colorfmt="rgb", bufferfmt="ubyte")
        tex.flip_vertical()

        self.img.texture = tex


if __name__ == "__main__":
    CameraApp().run()
