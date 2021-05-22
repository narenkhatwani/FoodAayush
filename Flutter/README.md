# **Flutter UI Documentation**

**APK link:**
https://drive.google.com/file/d/1mkXkOxHaLk23ldas-AEwtkmfEhoEjNUo/view?usp=sharing

### Installation:

We followed the following documentation provided by Flutter for installation of flutter on Windows.

[https://flutter.dev/docs/get-started/install/windows](https://flutter.dev/docs/get-started/install/windows)

**Environment Variable Needed:**

- JAVA_HOME
- Add *C:\src\flutter\bin* in system path variable

After Everything Set up, run 

```bash
flutter doctor
```

Open the folder in VS code and run debugger

Run Debugger won't work

### Null Safety

Dart 2.0 introduced null safety feature. Our code has one package i.e. flutter_bluetooth_serial which doesn't support null safety. As developer of this package didn't update package to support null safety. So to debug this code, we have to use unsound safety. Mixed-version programs can be executed with unsound null safety. [https://dart.dev/null-safety/unsound-null-safety](https://dart.dev/null-safety/unsound-null-safety) 

To run debugger

```bash
flutter run --no-sound-null-safety
```

### To Build APK

```bash
flutter build apk --no-sound-null-safety
```
