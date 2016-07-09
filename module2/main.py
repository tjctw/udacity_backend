# Copyright 2016 Google Inc.
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

import webapp2
from valid_year import *
from valid_day import *
from valid_month import *
# use post method for this will reslut a 405 method not exist response code.
form = """
<form method="post">
What is your birthday?
<br>
    <label> Month
        <input type="text" name="month">
    </label>
    <label> Day
    <input type="text" name="day">
    </label>
    <label> Yeat
    <input type="text" name="year">
    </label>
<br>
<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_year = valid_year(self.request.get('year'))
        user_day = valid_day(self.request.get('day'))

        if not(user_month and user_day and user_year):
            self.response.write(form)
        else:
            self.response.write("Thanks! That's a valid date.")

class TestHandler(webapp2.RequestHandler):
    def post(self):
        # q = self.request.get("q")
        # self.response.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),('/test', TestHandler)
], debug=True)
