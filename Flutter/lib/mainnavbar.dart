//Here, the navigation bar for the application has been designed.
//It is a side navigation bar, which is called as a drawer menu or a navigation drawer in Flutter.
//It is created using the Drawer widget.
//Then a ListView widget is used to add create a list of items in the navigation drawer.
//Each item in the navigation drawer is created using a ListTile widget.
//The dart files for all screens have to be imported into this dart file, so that all screens can be accessed from the navigation bar.
//Also, the dart file for the navigation bar has been imported into every other dart file, in order for the navigation bar to be accessible from each screen.
//A separate MaterialPageRoute is used to navigate to each screen from the navigation bar.
//This MaterialPageRoute has to be added in the OnTap attribute of the ListTile widget for navigation to a particular screen along with the path to the desired screen.
//Additionally, one of the ListTile widgets in the navigation drawer is used along with the url_launcher package to link the Flutter app to the Streamlit web app.
//The URL of the Streamlit web app is given.
//The url_launcher dependency has to be added to the pubspec.yaml file and the package needs to be imported.

//Import dart files for all screens
import 'package:flutter/material.dart';
import 'package:foodaayush/classify.dart';
import 'package:foodaayush/faq.dart';
import 'package:foodaayush/aboutus.dart';
import 'package:foodaayush/rancidity_check.dart';
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
            //Each ListTile widget creates one item in the navigation drawer
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
