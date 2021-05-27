# Python task reminder:

## File format
```
File format: 
    [date/timing info] Task name
Date:
    Simply put the date in dd/mm/yy format
    dd/mm/yyyy also accept
    dd/mm also accpeted, just assumes it is this year
    no leading zero needed, so 1/2/21 would be valid

    '.' as a separator instead of '/' aslo accepted
    You can also mix the seperators if you wish
Other timing info:
    If you want to have a task each monday then do:
    [Mon] task name
    If you want to be it every 2nd week on monday:
    [Mon 2] task name (it will start with the first
        week of the year and continue in the rythm)
    If you want to be it the same as above, but
        offsetted by 1 week:
    [Mon 2 1]

    So generally speaking it's like this:
    [Weekday | every Nth week | +/- offset] 
    (without the "|" in between, is just for readability)

    Accepted as weekdays would be:
    Mon,Tue,Wed,Thu,Fri,Sat,Sun
Task name:
    Has to be in one line
```

## How to setup (work in progress)
```
For now the code doesn't really do anything
but this would be a guide on how to set it up once it's done.

1. Create/Select a gmail account you want to use.
2. Enable less secure apps for it with this link:
    https://myaccount.google.com/lesssecureapps
3. Create and edit the tasks.txt file
4. Upload all the files on where you want to host it and keep the app running

```