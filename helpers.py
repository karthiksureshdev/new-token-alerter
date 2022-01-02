def parse_time(time: str) -> int:
    current_time_str: list[str] = []
    minutes: int = 0
    valid: bool = False
    for i in range(len(time)):
        if time[i].isdigit():
            current_time_str.append(time[i])
            continue
        if time[i] == 'h':
            valid = True
            minutes += int("".join(current_time_str)) * 60
            current_time_str.clear()
        if time[i] == 'm':
            valid = True
            minutes += int("".join(current_time_str))
            current_time_str.clear()

    if valid:
        return minutes
    else:
        raise ValueError


def parse_money(volume: str) -> float:
    current_volume_str: list[str] = []
    for i in range(len(volume)):
        if volume[i].isdigit() or volume[i] == '.':
            current_volume_str.append(volume[i])
            continue
        if volume[i] == 'K' and len(current_volume_str) > 0:
            return float("".join(current_volume_str)) * 1000
        if volume[i] == 'M' and len(current_volume_str) > 0:
            return float("".join(current_volume_str)) * 1000000

    if len(current_volume_str) > 0:
        return float("".join(current_volume_str))
    else:
        raise ValueError
