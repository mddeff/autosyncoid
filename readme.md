# autosyncoid

This is just my collection of scripts/systemd unit files that I use to wrap around Jim Salters' [syncoid](https://github.com/jimsalterjrs/sanoid) utility.  I am in no way affiliated with the sanoid/syncoid projects, nor am I associated with any official ZFS development projects.  See [disclaimer](#disclaimerwarranty).


## Tested on
- CentOS{7,8}

## Install


```bash
git clone https://github.com/mddeff/autosyncoid
cd autosyncoid
pip install -r requirements.txt # really we're just installing `pyyaml` here, you may already have it...
./install.sh
```
You'll get a message saying:
```
If you haven't seen any errors, then setup is complete! 
    Edit /etc/sanoid/autosyncoid.yaml and run
    
    systemctl enable --now autosyncoid.timer
    
    And you'll be good to go!
```

Do what it tells you, and you're off!

## Uninstall
```bash
cd autosyncid
./uninstall.sh
```

Thats it!

## Contributions welcome!
PRs will be reviewed as time allows (read: this project isn't my full time job).  PR that break functionality or 'opinionate' the tool in a drastically different direction will be respectfully declined.  

I.e. if you want to change paths/add support for another init system, you can, but you must include the logic in `install.sh` and `uninstall.sh` to behaive correctly in already [tested](#tested-on) setups.

## Disclaimer/Warranty
TL;DR - Caveat Emptor.

This works for me but I make no gurantees it works for you, or that any of it is even a good idea.  Assume none of what I'm doing is best practice. I make no warranty express or implied of fitness for a particular purpose.
