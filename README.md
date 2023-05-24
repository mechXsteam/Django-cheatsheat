# Django cheatsheet

<aside>
<img src="https://www.notion.so/icons/command-line_gray.svg" alt="https://www.notion.so/icons/command-line_gray.svg" width="40px" /> Django Cheatsheet: Step-by-Step Guide for Building Web Applications

This comprehensive Django cheatsheet provides a point-wise, step-by-step guide to help you quickly implement key functionalities in your Django web application. Handy for a beginer level developer.

Key Topics Covered:

1. Routing and URL Configuration: Learn how to define URL patterns, create views, and map them to URLs using Django's powerful routing system.
2. Models and Database Interaction: Explore how to define models, create database tables, perform CRUD operations, establish relationships, and leverage Django's ORM.
3. User Authentication and Authorization: Understand how to integrate user authentication and authorization into your Django application, including user registration, login, logout, and permission management.
4. Templating: Discover Django's template language and learn how to render dynamic content, utilize template inheritance, and pass data to templates.
5. Forms and Validation: Get familiar with creating and handling forms, performing form validation, and leveraging Django's built-in form features.
6. Django Admin: Learn how to leverage Django's powerful admin interface for easy management of your application's data.

With this Django cheatsheet, you'll have a handy reference to guide you through the implementation of various components and features in your Django application. 

Download the Django cheatsheet now and streamline your Django development process!"

Feel free to modify and adapt the description to fit the specific style and content of your cheatsheet.

</aside>

# 1. Useful commands in Django

- Creating a project in django - django-admin startproject projectName.
    
    ```python
    LearningLog
    |_ LearningLog
    |_ templates
    |_ db.sqlite
    |_ manage.py
    ```
    
- python manage.py makemigrations - generates migration files containing changes that need to be applied to the database, but doesn’t actually change anything in your database.
- python manage.py migrate - will make the actual modifications to your database, based on the migration files.
- Viewing the project - python manage.py runserver.
- Start an app - python manage.py startapp appName.
    
    After creating the app, ensure that you add it to the INSTALLED_APPS list in the settings.py file located in LearningLog.
    
    ```python
    LearningLog/settings.py
    
    INSTALLED_APPS = [
        'my_app',
        'users',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```
    
- Setting up a superuser - python manage.py createsuperuser.
- Open the Django shell - python manage.py shell

# 2. Defining models

The model class is the database table, and each instance of the model class represents a specific record (row) in that table. The attributes within the model class represent the columns of the table.

```python
my_app/models.py

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
```

To view your model in the admin panel, register it in the admin.py file of your app.

```python
my_app/admin.py

from django.contrib import admin

from .models import Topic
# Register your models here.
admin.site.register(Topic)
```

# 3. Foreign keys

To establish a connection between entries and their corresponding topics, we utilize foreign keys in Django. Foreign keys link two database tables together. In our case, each topic will have multiple entries associated with it. To achieve this, we define the Entry model as follows:

```python
my_app/models.py

class Entry(models.Model):
    """Something specific leaned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}"
```

# 4. Djnago shell

The Django shell provides an interactive environment where you can interact with your models and explore the data stored in your database. It launches a Python interpreter with Django's configuration loaded, allowing you to access your project's models and perform various operations.

```python
In [1]: from my_app.models import Topic

In [2]: Topic.objects.all()
Out[2]: <QuerySet [<Topic: Django>]>

In [3]: topics = Topic.objects.all()

In [4]: for topic in topics:
   ...:     print(topic,topic.id)
   ...:
Django 1

In [5]: topic = Topic.objects.get(id=1)

In [6]: topic
Out[6]: <Topic: Django>

In [7]: topic.text
Out[7]: 'Django'

In [8]: topic.date_added
Out[8]: datetime.datetime(2023, 5, 23, 8, 40, 43, 685611, tzinfo=datetime.timezone.utc)

In [9]: topic.entry_set.all()
Out[9]: <QuerySet [<Entry: Django is the best python backend framework.>]>

In [10]: for ele in topics:
   ...:     print(ele,ele.owner,ele.id)
   ...:
Django Aditya_Kumar 3
```

`CTRL+D` to exit the shell.

# 5. How to build a page in Django

**Step 1:** Include the URLs of my_app in the urls.py file in LearningLog/urls.py.

```python
LearningLog/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
]
```

**Step 2:** Create a template.

```html
templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Learning log</title>
</head>
<body>
    <h1>Hello world !</h1>
    <h2>{{ name }}</h2>
</body>
</html>
```

**Step 3:** Define a view.

```python
my_app/views.py

from django.shortcuts import render

# Create your views here.
def viewIndex(request):
    return render(request, 'index.html', {'name': "Aditya Kumar"})
```

**Step 4:** Define urls of the my_app in the my_app/urls.py file.

```python
my_app/urls.py

from django.urls import path

from .views import viewIndex

app_name = 'my_app' # this is very important for defining url's
urlpatterns = [
    path('', viewIndex, name='viewIndex') # indeed this too
]
```

