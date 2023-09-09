# mikelegal Task - 1

Build an Email Campaign Manager that can do the following:

1. Add Subscribers ('email', 'first_name')
    - An endpoint to unsubscribe users.
2. Mark unsubscribed users as "inactive”.
3. Use Django admin to add new records to each table. (*If you are not using Django for the task, expose an endpoint HTML page to add records into those tables with proper permissions*)
4. Write a function to send daily Campaigns using SMTP ( you can create a Mailgun sandbox account)
    - Each Campaign has 'Subject', 'preview_text', 'article_url', 'html_content', 'plain_text_content', 'published_date'.
    - Campaign email must be rendered with the above information from a base template.
5. Optimize the sending time by using pub-sub with multiple threads dispatching emails in parallel.


## Technologies used
* [Django 4.2.5](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF 3.10.](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs
* [PostgreSQL 14.9](https://www.postgresql.org/): PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads
* [Celery 5.3.4](https://docs.celeryq.dev/en/stable/django/index.html): Celery is a powerful asynchronous task queue system integrated with the Django web framework for handling background tasks and distributed computing.
* [Redis 5](https://redis.io/): The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker.


## Installation
* If you wish to run your own build, first ensure you have Python globally installed on your computer. If not, you can get python 3.10 [here](https://www.python.org").

* After doing this, clone this repo to your machine
    ```bash
        $ git clone git@github.com:AmmarAR97/mikelegal.git
    ```

* Then move into the cloned repo as:
    ```bash
        $ cd mikelegal
    ```

* Then, create virtual environment for python:
    ```bash
        $ python -m venv .
    ```

* #### Dependencies
    1. Activate the virtual env by running the following command:
        ```bash
            $ source bin/activate
        ```
    2. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt 
        ```
    3. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file API service on your browser by using
    ```
        http://localhost:8000/
    ```
    Fire up celery in a separate terminal:
    ```bash
    $ celery -A campaing_manager worker --loglevel=info
    $ celery -A campaing_manager beat --loglevel=info
    ```
