FROM 200ms/alpinenet_dev2

# Install all packages that are to be launched by defined unit files:
ENV PKGS_FOR_UNIT_FILES="busybox dropbear nftables"

ENV PKGS_ADD="micropython $PKGS_FOR_UNIT_FILES"

# for sharing files with propper UID:GID
#ENV FEATURES="dev2fs"
#ENV DEV2FS_TARGET=""
