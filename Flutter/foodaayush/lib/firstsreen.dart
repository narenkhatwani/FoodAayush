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
      backgroundColor: Colors.white,
      body: Container(
        alignment: Alignment.center,
        child: new Column(
          children: [
            new Container(
              alignment: Alignment(0.0, 0.0),
              height: 700,
              child: new Text(
                'Food Aayush',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 60, fontFamily: 'Comfortaa'),
              ),
            ),
          ],

          //child: Image.asset('assets/Opening.JPG'),

          //child: Text('This Works'),
        ),
      ),
    );
  }
}
