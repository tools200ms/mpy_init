
OUTPUT := hyinit-minic

all: ${OUTPUT}
compile: ${OUTPUT}

${OUTPUT}:
	mkdir -p build
	cython --embed -3 hyinit-mini/__main__.py

	gcc hyinit-mini/__main__.c \
		$(shell python3-config --cflags) \
		$(shell python3-config --ldflags --embed) \
		-o build/${OUTPUT}

    #hyinit-minic hyinit-mini/__main__.c

clean:
	rm hyinit-mini/*.c
