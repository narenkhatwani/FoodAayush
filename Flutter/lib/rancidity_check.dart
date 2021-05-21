//The Rancidity of the given oil is checked on this page.
//A hardware device which is integrated to mobile application via bluetooth sends the pH on this page.
//Based on the pH values obtained, the system determines whether the oil is rancid or edible.

import 'dart:async';
import 'package:flutter/material.dart';
// ignore: import_of_legacy_library_into_null_safe
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';

import 'DiscoveryPage.dart';
import 'SelectBondedDevicePage.dart';
import 'Connection.dart';
import 'package:foodaayush/mainnavbar.dart';

class Rancidity extends StatefulWidget {
  @override
  _MainPage createState() => new _MainPage();
}

class _MainPage extends State<Rancidity> {
  BluetoothState _bluetoothState = BluetoothState.UNKNOWN;

  String _address = "...";
  String _name = "...";

  Timer? _discoverableTimeoutTimer;
  int _discoverableTimeoutSecondsLeft = 0;

  //BackgroundCollectingTask _collectingTask;

  bool _autoAcceptPairingRequests = false;

  @override
  void initState() {
    super.initState();

    // Get current state
    FlutterBluetoothSerial.instance.state.then((state) {
      setState(() {
        _bluetoothState = state;
      });
    });

    Future.doWhile(() async {
      // Wait if adapter not enabled
      if (await FlutterBluetoothSerial.instance.isEnabled) {
        return false;
      }
      await Future.delayed(Duration(milliseconds: 0xDD));
      return true;
    }).then((_) {
      // Update the address field
      FlutterBluetoothSerial.instance.address.then((address) {
        setState(() {
          _address = address;
        });
      });
    });

    FlutterBluetoothSerial.instance.name.then((name) {
      setState(() {
        _name = name;
      });
    });

    // Listen for futher state changes
    FlutterBluetoothSerial.instance
        .onStateChanged()
        .listen((BluetoothState state) {
      setState(() {
        _bluetoothState = state;

        // Discoverable mode is disabled when Bluetooth gets disabled
        _discoverableTimeoutTimer = null;
        _discoverableTimeoutSecondsLeft = 0;
      });
    });
  }

  // @override
  // void dispose() {
  //   FlutterBluetoothSerial.instance.setPairingRequestHandler(null);
  //   _collectingTask?.dispose();
  //   _discoverableTimeoutTimer?.cancel();
  //   super.dispose();
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xffF7DC6F),
      appBar: AppBar(
        iconTheme: IconThemeData(color: Color(0xffF7DC6F)),
        backgroundColor: Color(0xff196F3D),
        title: const Text('Bluetooth Connection',
            style: TextStyle(
                fontFamily: 'Comfortaa',
                color: Color(0xffF7DC6F),
                fontSize: 30.0)),
      ),
      body: Container(
        child: ListView(
          children: <Widget>[
            Divider(),
            SwitchListTile(
              title: const Text('Enable Bluetooth',
                  style: TextStyle(
                    color: Color(0xff196F3D),
                    fontFamily: 'Comfortaa',
                    fontSize: 15.0,
                  )),
              value: _bluetoothState.isEnabled,
              onChanged: (bool value) {
                // Do the request and update with the true value then
                future() async {
                  // async lambda seems to not working
                  if (value)
                    await FlutterBluetoothSerial.instance.requestEnable();
                  else
                    await FlutterBluetoothSerial.instance.requestDisable();
                }

                future().then((_) {
                  setState(() {});
                });
              },
            ),
            ListTile(
              title: const Text('Bluetooth status',
                  style: TextStyle(
                    color: Color(0xff196F3D),
                    fontFamily: 'Comfortaa',
                    fontSize: 15.0,
                  )),
              subtitle: Text(_bluetoothState.toString()),
              trailing: FlatButton(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(5.0),
                    side: BorderSide(color: Color(0xffF7DC6F))),
                color: Color(0xff196F3D),
                textColor: Color(0xffF7DC6F),
                padding: EdgeInsets.all(8.0),
                child: const Text(
                  'Settings',
                  style: TextStyle(
                    //color: Color(0xff196F3D),
                    fontFamily: 'Comfortaa',
                    fontSize: 15.0,
                  ),
                ),
                onPressed: () {
                  FlutterBluetoothSerial.instance.openSettings();
                },
              ),
            ),
            ListTile(
              title: FlatButton(
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(5.0),
                      side: BorderSide(color: Color(0xffF7DC6F))),
                  color: Color(0xff196F3D),
                  textColor: Color(0xffF7DC6F),
                  padding: EdgeInsets.all(8.0),
                  child: const Text(
                    'Explore discovered devices',
                    style: TextStyle(
                      //color: Color(0xff196F3D),
                      fontFamily: 'Comfortaa',
                      fontSize: 15.0,
                    ),
                  ),
                  onPressed: () async {
                    final BluetoothDevice selectedDevice =
                        await Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) {
                          return DiscoveryPage();
                        },
                      ),
                    );

                    if (selectedDevice != null) {
                      print('Discovery -> selected ' + selectedDevice.address);
                    } else {
                      print('Discovery -> no device selected');
                    }
                  }),
            ),
            ListTile(
              title: FlatButton(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(5.0),
                    side: BorderSide(color: Color(0xffF7DC6F))),
                color: Color(0xff196F3D),
                textColor: Color(0xffF7DC6F),
                padding: EdgeInsets.all(8.0),
                child: const Text(
                  'Connect to Device',
                  style: TextStyle(
                    //color: Color(0xff196F3D),
                    fontFamily: 'Comfortaa',
                    fontSize: 15.0,
                  ),
                ),
                onPressed: () async {
                  final BluetoothDevice selectedDevice =
                      await Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (context) {
                        return SelectBondedDevicePage(checkAvailability: false);
                      },
                    ),
                  );

                  if (selectedDevice != null) {
                    print('Connect -> selected ' + selectedDevice.address);
                    _startChat(context, selectedDevice);
                  } else {
                    print('Connect -> no device selected');
                  }
                },
              ),
            ),
          ],
        ),
      ),
      drawer: MainNavbar(),
    );
  }

  void _startChat(BuildContext context, BluetoothDevice server) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) {
          return ConnectPage(server: server);
        },
      ),
    );
  }
}
