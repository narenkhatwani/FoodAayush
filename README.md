# FoodAayush
FoodAayush application





# Streamlit


# Deployment on Heroku

**How to deploy a Streamlit webapp on Heroku??**

###  Step 1:  ###

Make sure that your terminal is in your project folder. When you launch your project into the cloud, you need to create a requirements.txt file so that the server knows what to download to run your code. The library pipreqs can autogenerate requirements 

Use the following command in yout erminal to install the pipreqs library :

```pip install pipreqs```

###  Step 2:  ###

Then once it’s downloaded, just step out of the folder, run the following command, and in the folder, you should find your requirements.txt file.

```pipreqs <directory-path>```

The requirements file would contain the names of the libraries and their versions

**Example:**

altair==4.1.0
streamlit==0.64.0
matplotlib==3.2.2
pandas==1.0.5
plotly==4.9.0
numpy==1.18.5
dash==1.17.0

###  Step 3:  ###

**setup.sh and Procfile**

The setup.sh file contains some commands to set the problem on the Heroku side, so create a setup.sh file (you can use the nano command) and save the following in that file (change the email in the middle of the file to your correct email)



###  Step 4:  ###

###  Step 5:  ###

###  Step 6:  ###

###  Step 7:  ###









# Project Collaborators

Mentor- Prof Richard Joseph

Collaborators- Naren Khatwani, Raghav Potdar, Rahul Sohandani, Adithya Shrivastava,



