import 'package:flutter/material.dart';
import 'package:foodaayush/faq.dart';
import 'package:foodaayush/mainnavbar.dart';

class AboutUs extends StatefulWidget {
  @override
  _AboutUsState createState() => _AboutUsState();
}

class _AboutUsState extends State<AboutUs> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        iconTheme: IconThemeData(color: Color(0xffF7DC6F)),
        backgroundColor: Color(0xff196F3D),
        title: Text(
          'About Us 📝',
          style: TextStyle(
            fontSize: 35.0,
            fontFamily: "Comfortaa",
            color: Color(0xffF7DC6F),
          ),
        ),
      ),
      backgroundColor: Color(0xffF7DC6F),
      body: Column(
        children: <Widget>[
          Container(
            child: Center(
              child: Column(
                children: <Widget>[
                  Text(
                    "RARRN Developers",
                    style: TextStyle(
                      fontFamily: "Comfortaa",
                      fontSize: 22.0,
                      color: Color(0xff196F3D),
                    ),
                  ),
                  Text(
                    "VESIT,Chembur",
                    style: TextStyle(
                      fontFamily: "Comfortaa",
                      fontSize: 22.0,
                      color: Color(0xff196F3D),
                    ),
                  ),
                  Text("Mumbai",
                      style: TextStyle(
                        fontFamily: "Comfortaa",
                        fontSize: 22.0,
                        color: Color(0xff196F3D),
                      )),
                  Text(
                    "Maharashtra-400074",
                    style: TextStyle(
                      fontFamily: "Comfortaa",
                      fontSize: 22.0,
                      color: Color(0xff196F3D),
                    ),
                  ),
                  Text(
                    "For more details contact:",
                    style: TextStyle(
                      fontFamily: "Comfortaa",
                      fontSize: 22.0,
                      color: Color(0xff196F3D),
                    ),
                  ),
                  Text(
                    "rarrnfoodaayush@gmail.com",
                    style: TextStyle(
                      fontFamily: "Comfortaa",
                      fontSize: 22.0,
                      color: Color(0xff196F3D),
                    ),
                  ),
                  Text(
                    "Phone no.: +91 98349 86090",
                    style: TextStyle(
                      fontFamily: "Comfortaa",
                      fontSize: 22.0,
                      color: Color(0xff196F3D),
                    ),
                  ),
                  Text(
                    "Fax: 01234523730",
                    style: TextStyle(
                      fontFamily: "Comfortaa",
                      fontSize: 22.0,
                      color: Color(0xff196F3D),
                    ),
                  ),
                ],
              ),
            ),
            decoration: BoxDecoration(
              border: Border.all(
                width: 2,
              ),
            ),
            padding: EdgeInsets.all(20.0),
            margin: EdgeInsets.fromLTRB(25.0, 70.0, 25.0, 70.0),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: MaterialButton(
              onPressed: () {},
              color: Color(0xff196F3D),
              splashColor: Color(0xff58D68D),
              height: 60,
              minWidth: 250,
              child: Text(
                'Customer Care 🙋‍♂️',
                style: TextStyle(
                  fontFamily: 'Comfortaa',
                  color: Color(0xffF7DC6F),
                  fontSize: 27.0,
                ),
              ),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(9.0),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: MaterialButton(
              onPressed: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => FAQ(),
                    ));
              },
              color: Color(0xff196F3D),
              height: 60,
              minWidth: 250,
              splashColor: Color(0xff58D68D),
              child: Text(
                "F.A.Q 🤔",
                style: TextStyle(
                  fontFamily: 'Comfortaa',
                  color: Color(0xffF7DC6F),
                  fontSize: 27.0,
                ),
              ),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(9.0),
              ),
            ),
          ),
        ],
      ),
      drawer: MainNavbar(),
    );
  }
}
