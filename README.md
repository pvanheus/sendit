sendit.py
=========

Simple script to send an image as an email attachment to a comma separated list of addresses. The image is provided
on stdin or optionally by a filename argument.

This script can be used with scanbuttond, SANE and ImageMagick to email an image from a scanner, using this command
in the buttonpressed.sh shell script:

    /usr/bin/scanimage -x 215 -y 297 --resolution 100 --mode Gray |/usr/bin/convert -resize 768 pgm:- jpeg:- |/usr/local/bin/sendit.py pvh@webbedfeet.co.za

or for a colour and higher resolution image:

    /usr/bin/scanimage -x 215 -y 297 --resolution 300 --mode Color |/usr/bin/convert -resize 1024 pnm:- jpeg:- |/usr/local/bin/sendit.py pvh@webbedfeet.co.za

