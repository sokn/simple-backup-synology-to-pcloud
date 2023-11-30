# simple-backup-synology-to-pcloud
A simple periodic backup of folders for Synology without paying any to cloud to cloud service
Using synology build in function user define script to zip and copy the file to a remote folder, which is a SMB share drive hosted by NAS itself in a VM with pcloud client installed, automatically copy any file from SMB share to pcloud

# Dumb work around for user don't want to mod your synology. And should work to any kind of cloud service with client

1. create a linux vm in synology, install the offical pcloud client
2. set up a SMB share
3. remote mount to synology
4. copy user-define script to scheduled task, change to the path you want to backup
5. run python in VM

Done


