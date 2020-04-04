#!/bin/sh


python /app/realbackend/manage.py migrate
python /app/realbackend/manage.py runserver 0.0.0.0:8000



# cd `dirname $0`
# dir=`pwd`
# echo $dir
