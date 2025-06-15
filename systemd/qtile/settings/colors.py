from os import path
import json

theme = "blue-theme"

qtile_path = path.join(path.expanduser('~'), ".config", "qtile")
theme_file = path.join(qtile_path, "themes", f'{theme}.json')

if not path.isfile(theme_file):
    raise Exception(f'"{theme_file}" does not exist')

f = open(theme_file)

colors = json.load(f)