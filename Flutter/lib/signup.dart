//The new users of the application first need to sign up.
//This page allows the new users to sign up by entering their Email ID and creating a password.
//The Form widget is used to create this page.
//The Email and Password fields are created by using the TextFormField widget inside the Form widget.
//There is also a Confirm Password Field, also created using the TextFormField widget.
//Form validation is added, in order to make sure that all information is entered correctly by the user.
//After successfully signing up, the user will be directed to the login page.

import 'package:firebase_auth/firebase_auth.dart';
//import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

class Registerpage extends StatefulWidget {
  @override
  _RegisterState createState() => _RegisterState();
}

String? _email, _pwd;
final GlobalKey<FormState> _formkey = GlobalKey<FormState>();

class _RegisterState extends State<Registerpage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xffF7DC6F),
      appBar: AppBar(
        iconTheme: IconThemeData(color: Color(0xffF7DC6F)),
        backgroundColor: Color(0xff196F3D),
        elevation: 0.0,
        title: Text('Register',
            style: TextStyle(
                fontFamily: 'Comfortaa',
                color: Color(0xffF7DC6F),
                fontSize: 30.0)),
      ),
      body: Form(
          key: _formkey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            // crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              TextFormField(
                validator: (input) {
                  if (input!.isEmpty) {
                    return 'Please Enter your Email';
                  }
                },
                onSaved: (input) => _email = input!,
                style: TextStyle(color: Color(0xff196F3D)),
                decoration: InputDecoration(labelText: 'Email'),
              ),
              SizedBox(
                height: 25.0,
              ),
              TextFormField(
                validator: (input) {
                  if (input!.length < 8) {
                    return 'Please Enter password with length of atleast 8 characters';
                  }
                },
                onSaved: (input) => _pwd = input!,
                style: TextStyle(color: Color(0xff196F3D)),
                decoration: InputDecoration(labelText: 'Password'),
                obscureText: true,
              ),
              SizedBox(
                height: 25.0,
              ),
              RaisedButton(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(5.0),
                    side: BorderSide(color: Color(0xffF7DC6F))),
                color: Color(0xff196F3D),
                textColor: Color(0xffF7DC6F),
                padding: EdgeInsets.all(8.0),
                onPressed: signUp,
                child: Text(
                  'Register',
                  style: TextStyle(fontFamily: 'Comfortaa'),
                ),
              ),
            ],
          )),
    );
  }

  Future<void> signUp() async {
    final FormState = _formkey.currentState;
    if (FormState!.validate()) {
      FormState.save();
      try {
        final User user = (await FirebaseAuth.instance
                .createUserWithEmailAndPassword(
                    email: _email!, password: _pwd!))
            .user!;
        user.sendEmailVerification();
        Navigator.pushReplacementNamed(context, '/screen2');
      } catch (e) {
        print(e);
      }
    }
  }
}
