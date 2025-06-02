

from mpy_init.unit import Unit


class Target(Unit):
    def __init__(self, requires: tuple(str), wants: tuple(str) = None):
        pass

class Sysinit(Target):
    def __init__(self):
        self.__init__(('dev',))

# 1. Mount Essential Filesystems:
# /proc, /sys, /dev, /run
# Necessary for system information and device access.

# 2. Perform FS checks and re-mount file systems to rw.
# Checks and repairs (if necessary) file systems. Mount as read-write + initialize and configure swap space.

# 3. Load additional kernel modules (some modules, e.g. fs support is usually loaded by initramfs)
# This includes network devices, power managment, GPU etc.

# 4. Set hostname and console
# Initializes console settings (fonts, keyboard layout).

# 5. Start Device Management
# Starts udev (or equivalent) to manage dynamic device creation in /dev.
# Handles hotplugging and initialization of devices.
# Also it’s a time to start logging daemon.

# 6. Setup networking
# Starts DHCP clients, applies static Ips.
# Perfect time to start firewall.

# 7. Start System Services and Daemons
#          sshd, cron (systemd timer), dbus, nginx, mysql

# 8. Setup logins and user sessions
#     Starts virtual terminals (getty) for local logins.
#     Starts display manager (e.g., GDM, LightDM)


class Basic(Target):
    pass

class Natwork(Target):
    def __init__(self):
        self.__init__(('network',))

class Online(Target):
    def __init__(self):
        self.__init__(('online',))

class Multiuser(Target):
    pass

class Shutdown(Target):
    pass

class Reboot(Target):
    pass

class Rescue(Target):
    pass

