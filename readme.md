# Kronos Log In/Out

This works like a timestamp toggle script, i.e. executing it is the same as
pressing the timestamp button on your Kronos timecard.

This script should be run twice a day, in the morning to log you in and once
more to log you out.  Take care in attempting to logout close to midnight.  The
request process may take up to a minute and the clock on your local machine may
not be synced with the clock on the Kronos server.

## Setup

-   Do some Kronos detective work.  Find the pages that correspond to:
    -   The referer page, usually something like `http://kronos.workplace.com`
    -   The actual login page, usually ending in `logon.jsp`
    -   The logged-in home page
    -   The timestamp link

-   Edit the configuration file with your details.

-   Setup cron job.  For example


    00 10 * * * python ~/projects/kronos/kronos-logout.py
    58 21 * * * python ~/projects/kronos/kronos-logout.py

