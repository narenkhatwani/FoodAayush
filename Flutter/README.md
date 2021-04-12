# **Flutter UI Documentation**

This section explains the code for each of the screens in the user interface of the application, which has been designed using the Flutter toolkit. There is a separate dart file for each screen. Additionally, there is a navigation bar to navigate between the various screens in the application. A separate dart file has been created which contains the code for the navigation bar. 

### Dart File 1: mainnavbar.dart

**Description:**

Here, the navigation bar for the application has been designed. It is a side navigation bar, which is called as a drawer menu or a navigation drawer in Flutter. It is created using the Drawer widget. Then a ListView widget is used to add create a list of items in the navigation drawer. Each item in the navigation drawer is created using a ListTile widget. The dart files for all screens have to be imported into this dart file, so that all screens can be accessed from the navigation bar. Also, the dart file for the navigation bar has been imported into every other dart file, in order for the navigation bar to be accessible from each screen. A separate MaterialPageRoute is used to navigate to each screen from the navigation bar. This MaterialPageRoute has to be added in the OnTap attribute of the ListTile widget for navigation to a particular screen along with the path to the desired screen.

**Code:**

```dart
class MainNavbar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    //Create navigation drawer
    return Drawer( 
      child: Container(
          color: Color(0xff196F3D),
          child: ListView(
            // Important: Remove any padding from the ListView.
            padding: EdgeInsets.zero,
            children: <Widget>[
              DrawerHeader(
                child: Text( 'Food\nAayush 🍱', style: TextStyle( fontSize: 50.0, fontFamily: "Comfortaa", color: Color(0xffF7DC6F),),),
                decoration: BoxDecoration( color: Color(0xff196F3D),),
              ),
              ListTile(
                title: Text( 'Main Menu', style: TextStyle( fontSize: 20.0, fontFamily: "Comfortaa", color: Color(0xffF7DC6F),),),
                tileColor: Color(0xff196F3D),
                onTap: () {
                  // Update the state of the app
                  // ...
                  // Then close the drawer
                  Navigator.pop(context);
                  Navigator.push(context, MaterialPageRoute(builder: (context)=>HomePage(),),);
                },
              ),            
            ],
          ),
        ),
    );
  }
}
```

### **Dart File 2: signuppage.dart**

**Description:**

The new users of the application first need to sign up. This page allows the new users to sign up by entering their Email ID and creating a password. The Form widget is used to create this page. The Email and Password fields are created by using the TextFormField widget inside the Form widget. There is also a Confirm Password Field, also created using the TextFormField widget. Form validation is added, in order to make sure that all information is entered correctly by the user.  After successfully signing up, the user will be directed to the login page.

**Code:**

```dart

```

### Dart File 3: loginpage.dart

**Description:**

The login screen for the application has been designed here. A Container widget is used to create a small box with text fields for entering the Email ID and Password in order to log in to the application. The labelText attribute has been used in both text fields, which indicates to the user that the text field is for entering the Email ID or the password.  When the user clicks on a particular text field, e.g. the Email ID field, they are given a hint which instructs them on what to enter in the field. This is achieved using the hintText attribute. For security purposes, the password must not be visible while the user types it. So, the obscureText attribute is set to true in order for the password to be invisible. The Login button is created using a MaterialButton widget. A splashcolor attribute is added to the button, so that when the button is clicked, it creates an effect like an ink splash over the button and makes it more clearly visible that the button has been clicked. After successfully logging in, the user can access the features of the application.  

**Code:**

```dart

```

### **Dart File 4: mainnutriscreen.dart**

**Description:**

This is the screen that the user will be redirected to if they want to find the nutritional value of a particular dish. This screen consists of two buttons, which the user can click depending on whether they want to click a picture of the dish or add the ingredients of the dish individually, in order to find the nutritional value of the dish. The buttons are created using the MaterialButton widget and are arranged vertically in a Column widget. On clicking a button, the user must be redirected to a new page. For this, a MaterialPageRoute is added to the onPressed attribute of the button and the path to the required page is given. 

```dart
body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            MaterialButton(
              color: Color(0xff196F3D),
              splashColor: Color(0xff58D68D),
              height: 175,
              minWidth: 350,
              onPressed: (){},
              child: Text( "\nCapture Image of Dish\n", style: TextStyle(fontFamily: "Comfortaa", color: Color(0xffF7DC6F), fontSize: 30,),),
              shape: RoundedRectangleBorder( borderRadius: BorderRadius.circular(9.0),),
            ),
            MaterialButton(
              color: Color(0xff196F3D),
              splashColor: Color(0xff58D68D),
              height: 175,
              minWidth: 350,
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context) => AddIndividualIngredients(),));
              },
              child: Text( "\nAdd Each Ingredient\n", style: TextStyle( fontFamily: "Comfortaa", color: Color(0xffF7DC6F), fontSize: 30, ),),
              shape: RoundedRectangleBorder( borderRadius: BorderRadius.circular(9.0),),
            ),
          ],
        ),
      )
```

