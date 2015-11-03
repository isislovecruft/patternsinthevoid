Title: Automated, Bandwidth-Efficient, and Encrypted Backups
Date: 2011-12-19 19:29
Author: isis agora lovecruft
Category: hacking
Tags: bash, cryptography

<!-- PELICAN_BEGIN_SUMMARY -->

I made a bash shell script to automate encrypted (remote or local) data
backups with [Duplicity](http://duplicity.nongnu.org/). Duplicity
uses asymmetric OpenPGP RSA keys to
encrypt a tarballs of specified files to be backed up, and it also
supports incremental backups. So, after making a full backup, it is more
efficient do to the fact that it only saves changes made to files and
not entirely new copies of files. Duplicity also supports versioning,
i.e. you can say "give me File A from 3 days ago".

Duplicity is *not* efficient in it's cryptographic design, as my friend
Tom wisely pointed out, in that use of asymmetric cryptographic
algorithms is heavily intensive upon processor resources, and it would
be better to replace this feature with something more along the lines of
the algorithms (e.g. AES, Serpent, and Twofish) and read/write speed
testing features which [TrueCrypt](http://www.truecrypt.org/) supports,
for example.

This script depends on both curl and a newer version of duplicity (which
is not yet included in the standard repositories), so to install those
dependencies in Debian-based distros do:

<pre class="prettyprint lang-bash">
    $ sudo apt-add-repository ppa:duplicity-team/ppa
    $ sudo apt-get update
    $ sudo apt-get install duplicity curl
</pre>

Here's version 0.1.2 of the backup script ([or view it on Github
here](https://github.com/isislovecruft/scripts/duplikat)):

<!-- PELICAN_END_SUMMARY -->

<pre class="prettyprint lang-bash">
#!/bin/bash
# _____________________
#| BACKUP[your].SH[it] |
#|---------------------|
#|v.0.1.2              |\                    ^    /^
#|Written by           | \                  / \  // \
#|Isis Lovecruft       |  \   |\___/|      /   \//  .\
#|isis@patternsinthe   |   \  /O  O  \__  /    //  | \ \           *----*
#|             void.net|     /     /  \/_/    //   |  \  \          \   |
#|_____________________|     @___@`    \/_   //    |   \   \         \/\ \
#                           0/0/|       \/_ //     |    \    \         \  \
#                       0/0/0/0/|        \///      |     \     \       |  |
#                    0/0/0/0/0/_|_ /   (  //       |      \     _\     |  /
#                 0/0/0/0/0/0/`/,_ _ _/  ) ; -.    |    _ _\.-~       /   /
#                             ,-}        _      *-.|.-~-.           .~    ~
#            \     \__/        `/\      /                 ~-. _ .-~      /
#             \____(oo)           *.   }            {                   /
#             (    (--)          .----~-.\        \-`                 .~
#             //__\\  \__ zomg!  ///.----..<        \             _ -~
#            //    \\               ///-._ _ _ _ _ _ _{^ - - - - ~
#
# Backup script to automate SSH, SCP, SFTP, FTP, and IMAP backups through
# Duplicity. Duplicity encrypts backup files through GPG before sending
# files through protocol. This script runs a check on the available 
# bandwidth, and only runs the backup when the bandwidth available is 
# above a configurable threshhold.
#
# This is going to be rewritten using duplicati instead of duplicity in the
# next major version release.

SPEED=$(curl -w %{speed_download} -o /dev/null -s http://speedtest.sea01.softlayer.com/speedtest/speedtest/random1000x1000.jpg)
INT=${SPEED/\.*}
KBPS=$(echo $[INT / 1024])
THRESHOLD="200"
# Uncomment and set the following in order to not type your password.
# This is incredibly insecure, as your password is then stored 
# plaintext.
#export PASSPHRASE='passphrase'

# The $SPEED variable downloads a nice image of snow (into /dev/null so that
# it isn't actually saved anywhere on disk). It also gives us a write-out 
# (-w %{speed_download}) for the average available bandwidth (incoming) in
# bytes per second.
#
# $INT turns the float $SPEED into an integer.
#
# $KBPS, as I'm sure you can surmise, turns the bytes per second into
# kilobytes per second.
#
# $THRESHOLD can be changed to fit the user's preferences, and it defines
# the minimum bandwidth which should be available for a duplicity backup to
# take place.

if [[ "$#" == "0" ]]; then
    echo ""
    echo "Usage: ./backup.sh <BACKUP_TO_LOCATION_1> <BACKUP_TO_LOCATION_2> ... <BACKUP_TO_LOCATION_N>"
    echo ""
    echo "Backup locations can be locally stored on the same disk (not recommended), "
    echo "or may be stored remotely. For remote backups, duplicity provides several "
    echo "options for transport, including SCP, FTP, and IMAP, please see 'man duplicity' "
    echo "for more information. Also, all duplicity backups are automatically GnuPG "
    echo "encrypted, so transportation is much safer than it would be otherwise. "
    echo ""
    echo "Note: Duplicity's SSH backend performs a check that the remote directory end "
    echo "in a '/', so this must be present for SSH, SCP, or SFTP backups to work correctly."
    echo ""
    exit 1
fi

# Make sure this script is run as root.
if [[ `id -u` != 0 ]]; then
    echo ""
    echo "Sorry, backups must be made as root in order for files in the / directory to"
    echo "be backed up safely. Please do 'sudo su' and try running this script again."
    echo "Exiting..."
    echo ""
    exit 1
fi

# Set up BACKUP_TO_LOCATION positional parameters.
for i in "$@"; do
    $(BACK_UP_LOCATION_$i)=$i
    echo ""
    echo "Would you like to make a full backup, or add an incremental backup to the "
    echo "last full backup stored?"
    select fullinc in "Full" "Incremental"; do
    case $fullinc in
            Full)
            USERLIST=$(cat /etc/passwd | grep "/home" | grep -E "([1-5][0-9]{3})|([5-9][0-9]{2})?" | cut -d : -f 1)
            # fix above regex to match '1000', '500' and '1392'
            # 
            # This command searches the password file for users with a home directory 
            # (to filter out programs with user accounts) whose UID number is in the 
            # range of 500-1599 (normal users, does not include root). It then takes 
            # that returned list of users and cuts it (the delimiter is ":") and returns 
            # only the first field, which is the username.
            echo ""
            echo "Please select the user(s) whose home directories should also be backed up:"
            echo ""
for users in $USERLIST; do
    # need a way to assign numbers like $1 $2 $3 to users
    select users in $USERLIST; do
        case $users in
            # so that those numbers can be passed in over here
            $@)
                echo "Please confirm that this is where you wish to store your full backup: ("$BACKUP_TO_LOCATION_$i")?"
                select yn in "Yes" "No"; do
                    case $yn in
                        Yes)
                            if [[ $KBPS -gt $THRESHOLD ]]; then
                                duplicity full -vN --ssh-askpass --exclude /proc \
                                    --exclude /mnt --exclude /media --exclude /tmp \
                                    --exclude /sys --exclude $HOME/.local \
                                    --exclude $HOME/.config --exclude /var/log \
                                    / $BACKUP_TO_LOCATION_$i
                            fi
                            break;;
                        No)
                            break;;
                    esac
                done
                break;;
        esac
    done
