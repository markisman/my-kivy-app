[app]
title = CameraApp
package.name = cameraapp
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg

version = 0.1

requirements = python3,kivy,opencv-python,numpy

orientation = portrait
fullscreen = 1

android.permissions = CAMERA
android.api = 33
android.minapi = 21

# خیلی مهم
android.skip_update = True
android.accept_sdk_license = True

# ANT رو کامل غیرفعال می‌کنیم
android.ant_path =
android.use_androidx = True

log_level = 2
