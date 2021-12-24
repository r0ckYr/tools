#hide desktop icons
gsettings set org.gnome.desktop.background show-desktop-icons false
gsettings set org.gnome.shell.extensions.desktop-icons show-trash false
gsettings set org.gnome.shell.extensions.desktop-icons show-home false

#move dock to bottom
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM

#disable dock
gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed false

#show dock when there is no app
gsettings set org.gnome.shell.extensions.dash-to-dock intellihide false

#transparent dock
gsettings set org.gnome.shell.extensions.dash-to-dock transparency-mode 'FIXED'
gsettings set org.gnome.shell.extensions.dash-to-dock background-opacity 0.2

#reset transparency
gsettings reset org.gnome.shell.extensions.dash-to-dock background-opacity
gsettings reset org.gnome.shell.extensions.dash-to-dock background-opacity

#backlit on running apps
gsettings set org.gnome.shell.extensions.dash-to-dock unity-backlit-items false
