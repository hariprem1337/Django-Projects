from django.shortcuts import render
from django.http import HttpResponse

def showIndex(http_request):
    message='''
            <html>        
              <body align="center" bgcolor="burlywood">
                <form action="sample">
                  <h1><u>Registration Form</u></h1><br><br>
                  <input type="text" placeholder="First Name" required>*<br><br>
                  <input type="text" placeholder="Last Name" required>*<br><br>
                  <input type="number" placeholder="Mobile Number" required>*<br><br>
                  <input type="email" placeholder="Email Id" required>*<br><br>
                  <input type="number" placeholder="Age" min="1" max="100" required>*<br><br>
                  Male <input type="radio" name="Gender">
                  Female <input type="radio" name="Gender">
                  Others <input type="radio" name="Gender"><br><br>
                  <select>
                    <option>Python</option>
                    <option>Django</option>
                    <option>Java</option>
                    <option>Dot Net</option>
                  </select><br><br>
                  <select multiple>
                    <option>Python</option>
                    <option>Django</option>
                    <option>Java</option>
                    <option>Dot Net</option>
                  </select><br><br>
                  <button type="submit">Register</button>
                  <button type="reset">Reset</button>
                </form>
              </body>
            </html> '''
    return HttpResponse(message)
