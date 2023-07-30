#!/bin/bash
# This script downloads file with actual data about corona-virus from WHO official site.
# This script downloads json file with iso data about countries.


if mkdir upload; touch upload/countries.json
then
  echo 'Created upload/countries.json'
else
  echo 'Something wrong with creating file!'
fi

if wget https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json -O upload/countries.json
then
  echo 'File downloaded with name countries.xml'
else
  echo 'Something wrong with downloading file!'
fi
