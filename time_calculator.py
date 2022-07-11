# A function that adds the duration time to the start time and returns the result.
# day is an optional argument that, when specified as a day of the week, returns the corresponding day of the week of the calculated end time.
def add_time(start, duration, day=None):
    # Split the duration time into a tuple of (hours, ':', minutes).
    # Chose 'partition' instead of the 'split' method because it always returns a tuple of fixed length, making it more predictable.
    duration = duration.partition(":")
    # Convert the hours and minutes strings into integers.
    duration_hours = int(duration[0])
    duration_minutes = int(duration[2])

    # Split the start time into a tuple of (hours, ':', minutes + AM/PM).
    start = start.partition(":")

    # Further split the minutes element into a tuple of (minutes, AM/PM)
    start_minutes_ampm = start[2].split()

    # Convert the hours and minutes strings into integers and store the AM/PM value into its own variable.
    start_hours = int(start[0])
    start_minutes = int(start_minutes_ampm[0])
    am_pm = start_minutes_ampm[1]

    # Store how many days passed.
    days_amount = duration_hours // 24

    # Calculate the minutes of the end time. If the minutes value is equal to or higher than 60, increase hours by 1 and store the remainder of the minutes of the fractional hour.
    end_minutes = start_minutes + duration_minutes
    if end_minutes >= 60:
        start_hours += 1
        end_minutes = end_minutes - 60

    # Dictionary with keys assigned to the inverse value to flip values between AM and PM.
    am_pm_flip = {"AM": "PM", "PM": "AM"}

    if day is not None:
        days_of_the_week_array = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

    return new_time
