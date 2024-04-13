def make_readable(seconds):
    # Do something
    minutes = 0
    hours = 0
    while seconds >= 60:
        if seconds >= 60:
            minutes += 1
            seconds -= 60
        if minutes >= 60:
            hours += 1
            minutes -= 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(make_readable(5))
