[app]
title = CameraDepth
package.name = cameradepth
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy,numpy,opencv

orientation = portrait

android.permissions = CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b

fullscreen = 0
