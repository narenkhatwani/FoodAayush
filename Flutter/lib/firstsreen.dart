import 'dart:async';
import 'package:flutter/material.dart';

class Welcomescreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return StartState();
  }
}

class StartState extends State<Welcomescreen> {
  @override
  void initState() {
    super.initState();
    startTimer();
  }

  startTimer() async {
    var duration = Duration(seconds: 4);
    return Timer(duration, route);
  }

  route() {
    Navigator.pushReplacementNamed(context, '/screen2');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xffF7DC6F),
      body: Container(
        alignment: Alignment.center,
        child: new Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            new Center(
              child: new Text(
                'Food Aayush',
                textAlign: TextAlign.center,
                style: TextStyle(
                    fontSize: 60,
                    fontFamily: 'Comfortaa',
                    color: Color(0xff196F3D)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
