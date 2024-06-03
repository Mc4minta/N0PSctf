#!/bin/bash
cat discord-message.txt | xxd -r -p | grep "N0PS{.*}" > flag.txt && cat flag.txt
