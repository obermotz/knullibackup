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
    SMBUSER="obermotz"
    SMBPASSWORD="Leondong9"
    SMBSHARE="//192.168.1.13/homes"
    SMBDIRECTORY="backup/Knulli"

    # SFTP specific stuff
    SCPENABLE=False
    # create the necessary key by executing this command from a command shell on your device:
    # dropbearkey -t ed25519 -f ~/.ssh/id_dropbear
    # don't forget to add the public key to the authorized_keys file on your server !
    SCPKEY="~/.ssh/dropbear"
    # this is the SCP target, including the username, server name/IP and the backup target directory
    SCPTARGET="obermotz@192.168.1.13:~/backup/Knulli"
