import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';

class LoginClass extends StatefulWidget {
  @override
  // ignore: missing_return
  State<StatefulWidget> createState() {
    return _LoginClass();
  }
}

class _LoginClass extends State<LoginClass> {
  String _email, _pwd;
  final GlobalKey<FormState> _formkey = GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.black,
        elevation: 0.0,
        title: Text('Login',
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
                    return 'Please Enter correct Password';
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
                onPressed: login,
                child: Text(
                  'Login',
                  style: TextStyle(fontFamily: 'Comfortaa'),
                ),
              ),
              SizedBox(
                height: 25.0,
              ),
              RaisedButton(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(5.0),
                    side: BorderSide(color: Colors.black)),
                color: Colors.white,
                textColor: Colors.black,
                padding: EdgeInsets.all(8.0),
                onPressed: Register,
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

  Future<void> login() async {
    final FormState = _formkey.currentState;
    if (FormState.validate()) {
      FormState.save();
      try {
        FirebaseUser user = (await FirebaseAuth.instance
                .signInWithEmailAndPassword(email: _email, password: _pwd))
            .user;
        Navigator.pushReplacementNamed(context, '/screen3');
      } catch (e) {
        print(e.message);
      }
    }
  }

  void Register() {
    Navigator.pushReplacementNamed(context, '/screen4');
  }
}
