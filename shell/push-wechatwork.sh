#!/usr/bin/env bash

set -ex

TEMPLATE="{\"msgtype\": \"markdown\", \"markdown\": {\"content\": \"# $MSG_TITLE\n > $MSG_CONTENT\n\n > 🔗 [View] $MSG_LINK\"}}"

echo $BOT_ID

echo $TEMPLATE | curl -s 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key='$BOT_ID \
   -H 'Content-Type: application/json' \
   --data-binary "@-"