# 6. Template inheritance

When building a website, some elements will always need to be repeated on each page. Rather than writing these elements directly into each page, you can write a base template containing the repeated elements and then have each page inherit from the base. This approach lets you focus on developing the unique aspects of each page and makes it much easier to change the overall look and feel of the project.

**Step 1:** Create a base.html file (the parent .html file), from which all the files will inherit from

```html
templates/base.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Learning log</title>
</head>
<body>
    <h1>Welcome hello World !</h1>
    <h2>templates/base.html</h2>

    {# these pair of tags will act as a placeholder, it is upon the child template which kind of information goes into #}
    {% block content %}{% endblock content %}
    {% block footer %}{% endblock footer %}

</body>
</html>
```

**Step 2:** Create a child .html file

```html
templates/index.html

{# extends the common portion from the base.html such as navigation bar #}
{% extends 'base.html' %}

{% block content %}
    {{ name }}
{% endblock content %}

{% block footer %}
    <ul>
        <li>Web developer</li>
        <li>Python developer</li>
        <li>Mechanical engineer</li>
    </ul>
{% endblock footer %}
```

# 7. How to send data from view functions to templates

We can retrieve some data from the database and send it to the templates by using the context in view function in the my_app/views.py file. A context is essentially a dictionary that contains values later to be used in the templates against keywords used to specify the values in the context.

```python
my_app/views.py

def topics(request):
    """show all topics"""
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'index.html', context)
```

```html
templates/topics.html

{# extends the common portion from the base.html such as navigation bar #}
{% extends 'base.html' %}

{% block content %}
    <ul>
        {% for topic in topics %}
            <li>{{ topic }}</li>
        {% empty %}
            <li>No topics have been added yet !</li>
        {% endfor %}
    </ul>
{% endblock content %}
```

# 8. Loops and conditionals

**for loop**

```python
{% for ele in list %}
	do something
{% empty %} 
	do something else
{% endfor %}
```

**If else**

```python
{% if variable %}
	// statements
{% else %}
	// statements
{% endif %}
```

# 9. Insert URLs in the anchor tags

```python
<p>
	<a href="{% url 'my_app:index' %}">Learning Log</a> -
	<a href="{% url 'my_app:topics' %}">Topics</a>
</p>
```

# 10. How to pass an argument in the URLs

```python
my_app/urls.py

from django.urls import path

from . import views

app_name = 'my_app'
urlpatterns = [
    path('entries/<int:topic_id>', views.entry, name='entry'),
]
```

To use such a path in the template, follow the code below,

```html
<a href="{% url 'my_app:entry' topic.id %}">{{ topic }}</a>
```

To redirect to such a URL

```python
my_app/views.py

def new_entry(request, topic_id):
    """Add a new entry to a topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:entry', topic_id)
    # Display a blank or invalid form
    context = {'form': form, 'topic': topic}
    return render(request, 'new_entry.html', context)
```

# 11. Model forms

Model forms allow us to build forms on the basis of the models defined in the my_app/models.py file.

**Step 1:** Define a form class

```python
my_app/forms.py

from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
```

**Step 2:** Define the view function

```python
my_app/views.py

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('my_app:topic')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'new_topic.html', context)

# Other types of view function

# 1. To connect new entries to a particular topic

def new_entry(request, topic_id):
    """Add a new entry to a topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('my_app:entry', topic_id)
    # Display a blank or invalid form
    context = {'form': form, 'topic': topic}
    return render(request, 'new_entry.html', context)

# 2. To edit an entry

def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request, pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:entry', topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)
```

**Step 3:** Write a template 

```python
templates/new_topic.html

{% extends 'base.html' %}
{% block content %}
<p>Add a new topic:</p>
<form action="{% url 'my_app:new_topic' %}" method='post'>
    {% csrf_token %}
    {{ form.as_p }}
    <button name="submit">Add topic</button>
</form>
{% endblock content %}
```

# 12. User authentication and authorization

Authentication refers to determining "who you are," while authorization determines "what you can do."

**Step 1:** Create a user app using the command, python manage.py startapp users.

**Step 2:** Add it to the INSTALLED_APPS list in the LearningLog/settings.py file. 

**Step 3:** Include the URL of the user's app.

```python
users/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('users/', include('users.urls')),
]
```

**Step 4:** Build the login page.

1. Define urls.py file.
    
    ```python
    users/urls.py
    
    from django.urls import path, include
    
    app_name = 'users'
    urlpatterns = [
        # include the default auth urls
        path('', include('django.contrib.auth.urls'))
    ]
    ```
    
