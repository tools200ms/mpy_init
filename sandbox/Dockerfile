FROM 200ms/alpinenet_dev2

# Install all packages that are to be launched by defined unit files:
ENV PKGS_INIT_LEVEL="mdevd"
ENV PKGS_FOR_UNIT_FILES="busybox dropbear nftables util-linux-misc"

# pypy3 is in testing repo.
ENV PKGS_ADD="micropython python3 util-linux-misc $PKGS_FOR_UNIT_FILES"

# for sharing files with propper UID:GID
#ENV FEATURES="dev2fs"
#ENV DEV2FS_TARGET=""

COPY dummy-service /usr/local/bin/
RUN chmod +x /usr/local/bin/dummy-service

 # Belongs to 'busybox'
 RUN rm /sbin/udhcpc

# create dummy services
RUN ln -s /usr/local/bin/dummy-service /usr/bin/mdevd && \
    ln -s /usr/local/bin/dummy-service /sbin/udhcpc
