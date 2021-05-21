//Import dart files for all screens
import 'package:flutter/material.dart';
import 'package:foodaayush/classify.dart';
import 'package:foodaayush/faq.dart';
import 'package:foodaayush/aboutus.dart';
//import 'package:foodaayush/home.dart';
//import 'package:foodaayush/main.dart';
import 'package:foodaayush/rancidity_check.dart';
//import 'package:foodaayush/mainnutriscreen.dart';
import 'package:url_launcher/url_launcher.dart';

class MainNavbar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //Create navigation drawer
    return Drawer(
      child: Container(
        color: Color(0xff196F3D),
        child: ListView(
          // Important: Remove any padding from the ListView.
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              child: Text(
                'Food\nAayush 🍱',
                style: TextStyle(
                  fontSize: 50.0,
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              decoration: BoxDecoration(
                color: Color(0xff196F3D),
              ),
            ),
            ListTile(
              title: Text(
                'Identify the Freshness',
                style: TextStyle(
                  fontSize: 20.0,
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              tileColor: Color(0xff196F3D),
              hoverColor: Color(0xff58D68D),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => Classifier(),
                  ),
                );
              },
            ),
            ListTile(
              title: Text(
                'Nutritional Analysis',
                style: TextStyle(
                  fontSize: 20.0,
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              tileColor: Color(0xff196F3D),
              hoverColor: Color(0xff58D68D),
              onTap: _launchURL,
            ),
            ListTile(
              title: Text(
                'Rancidity of Oil',
                style: TextStyle(
                  fontSize: 20.0,
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              tileColor: Color(0xff196F3D),
              hoverColor: Color(0xff58D68D),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => Rancidity(),
                  ),
                );
              },
            ),
            ListTile(
              title: Text(
                'About Us',
                style: TextStyle(
                  fontSize: 20.0,
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              tileColor: Color(0xff196F3D),
              hoverColor: Color(0xff58D68D),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer

                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => AboutUs(),
                  ),
                );
              },
            ),
            ListTile(
              title: Text(
                'Customer Care',
                style: TextStyle(
                  fontSize: 20.0,
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              tileColor: Color(0xff196F3D),
              hoverColor: Color(0xff58D68D),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: Text(
                'Frequently Asked Questions',
                style: TextStyle(
                  fontSize: 20.0,
                  fontFamily: "Comfortaa",
                  color: Color(0xffF7DC6F),
                ),
              ),
              tileColor: Color(0xff196F3D),
              hoverColor: Color(0xff58D68D),
              onTap: () {
                // Update the state of the app
                // ...
                // Then close the drawer

                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => FAQ(),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}

_launchURL() async {
  const url = 'https://food-aayush.herokuapp.com/';
  if (await canLaunch(url)) {
    await launch(url);
  } else {
    throw 'Could not launch $url';
  }
}
