#!/bin/bash

find ./data -maxdepth 4 -type f -name "*.log" -exec rm -f {} \;

