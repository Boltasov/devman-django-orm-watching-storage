def format_duration(duration):
    hours = duration.seconds // 3600
    minutes = (duration.seconds // 60) % 60
    return f'{duration.days}д {hours}ч {minutes}мин {duration.seconds%60}сек'
