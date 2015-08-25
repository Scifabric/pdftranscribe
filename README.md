PyBossa demo project PDF Transcribe
=======================================
PDF Transcribe is a **demo project** for PyBossa that shows how you can 
crowdsource a PDF transcription problem.

This project uses the [Mozilla PDF.JS](http://mozilla.github.com/pdf.js) library to load 
an [external PDF file](https://github.com/mozilla/pdf.js/wiki/Frequently-Asked-Questions#wiki-faq-xhr) 
and render it directly in the web browser **without using any third party plugin**.

By using PDF.JS, we have the possibility of rendering almost any PDF that is hosted under an 
[HTTP server](https://github.com/mozilla/pdf.js/wiki/Frequently-Asked-Questions#wiki-faq-xhr)
and then use a customized form to get the data that we want to extract from it.

In this **simple demo project**, we **load a PDF file** in one side of the page, and in the other one **a form** where the volunteer will be able to transcribe the PDF page by typing the text in the input form. While this example is really simple, adapting the template to extract specific bits of information from the PDF will be really easy (you will only need to add more HTML input fields with instructions about what you want to extract from the PDF file). The idea is that you could be able for example to extract specific items from the documents, like captions, tabular data, authorship, institutions, etc.

![alt screenshot](http://img10.imageshack.us/img10/5364/pdftranscribe1.png)

The provided script for creating the tasks is very simple: you only need to tell the script where is the PDF file hosted, the URL, and which pages you want to convert as tasks. By default, this demo explores the 14 pages of the example PDF file.

Re-using the project for your project
=========================================

You need to install the pybossa-pbs library first. Use of a virtual environment
is recommended:

```bash
    $ virtualenv env
    $ source env/bin/activate
```

```bash
    $ pip install -r requirements.txt
```

## Creating an account in a PyBossa server
Now that you've all the requirements installed in your system, you need
a PyBossa account:

*  Create an account in your PyBossa server (use [Crowdcrafting](https://crowdcrafting.org) if you want).
*  Copy your API-KEY (you can find it in your profile page).

## Configure pybossa-pbs command line

PyBossa-pbs command line tool can be configured with a config file in order to
avoid typing the API-KEY and the server every time you want to take an action
on your project. For this reason, we recommend you to actually create the
config file. For creating the file, follow the next steps:

```bash
    $ cd ~
    $ editorofyourchoice .pybossa.cfg
```

That will create a file. Now paste the following:

```python
[default]
server: http://yourpybossaserver.com
apikey: yourapikey
``` 

Save the file, and you are done! From now on, pybossa-pbs will always use the
default section to run your commands.

## Create the project

Now that we've everything in place, creating the project is as simple as
running this command:

```bash
    $ pbs create_project
```

## Adding tasks

### Using a CSV or JSON file for adding tasks

This is very simple too. There's a sample tasks CSV file included. You can adapt
it to your own PDF files URLs, and then just let pbs do the job:

```bash
    $ pbs add_tasks --tasks-file pdf_tasks.csv
```

### Using the Dropbox importer (via web)

You can also use the built-in Dropbox importer that comes with PyBossa servers
(if configured by the admin). For more details, please visit the [PyBossa documentation](http://docs.pybossa.com/en/latest/user/overview.html?highlight=dropbox#importing-the-tasks-from-a-dropbox-account).

## Finally, add the task presenter, tutorial and long description

Now that we've some data to process, let's add to our project the required
templates to show a better description of our project, to present the tasks to
our users, and a small tutorial for the volunteers:

```bash
    $ pbs update_project
```

Please, check the full documentation here about how to create a project in the
command line with pbs:

http://docs.pybossa.com/en/latest/user/pbs.html

Setting up your Apache web server for hosting the PDF files
===========================================================

Usually you will have a set of PDF files that you are currently serving via
a web server.

If you use the project as it is, you will see that it does not work loading
the PDFs, even though the URL links are fine and the PDF pages are correct in
the Google Spreadsheet that you have created. The problem, is that you need to
enable [CORS](http://www.w3.org/TR/cors/) in order to get access to your PDF files.

In [Enable Cors webpage](http://enable-cors.org/) you can check how you can
configure most of the web servers properly, so this project can load the
PDF files from other domains without problems. For example, for an Apache web
server all you have to do is to enable the module **mod_headers**:

```bash
 $ sudo a2enmod headers
```

Then, open the site config file, i.e.
**/etc/apache2/sites-enabled/000-default** and add the following to the
**VirtualHost section:

```
Header set Access-Control-Allow-Origin "*"
```

Finally restart the web server and you will be done! The PDFs now should be
loaded without problems. Note: you can use .htaccess files too in order to not
enable CORS to all your site, or if you prefer place the previous sentence in
a Directory or Location, instead of at the level of the VirtualHost section.

Using Dropbox to host your PDF files
====================================

Alternatively, if you are using a PyBossa server configured to be integrated with
Dropbox (like [Crowdcrafting](https://crowdcrafting.org)) you can use the built-in
Dropbox importer to serve the PDF files directly from a Dropbox account. Check the
[PyBossa docs](http://docs.pybossa.com/en/latest/user/overview.html?highlight=dropbox#importing-the-tasks-from-a-dropbox-account) for more details.

Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This project uses the [pybossa-pbs](https://pypi.python.org/pypi/pybossa-pbs) library in order to simplify the development of the project and its usage. Check the [documentation](https://github.com/PyBossa/pbs).


LICENSE
=======

Please, see the COPYING file.




Acknowledgments
===============

The thumbnail has been created using a [photo](http://www.flickr.com/photos/mrmorodo/8174824430/) from TempusVolat (license CC BY-NC-SA 2.0). 

Special thanks to [Miquel Herrera for his JS libraries for the canvas scrolling](http://hitconsultants.com/dragscroll_scrollsync/scrollpane.html), and [Mozilla Foundation](http://mozilla.github.io/pdf.js/) for their PDF.JS library.
