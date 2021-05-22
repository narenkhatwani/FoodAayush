// ignore: unused_import
import 'dart:async';
// ignore: unused_import
import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';
// ignore: import_of_legacy_library_into_null_safe
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';

class ConnectPage extends StatefulWidget {
  final BluetoothDevice? server;

  const ConnectPage({this.server});
  @override
  _ConnectPageState createState() => _ConnectPageState();
}

class _Message {
  int whom;
  String text;

  _Message(this.whom, this.text);
}

class _ConnectPageState extends State<ConnectPage> {
  // ignore: unused_field
  static final clientID = 0;
  BluetoothConnection? connection;

  List<_Message> messages = [];
  String _messageBuffer = '';

  final TextEditingController textEditingController =
      new TextEditingController();
  final ScrollController listScrollController = new ScrollController();

  bool isConnecting = true;
  bool get isConnected => connection != null && connection!.isConnected;

  bool isDisconnecting = false;

  var myDouble;

  @override
  void initState() {
    super.initState();

    BluetoothConnection.toAddress(widget.server!.address).then((_connection) {
      print('Connected to the device');
      connection = _connection;
      setState(() {
        isConnecting = false;
        isDisconnecting = false;
      });
      connection!.input.listen(_onDataReceived).onDone(() {
        // Example: Detect which side closed the connection
        // There should be `isDisconnecting` flag to show are we are (locally)
        // in middle of disconnecting process, should be set before calling
        // `dispose`, `finish` or `close`, which all causes to disconnect.
        // If we except the disconnection, `onDone` should be fired as result.
        // If we didn't except this (no flag set), it means closing by remote.
        if (isDisconnecting) {
          print('Disconnecting locally!');
        } else {
          print('Disconnected remotely!');
        }
        if (this.mounted) {
          setState(() {});
        }
      });
    }).catchError((error) {
      print('Cannot connect, exception occured');
      print(error);
    });
  }

  @override
  void dispose() {
    // Avoid memory leak (`setState` after dispose) and disconnect
    if (isConnected) {
      isDisconnecting = true;
      connection!.dispose();
      connection = null;
    }

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    messages.add(_Message(0, '0.0'));
    myDouble = double.parse(messages[0].text.toString().trim());
    return Scaffold(
      backgroundColor: Color(0xffF7DC6F),
      appBar: AppBar(
          iconTheme: IconThemeData(color: Color(0xffF7DC6F)),
          backgroundColor: Color(0xff196F3D),
          title: (isConnecting
              ? Text('Connecting to ' + widget.server!.name + '...',
                  style: TextStyle(
                      fontFamily: 'Comfortaa',
                      color: Color(0xffF7DC6F),
                      fontSize: 25.0))
              : isConnected
                  ? Text('Connected to ' + widget.server!.name,
                      style: TextStyle(
                          fontFamily: 'Comfortaa',
                          color: Color(0xffF7DC6F),
                          fontSize: 30.0))
                  : Text('Logs ' + widget.server!.name,
                      style: TextStyle(
                          fontFamily: 'Comfortaa',
                          color: Color(0xffF7DC6F),
                          fontSize: 30.0)))),
      body: Container(
        margin: EdgeInsets.all(20),
        width: MediaQuery.of(context).size.width,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              child: Text(
                'The pH of the Oil is:',
                style: TextStyle(
                  color: Color(0xff196F3D),
                  fontSize: 40.0,
                  fontFamily: 'Comfortaa',
                ),
              ),
            ),
            SizedBox(
              height: 10,
            ),
            Container(
              child: Text(
                messages[0].text.toString().trim(),
                style: TextStyle(
                    color: Color(0xff196F3D),
                    fontSize: 80.0,
                    letterSpacing: -5),
              ),
            ),
            SizedBox(
              height: 10,
            ),
            myDouble < 1.0 || myDouble > 13.00
                ? Container(
                    child: Text(
                      'Invalid Values',
                      style: TextStyle(
                        color: Colors.red,
                        fontSize: 40.0,
                        fontFamily: 'Comfortaa',
                      ),
                    ),
                  )
                : myDouble < 6.50
                    ? Container(
                        child: Text(
                          'Rancid',
                          style: TextStyle(
                            color: Colors.red,
                            fontSize: 40.0,
                            fontFamily: 'Comfortaa',
                          ),
                        ),
                      )
                    : Container(
                        child: Text(
                          'Edible',
                          style: TextStyle(
                            color: Colors.green,
                            fontSize: 40.0,
                            fontFamily: 'Comfortaa',
                          ),
                        ),
                      )
          ],
        ),
      ),
    );
  }

  void _onDataReceived(Uint8List data) {
    // Allocate buffer for parsed data
    int backspacesCounter = 0;
    data.forEach((byte) {
      if (byte == 8 || byte == 127) {
        backspacesCounter++;
      }
    });
    Uint8List buffer = Uint8List(data.length - backspacesCounter);
    int bufferIndex = buffer.length;

    // Apply backspace control character
    backspacesCounter = 0;
    for (int i = data.length - 1; i >= 0; i--) {
      if (data[i] == 8 || data[i] == 127) {
        backspacesCounter++;
      } else {
        if (backspacesCounter > 0) {
          backspacesCounter--;
        } else {
          buffer[--bufferIndex] = data[i];
        }
      }
    }
    // Create message if there is new line character
    String dataString = String.fromCharCodes(buffer);
    int index = buffer.indexOf(13);
    if (~index != 0) {
      setState(() {
        messages.insert(
          0,
          _Message(
            1,
            backspacesCounter > 0
                ? _messageBuffer.substring(
                    0, _messageBuffer.length - backspacesCounter)
                : _messageBuffer + dataString.substring(0, index),
          ),
        );
        _messageBuffer = dataString.substring(index);
      });
    } else {
      _messageBuffer = (backspacesCounter > 0
          ? _messageBuffer.substring(
              0, _messageBuffer.length - backspacesCounter)
          : _messageBuffer + dataString);
    }
  }
}
