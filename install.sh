#!/bin/bash

if [[ $(id -u) != 0 ]]; then
    echo "Not running as root, bailing out!"
    exit 1
fi

cp autosyncoid.py /usr/local/sbin/.
cp autosyncoid.{service,timer} /etc/systemd/system/.
systemctl daemon-reload
mkdir -p /etc/sanoid
cp autosyncoid.example.yaml /etc/sanoid/autosyncoid.yaml

echo "If you haven't seen any errors, then setup is complete! 
    Edit /etc/syncoid/autosyncoid.yaml and run
    
    systemctl enable autosyncoid.timer
    
    And you'll be good to go!"