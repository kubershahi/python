import re

text_to_search = ''' 
abcdefghijklmnopqrst
ABCdEFGHIJLMNOPQRST
1234567890

Ha Haha Hahha
Metacharacters needs to be escaped: 
. ^ $ * + ? { } [ ] / \ | ( )

coremys.com
facebook.com

321-555-4321
657.789.4566
657*789*4566
657,789,4566
800-789-4566
900-789-4566

Mr. Schafer
Mr Gaffer
Mr. T
Ms Patel
Mrs. Nepal
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu 
corey_schufer@university.edu.in
corey-321-schafer@my-work.net
corey-321-schafer@my-work.net.net

'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.com
https://www.ashoka.edu.in

'''

sentence = "Start a sentence and then bring it to the end"

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)(\.\w+)*')
# pattern = re.complile(r'start', re.I)  # ignores the case

matches = pattern.finditer(urls)  	# findall will return the matches as a string or groups in tuples 
									# match returns match at the begining or a sentence 
									# search returns match at the whole of a sentence 

subbed_urls = pattern.sub(r'\2\3\4')

for match in matches:
	print(match)

print(subbed_urls)
	




