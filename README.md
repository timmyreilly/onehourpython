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
10. What's next? 

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
## 10. What's next?

Now that we've taken our first couple steps with Python, where should we do next? 

#### Want to learn more about how to use the language? 
- [Hitchhikers Guide to Python](http://docs.python-guide.org/en/latest/)
- Cheatsheet [1](http://www.cogsci.rpi.edu/~destem/igd/python_cheat_sheet.pdf) + [2](http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf)

#### MOAR Websites!
- [Flask](http://flask.pocoo.org/) - Lightweight easy to get started
- [Django](https://www.djangoproject.com/) - Batteries Included + [Great Documentation](http://www.djangobook.com/en/2.0/index.html) 
- [Cloud Deployment](http://timmyreilly.azurewebsites.net/starter-site-for-flask-on-azure-web-apps/)  

#### APIS?
- [Requests](http://docs.python-requests.org/en/latest/) library
- [Reddit](https://books.google.com/books?id=P0TsCQAAQBAJ&pg=PA60&lpg=PA60&dq=requests+python+reddit&source=bl&ots=43v1_rVJcs&sig=exuUeJPvkHKoWIgh8rbe3h7W5yQ&hl=en&sa=X&ved=0ahUKEwinurCclNDKAhXBMGMKHVqNDnsQ6AEInAEwEw#v=onepage&q=requests%20python%20reddit&f=false), [Twitter](http://www.tweepy.org/), [GitHub](http://engineering.hackerearth.com/2014/08/21/python-requests-module/), [Microsoft](https://msdn.microsoft.com/en-us/library/)
- [Project Oxford Machine Learning](http://timmyreilly.azurewebsites.net/using-oxford-tts-service-with-python-2-7-and-requests/)

#### Databases! 
- [MySql](https://en.wikipedia.org/wiki/MySQL) + [PyMySql](https://github.com/PyMySQL/PyMySQL)
- [SQLite](http://zetcode.com/db/sqlitepythontutorial/) 
- [the Cloud](https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-table-storage/) 
- [CSVs?](http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/)

#### Data Scraping!
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Books](https://automatetheboringstuff.com/chapter11/) 
- [Hitchhiker's guide](http://docs.python-guide.org/en/latest/scenarios/scrape/)

#### Hardware!
- [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)
- [Adafruit Documentation](https://learn.adafruit.com/category/learn-raspberry-pi)

#### Science + Data Visualization 
- [SciPy](http://www.scipy.org/about.html) library of scientific tools
- [Jupyter](http://jupyter.org/) Interactive Notebooks
- [IPython](http://ipython.org/notebook.html) Interactive Python
- [pandas](http://pandas.pydata.org/) data structures
- [Astropy](http://www.astropy.org/) for Astronomy




## WEEEE!


Please contact me if you have any questions: 
[@timmyreilly](http://twitter.com/timmyreilly)