
PROJ_NAME := YInit

SRC_DIR := ./src
BLD_DIR := ./build
OUTPUT := yinit-bin

CFLAGS := -fno-strict-overflow -Wsign-compare -O2 -Wall

PY_INC = $(shell python3-config --cflags)
PY_LIB = $(shell python3-config --ldflags)

#PYX_SRC := ${wildcard $(SRC_DIR)/*.pyx}
PYX_SRC := $(shell find ${SRC_DIR} -name '*.py')
C_SRC := $(patsubst $(SRC_DIR)%.py, $(BLD_DIR)%.c, $(PYX_SRC))


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

cythonize:
	mkdir -p ${BLD_DIR}/yinit

	cython --embed -3 -w ${SRC_DIR} \
	    launcher.py \
	    -o ../${BLD_DIR}/launcher.c
	cython -3 -w ${SRC_DIR} \
	    yinit/main.py \
	    -o ../${BLD_DIR}/yinit/main.c
	cython -3 -w ${SRC_DIR} \
	    yinit/runenv.py \
	    -o ../${BLD_DIR}/yinit

	echo ${PYX_SRC}
	echo ${C_SRC}

# Final compilation
compile:
	gcc ${CFLAGS} \
		$(shell python3-config --includes) \
		${BLD_DIR}/launcher.c \
		${BLD_DIR}/yinit/main.c \
		${BLD_DIR}/yinit/runenv.c \
		$(shell python3-config --ldflags --embed) \
		-o ${BLD_DIR}/${OUTPUT}

# 	gcc ${CFLAGS} ${PY_INC} \
# 		${BLD_DIR}/yinit/main.c \
# 		${PY_LIB} \
# 		-o ${BLD_DIR}/${OUTPUT}

${OUTPUT}: cythonize compile

runinpython:
	cd src && python -m yinit ${ARGS}

clean:
	rm -f 	${C_SRC} \
			${BLD_DIR}/${OUTPUT}
