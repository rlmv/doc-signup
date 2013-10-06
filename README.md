

An online trip signup app for CnT.

run this ish!
------------
You need: Python 2.7, Django 1.5

    git clone https://github.com/rlmv/doc-signup.git
    cd doc-signup
    python mange.py syncdb

Make a superuser account when prompted. Then, run the dev server:
     
     python manage.py runserver

Yay! Check out localhost:8000/signup and localhost:8000/admin.
     

todo:
----
* email notifications to leaders
* styling
* allow leader login - integrate with User framework
* allow trippee login 
* produce 'This week' blitz from upcoming trips
