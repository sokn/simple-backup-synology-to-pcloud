# simple-backup-synology-to-pcloud
# For the usage of a simple periodic backup of folders for Synology without paying any to cloud to cloud service
# We use synology build in function user define script to zip and copy the file to a remote folder, which is a SMB share drive hosted by NAS itself
# on VM with pcloud client installed, copy any file from SMB share to pcloud\

1. create a linux vm in synology, install the offical pcloud client
2. set up a SMB share
3. remote mount to synology
4. copy user-define script to scheduled task, change to the path you want to backup
5. run python in VM

Done

# Dump work around for user don't want to mod your synology. And should work to any kind of cloud service with client
