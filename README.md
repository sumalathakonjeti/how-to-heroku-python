# how-to-heroku-python

THIS IS mainly a Demo.

How to create a quick Heroku app. 
Using a Flask app, gunicorn, and just plain wicked cool tech.

```
$ git checkout main
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt

# install heroku CLI and then

$ heroku --version

$ heroku create $PROJECT

# this will create an app which is what we think of as $PROJECT

$ heroku git:remote -a $PROJECT
$ git push heroku main
```

make changes by adding to page, then

be sure to git commit(!) and I usually push too.

```
git add .
git commit -m "wash your bowls"
git push # optional, but you should do this quite often.
```

```
$ git push heroku main
```

talk about Config vars...

cleanup

```
$ deactivate
$ rm -rf venv
```
Remove the heroku app too.