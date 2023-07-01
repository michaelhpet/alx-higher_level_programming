#!/usr/bin/bash
# Display all HTTP methods server will accept
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2-
