#!/bin/bash
# anuy description
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
