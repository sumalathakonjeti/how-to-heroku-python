# how-to-heroku-python

```
$ git checkout main
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt

# install heroku CLI and then

$ heroku --version

$ heroku create $PROJECT
$ heroku git:remote -a $PROJECT
$ git push heroku main
```