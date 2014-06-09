sendit.py
=========

Simple script to send an image as an email attachment to a comma separated list of addresses. The image is provided
on stdin or optionally by a filename argument. The script maintains a count of the images it has sent, by default in
/etc/scanbuttond/count.txt. This file needs to be writeable by the user running the script (by default saned). The
count is used in the name of the scanned image so that they can be distinguished.

This script can be used with scanbuttond, SANE and ImageMagick to email an image from a scanner, using this command
in the buttonpressed.sh shell script:

```
/usr/bin/scanimage -x 215 -y 297 --resolution 100 --mode Gray |/usr/bin/convert -resize 768 pgm:- jpeg:- |/usr/local/bin/sendit.py pvh@webbedfeet.co.za
```

or for a colour and higher resolution image:

```
/usr/bin/scanimage -x 215 -y 297 --resolution 300 --mode Color |/usr/bin/convert -resize 1024 pnm:- jpeg:- |/usr/local/bin/sendit.py pvh@webbedfeet.co.za
```

Script options
--------------

--smtp_server: SMTP server to use for sending mail. Must support mail relaying using the combination of sender and destination you want to send to

--smtp_port: The port the SMTP server is listening on

--from_address: The address to be used as the 'From' address in the email. In general should be a valid email address

--count_file: The file to use to maintain a count of images sent. Must be writeable by the user running the script
