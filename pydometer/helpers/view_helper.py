import time

class ViewHelper:

    DISTANCE = { 'cm_per_m': 100, 'cm_per_km': 100000, 'm_per_km': 1000 }
    DECIMAL_PLACES = 2

    def format_distance(distance_cm):
        if not distance_cm: return None
        distance_cm = round(distance_cm, ViewHelper.DECIMAL_PLACES)
        if distance_cm>=ViewHelper.DISTANCE['cm_per_km']:
            return "{d:.{D}f} km".format(
                    d=round(distance_cm/ViewHelper.DISTANCE['cm_per_km'], ViewHelper.DECIMAL_PLACES),
                    D=ViewHelper.DECIMAL_PLACES)
        elif distance_cm>=ViewHelper.DISTANCE['cm_per_m']:
            distance = round(distance_cm/ViewHelper.DISTANCE['cm_per_m'], ViewHelper.DECIMAL_PLACES)
            if distance==ViewHelper.DISTANCE['m_per_km']:
                return f"{1:.{ViewHelper.DECIMAL_PLACES}f} km"
            else:
                return "{d:.{D}f} m".format(d=distance, D=ViewHelper.DECIMAL_PLACES)
        else:
            if distance_cm==ViewHelper.DISTANCE['cm_per_m']:
                return f"{1:.{ViewHelper.DECIMAL_PLACES}f} m"
            else:
                return "{d:.{D}f} cm".format(d=distance_cm, D=ViewHelper.DECIMAL_PLACES)

    def format_time(time_sec):
        return '' if not time_sec else time.strftime('%-H hr, %-M min, %-S sec', time.gmtime(round(time_sec)))

    def limit_1000(series):
        return series[:999] if series else []
