# Python_Django_Repository
#Before start to work in django we need to install pyhton in our local machine then install django MVT framework using command prompt . version of python is your chioce you can choose 2.0 version and 3.0 version. 

-install django using command-
pip3 install django
  
-install rest-framework using command-
pip3 install restframework
  
-create project using command-
django-admin startproject yourprojectname
  
-create app using command-
python3 manage.py startapp yourappname

-register your app into installed_app of settings.py file

-configure new database into DATABASE field of settings.py

-migration with database using command inside your project directory-
python3 manage.py makemigrations

-command for migrate-
python3 manage.py migrate
 
-create super user using command -
python3 manage.py createsuperuser

-project run on server using command-
python3 manage.py runserver 153.163.0.32:8000#  you can put your custom ip-address and port number
