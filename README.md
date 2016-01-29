# One Hour Python Workshop

Python is a great programming language for creators and engineers. 
You don't have to have a degree in computer science to build amazing things. 

This tutorial will get you up and running with Python in one hour so you can begin learning and creating. 

### Here's the list of everything we'll accomplish in the next hour: 

1. Install Python
2. use the REPL
3. Run our first program
4. Install a package - (Flask/Beautiful Soup)
5. Uninstall a package
6. Install virtualenv
7. Install virtualenvwrapper or virtualenvwrapper-win
8. Create a virtual environment
9. Install flask and run our first app

#Let's do this


## 1. Install Python

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/starting/install/osx/)

## 2. use the REPL

The REPL stands for Read Evaluate Print Loop

Makes iterating and testing easy! 

python

'>>>'

try these commands:

x = 2 + 2

print x 

import this

[More Practice](http://timmyreilly.azurewebsites.net/python-introduction/)

## 3. Run our first program

Use your favorite text editor. I'm using [Visual Studio Code](https://code.visualstudio.com/)

beginnings.py

```python 
sentence = "Four score and seven years ago"
sentence_no_vowels = ""
for letter in sentence: 
    if letter not in "AEIOUaeiou":
        sentence_no_vowels = sentence_no_vowels + letter
         
print sentence_no_vowels
```

## 4. Install a package
	
Python Packages are installed with pip

We'll install [requests](http://docs.python-requests.org/en/latest/)

```
pip -v

pip install requests
```

## 5. Uninstall a package

```
pip uninstall requests

```

## 6. Install virtualenv

```
pip install virtualenv
```

## 7. Install virtualenvwrapper or virtualenvwrapper-win

virtualenv wrappers make it easy to manage multiple environments and can make iterating on project easy. 

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## 8. Create a virtual environment

```
mkvirtualenv helloworld
```

cd into root of project

```
setprojectdir .

deactivate

workon helloworld
```


## 9. Install flask and run our first app

Now we need [flask](http://flask.pocoo.org/) for our first website!

```
pip install flask
```

Create our hello.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

SWEET!

```
python hello.py
 * Running on http://localhost:5000/
```


## WEEEE!


Please contact me if you have any questions: 
[@timmyreilly](http://twitter.com/timmyreilly)