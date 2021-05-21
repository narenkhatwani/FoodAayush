//The login screen for the application has been designed here.
//The labelText attribute has been used in both text fields, which indicates to the user that the text field is for entering the Email ID or the password.
//When the user clicks on a particular text field, e.g. the Email ID field, they are given a hint which instructs them on what to enter in the field.
//This is achieved using the hintText attribute. For security purposes, the password must not be visible while the user types it.
//So, the obscureText attribute is set to true in order for the password to be invisible.
//The Login button is created using a MaterialButton widget.
//After successfully logging in, the user can access the features of the application.

//import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:foodaayush/home.dart';

class LoginClass extends StatefulWidget {
  @override
  // ignore: missing_return
  State<StatefulWidget> createState() {
    return _LoginClass();
  }
}

class _LoginClass extends State<LoginClass> {
  String? _email, _pwd;
  final GlobalKey<FormState> _formkey = GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xffF7DC6F),
      appBar: AppBar(
        backgroundColor: Color(0xff196F3D),
        elevation: 0.0,
        title: Text('Login',
            style: TextStyle(
                fontFamily: 'Comfortaa',
                color: Color(0xffF7DC6F),
                fontSize: 30.0)),
      ),
      body: Form(
          key: _formkey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Padding(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    validator: (input) {
                      if (input!.isEmpty) {
                        return 'Please Enter your Email';
                      }
                    },
                    onSaved: (input) => _email = input!,
                    // style: kLabelStyle,
                    style: TextStyle(color: Color(0xff196F3D)),
                    decoration: InputDecoration(
                        border: OutlineInputBorder(), labelText: 'Email'),
                  )),
              SizedBox(
                height: 10.0,
              ),
              Padding(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    validator: (input) {
                      if (input!.length < 8) {
                        return 'Please Enter correct Password';
                      }
                    },
                    onSaved: (input) => _pwd = input!,
                    // style: kLabelStyle,
                    style: TextStyle(color: Color(0xff196F3D)),
                    decoration: InputDecoration(
                        border: OutlineInputBorder(), labelText: 'Password'),
                    obscureText: true,
                  )),
              SizedBox(
                height: 10.0,
              ),
              Container(
                  height: 50,
                  width: 250,
                  child: FlatButton(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(5.0),
                        side: BorderSide(color: Color(0xffF7DC6F))),
                    color: Color(0xff196F3D),
                    textColor: Color(0xffF7DC6F),
                    padding: EdgeInsets.all(8.0),
                    onPressed: login,
                    child: Text(
                      'Login',
                      style: TextStyle(fontFamily: 'Comfortaa'),
                    ),
                  )),
              SizedBox(
                height: 25.0,
              ),
              GestureDetector(
                onTap: Register,
                child: Text(
                  'New User?  Create an Account',
                  style: TextStyle(
                    color: Color(0xff196F3D),
                    fontFamily: 'Comfortaa',
                    fontSize: 15.0,
                  ),
                ),
              ),
            ],
          )),
    );
  }

  Future<void> login() async {
    final FormState = _formkey.currentState;
    if (FormState!.validate()) {
      FormState.save();
      try {
        final User user = (await FirebaseAuth.instance
                .signInWithEmailAndPassword(email: _email!, password: _pwd!))
            .user!;
        Navigator.pushReplacement(context,
            MaterialPageRoute<Map>(builder: (BuildContext context) {
          return HomeClass(user);
        }));
      } catch (e) {
        print(e);
      }
    }
  }

  void Register() {
    Navigator.pushReplacementNamed(context, '/screen4');
  }
}
