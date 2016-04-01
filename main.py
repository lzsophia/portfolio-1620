#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2
from google.appengine.api import mail

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(self.request.path)
        logging.info("Test")
        try:
            template = JINJA_ENVIRONMENT.get_template('templates%s.html' % self.request.path)
            self.response.write(template.render({'name': self.request.path}))
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'name': 'index'}))


class MailHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'name': '/contact'}))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'msg': 'Your message has been sent.'}))
        name=self.request.get('name')
        phone=self.request.get('phone')
        email=self.request.get('email')
        message=self.request.get('message')
        mail.send_mail(sender="<name@portfolio-1620.appspotmail.com>",
              to="Zhe Li <lzsophia@umich.edu>",
              subject="Website Contact Form",
              body="You have received a new message from your website contact form.\n\nHere are the details:\n\nName: "+name+"\n\nEmail: "+email+"\n\nPhone: "+phone+"\n\nMessage: "+message
)


app = webapp2.WSGIApplication([
    ('/contact', MailHandler),
    ('/.*', IndexHandler)
], debug=True)
