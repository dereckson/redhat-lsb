# Makefile for source rpm: redhat-lsb
# $Id$
NAME := redhat-lsb
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
