#!/bin/bash

if [[ $(id -u) != 0 ]]; then
    echo "Not running as root, bailing out!"
    exit 1
fi

systemctl disable --now autosyncoid.timer
rm /usr/local/sbin/autosyncoid.py
rm /etc/systemd/system/autosyncoid.{service,timer}
systemctl daemon-reload

diff autosyncoid.example.yaml /etc/sanoid/autosyncoid.yaml > /dev/null 2>&1

if [[ $? != 0 ]]; then
    echo "/etc/sanoid/autosyncoid.yaml not same as default, not touching."
else
    rm /etc/sanoid/autosyncoid.yaml
fi

echo "If you haven't seen any errors, then uninstall is complete! Thanks for playing!"