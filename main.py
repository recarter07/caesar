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

# import webapp2 as usual, and cgi for escape_html method:
import webapp2
import cgi

# from the caesar.py doc, import the prev defined method called "encrypt"
from caesar import encrypt

#define escape_html method:
def escape_html(s):
    return cgi.escape(s, quote = True)

# general functionality of main.py
# given example:
#answer = encrypt("Hello, Zach!", 2)
#print(answer)
# => prints Jgnnq, Bcej!

# define answer via imported encrypt method:
answer = encrypt("%(text)s", 8)
print(answer)

# define the form format:
form="""
<form method="post">
    <label>
    <b>Enter some text please.</b><br>
    <input type="textarea" name="q" style="height: 25px; width: 400px; value="%(text)s">
    </label>
    <br>
    <label for "rot"> Rotation Amount </label>
    <br>
    <input type=number name="rot" value="{0}">
    <br>
    <div style="color: blue">%(error)s</div>
    <br>
    <input type="Submit">
</form>
"""

#form.format("Hello")
#alternative textarea code:
#<textarea name="text" style="height: 100px; width: 400px;">wxy;</textarea>


class MainHandler(webapp2.RequestHandler):
    # define write_form method with blank defaults:
    def write_form(self, error="", text="", rot="5"):
        self.response.write(form % {"error": escape_html(error),
                                    "text": escape_html(text),
                                    "0": rot})

    # write form using above write_form method with blank defaults:
    def get(self):
        self.write_form()
        # if you used the below method, you'd be using any input as defaults:
        #self.response.write(form)

    # return form with encrypted answer:
    def post(self):
        self.response.write(answer)


# usual footer, webapp2 and debugger:
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
