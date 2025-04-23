import re
from features.steps.steps import convertir_palabra_a_numero

def parse_time_description(time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ').replace(',', ' ')
    time_description = time_description.strip()

    pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
    match = pattern.match(time_description)

    if match:
        hours_word = match.group(1) or "0"
        minutes_word = match.group(2) or "0"
        seconds_word = match.group(3) or "0"

        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds = convertir_palabra_a_numero(seconds_word)

        return hours + (minutes / 60) + (seconds / 3600)
    else:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

def test_parse_time_description():
    assert parse_time_description("1 hora y 30 minutos y 45 segundos") == 1.5125
    assert parse_time_description("90 minutos") == 1.5
    assert parse_time_description("3600 segundos") == 1
    assert parse_time_description("2 horas, 15 minutos y 30 segundos") == 2.2583333333333333
    assert parse_time_description("media hora") == 0.5