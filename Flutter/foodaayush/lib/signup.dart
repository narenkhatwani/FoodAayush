import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class Registerpage extends StatefulWidget {
  @override
  _RegisterState createState() => _RegisterState();
}

String _email, _pwd;
final GlobalKey<FormState> _formkey = GlobalKey<FormState>();

class _RegisterState extends State<Registerpage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.black,
        elevation: 0.0,
        title: Text('Register',
            style: TextStyle(
                fontFamily: 'Comfortaa', color: Colors.white, fontSize: 30.0)),
      ),
      body: Form(
          key: _formkey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              TextFormField(
                validator: (input) {
                  if (input.isEmpty) {
                    return 'Please Enter your Email';
                  }
                },
                onSaved: (input) => _email = input,
                decoration: InputDecoration(labelText: 'Email'),
              ),
              SizedBox(
                height: 25.0,
              ),
              TextFormField(
                validator: (input) {
                  if (input.length < 8) {
                    return 'Please Enter password with length of atleast 8 characters';
                  }
                },
                onSaved: (input) => _pwd = input,
                decoration: InputDecoration(labelText: 'Password'),
                obscureText: true,
              ),
              SizedBox(
                height: 25.0,
              ),
              RaisedButton(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(5.0),
                    side: BorderSide(color: Colors.white)),
                color: Colors.black,
                textColor: Colors.white,
                padding: EdgeInsets.all(8.0),
                onPressed: signUp,
                child: Text(
                  'Register',
                  style: TextStyle(fontFamily: 'Comfortaa'),
                ),
              ),
            ],
          )),
      // body: Container(
      //   child: Center(
      //     child: Text('Hello'),
      //   ),
      // ),
    );
  }

  Future<void> signUp() async {
    final FormState = _formkey.currentState;
    if (FormState.validate()) {
      FormState.save();
      try {
        FirebaseUser user = (await FirebaseAuth.instance
                .createUserWithEmailAndPassword(email: _email, password: _pwd))
            .user;
        user.sendEmailVerification();
        Navigator.pushReplacementNamed(context, '/screen2');
      } catch (e) {
        print(e.message);
      }
    }
  }
}
