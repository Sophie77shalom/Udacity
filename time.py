def calculate_end_time(start_time, duration_minutes):
    hours = duration_minutes // 60
    minutes = duration_minutes % 60

    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour = (start_hour + hours) % 24
    end_minute = (start_minute + minutes) % 60

    end_time = f"{end_hour:02d}:{end_minute:02d}"
    return end_time

# Example usage
start_time = "12:17"  # Starting time in HH:MM format
duration_minutes = 90  # Duration in minutes

end_time = calculate_end_time(start_time, duration_minutes)
print("End time:", end_time)