done
break;;

            Incremental)
                echo "Please confirm that this is where you wish to store your incremental backup: ("$BACKUP_TO_LOCATION_$i")?"
                select yn in "Yes" "No"; do
                    case $yn in
                        Yes)
                            if [[ $KBPS -gt $THRESHOLD ]]; then
                                duplicity incremental -vN --ssh-askpass \
                                    --exclude /proc --exclude /mnt --exclude /media \
                                    --exclude /tmp --exclude /sys --exclude $HOME/.local \
                                    --exclude $HOME/.config --exclude /var/log \
                                    / $BACKUP_TO_OCATION_$i
                            fi
                            break;;
                        No)
                            break;;
                    esac
                done
        esac
    done
done

unset PASSPHRASE

</pre>

This can be added as a [crontab](http://unixgeeks.org/security/newbie/unix/cron-1.html)
(so that the script, in this crontab
example, will run automatically, once per hour at one minute after the
hour) by doing (but the script will still check the network connection
before sending anything out).

If you have any comments, suggestion, or feature requests, please [email
me](mailto:isis@patternsinthevoid.net?Subject=Bash%20Backup%20Script)
and [my GPG public key is here](http://blog.patternsinthevoid.net/isis.txt).

Features yet to be added:

 * Differentiation between Wifi, Ethernet, and 3G/4G connections.

 * Support for cleaning up old backups and how often to do so.

 * Configurable setting for what percentage of the available bandwidth
   should be utilised.

 * ~~Fix the bug in Duplicity that makes it default to SFTP when SCP
   is called.~~
