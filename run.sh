#!/bin/bash

name=$1

if [ "${name}" == '' ] ; then
  echo 'please specify your name.'
  exit 0
fi


poetry run ./manage.py greet --name ${name}
