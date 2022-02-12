def add_time(start, duration, day = False):
    dayslist = []
    x = start.split(":")
    hour = x[0]
    minutes = x[1]

    y = minutes.split()
    minutes2 = y[0]
    ap = y[1]

    dayslist.append("monday")
    dayslist.append("tuesday")
    dayslist.append("wednesday")
    dayslist.append("thursday")
    dayslist.append("friday")
    dayslist.append("saturday")
    dayslist.append("sunday")


    new_time = x

    m = duration.split(":")
    durhour = m[0]
    durmin = m[1]
    durday = round(int(durhour) / 24 + (int(durhour) % 24 > 0))

    if day:
        newday = str.lower(day)
        daypos = dayslist.index(newday)

    newhour = int(hour) + int(durhour)
    newmin = int(minutes2) + int(durmin)

    if int(newhour) == 0:
        newhour = 12

    if ap == "PM":
        newap = "AM"
    else:
        newap = "PM"

    if int(hour) < int(newhour) < 12:
        if day is False:
            new_time = (str(newhour) + ":" + str(newmin).rjust(2, '0') + " " + str(ap))
        elif day:
            new_time = (str(newhour) + ":" + str(newmin).rjust(2, '0') + " " + str(ap) + ", " + str(day))
    elif int(newmin) > 60:
        finalmin = int(newmin - 60)
        finalhour = int(newhour - 11)
        if int(finalhour) == 0:
            finalhour = 12
            new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + newap)
        elif int(finalhour > 23):
            finalhour = finalhour - 12
            if day:
                newday = dayslist[daypos + 2]
                new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + newap + ", " + str.capitalize(newday) + " (" + str(durday + 1) + " days later)")
            else:
                new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + newap + " (2 days later)")
        else:
            new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + newap)
    elif int(newhour) > 12 and int(newhour) < 24:
        finalmin = newmin
        finalhour = int(newhour - 12)
        new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + newap + " (next day)")
    elif int(newhour) > 24 and int(newhour) < 36:
        finalmin = newmin
        finalhour = int(newhour - 24)
        if day:
            newday = dayslist[daypos + 1]
            new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + ap + ", " + str.capitalize(newday) + " (next day)")
        else:
            new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + ap + " (next day)")
    elif int(newhour) > 36:
        finalmin = newmin
        finalhour = (durday * 24) - int(newhour)
        if day:
            newday = dayslist[7 - (durday - 13)]
            new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + newap + ", " + str.capitalize(newday) + " (" + str(durday) + " days later)")
        else:
            new_time = (str(finalhour) + ":" + str(finalmin).rjust(2, '0') + " " + newap + " (" + str(durday) + " days later)")
    elif int(durhour) < 1 and int(durmin) < 1:
        new_time = (str(newhour) + ":" + str(newmin).rjust(2, '0') + " " + str(ap))

    return new_time