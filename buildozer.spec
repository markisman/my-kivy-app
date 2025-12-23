[app]
title = CameraApp
package.name = cameraapp
package.domain = org.test

source.dir = .
source.include_exts = py

version = 0.1

requirements = python3,kivy,opencv,numpy

orientation = portrait
fullscreen = 1

android.permissions = CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b


android.skip_update = True

[buildozer]
log_level = 2
warn_on_root = 1
