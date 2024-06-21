# Why?

Because I had to learn the hard way that my game saves are not stored in the ROM directories in Knulli (and possibly Batocera), but in /userdata/saves. So I wrote this little Python script to simplify the backup process, which was only tested on my Trimui Smart Pro, but should work on other systems running Knulli / Batocera.

## Installation

Unfortunately some manual tinkering is necessary:
- download the knullibackup.zip file from the repo and extract it **preserving the directory structure** to the /userdata/roms/pygame directory on your device (this is the \roms\pygame directory if you access your device via the SMB file share). After succesfully extracting the archive you will have the following files under /userdata/roms/pygame/knullibackup:
```
knullibackup.png
knullibackup.pygame
settings.py
```
## Configuration
- if you want a _fancy_ entry in the Pygame section of your main  icon somefirst and foremost paste the content of gamelist_insert.xml into the gamelist.xml file in the 
- you will need to edit the settings.py file to configure a backup destination for you game saves. The file looks like this:
```
def init():
    global TARGZDIR
    global TARGZPREFIX
    global BACKUPDIR

    global SCPENABLE
    global SCPKEY
    global SCPTARGET

    global SMBENABLE
    global SMBUSER
    global SMBPASSWORD
    global SMBSHARE
    global SMBDIRECTORY
        
    # archive name looks like $[TARGZPREFIX]-YYYMMDD-HHMMSS.tar.gz
    TARGZDIR="/tmp"
    TARGZPREFIX="savestate-trimui-"
    # this is the default directory for game saves - you can backup the whole /userdata folder
    # if you want by modifying this variable
    BACKUPDIR="/userdata/saves"

    # SMB specific stuff
    SMBENABLE=True
    SMBUSER="username"
    SMBPASSWORD="password"
    SMBSHARE="//192.168.1.200/fileshare"
    SMBDIRECTORY="backup/directory"

    # SFTP specific stuff
    SCPENABLE=False
    # create the necessary key by executing this command from a command shell on your device:
    # dropbearkey -t ed25519 -f ~/.ssh/id_dropbear
    # don't forget to add the public key to the authorized_keys file on your server!
    SCPKEY="~/.ssh/id_dropbear"
    # this is the SCP target, including the username, server name/IP and the backup target directory
    SCPTARGET="username@192.168.1.200:/backup/directory"
```
The parameters that need to be tailored to your needs are under the SMB and SFTP specific sections. Here you can enable or disable the respective file transfer method by changing the SMBENABLE and SCPENABLE variables to True or False and set up your file paths and credentials.
