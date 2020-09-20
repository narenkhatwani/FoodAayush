import 'package:flutter/material.dart';

class MyTitlePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var assetsImage = new AssetImage('assets/Opening.JPG');
    var image = new Image(
      image: assetsImage,
      fit: BoxFit.fitWidth,
      height: 500.0,
    );
    return Container(
      child: image,
    );
  }
}
