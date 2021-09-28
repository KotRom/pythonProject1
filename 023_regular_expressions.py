import re

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''

pattern = re.compile(r'(http://|https://)*(www\.)*([a-z]+\.[a-z]{2,3})')
matches = pattern.finditer(urls)
for match in matches:
    #print(match)
    print(match.group(2, 3))

subbed_urls = pattern.sub(r'Hello, my website is \2\3', urls)  # vyvod 2 i 3 gruppu iz pattern
print(subbed_urls)
