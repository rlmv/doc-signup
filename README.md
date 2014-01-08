
A trip signup app for CnT.

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
    python manage.py syncdb --noinput

And run the dev server:

    python manage.py runserver

Yay! Check out localhost:8000/signup.

If you want to access the admin site (currently the only way to add trips) at localhost:8000/admin, you first need to visit /signup and login in via WebAuth (so that your information is in the database) and run 
    
    python manage.py superuser <Your Full Name>

This will give you superuser rights. 


todo:
----
* let users see current trips
* let users cancel trips
* let leaders submit trips - (with approval?)
* let leaders see trippee list
* let leaders message/notify trippees (or export email list?)
* email notifications to leaders
* automatic reminders for upcoming trips?
* styling
* produce 'This week' blitz from upcoming trips

