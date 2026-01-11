
PROJ_NAME := MPy Init

SRC_DIR := ./mpy_init
BLD_DIR := ./build
OUTPUT := hyinit-minic

CFLAGS := -fno-strict-overflow -Wsign-compare -O2 -Wall

#PYX_SRC := ${wildcard $(SRC_DIR)/*.pyx}
PYX_SRC := $(shell find ${SRC_DIR} -name '*.pyx')
C_SRC := $(patsubst $(SRC_DIR)%.pyx, $(BLD_DIR)%.c, $(PYX_SRC))


ifdef DEBUG
$(info ---=== DEBUG mode is ON: Compiling with debug flags. ===---)

ifeq ("${DEBUG}","y")
	CFLAGS += -g1
else ifeq ("${DEBUG}","Y")
	CFLAGS += -g3
endif
# TODO: if ${DEBUG}: 0-3 add appropriate level
else
CFLAGS += -DNDEBUG -g
endif

all: ${OUTPUT}

compile2c:
	mkdir -p ${BLD_DIR}
	cython --embed -3 ${SRC_DIR}/entry.pyx -o ${BLD_DIR}
	cython -3 ${SRC_DIR}/sys/__init__.pyx -o ${BLD_DIR}/sys

	echo ${PYX_SRC}
	echo ${C_SRC}

# Final compilation
compilecc:
	gcc ${CFLAGS} \
		$(shell python3-config --includes) \
		${C_SRC} \
		$(shell python3-config --ldflags --embed) \
		-o ${BLD_DIR}/${OUTPUT}

    #hyinit-minic hyinit-mini/__main__.c

compile: compile2c compilecc

${OUTPUT}: compile

clean:
	rm -f 	${C_SRC} \
			${BLD_DIR}/${OUTPUT}
