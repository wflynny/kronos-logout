# Kronos Log In/Out

This works like a timestamp toggle script, i.e. executing it is the same as
pressing the timestamp button on your Kronos timecard.

This script should be run twice a day, in the morning to log you in and once
more to log you out.  Take care in attempting to logout close to midnight.  The
request process may take up to a minute and the clock on your local machine may
not be synced with the clock on the Kronos server.

**Advisory**: Make sure you consult your supervisor before using this script.
You may be responsible for accurate time reporting, and in that case the use of
this script may be unethical.

It was often the case as a graduate student that, due to administrative
constraints, my summer stipend would be divided up into an hourly wage with a
maximum number of loggable hours, the sum of which was the entire stipend.  This
script was a way to ensure my summer stipend would be evenly distributed
throughout the summer.  For example, despite working 60+ hours/week, I could
only log 35 at a given rate such that after 8 weeks I would be allotted my
entire stipend.  I used this script to log 7 hours per work day (8 hours - 1
hour for lunch).

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

