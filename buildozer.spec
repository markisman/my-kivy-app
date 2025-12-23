[app]
title = MyApp
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 1

android.api = 33
android.minapi = 21

android.sdk = 33
android.ndk = 25b
android.skip_update = True

[buildozer]
log_level = 2
warn_on_root = 0
