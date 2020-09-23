#!/bin/bash
sed "s/[\(|\)]//g" *.html
sed 's/\./-/g'
sed 's/ /-/g'

