

cython --embed hyinit-mini/__main__.py
gcc -Os $(python3-config --cflags) hyinit-mini/__main__.c $(python3-config --ldflags --embed) -o hyinit-minic

hyinit-minic hyinit-mini/__main__.c
