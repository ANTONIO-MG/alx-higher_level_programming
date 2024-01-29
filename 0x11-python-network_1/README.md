In this Project we explore the usage of the URLLIB module in python
to get content from url's, each file handles a specific function as
listed below:

0-hbtn_status.py
This Python script fetches the status of the URL
https://alx-intranet.hbtn.io/status
using the urllib package. The response body is
displayed with information about its type and content.

1-hbtn_header.py
This Python script takes a URL as input, sends a
request using urllib, and displays
the value of the X-Request-Id variable
found in the header of the response.

2-post_email.py
This Python script takes a URL and an email as input,
sends a POST request to the
specified URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).

3-error_code.py
This Python script takes a URL as input,
sends a request using urllib, and displays
the body of the response. It handles urllib.error.
HTTPError exceptions and prints the HTTP status code in case of an error.

4-hbtn_status.py
This Python script fetches the status of the
URL https://alx-intranet.hbtn.io/status
using the requests package. The response body is
displayed with information about its type and content.

5-hbtn_header.py
This Python script takes a URL as input, sends
a request using requests, and displays
the value of the X-Request-Id variable in the response header.

6-post_email.py
This Python script takes a URL and an email
as input, sends a POST request to the
specified URL with the email as a parameter using requests,
and displays the body of the response.

7-error_code.py
This Python script takes a URL as input, sends
a request using requests, and displays
the body of the response. If the HTTP status code is
greater than or equal to 400, it prints an error
message with the HTTP status code.

8-json_api.py
This Python script takes a letter as input,
sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter using requests. 
It displays the user id and name if the response
body is properly formatted and not empty.

10-my_github.py
This Python script takes GitHub credentials
(username and personal access token) as input,
uses Basic Authentication with the GitHub API,
and displays the user id using the requests package.
The personal access token is used as the password for authentication