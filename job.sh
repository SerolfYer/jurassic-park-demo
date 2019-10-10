#!/bin/bash
#User logged into the app requests QR code
export ROOT_TOKEN=$(vault token create -ttl=60s | awk 'NR==3 {print $2}')

python python.py
