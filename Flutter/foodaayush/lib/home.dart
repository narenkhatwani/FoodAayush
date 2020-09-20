import 'package:camera/camera.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:foodaayush/fresh.dart';

class HomeClass extends StatefulWidget {
  const HomeClass({Key key, this.user}) : super(key: key);
  final FirebaseUser user;
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<HomeClass> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          backgroundColor: Colors.black,
          title: Text(
            'Menu',
            style: TextStyle(
                fontFamily: 'Comfortaa', color: Colors.white, fontSize: 30.0),
          ),
        ),
        body: Container(
            child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            RaisedButton(
              onPressed: fcam,
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(5.0),
                  side: BorderSide(color: Colors.white)),
              color: Colors.black,
              textColor: Colors.white,
              padding: EdgeInsets.all(12.0),
              child: Text('Identify The Freshness',
                  style: TextStyle(fontFamily: 'Comfortaa')),
            ),
            SizedBox(
              height: 100.0,
            ),
            RaisedButton(
              onPressed: () {},
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(5.0),
                  side: BorderSide(color: Colors.white)),
              color: Colors.black,
              textColor: Colors.white,
              padding: EdgeInsets.all(12.0),
              child: Text('Custom Dish Recipe',
                  style: TextStyle(fontFamily: 'Comfortaa')),
            ),
            SizedBox(
              height: 100.0,
            ),
            RaisedButton(
              onPressed: () {},
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(5.0),
                  side: BorderSide(color: Colors.white)),
              color: Colors.black,
              textColor: Colors.white,
              padding: EdgeInsets.all(12.0),
              child: Text('Rancidity of oil',
                  style: TextStyle(fontFamily: 'Comfortaa')),
            ),
            SizedBox(
              height: 100.0,
            ),
            RaisedButton(
              onPressed: () {},
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(5.0),
                  side: BorderSide(color: Colors.white)),
              color: Colors.black,
              textColor: Colors.white,
              padding: EdgeInsets.all(12.0),
              child: Text('Nutrional Value of the Item',
                  style: TextStyle(fontFamily: 'Comfortaa')),
            )
          ],
        )));
  }

  Future<void> fcam() async {
    final cameras = await availableCameras();
    //Navigator.pushReplacementNamed(context, '/screen5');
    Navigator.pushReplacement(
        context,
        MaterialPageRoute(
            builder: (BuildContext context) => Freshcam(
                  camera: cameras.first,
                )));
  }
}