2. Build the login and logout template
    
    To create the necessary templates for registration, create a directory named "registration" in the location users/templates/registration. Save login.html and logged_out.html files in the registration directory. Make sure to name the logout page as logged_out.html to avoid displaying the default admin logout page.
    
    ```html
    users/templates/registration/login.html

    {% extends 'base.html' %}
    
    {% block content %}
        {% if form.errors %}
            <p>Your username and password didn't match. Please try again</p>
        {% endif %}
    
        <form action="{% url 'users:login' %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button name="submit">Log in</button>
            <input type="hidden" name="next" value="{% url 'my_app:index' %}"/>
        </form>
    {% endblock content %}
    ```
    
    ```html
    users/templates/registration/logged_out.html

    {% extends 'base.html' %}
    {% block content %}
        <h1>You have been logout</h1>
    {% endblock content %}
    ```
    
    Modify the base.html to include the login and logout links.
    
    ```html
    templates/base.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Learning log</title>
    </head>
    <body>
        <h1>Welcome hello World !</h1>
        <p>
            <a href="{% url 'my_app:index' %}">Home</a>
            <a href="{% url 'my_app:topic' %}">Topics</a>
            <a href="{% url 'my_app:new_topic' %}">Add new topic</a>
            {% if user.is_authenticated %}
                Hello, {{ user.username }}.
                <a href="{% url 'users:logout' %}">logout</a>
            {% else %}
                <a href="{% url 'users:login' %}">Log in</a>
            {% endif %}
        </p>
        {# These pair of tags will act as a placeholder, it is upon the child template which kind of information goes into #}
        {% block content %}{% endblock content %}
    
    </body>
    </html>
    ```
    

**Step 5:** Build a signup page where users can create their accounts.

1. Include the registration link in the users/urls.py file.
    
    ```python
    users/urls.py
    
    from django.urls import path, include
    
    from . import views
    
    app_name = 'users'
    urlpatterns = [
        # include the default auth urls
        path('', include('django.contrib.auth.urls')),
        # include registration urls
        path('register/', views.register, name='register')
    ]
    ```
    
2. Create registration view
    
    ```python
    users/views.py
    
    from django.contrib.auth import login
    from django.contrib.auth.forms import UserCreationForm
    from django.shortcuts import redirect, render
    
    # Create your views here.
    def register(request):
        """Register a new user"""
        if request.method != 'POST':
            # display a blank registration form
            form = UserCreationForm()
        else:
            # Process completed form
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                new_user = form.save()
                # Log in the user, and redirect to the home page
                login(request, new_user)
                return redirect('my_app:index')
        # Display a blank or invalid form
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    ```
    
3. Create registration template
    
    For the registration template, name it as register.html and save it in the users/templates/registration directory.
    
    ```html
    users/templates/registration/register.html
    
    {% extends "base.html" %}
    
    {% block content %}
        <form method="post" action="{% url 'users:register' %}">
            {% csrf_token %}
            {{ form.as_p }}
            <button name="submit">Register</button>
            <input type="hidden" name="next" value="{% url 'my_app:index' %}"/>
        </form>
    {% endblock content %}
    ```
    

**Step 6:** Allowing users to see their own data

1. Restricting access with the @login_required decorator.
    
    ```python
    my_app/views.py
    
    from django.contrib.auth.decorators import login_required
    from django.shortcuts import render, redirect
    
    from .forms import TopicForm, EntryForm
    from .models importTopic, Entry
    
    # Create your views here.
    
    @login_required
    def topics(request):
        """show all topics"""
        topics = Topic.objects.all()
        context = {'topics': topics}
        return render(request, 'topics.html', context)
    ```
    
2. To enhance security, we have implemented restricted access to the home page, allowing only logged-in users to access its content. To handle unauthenticated access attempts, we need to configure Django's redirect behaviour. Without proper configuration, Django will raise an error when an unauthenticated person tries to access the home page.
    
    We must specify the desired redirect location for such cases, ensuring a smooth user experience. So to make this redirect work, we modify the LearningLog/settings.py file as follows.
    
    ```python
    LearningLog/settings.py
    
    # My settings
    LOGIN_URL = 'users:login'
    ```
    

**Step 7:** Connect the users with their data using foreign keys.

```python
my_app/models.py

class Topic(models.Model):
"""A topic the user is learning about"""
		text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def__str__(self):
	"""Return a string representation of the model"""
	return self.text


```

Migrate the database, as a model is modified.

Connect new entries with the current user.

```python
my_app/views.py

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
    if form.is_valid():
	new_topic = form.save(commit=False)
	new_topic.owner = request.user
	new_topic.save()
	return redirect('my_app:topic')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'new_topic.html', context)
```

**Step 8:** Filter topics as per the user.

```python
my_app/views.py
****
@login_required
def topics(request):
    """show all topics"""
    *topics = Topic.objects.filter(*owner=request.user*).order_by('-date_added')*
    context = {'topics': topics}
    return render(request, 'topics.html', context)
```

**Step 9:** Protect a User’s topic, such that any other user can’t see it.

```python
**my_app/views.py**

from django.http import Http404

@login_required
def entry(request, topic_id):
    """detail page of a single topic"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'entry.html', context)
```

Ensure to implement this process for all view functions whenever safeguarding a user's data is necessary.
