#!/bin/bash
# This script downloads file with actual data about corona-virus from WHO official site.
# This script downloads json file with iso data about countries.
date=$(date +%F)

if wget https://dashboards-dev.sprinklr.com/data/9043/global-covid19-who-gis.json -O upload/statistic-$date.json
then
  echo 'File downloaded with name statistic-$date.json'
else
  echo 'Something wrong with downloading file!'
fi
