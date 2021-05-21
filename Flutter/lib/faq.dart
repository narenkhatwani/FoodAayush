//This is a page that has been added for the users to gain additional information about the app and its developers.
//A simple Container widget has been used to create a box, containing information entered in simple Text widgets.
//These Text widgets are arranged vertically in a column within the Container, by declaring them as the children widgets of a Column widget.
//The page also has two buttons (outside the Container widget), one which redirects the user to the Customer Care page and another which takes the user to the F.A.Qs page.
//The buttons are created using the MaterialButton widget. A splashcolor attribute is also added to the buttons.

import 'package:flutter/material.dart';
import 'package:foodaayush/mainnavbar.dart';

class FAQ extends StatefulWidget {
  @override
  _FAQState createState() => _FAQState();
}

class _FAQState extends State<FAQ> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        iconTheme: IconThemeData(color: Color(0xffF7DC6F)),
        backgroundColor: Color(0xff196F3D),
        title: Text(
          "F.A.Q 🤔",
          style: TextStyle(
            fontSize: 35.0,
            fontFamily: "Comfortaa",
            color: Color(0xffF7DC6F),
          ),
        ),
      ),
      backgroundColor: Color(0xffF7DC6F),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Text(
              "Q. On what parameters is the freshness of food items decided? \n\nA. The freshness of a food item is decided from the photo captured by the camera by analysing the visual properties such as color and texture as well as surface defects.\n\n",
              style: TextStyle(
                fontSize: 23.0,
                fontFamily: "Comfortaa",
                color: Color(0xff196F3D),
              ),
            ),
            Text(
              "Q. Why is it important that the oil is not rancid? \n\nA. Rancid oil not only reduces the quality of food in terms of taste and odour, but can also be harmful to health. Hence it is essential that oil is not rancid.\n\n",
              style: TextStyle(
                fontSize: 23.0,
                fontFamily: "Comfortaa",
                color: Color(0xff196F3D),
              ),
            ),
            Text(
              "Q. Why should some ingredients not be used with certain other ingredients in cooking? \n\nA. Certain ingredients when used in combination reduce each other's nutritional value, e.g. in Palak Paneer, spinach and paneer actually reduce each other's nutritional value. Therefore our app provides a feature where the image of dish can be captured or the ingredients can be added individually and then it is checked whether the combination of ingredients is compatible, by finding the nutritional value of the dish.\n\n",
              style: TextStyle(
                fontSize: 23.0,
                fontFamily: "Comfortaa",
                color: Color(0xff196F3D),
              ),
            ),
            Text(
              "Q. What causes oils to become rancid? \n\nA. Oil becomes rancid when it is exposed to air for a long time, due to the moisture and oxygen in the air. It also becomes rancid on exposure to heat, i.e . when the same oil is used repetitively for cooking. Hence it becomes important to check for rancidity in oil, especially if it is being used repetitively.\n\n",
              style: TextStyle(
                fontSize: 23.0,
                fontFamily: "Comfortaa",
                color: Color(0xff196F3D),
              ),
            ),
            Text(
              "Q. How are pH value and rancidity related? \n\nA. Rancid oils are more acidic. Therefore as rancidity of oil increases, its pH value decreases.\n\n",
              style: TextStyle(
                fontSize: 23.0,
                fontFamily: "Comfortaa",
                color: Color(0xff196F3D),
              ),
            ),
          ],
        ),
      ),
      drawer: MainNavbar(),
    );
  }
}
