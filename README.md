# lavastat
Discord bot written in python that reports server statistics as discord status. Current servers deployed: lava, icicle

Current features:
  - Live CPU utilization / load reporting as discord status
  - Live RAM / SWAP usage reporting as discord status
  - Live Uptime reporting as discord status

Lost previous progress so I have to re-add:
  - User count reporting as discord status
  - CPU temp reporting as discord status
  - Shell command that returns user count
  - Installation script (installs the aforementioned shell command as system command / sets up systemd service).

Plans / Goals:
  - Report every 4 hours samba and disk status as message
  - Alert (message) on new ssh session
  - PSU on-battery status alerts
  - Alert when a user uses sudo (with a cooldown ofc)
