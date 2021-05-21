//import 'dart:io';

//import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:foodaayush/aboutus.dart';

import 'package:foodaayush/firstsreen.dart';
import 'package:foodaayush/mainnutriscreen.dart';
import 'package:foodaayush/rancidity_check.dart';
import 'package:foodaayush/signup.dart';

import 'package:foodaayush/classify.dart';
import 'login.dart';

Future<Null> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  future:
  Firebase.initializeApp();
  //final cameras = await availableCameras();
  //final firstCamera = cameras.first;
  runApp(
    MyClass(
        //camera: firstCamera,

        ),
  );
}

// class MyClass extends StatefulWidget {
//   final CameraDescription camera;

//   const MyClass({
//     Key key,
//     @required this.camera,
//   }) : super(key: key);

//   @override
//   State<StatefulWidget> createState() {
//     throw UnimplementedError();
//   }
// }

class MyClass extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        routes: <String, WidgetBuilder>{
          // ignore: non_constant_identifier_names
          '/screen1': (BuildContext context) => new Welcomescreen(),
          '/screen2': (BuildContext context) => new LoginClass(),
          //'/screen3': (BuildContext context) => new HomeClass(user),
          '/screen4': (BuildContext context) => new Registerpage(),
          '/screen5': (BuildContext context) => new MainNutriScreen(),
          '/screen6': (BuildContext context) => new AboutUs(),
          // "/screen5": (BuildContext context) =>
          //     new Freshcam(camera: cameras.first)
          '/screen7': (BuildContext context) => new Classifier(),
          '/screen8': (BuildContext context) => new Rancidity()
        },
        title: "Food Aayush",
        home: Welcomescreen());
  }
}
