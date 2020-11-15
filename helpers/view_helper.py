import time

class ViewHelper

    DISTANCE = { 'cm_per_m': 100, 'cm_per_km': 100000, 'm_per_km': 1000 }
    DECIMAL_PLACES = 2

    def format_distance(distance_cm):
        distance_cm = round(DECIMAL_PLACES, distance_cm)
        if distance_cm>=DISTANCE['cm_per_km']:
            return f"{round(distance_cm/DISTANCE['cm_per_km'], DECIMAL_PLACES) km"
        elif distance_cm>=DISTANCE['cm_per_m']:
            distance = round(distance_cm/DISTANCE['cm_per_m'], DECIMAL_PLACES)
            return "1.0 km" if distance==DISTANCE['m_per_km'] else f"{distance} m"
        else:
            return "1.0 m" if distance_cm==DISTANCE['cm_per_m'] else f"{distance} cm"

    def format_time(time_sec):
        return '' if not time_sec else time.strftime('%H hr, %M min, %S sec', time.gmtime(timesec))

    def limit_1000(series):
        return series[:999]
        #TODO? original is `series.to_a[0..999]`. `to_a` needed? example: (1..10).to_a
