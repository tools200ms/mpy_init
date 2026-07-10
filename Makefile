
PROJ_NAME := YInit

SRC_DIR := ./src
BLD_DIR := ./build
OUTPUT := yinit-bin
MODULE := yinit
ENTRY_POINT := launcher.py

CFLAGS := -fno-strict-overflow -Wsign-compare -O2 -Wall
PY_CFLAGS = $(shell python3-config --cflags)

PY_INCLUDES := $(shell python3-config --includes)

PY_LIB = $(shell python3-config --ldflags)

PY_FILES := $(shell find ${SRC_DIR}/${MODULE} -name '*.py' | grep -ve '__.*__\.py')
PY_SRC := $(patsubst ${SRC_DIR}/%, %, ${PY_FILES})
C_SRC := $(patsubst ${SRC_DIR}/%.py, ${BLD_DIR}/%.c, ${PY_FILES})
OBJS := $(patsubst %.c, %.o, ${C_SRC})

MOD_NAMES := $(patsubst ${SRC_DIR}/%.py, %, ${PY_FILES} | tr '/' '.')

ENTRY_POINT_C := $(patsubst %.py,%.c, ${ENTRY_POINT})


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
	    ${ENTRY_POINT} \
	    --embed-modules 'main,runenv' \
	    -o ../${BLD_DIR}/launcher.c

	$(foreach mod_file,${PY_SRC}, \
		cython -3 -w ${SRC_DIR} ${mod_file} -o $(patsubst %.py, ../${BLD_DIR}/%.c, ${mod_file});)


# Final compilation
compile:

	$(foreach mod_file,${PY_SRC}, \
		gcc ${CFLAGS} ${PY_INCLUDES} -c ${BLD_DIR}/$(patsubst %.py,%.c, ${mod_file}) -o ${BLD_DIR}/$(patsubst %.py,%.o, ${mod_file});)


	gcc ${CFLAGS} ${PY_INCLUDES} \
		${BLD_DIR}/${ENTRY_POINT_C} \
		$(patsubst %.py, ${BLD_DIR}/%.o, ${PY_SRC}) \
		$(shell python3-config --ldflags --embed) \
		-o ${BLD_DIR}/${OUTPUT}


${OUTPUT}: cythonize compile

cpyrun:
	cd src && python -m yinit ${ARGS}

clean:
	rm -f 	${C_SRC} ${OBJS} \
			${BLD_DIR}/${OUTPUT}

