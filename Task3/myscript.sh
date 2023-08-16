#!/bin/bash

grep -oE '([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);' input.txt | awk -F';' '{print $4 "\t" $5}' > output.tsv
