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
- you will need to edit the settings.py file to configure a backup destination for you game saves. The file looks like this:
```
```
