import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter_auths/controllers/authentications.dart';
import 'package:flutter_auths/main.dart';

class TasksPage extends StatefulWidget {
  final String uid;

  TasksPage({Key key, @required this.uid}) : super(key: key);

  @override
  _TasksPageState createState() => _TasksPageState(uid);
}

class _TasksPageState extends State<TasksPage> {
  final String uid;
  _TasksPageState(this.uid);

  var taskcollections = Firestore.instance.collection('tasks');
  String task;

  void showdialog(bool isUpdate, DocumentSnapshot ds) {
    GlobalKey<FormState> formkey = GlobalKey<FormState>();

    showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: isUpdate ? Text("Update Todo") : Text("Add Todo"),
            content: Form(
              key: formkey,
              autovalidate: true,
              child: TextFormField(
                autofocus: true,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: "Task",
                ),
                validator: (_val) {
                  if (_val.isEmpty) {
                    return "Can't Be Empty";
                  } else {
                    return null;
                  }
                },
                onChanged: (_val) {
                  task = _val;
                },
              ),
            ),
            actions: <Widget>[
              RaisedButton(
                color: Colors.purple,
                onPressed: () {
                  if (formkey.currentState.validate()) {
                    formkey.currentState.save();
                    if (isUpdate) {
                      taskcollections
                          .document(uid)
                          .collection('task')
                          .document(ds.documentID)
                          .updateData({
                        'task': task,
                        'time': DateTime.now(),
                      });
                    } else {
                      //  insert
                      taskcollections.document(uid).collection('task').add({
                        'task': task,
                        'time': DateTime.now(),
                      });
                    }
                    Navigator.pop(context);
                  }
                },
                child: Text(
                  "Add",
                  style: TextStyle(
                    fontFamily: "tepeno",
                    color: Colors.white,
                  ),
                ),
              ),
            ],
          );
        });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () => showdialog(false, null),
        child: Icon(Icons.add),
      ),
      appBar: AppBar(
        title: Text(
          "Tasks",
          style: TextStyle(
            fontFamily: "tepeno",
            fontWeight: FontWeight.w600,
          ),
        ),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.exit_to_app),
            splashColor: Colors.transparent,
            highlightColor: Colors.transparent,
            onPressed: () => signOutUser().then((value) {
              Navigator.of(context).pushAndRemoveUntil(
                  MaterialPageRoute(builder: (context) => HomePage()),
                  (Route<dynamic> route) => false);
            }),
          ),
        ],
      ),
      body: StreamBuilder<QuerySnapshot>(
        stream: taskcollections
            .document(uid)
            .collection('task')
            .orderBy('time')
            .snapshots(),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data.documents.length,
              itemBuilder: (context, index) {
                DocumentSnapshot ds = snapshot.data.documents[index];
                return Container(
                  decoration: BoxDecoration(
                    color: Colors.purple,
                    borderRadius: BorderRadius.circular(5.0),
                  ),
                  margin: EdgeInsets.all(8.0),
                  child: ListTile(
                    title: Text(
                      ds['task'],
                      style: TextStyle(
                        fontFamily: "tepeno",
                        fontSize: 18.0,
                        color: Colors.white,
                      ),
                    ),
                    onLongPress: () {
                      // delete
                      taskcollections
                          .document(uid)
                          .collection('task')
                          .document(ds.documentID)
                          .delete();
                    },
                    onTap: () {
                      // == Update
                      showdialog(true, ds);
                    },
                  ),
                );
              },
            );
          } else if (snapshot.hasError) {
            return CircularProgressIndicator();
          } else {
            return CircularProgressIndicator();
          }
        },
      ),
    );
  }
}
