[app]
title = Health App
package.name = healthapp
package.domain = org.health
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3==3.8.5, kivy==2.0.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 28
android.minapi = 21

[buildozer]
log_level = 2
