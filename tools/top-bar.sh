#!/bin/bash

status1=`gdbus call --session --dest org.gnome.Shell --object-path /org/gnome/Shell --method org.gnome.Shell.Eval string:'Main.panel.actor.visible;'`
status2=`gdbus call --session --dest org.gnome.Shell.Extensions --object-path /org/gnome/Shell/Extensions --method org.gnome.Shell.Extensions.GetExtensionInfo ubuntu-dock@ubuntu.com | grep "'state': <2.0>" >/dev/null && echo "OFF" || echo "ON"`


if [ "$status1" == "(true, 'false')" ]; then
gdbus call --session --dest org.gnome.Shell --object-path /org/gnome/Shell --method org.gnome.Shell.Eval 'Main.panel.actor.show();'
else
gdbus call --session --dest org.gnome.Shell --object-path /org/gnome/Shell --method org.gnome.Shell.Eval 'Main.panel.actor.hide();'
fi

if [ "$status2" == "ON" ]; then
gdbus call --session --dest org.gnome.Shell.Extensions --object-path /org/gnome/Shell/Extensions --method org.gnome.Shell.Extensions.DisableExtension ubuntu-dock@ubuntu.com
else
gdbus call --session --dest org.gnome.Shell.Extensions --object-path /org/gnome/Shell/Extensions --method org.gnome.Shell.Extensions.EnableExtension ubuntu-dock@ubuntu.com
fi
