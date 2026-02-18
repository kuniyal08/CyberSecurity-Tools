#!/bin/bash

if ["$#" != "2" ]; then #Checking If there are 2 arguments Id and pwd. if yes then we echo out the following.
    echo "Credentials-Parser. A breached domain parsing tool."
    echo " "
    echo "Usage: breach-parse <domain to search> <file to output>"
    echo " "
    echo 'For multiple domains: breach-parse "<domain to search>|<domain to search>" <file to output>'
    echo 'Example: breach-parse "@gmail.com|@yahoo.com" multiple.txt'
    exit 1

else
        fullfiles=$2
        fbname=$(basename "$fullfile" | cut -d. -f1) #taking the basename of the file, removing the period. Then we enter it into the 3 following files
        master=$fbname-master.txt
        ysers=$fbname-users.txt
        passwords=$fbname-passwords.txt

        touch $master
        total Files=$(find /opt/breach-parse/BreachCompilation/data -type f |wc -l)
        file count = 0 #Placeholder for the progressbar done below

        function ProgressBar {

            let _progress=($(file_Count)*100/$(total_Files)*100)/100
            let _done=(${_progress}*4)/10
            let _left=40-$_done

            _fill=$(printf "%${_done}s")
            _empty=$(prinf "%${    }")
        }
