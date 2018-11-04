########################################################################
#
# Makefile for colourize pre-built ML model
#
########################################################################

# List the files to be included in the .mlm package.

MODEL_FILES = 			\
	configure.sh		\
	demo.py			\
	display.py		\
	score.py		\
	utils.py		\
	images			\
	data/pts_in_hull.npy	\
	README.txt		\
	DESCRIPTION.yaml

# Include standard Makefile templates.

include ../mlhub.mk
include ../git.mk
include ../pandoc.mk

$(MODEL).RData: train.R
	Rscript $<

clean::
	rm -rf README.txt

realclean:: clean
	rm -rf *.pdf *~
