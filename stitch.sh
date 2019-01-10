#!/bin/bash
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# file: stitch.sh
# date: 2019-01-10
# description: stichtes pdf files together
# requires pdfunite as a part of the poppler library
##########################################################################################

# pdfunite syntax
# $pdfunite file_A.pdf file_B.pdf ... target.pdf
# The list of pdf files after the pdfcommand will be 
# stichted together in the specified order and
# saved in the last target pdf file (here "target.pdf").

pdfunite \
	file_A.pdf \
	file_B.pdf \
	file_C.pdf \
	file_D.pdf \
	file_E.pdf \
	target.pdf
