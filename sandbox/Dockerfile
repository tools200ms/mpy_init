FROM 200ms/alpinenet_dev2:testing

ENV FEATURES="python"

ENV PKGS_PY="poetry"
#ENV PKGS_MPY="micropython"
ENV PKGS_DEP_MPY "gcc git make musl-dev libbsd-dev libffi-dev"

# Notice, pypy3 is in testing repo.
ENV PKGS_CORE="util-linux-misc"
# Install packages requided by unit files:
ENV PKGS_DEP_UNIT="busybox dropbear nftables util-linux-misc"

# Set `PKGS_ADD` so `200ms/alpinenet_dev2` installs these packages at build time:
ENV PKGS_ADD="$PKGS_CORE $PKGS_PY $PKGS_DEP_MPY $PKGS_DEP_UNIT"

ENV DEV2FS_TARGET="/root/targets"
ENV DEV2FS_SOURCE="/.targets"


# Install MicroPython from sources:
ENV MPY_GIT_URL="https://github.com/micropython/micropython"
ENV MPY_SRC="/usr/src/micropython"
# wget -qO- $MPY_GIT_URL/archive/refs/heads/master.tar.gz | tar -xz --strip-components=1 -C $MPY_SRC
ENV MPY_MAKE_FLAGS="MICROPY_PY_BTREE=0"

RUN apk add $PKGS_ADD
RUN mkdir -p $MPY_SRC && git clone $MPY_GIT_URL $MPY_SRC  && \
    make -C $MPY_SRC/mpy-cross && cp $MPY_SRC/mpy-cross/build/mpy-cross /usr/local/bin/ && \
    make -C $MPY_SRC/ports/unix submodules && \
    make install $MPY_MAKE_FLAGS -C $MPY_SRC/ports/unix

RUN micropython -mip install logging

RUN mkdir -p $DEV2FS_TARGET
# Create 'dummy service':
COPY dummy-service /usr/local/bin/
RUN chmod +x /usr/local/bin/dummy-service


# Create dummy services:
RUN ln -s /usr/local/bin/dummy-service /usr/bin/mdevd
 # Replace link to 'busybox':
RUN rm /sbin/udhcpc && ln -s /usr/local/bin/dummy-service /sbin/udhcpc


WORKDIR /root
