#!/bin/sh
curl --preproxy socks5://127.0.0.1:1080 -L -H "Cache-Control: no-cache" -O $1