### **Dart File 5: addindividualingredients.dart**

The user will be redirected to this page, if they decide to add the ingredients of the dish individually in order to calculate the nutritional value and click the 'Add Individual Ingredients' button on the Nutritional Value page. Here, there are multiple dropdown lists from which the user can select ingredients. If no ingredient is needed from a particular dropdown, then the user can select the None option. Each dropdown list is created using a DropdownButton widget, and each item is added to the dropdown list using the DropdownMenuItem widget. The hint attribute of the DropdownButton widget gives an indication to the user such as 'Add Ingredient 1' if no option has been selected from the dropdown list. At the bottom of the page, there is a button that the user clicks to calculate the nutritional value once all ingredients have been selected. This button is created using the MaterialButton widget.

**Code:**

```dart

```

### **Dart File 6: aboutus.dart**

**Description:**

This is an additional page that has been added for the users to gain additional information about the app and its developers. A simple Container widget has been used to create a box, containing information entered in simple Text widgets. These Text widgets are arranged vertically in a column within the Container, by declaring them as the children widgets of a Column widget. The page also has two buttons (outside the Container widget), one which redirects the user to the Customer Care page and another which takes the user to the F.A.Qs page. The buttons are created using the MaterialButton widget. A splashcolor attribute is also added to the buttons.

**Code:**

```dart
body: Column(        
        children: <Widget>[
          Container(            
            child: Center(
              child: Column(               
                children: <Widget>[
                  Text( "RARRN Developers", style: TextStyle( fontFamily: "Comfortaa", fontSize: 22.0, color: Color(0xff196F3D),),),
                  Text( "VESIT,Chembur", style: TextStyle( fontFamily: "Comfortaa", fontSize: 22.0, color: Color(0xff196F3D), ),),
                  Text( "Mumbai", style: TextStyle( fontFamily: "Comfortaa",fontSize: 22.0, color: Color(0xff196F3D),),),                                   
                ],
              ),
            ),
            decoration: BoxDecoration( border: Border.all( width: 2,),),
            padding: EdgeInsets.all(20.0),
            margin: EdgeInsets.fromLTRB(25.0, 70.0, 25.0, 70.0),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: MaterialButton(
              onPressed:(){
                Navigator.push(context, MaterialPageRoute(builder: (context)=>FAQ(),));
              },
              color: Color(0xff196F3D),
              height: 60,
              minWidth: 250,
              splashColor: Color(0xff58D68D),
              child: Text( "F.A.Q 🤔", style: TextStyle( fontFamily: 'Comfortaa', color: Color(0xffF7DC6F), fontSize: 27.0,),),
              shape: RoundedRectangleBorder( borderRadius: BorderRadius.circular(9.0),),
            ),
          ),
        ], 
      ),
```

### **Dart File 7: faq.dart**

**Description:**

Similar to the About Us page, there is an FAQs (Frequently Asked Questions) Page where users can find the answers to common questions related to food and oils quality. This is a static page. A SingleChildScrollView widget is used so that the user can scroll the page up and down. The questions and their answers are entered in simple Text widgets arranged vertically inside a Column widget.

**Code:**

```dart
body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Text( "Q. On what parameters is the freshness of food items decided? \n\nA. The freshness of a food item is decided from the photo captured by the camera by analysing the visual properties such as color and texture as well as surface defects.\n\n", style: TextStyle( fontSize: 23.0, fontFamily: "Comfortaa", color: Color(0xff196F3D),),),
            Text( "Q. Why is it important that the oil is not rancid? \n\nA. Rancid oil not only reduces the quality of food in terms of taste and odour, but can also be harmful to health. Hence it is essential that oil is not rancid.\n\n", style: TextStyle( fontSize: 23.0, fontFamily: "Comfortaa", color: Color(0xff196F3D),),),
            Text( "Q. Why should some ingredients not be used with certain other ingredients in cooking? \n\nA. Certain ingredients when used in combination reduce each other's nutritional value, e.g. in Palak Paneer, spinach and paneer actually reduce each other's nutritional value. Therefore our app provides a feature where the image of dish can be captured or the ingredients can be added individually and then it is checked whether the combination of ingredients is compatible, by finding the nutritional value of the dish.\n\n", style: TextStyle( fontSize: 23.0, fontFamily: "Comfortaa", color: Color(0xff196F3D),),
            ),
          ],
        ),
      ),
```
