name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build APK
        run: |
          sudo apt update
          sudo apt install -y python3-pip openjdk-8-jdk zip
          pip3 install buildozer
          buildozer init
          echo "[app]
          title = Рассея Мастерская
          package.name = rassea  
          package.domain = org.rassea
          source.dir = .
          source.main = main.py
          version = 1.0.0
          requirements = python3,kivy
          orientation = portrait
          android.arch = arm64-v8a" > buildozer.spec
          buildozer -v android debug
      - name: Upload APK
        uses: actions/upload-artifact@v2
        with:
          name: app-apk
          path: bin/*.apk
