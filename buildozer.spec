[app]
title = MyKivyApp
package.name = mykivyapp
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
android.accept_sdk_license = True

android.enable_androidx = True
android.gradle_dependencies = 

android.permissions = INTERNET

android.use_legacy_ant = False
log_level = 2
