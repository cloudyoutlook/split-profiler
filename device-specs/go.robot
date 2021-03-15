
*** Settings ***

*** Variables ***

*** Test Cases ***
Install Chrome
   Run shell

*** Keywords ***
Run adb shell




   dumpsys package com.android.vending | grep versionName
   getprop ro.build.version.sdk
   getprop ro.build.version.sdk
   getprop ro.product.device
   getprop ro.hardware
   getprop ro.build.product
   getprop ro.build.id
   getprop ro.build.type


pm list features && \
dumpsys display | grep mBaseDisplayInfo && \
wm size && \
wm density && \
getprop | grep density && \
getprop persist.sys.locale && \
dumpsys SurfaceFlinger |grep GLES && \
dumpsys SurfaceFlinger |grep ^GL