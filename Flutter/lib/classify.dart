//This is the page where image is captured and the InceptionV3 model classifies the food item by identifying which food it is and Into stale or fresh

import 'dart:io';

import 'package:flutter/material.dart';
import 'package:tflite/tflite.dart';
import 'package:image_picker/image_picker.dart';
import 'mainnavbar.dart';

class Classifier extends StatefulWidget {
  //final String imagepath;
  //const Classifier({Key key, @required this.imagepath}) : super(key: key);
  @override
  _ClassifierState createState() => _ClassifierState();
}

class _ClassifierState extends State<Classifier> {
  List? _outputs;
  File? _image;
  bool _loading = false;
  String? ip;
  ImagePicker picker = new ImagePicker();

  @override
  void initState() {
    super.initState();
    _loading = true;
    //ip = widget.imagepath;
    loadModel().then((value) {
      setState(() {
        _loading = false;
      });
    });
  }

  loadModel() async {
    await Tflite.loadModel(
      //model: "assets/model_unquant.tflite",
      //labels: "assets/labels.txt",
      model: "assets/float16_optimised_model_Inceptionv3.tflite",
      labels: "assets/ImageLabels.txt",
      numThreads: 4,
    );
  }

  classifyImage(File image) async {
    var output = await Tflite.runModelOnImage(
        path: image.path,
        imageMean: 0.0,
        imageStd: 255.0,
        numResults: 2,
        threshold: 0.2,
        asynch: true);
    setState(() {
      _loading = false;
      _outputs = output;
    });
  }

  @override
  void dispose() {
    Tflite.close();
    super.dispose();
  }

  pickImage() async {
    // ignore: deprecated_member_use
    final image = await picker.getImage(source: ImageSource.camera);
    if (image == null) return null;
    setState(() {
      _loading = true;
      _image = File(image.path);
    });
    classifyImage(File(image.path));
  }

  galleryImage() async {
    // ignore: deprecated_member_use
    final image = await picker.getImage(source: ImageSource.gallery);
    if (image == null) return null;
    setState(() {
      _loading = true;
      _image = File(image.path);
    });
    classifyImage(File(image.path));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          iconTheme: IconThemeData(color: Color(0xffF7DC6F)),
          backgroundColor: Color(0xff196F3D),
          title: Text(
            'Freshness Detection',
            style: TextStyle(
                fontFamily: 'Comfortaa',
                color: Color(0xffF7DC6F),
                fontSize: 30.0),
          )),
      body: Container(
        color: Color(0xffF7DC6F),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _loading
                ? Container(
                    height: 300,
                    width: 300,
                  )
                : Container(
                    margin: EdgeInsets.all(20),
                    width: MediaQuery.of(context).size.width,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        _image == null ? Container() : Image.file(_image!),
                        SizedBox(
                          height: 20,
                        ),
                        _image == null
                            ? Container()
                            : _outputs != null
                                ? Text(
                                    _outputs?[0]["label"],
                                    style: TextStyle(
                                        color: Color(0xff196F3D), fontSize: 20),
                                  )
                                : Container(child: Text(""))
                      ],
                    ),
                  ),
            SizedBox(
              height: MediaQuery.of(context).size.height * 0.01,
            ),
            FloatingActionButton(
              tooltip: 'Pick Image',
              onPressed: pickImage,
              child: Icon(
                Icons.add_a_photo,
                size: 20,
                color: Color(0xffF7DC6F),
              ),
              backgroundColor: Color(0xff196F3D),
            ),
            SizedBox(
              height: MediaQuery.of(context).size.height * 0.01,
            ),
            FloatingActionButton(
              tooltip: 'Gallery Image',
              onPressed: galleryImage,
              child: Icon(
                Icons.camera_front,
                size: 20,
                color: Color(0xffF7DC6F),
              ),
              backgroundColor: Color(0xff196F3D),
            ),
          ],
        ),
      ),
      drawer: MainNavbar(),
    );
  }
}
