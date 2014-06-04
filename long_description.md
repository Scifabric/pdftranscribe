PDF Transcribe is a **demo application** for PyBossa that shows how you can
crowdsourcing a PDF transcription problem.

This application uses the [Mozilla PDF.JS](http://mozilla.github.com/pdf.js)
library to load an [external PDF file](https://github.com/mozilla/pdf.js/wiki
/Frequently-Asked-Questions#wiki-faq-xhr) and render it directly in the web
browser **without using any third party plugin**.

By using PDF.JS, we have the possibility of rendering almost any PDF that is
hosted under an [HTTP server](https://github.com/mozilla/pdf.js/wiki
/Frequently-Asked-Questions#wiki-faq-xhr) and then use a customized form to
get the data that we want to extract from it .

In this **simple demo application**, we **load a PDF file** in one side of the
page, and in the other one **a form** where the volunteer will be able to
transcribe the PDF page by typing the text in the input form. While this
example is really simple, adapting the template to extract specific bits of
information from the PDF will be really easy (you will only need to add more
HTML input fields with instructions about what you want to extract from the
PDF file). The idea is that you could be able for example to extract specific
items from the documents, like captions, tabular data, authorship,
institutions, etc.

![](http://img10.imageshack.us/img10/5364/pdftranscribe1.png)

The provided script for creating the tasks is very simple: you only need to
tell the script where is the PDF file hosted, the URL, and which pages you
want to convert as tasks. By default, this demo explores the 14 pages of the
example PDF file.

Info You can download the PDF file used in this demo
[here](http://cdn.mozilla.net/pdfjs/tracemonkey.pdf).

Based on the answer of the users, we will be able to transcribe the pages,
distributing the tasks (thanks to PyBossa) to different users and volunteers.

__ Note If you want to learn more about how to use this application as a
template, check the:

  * [source code](http://github.com/PyBossa/pdftranscribe)
  * [Google Docs Spreadsheet Task template for the application](https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdEVVamc0R0hrcjlGdXRaUXlqRXlJMEE&usp=sharing)
  * [the official documentation of PyBossa](http://docs.pybossa.com/) and 
  * [the step by step tutorial.](http://docs.pybossa.com/en/latest/user/tutorial.html)

Logo image courtesy of
[TempusVolat](http://www.flickr.com/photos/mrmorodo/8174824430/)

* * *

