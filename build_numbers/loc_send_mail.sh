#!/bin/sh

mail -s "New release in local 1911" nuthanc@juniper.net < /dev/null

date_occ=`date`
touch /home/nuthanc/build_numbers/date
echo "$date_occ">>/home/nuthanc/build_numbers/date