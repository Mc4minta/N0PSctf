#!/bin/bash

cat morse-to-hex.txt | xxd -r -p | grep -o N0PS{.*} > flag.txt && cat flag.txt
