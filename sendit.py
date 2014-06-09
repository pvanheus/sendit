#!/usr/bin/env python

import smtplib
import email.mime.image
import argparse
import sys
import datetime

parser = argparse.ArgumentParser(description='Mail an image to a given address')
parser.add_argument('--smtp_server', default='smtp.mweb.co.za', help='SMTP server to use for mailing')
parser.add_argument('--smtp_port', default=25, type=int, help='SMTP port to use')
parser.add_argument('--from_address', default='Image Sending Server <pvh@webbedfeet.co.za>', help='Address that message should originate from')
parser.add_argument('--count_file', default=open('/etc/scanbuttond/count.txt', 'r'), type=argparse.FileType('r'), help='File containing count of scans used in name of image. Must be writeable by user running sendit.py')
parser.add_argument('destination', help='Email addresses to send to (comma separated)')
parser.add_argument('image_file', nargs='?', default=sys.stdin, type=argparse.FileType(), help='File containing image')
args = parser.parse_args()

try:
    count = int(args.count_file.next()) + 1
except ValueError:
    count = 1
except  StopIteration:
    count = 1
args.count_file = open(args.count_file.name, 'w')
args.count_file.write(str(count) + '\n')
args.count_file.close()

email_addresses = args.destination.split(',')
msg = email.mime.image.MIMEImage(args.image_file.read())
msg['From'] = args.from_address
msg['Subject'] = 'Image at ' + datetime.datetime.now().strftime('%a %d %m %Y %H:%M:%S')
msg['Content-Disposition'] = 'attachment; filename=scan.jpg'
server = smtplib.SMTP(args.smtp_server, args.smtp_port)
for address in email_addresses:
    address = address.strip()
    msg['To'] = address
    server.sendmail(args.from_address, address, msg.as_string())
server.quit()
