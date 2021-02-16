import re

text = """
https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477774#overview
http://www.icicibank.com/safe-online-banking/safe-online-banking.page
https://bcgmspcatalyst.okta.com/app/UserHome#
http://www.coursera.org/courses?query=e-learning
https://news.google.com/articles/CAIiEGnlD0k9rj4K5dsmjQ3SLUAqGQgEKhAIACoHCAowr6n9CjCr4PQCMI781QM?hl=en-IN&gl=IN&ceid=IN%3Aen
<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>
"""

pattern = re.compile(r"http[s]?://(www.)?\w+?(com|org|)")

print(pattern.findall(text))
