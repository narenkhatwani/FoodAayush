import 'package:flutter/material.dart';
//import 'addindividualingredients.dart';

class MainNutriScreen extends StatefulWidget {
  @override
  _MainNutriScreenState createState() => _MainNutriScreenState();
}

class _MainNutriScreenState extends State<MainNutriScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xffF7DC6F),
      appBar: AppBar(
        backgroundColor: Color(0xff196F3D),
        title: Text(
          "Nutritional Value",
          style: TextStyle(
            fontSize: 30.0,
            fontFamily: "Comfortaa",
            color: Color(0xffF7DC6F),
          ),
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            RaisedButton(
              color: Color(0xff196F3D),
              onPressed: () {},
              child: Text(
                "Capture Image of Dish",
                style: TextStyle(
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              padding: EdgeInsets.all(8.0),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(5.0),
              ),
            ),
            RaisedButton(
              color: Color(0xff196F3D),
              onPressed: () {
                Navigator.pushNamed(context, '/screen6');
              },
              padding: EdgeInsets.all(8.0),
              child: Text(
                "Add Individual Ingredients",
                style: TextStyle(
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(5.0),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
