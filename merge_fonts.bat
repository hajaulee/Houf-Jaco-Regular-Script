@echo off

call fontforge -lang=ff -script merge_fonts.ff ^
  .\new_fonts\ttf\HoufRegularScript_base.ttf ^
  .\generated\HoufRegularScript-Light.ttf ^
  1000 1000 ^
  .\new_fonts\ttf\HoufRegularScript-Light_1.ttf


call fontforge -lang=ff -script merge_fonts.ff ^
  .\new_fonts\ttf\HoufRegularScript-Light_1.ttf ^
  .\new_fonts\ttf\SJkaishu.svg ^
  1000 1100 ^
  .\new_fonts\ttf\HoufRegularScript-Light.ttf