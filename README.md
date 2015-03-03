# Hedging in Spanish

Source code and documentation for research project on hedges

- Author: Javier Llaca
- Speech Lab, Department of Computer Science, Columbia University

## Overview

This program detects and tags potential hedges in Spanish text.

More specifically, the program goes through a Spanish corpus,
extracts usable text, analyzes it, and produces a csv file for 
use in a crowd-sourcing task.

The csv file contains random and evenly-distributed instances 
of possible hedges in the corpus.

This repository also contains a series of scripts for data analysis.

## Dependencies

Java Libraries:
- [Apache OpenNLP](https://opennlp.apache.org)
- [Apache Commons CSV](http://commons.apache.org/proper/commons-csv/)

## Encoding

In order to account for non-ASCII characters in Spanish data,
programs are compiled and executed using UTF-8 encoding.
