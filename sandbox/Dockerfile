FROM 200ms/alpinenet_dev2:testing

ENV FEATURES="python"

ENV PKGS_PY="poetry"
ENV PKGS_MPY="micropython"

# Notice, pypy3 is in testing repo.
ENV PKGS_CORE="util-linux-misc"
# Install packages requided by unit files:
ENV PKGS_DEP_UNIT="busybox dropbear nftables util-linux-misc"

# Set `PKGS_ADD` so `200ms/alpinenet_dev2` installs these packages at build time:
ENV PKGS_ADD="$PKGS_CORE $PKGS_PY $PKGS_MPY $PKGS_DEP_UNIT"

ENV DEV2FS_TARGET="/root/targets"
ENV DEV2FS_SOURCE="/.targets"

RUN mkdir -p $DEV2FS_TARGET
# Create 'dummy service':
COPY dummy-service /usr/local/bin/
RUN chmod +x /usr/local/bin/dummy-service

# Create dummy services:
RUN ln -s /usr/local/bin/dummy-service /usr/bin/mdevd
 # Replace link to 'busybox':
RUN rm /sbin/udhcpc && ln -s /usr/local/bin/dummy-service /sbin/udhcpc


WORKDIR /root
