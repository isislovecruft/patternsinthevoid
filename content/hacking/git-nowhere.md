Title: Git Nowhere
Date: 2012-04-04 20:19
Author: isis agora lovecruft
Category: hacking
Tags: anonymity, bash, git

<!-- PELICAN_BEGIN_SUMMARY -->

[Arturo](https://twitter.com/#!/hellais) and I were going through our commit
logs for [ooni-probe](https://gitweb.torproject.org/ooni-probe.git) this
morning when he noted that git commits leak geodata through timezone
settings. I figured git would have an easy way to set the timezone to GMT, but
it turns out that it uses mktime() to get a struct representing the system
clock time. [There's a few hacks already](http://www.alexpeattie.com/blog/working-with-dates-in-git/)
for dealing with this, namely setting GIT\_AUTHOR\_DATE with the --date
command:

<pre class="prettyprint lang-bash">
$ git commit --date="Wed Feb 16 14:00 2037 +0100"
</pre>

This is not only annoying, but it also doesn't set GIT\_COMMITTER\_DATE,
so if you wrote the patch and also committed it to a repo, your timezone
still leaks.

<!-- PELICAN_END_SUMMARY -->

I thought this was all incredibly annoying, and I don't want to change
my system clock, so [I made a bash script](https://github.com/isislovecruft/configs/blob/master/scripts/gitdate.sh) to fix it:

<pre class="prettyprint lang-bash">
#!/bin/bash
#_____________________________________________________________________________
# Git Nowhere
#-----------------------------------------------------------------------------
#
# Use: Run as "$ . ./gitdate.sh" before "$ git commit" to manually set
# the date to GMT in order to obscure timezone-based geodata tracking.
#
# If you would always like your timestamps to be obscured for a specific
# project, then place this script in /usr/local/bin/. Next, edit
# /your_project_path/.git/hooks/pre-commit and place in it the following two
# lines:
#
# #!/bin/sh
# exec source /usr/local/bin/gitdate.sh
#
# @author Isis Lovecuft, 0x2CDB8B35 isis@patternsinthevoid.net
# @version 0.0.3
#
# v0.0.3: Also changes the months and years, because that would suck if your
#         commits were accidentally made last year
# v0.0.2: Changes the days too# v0.0.1: Changes the hours
#_____________________________________________________________________________

DAY=$(date | cut -d ' ' -f 1)
MONTH=$(date | cut -d ' ' -f 2)
DATE=$(date | cut -d ' ' -f 4)
TIME=$(date | cut -d ' ' -f 5)
TIMEZONE="+0000"YEAR=$(date | cut -d ' ' -f 7)
HOUR=$(echo "$TIME" | cut -d ':' -f 1)
MINUTE=$(echo "$TIME" | cut -d ':' -f 2)
SECOND=$(echo "$TIME" | cut -d ':' -f 3)

# Git uses the system time settings through mktime().  Do a "$ git log" to see
# the timezone offset for your system.  This script assumes -0700. For
# example, if "$ git log" says your timezone is -0500, you would change all
# occurences in the next code block of "7" to "5" and change "17" to "19".

TIMEOFFSET=7
if [ "$HOUR" -lt "17" ]; then
    let HOUR+=7else
    let TILMIDNIGHT=24-HOUR
    let FALSEDAWN=TIMEOFFSET-TILMIDNIGHT
    let HOUR=FALSEDAWN
fi

# If the hour is one digit, prepend a zero.
if [ "${#HOUR}" -eq "1" ]; then
    HOUR=$(printf "%02d" $HOUR)
fi

# If it is tomorrow in UTC, make sure we increment the day.
if [[ -n "$FALSEDAWN" ]]; then
    if [ "$DAY" = "Mon" ]; then
        NEXTDAY=$(echo "Tue")
    elif [ "$DAY" = "Tue" ]; then
        NEXTDAY=$(echo "Wed")
    elif [ "$DAY" = "Wed" ]; then
        NEXTDAY=$(echo "Thu")
    elif [ "$DAY" = "Thu" ]; then
        NEXTDAY=$(echo "Fri")
    elif [ "$DAY" = "Fri" ]; then
        NEXTDAY=$(echo "Sat")
    elif [ "$DAY" = "Sat" ]; then
        NEXTDAY=$(echo "Sun")
    elif [ "$DAY" = "Sun" ]; then
        NEXTDAY=$(echo "Mon")
    fi

    DAY=$NEXTDAY

    if [[ "$MONTH" = "Jan" ]] || [[ "$MONTH" = "Mar" ]] || [[ "$MONTH" = "May" ]] || [[ "$MONTH" = "Jul" ]] || [[ "$MONTH" = "Aug" ]] || [[ "$MONTH" = "Oct" ]] || [[ "$MONTH" = "Dec" ]]; then
        if [[ "$DATE" -lt "31" ]]; then
            let DATE+=1
        elif [[ "$DATE" -eq "31" ]]; then
            if [[ "$MONTH" = "Jan" ]]; then
                NEXTMONTH=$(echo "Feb")
            elif [[ "$MONTH" = "Mar" ]]; then
                NEXTMONTH=$(echo "Apr")
            elif [[ "$MONTH" = "May" ]]; then
                NEXTMONTH=$(echo "Jun")
            elif [[ "$MONTH" = "Jul" ]]; then
                NEXTMONTH=$(echo "Aug")
            elif [[ "$MONTH" = "Aug" ]]; then
                NEXTMONTH=$(echo "Sep")
            elif [[ "$MONTH" = "Oct" ]]; then
                NEXTMONTH=$(echo "Nov")
            elif [[ "$MONTH" = "Dec" ]]; then
                NEXTMONTH=$(echo "Jan")
                let YEAR+=1
            fi

            DATE=1
        fi
    elif [[ "$MONTH" = "Feb" ]] && [[ "$DATE" -lt "28" ]]; then
        let DATE+=1
    elif [[ "$MONTH" = "Feb" ]] && [[ "$DATE" -eq "28" ]]; then
        NEXTMONTH=$(echo "Mar")
        DATE=1
    elif [[ "$MONTH" = "Apr" ]] || [[ "$MONTH" = "Jun" ]] || [[ "$MONTH" = "Sep" ]] || [[ "$MONTH" = "Nov" ]]; then
        if [[ "$DATE" -lt "30" ]]; then
            let DATE+=1
        elif [[ "$DATE" -eq "30" ]]; then
            if [[ "$MONTH" = "Apr" ]]; then
                NEXTMONTH=$(echo "May")
            elif [[ "$MONTH" = "Jun" ]]; then
                NEXTMONTH=$(echo "Jul")
            elif [[ "$MONTH" = "Sep" ]]; then
                NEXTMONTH=$(echo "Oct")
            elif [[ "$MONTH" = "Nov" ]]; then
                NEXTMONTH=$(echo "Dec")
            fi

            DATE=1
        fi
    fi
    if [[ -n "$NEXTMONTH" ]]; then
        MONTH=$NEXTMONTH
    fi
fi
export GIT_AUTHOR_DATE=$(echo "$DAY $MONTH $DATE $HOUR:$MINUTE:$SECOND $YEAR $TIMEZONE")
export GIT_COMMITTER_DATE=$GIT_AUTHOR_DATE
unset NEXTMONTH
unset DAY
unset MONTH
unset DATE
unset HOUR
unset MINUTE
unset SECOND
unset YEAR
unset TIMEZONE
unset TILMIDNIGHT
unset FALSEDAWN
unset NEXTDAY
unset TIMEOFFSET
</pre>
