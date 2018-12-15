########################################################################
#
# Makefile for colourize pre-built ML model
#
########################################################################

# List the files to be included in the .mlm package.

MODEL_FILES = 			\
	configure.sh		\
	demo.py			\
	print.py		\
	display.py		\
	score.py		\
	utils.py		\
	images			\
	data/pts_in_hull.npy	\
	README.txt		\
	DESCRIPTION.yaml

# Include standard Makefile templates.

INC_BASE    = $(HOME)/.local/share/make
INC_PANDOC  = $(INC_BASE)/pandoc.mk
INC_GIT     = $(INC_BASE)/git.mk
INC_MLHUB   = $(INC_BASE)/mlhub.mk
INC_CLEAN   = $(INC_BASE)/clean.mk

ifneq ("$(wildcard $(INC_PANDOC))","")
  include $(INC_PANDOC)
endif
ifneq ("$(wildcard $(INC_GIT))","")
  include $(INC_GIT)
endif
ifneq ("$(wildcard $(INC_MLHUB))","")
  include $(INC_MLHUB)
endif
ifneq ("$(wildcard $(INC_CLEAN))","")
  include $(INC_CLEAN)
endif




$(MODEL).RData: train.R
	Rscript $<

clean::
	rm -rf README.txt

realclean:: clean
	rm -rf *.pdf *~
