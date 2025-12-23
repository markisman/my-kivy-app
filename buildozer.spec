[app]
title = CameraDepth
package.name = cameradepth
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy,opencv,numpy

orientation = portrait
fullscreen = 1

android.permissions = CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b

android.gradle_dependencies =
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 0
