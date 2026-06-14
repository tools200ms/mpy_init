
PROJ_NAME := YInit

SRC_DIR := ./src
BLD_DIR := ./build
OUTPUT := yinit-bin

CFLAGS := -fno-strict-overflow -Wsign-compare -O2 -Wall

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

compile2c:
	mkdir -p ${BLD_DIR}/yinit

	cython --embed -3 ${SRC_DIR}/yinit/__main__.py -o ${BLD_DIR}/yinit
	cython -3 ${SRC_DIR}/yinit/__init__.py -o ${BLD_DIR}/yinit
	cython -3 ${SRC_DIR}/yinit/about.py -o ${BLD_DIR}/yinit

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
