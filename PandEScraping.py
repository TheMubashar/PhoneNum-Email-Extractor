
import pyperclip
import re

PhoneNumberRegex = re.compile(r'\d{11}')
emailregex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
)''',re.VERBOSE)

message="phone Number: 03212365247 JS_6S2@gmail.com f2013_4@bnu.edu.pk Daggerx45@outlook.com 03055462423 Info@nostarch.com media@nostarch.com academic@nostarch.com help@nostarch.com"

PhoneNumbers = PhoneNumberRegex.findall(message)
emails = emailregex.findall(message)

file = open("extractedInfo.txt", "w")
file.write("Phone Number:\n")

for PhoneNumber in PhoneNumbers:
    file.write(PhoneNumber+'\n')

file.write("Email Address:\n")
for email in emails:
    file.write(email+'\n')

print('please check your folder.')
