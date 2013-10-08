

An online trip signup app for CnT.

run this ish!
------------
You need: Python 2.7, Django 1.5, [django-cas](https://github.com/kstateome/django-cas)

Install django-cas:

    git clone https://github.com/kstateome/django-cas
    cd django-cas
    python setup.py install

Get our codebase:

    git clone https://github.com/rlmv/doc-signup.git
    cd doc-signup
    python manage.py syncdb

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


info:
----
CAS process walkthrough: https://wiki.jasig.org/display/CAS/Proxy+CAS+Walkthrough