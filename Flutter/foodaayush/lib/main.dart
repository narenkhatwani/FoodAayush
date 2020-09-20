import 'dart:io';

import 'package:camera/new/src/support_android/camera.dart';
import 'package:flutter/material.dart';
import 'package:foodaayush/firstsreen.dart';
import 'package:foodaayush/fresh.dart';
import 'package:foodaayush/home.dart';
import 'package:foodaayush/signup.dart';

import 'login.dart';
//import 'widgets.dart';
import 'package:camera/camera.dart';

Future<Null> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final cameras = await availableCameras();
  final firstCamera = cameras.first;
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
  //  const MyClass({
  //    Key key,
  //    @required this.camera,
  //  }) : super(key: key);

  //final firstCam = cameras.first;
  // final CameraDescription camera;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        routes: <String, WidgetBuilder>{
          // ignore: non_constant_identifier_names
          '/screen1': (BuildContext context) => new Welcomescreen(),
          '/screen2': (BuildContext context) => new LoginClass(),
          '/screen3': (BuildContext context) => new HomeClass(),
          '/screen4': (BuildContext context) => new Registerpage(),
          // "/screen5": (BuildContext context) =>
          //     new Freshcam(camera: cameras.first)
        },
        title: "Food Aayush",
        home: Welcomescreen()
        //Scaffold(
        // appBar: AppBar(
        //   title: Text('Welcome to Food Aayush'),
        //   backgroundColor: Colors.black,
        //   elevation: 10.0,
        // ),

        );
  }
}
