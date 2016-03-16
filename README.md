# Windows Workshop

Well you got just your new Windows PC. 
Hopefully a crispy Surface Pro 4 (Starting at $899)

And you want to learn how to program, and Python is the language you're going with. 
Or you already know how to program and this is the first windows PC you've used in a while and like Python. 
I don't know you…

Well that's fine too. 

If at any point you get lost or confused, feel free to raise your hand/add a comment or PM me on twitter @timmyreilly http://twitter.com/timmyreilly 

### In this course we'll cover: 
1. Installing Python
2. Using the REPL
3. Running our first program
4. Examining the Python Folders 
5. Using Pip 
6. Creating, installing to, and using virtualenv and virtualenvwrapper-win 
7. Examining the Envs folders! 
8. setprojectdir and Workflow
- Visual Studio
- Virtual Envs in VS
- Exploring Visual Studio Directories  
- Using the REPL in VS 
- Shortcuts for VS 
- Continued Learning 

## 1. Installing Python

[Windows](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/)

## 2. Using the REPL

The REPL stands for Read Evaluate Print Loop

Makes iterating and testing easy! 

Type python into your command prompt

```
C:\..\> python
Python 2.7...
>>>
```

try these commands:
```
>>> x = 2 + 2
>>> print x 
>>> import this
>>> type(x) 
>>> dir(x) 

```

[More Practice](http://timmyreilly.azurewebsites.net/python-introduction/)

## 3. Running our first program

Use your favorite text editor. I'm using [Visual Studio Code](https://code.visualstudio.com/)

I've named my example: [beginnings.py](https://github.com/timmyreilly/onehourpython/blob/windows/README.md)

```python 
sentence = "Four score and seven years ago"
sentence_no_vowels = ""
for letter in sentence: 
    if letter not in "AEIOUaeiou":
        sentence_no_vowels = sentence_no_vowels + letter
         
print sentence_no_vowels
```

## 4. Examining the Python Folders 

So because we're on windows let's take a look and explore our current folder structure just to get familiar with how Python works. 

We'll also show some helpful ways of interacting with python in our terminal 
- Calling Python Explicitly
```
> C:\Python27\python.exe 
```
- Calling Pip directly
```
> C:\Python27\Scripts\pip.exe list 
```
- Using Easy Install
```
> C:\Python27\Scripts\easy_install.exe 
```
- What Else is in there?
``` 
> dir C:\Python27\
```

## 5. Using Pip 

Install a package
	
Python Packages are installed with pip

We'll install [requests](http://docs.python-requests.org/en/latest/)

```
pip -v

pip install requests
```

Uninstall a package

```
pip uninstall requests

```


## 6. Creating, installing to, and using virtualenv and virtualenvwrapper-win 

Back to my other blog: http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/ 


## 7. Examining the Envs folders! 

Now that we've used our first virtual environment where is it? 
Let's go find it! The files are in the computer! 

```
> C:\Users\tireilly\Envs\helloworld\Scripts\pip.exe list 
> C:\Users\tireilly\Envs\helloworld\Scripts\easy_install.exe 
```

## 8. setprojectdir and workflow  

That was fun. Let's do it a lot. 

cd into root of project

```
> workon newProject 

> cd newProjectDirectory 

> setprojectdir .

> deactivate

> workon helloworld
```

Now that was all fun and agnostic. 
Let's dive into Visual Studio. 

## 9. Visual Studio

- Community Edition is Free and Awesome! 
- And there's support for extensions like PTVS: http://microsoft.github.io/PTVS 
- It’s a beast! 
- Great for debugging, large projects and working with many different technologies. 
The python offering is found in the form of Python Tools for Visual Studio. 

### The three things I want to introduce are Virtual Envs, the REPL, and Shortcuts 

## 10. Virtual Envs in VS 
- Visual Studio will Manage Virtual Environments for you! 

[Full breakdown here](https://www.youtube.com/watch?v=eKPeC1remt4 )


## 11. Exploring Visual Studio Directories 

```
> C:\visualstudio\projects\OneHourPython\OneHourPython\env\Scripts\pip.exe
> C:\visualstudio\projects\OneHourPython\OneHourPython\env\Scripts\python.exe 

```

Check them out in the directory too! 

## 12. Using the REPL in VS 

[Full Breakdown here](https://www.youtube.com/watch?v=JNNAOypc6Ek&feature=iv&src_vid=TuewiStNT0M&annotation_id=annotation_3141657985)

## 13. Shortcuts for VS 

Make it [buttery](http://timmyreilly.azurewebsites.net/3-shortcuts-that-justify-opening-visual-studio/)

- Ctrl+F5 = Run Without Debugging 
- Ctrl+E, Ctrl+E = Selected text to interactive 
- Alt+Shift+F5 = Send file to interactive


That's it for now, but don't stop here the funs about to start! 

# Continued Learning & Other Resources:
Try Azure
Take your ideas of the Ground: BizSpark

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




