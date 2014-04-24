#!/usr/bin/env python

#makefaq -- a script for generating the frequently asked questions page

import os
import glob


faqfile = 'faq.html'
if os.path.isfile(faqfile): os.remove(faqfile)


#build header string
header_str = """
<!doctype html>
<head>

   <meta name="description" content="Resources for git and github">
   <meta name="author" content="Steve Crawford">
</head>

<body>
"""

#for each question in file list, read it in and parse it
file_list = glob.glob('questions/q*txt')
question_str=''
for f in file_list:
    text = open(f).read().split('\n')
    print text
    found =False
    for t in text:
	if t.startswith('Question'):
	   question_str += '<h3> %s </h3>' % t
	   found=True
	elif t.startswith('Answer') and found:
	   question_str += '<p> %s </p>' % t
	   found=True
    question_str += '<br>\n'

#write results to file
fout = open(faqfile, 'w')
fout.write(header_str+question_str+'</body>')
