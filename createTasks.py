#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

from optparse import OptionParser
import pbclient

if __name__ == "__main__":
    # Arguments for the application
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    # URL where PyBossa listens
    parser.add_option("-s", "--server", dest="api_url",
                      help="PyBossa URL http://domain.com/", metavar="URL")
    # API-KEY
    parser.add_option("-k", "--api-key", dest="api_key",
                      help="PyBossa User API-KEY to interact with PyBossa",
                      metavar="API-KEY")
    # Create App
    parser.add_option("-c", "--create-app", action="store_true",
                      dest="create_app",
                      help="Create the application",
                      metavar="CREATE-APP")
    # PDF file URL
    parser.add_option("-f", "--file-pdf",
                      dest="pdf_url",
                      help="PDF File URL",
                      metavar="PDF-FILE-URL")

    # PDF file pages
    parser.add_option("-p", "--pages-pdf",
                      dest="pdf_pages",
                      help="PDF File Pages",
                      metavar="PDF-FILE-PAGES")

    # Update template for tasks and long_description for app
    parser.add_option("-u", "--update-template", action="store_true",
                      dest="update_template",
                      help="Update Tasks template",
                      metavar="UPDATE-TEMPLATE"
                     )

    # Update tasks question
    parser.add_option("-q", "--update-tasks", action="store_true",
                      dest="update_tasks",
                      help="Update Tasks question",
                      metavar="UPDATE-TASKS"
                     )

    parser.add_option("-x", "--extra-task", action="store_true",
                      dest="add_more_tasks",
                      help="Add more tasks",
                      metavar="ADD-MORE-TASKS"
                      )
    # Modify the number of TaskRuns per Task
    # (default 30)
    parser.add_option("-n", "--number-answers",
                      dest="n_answers",
                      help="Number of answers per task",
                      metavar="N-ANSWERS"
                     )

    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")
    (options, args) = parser.parse_args()

    if not options.api_url:
        options.api_url = 'http://localhost:5000/'
        pbclient.set('endpoint', options.api_url)

    if not options.api_key:
        parser.error("You must supply an API-KEY to create an \
                      applicationa and tasks in PyBossa")
    else:
        pbclient.set('api_key', options.api_key)

    if not options.pdf_url:
        options.pdf_url='http://cdn.mozilla.net/pdfjs/tracemonkey.pdf'
        print("Using default PDF file from Mozilla")

    if not options.pdf_pages:
        options.pdf_pages = 14
        print ("Using the number of pages of the default PDF file from Mozilla")

    if (options.verbose):
        print('Running against PyBosssa instance at: %s' % options.api_url)
        print('Using API-KEY: %s' % options.api_key)

    if not options.n_answers:
        options.n_answers = 100

    if options.create_app:
        pbclient.create_app('PDF Transcription',
                'pdftranscribe',
                'Help us to transcribe this PDF file')
        app = pbclient.find_app(short_name='pdftranscribe')[0]
        app.long_description = open('long_description.html').read()
        app.info['task_presenter'] = open('template.html').read()
        app.info['thumbnail'] = "http://img152.imageshack.us/img152/3987/pdftranscribe.png"


        pbclient.update_app(app)
        for page in range(1,15):
            # Data for the tasks
            task_info = dict(question="Transcribe the following page",
                        page=page,
                        pdf_url='http://cdn.mozilla.net/pdfjs/tracemonkey.pdf')
            pbclient.create_task(app.id, task_info)

    else:
        if options.add_more_tasks:
            for page in range(1,options.pdf_pages + 1):
                # Data for the tasks
                task_info = dict(question="Transcribe the following page",
                            page=page,
                            pdf_url=options.pdf_url)
                pbclient.create_task(app.id, task_info)

    if options.update_template:
        print "Updating app template"
        app = pbclient.find_app(short_name='pdftranscribe')[0]
        app.long_description = open('long_description.html').read()
        app.info['task_presenter'] = open('template.html').read()
        app.info['tutorial'] = open('tutorial.html').read()
        pbclient.update_app(app)

    if options.update_tasks:
        print "Updating task question"
        app = pbclient.find_app(short_name='pdftranscribe')[0]
        for task in pbclient.get_tasks(app.id):
            task.info['question'] = u'Transcribe'
            pbclient.update_task(task)

    if not options.create_app and not options.update_template\
            and not options.add_more_tasks and not options.update_tasks:
        parser.error("Please check --help or -h for the available options")
