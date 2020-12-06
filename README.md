# FoodAayush

#### Abstract ####

**Food is an essential parameter that plays an important role in the survival of humans. It also plays a major part in depicting a country’s culture. Healthy, nutritious, and high-quality food results in not only a better lifestyle but also develops a person’s immunity and health. Likewise, the consumption of low-quality food which might be deprived of nutritional value impacts a person’s health negatively and makes them susceptible to all types of diseases. In India, there is a persistent complaint, in any civic body-related food section, about the quality of meals available. Likewise, the quality of the oil is also an important factor while cooking any meal. Therefore, the Quality of oil used in frying the food to affect its taste must be monitored too. Its continuous exposure to relatively high temperatures results in degradation of its quality. The purpose of this study is to build an application for the detection of the quality of food and also to detect repeated frying on cooking oils based on the visual properties of the oils. Classification of food items is done on the basis of time left for consumption, edibility, quality, color, and rancidity. The food items are further classified as stale or usable using artificial intelligence algorithms based on the images acquired through a Cell Phone’s camera.**


![Imgur Image](https://i.imgur.com/OqjjZQA.jpg)

# About FoodAayush Data Analysis using Streamlit


## Requirements for the project

- streamlit==0.64.0
- matplotlib==3.2.2
- pandas==1.0.5
- plotly==4.9.0
- numpy==1.18.5
- dash==1.17.0

## How to Run the Project

Open the terminal/cmd in the Streamlit Folder and run the following command

```streamlit run app.py```

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

- altair==4.1.0
- streamlit==0.64.0
- matplotlib==3.2.2
- pandas==1.0.5
- plotly==4.9.0
- numpy==1.18.5
- dash==1.17.0

###  Step 3:  ###

**setup.sh and Procfile**

The setup.sh file contains some commands to set the problem on the Heroku side, so create a setup.sh file (you can use the nano command) and save the following in that file (change the email in the middle of the file to your correct email)

Make sure that your terminal is in your project folder

Type the command 
```nano setup.sh```

Now you will see a setup.sh file has been opened. Copy one of the codes that you like and paste it in the setup.sh file

**setup.sh (without email verification - preferrable)**

```
mkdir -p ~/.streamlit/ 
echo " 
[server]\n 
headless = true\n 
enableCORS=false\n 
port = $PORT\n 
\n 
" > ~/.streamlit/config.toml 
```

**setup.sh (with email verification - not preferrable)**

```
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
```
**Procfile**

Again,Make sure that your terminal is in your project folder

Type the command 
```nano Procfile```  (Procfile here is case sensitive - type it as it is mentioned)

and now insert the following piece of code in the Procfile file

```web: sh setup.sh && streamlit run [name-of-app].py```

**Note- [name-of-app] being the name of your project's main .py file**

###  Step 4:  ###

Heroku builds systems using Git and it’s pretty easy to get set up. Git is a version control system and runs as default on a lot of operating systems. 
Check if you have it **(if yes then skip this step)** 
**If not, install it.**

Open terminal in your project folder and run the following commands :

```git init```

This initialises a git repository in your project folder and you should see something like the following print out:

```Initialized empty Git repository in /Users/…```

(If you are doing this for the first time make sure you visit - https://devcenter.heroku.com/articles/heroku-cli and create your account there)


###  Step 5:  ###

###  Step 6:  ###

###  Step 7:  ###



# Project Collaborators

Mentor- Prof Richard Joseph

Collaborators- Naren Khatwani, Raghav Potdar, Rahul Sohandani, Adithya Shrivastava,



