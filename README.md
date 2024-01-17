## Python and Django for Beginners course's   Djago part

# certificate 
![certificte](/Python_and_Django_or_Beginners.jpg)

### [Udemy Course Python and Django for Beginners link](https://www.udemy.com/share/102iF43@v4ORxCjSLgu9Tg0ZoLQ1TChKN79w_05ClrQTrbvOQnW-RLV3NlNd9lhOHzTzoaVEhA==/)


### Setup and run locally
```shell
# Create virtual env 
virtualenv venv
# Give proper permission to activate file
chmod u+x activate
# Activate Virtual env
source venv/bin/activate
# deactivate Virtual env :- 
deactivate

```

### Install django
#### Run : `pip install django`

### Create project and app and start server

```shell
# Create new project  :-  
django-admin startproject <telusko(project name)>
#Go into project :-   
cd telusko
#Run server :-  
python manage.py runserver
#Stop server by press 
ctrl+C

# Then 

# Create a new App :- 
python manage.py startapp calc

```
#### Log in psql  user  `sudo -u postgres psql`

### Run static files(style and javascripts)
```shell

# go in this location:-  "django-course/assets"
# and run on 5000 port localhost
python3 -m http.server 5000

```

