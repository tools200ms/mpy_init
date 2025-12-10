# 'mpy-init' – Unix init system developed in Python [Experimental code]

This is a Unix init system developed in Python. 

> **Q:**
> 
> What's the point of developing an init system that should have a small footprint using hi-level language that additionally requires VM (an overhead)?
> 
> **A:**
> 
> Python in the form of **MicroPython** was successfully re-implemented to run on microcontrollers – small computers with a very limited memory and CPU resources. 
> 
> Python is a flexible object-oriented language, great for expressing complexity – that Init System must deal with.

Project is developed with MicroPython limitations in mind (simplified modules and language API); therefore, it can be run on both - MicroPython and CPyhon. It is aimed to be run in MicroPython 'unix' port.

Project's testing bench is AlpineLinux, however, porting it to another Linux distribution or unix system should be relatively straight forward.

## Design philosophy

`mpy_init` implements `target-based` system initialization approach - in the contrast to obosolet [runlevels](https://en.wikipedia.org/wiki/Runlevel). 

Defined targets are:

- **init** - does initializations of special filesystems: devfs, procfs, sysfs, 
- **launch** - cheks and mounts root and user filesystems, loads drivers, sets up hardware settings, launches logging capability
- **network** - initializes network
- **network.online** – brings up network services that require network access; fullfilling this target means that the machine is probably online
- **system** - starts system services such as SSH server
- **user** - runs user related services: login manager, task scheduler.

### Project (planned) features:

1. **In between OpenRC and SystemD** – `mpy_init` goes beyond the traditional scope of classic init systems like OpenRC and SysVinit. In addition to service initialization and control, it also manages: 

    a. **Time** – ensures OS runs with a correct time.

    b. **Network** – ensures applications are capable of communication (necessary also for time synchronization).

     c. **Periodic tasks** – provides cron functionality.

     d. **SSD trimming** – Ensure partitions located on flash storage are mounted with a TRIM option, and/or periodic trims are enabled.
2. **Parallel boot** – boot services in parallel (if no dependency bound).
3. **Web API** – for initialization and management of machines over network.

I believe that the above scope defines a good balance in what a modern init system should do, what not.


# References

- The MicroPython Project repository [link](https://github.com/micropython/micropython).
- Micropython [APK BUILD](https://gitlab.alpinelinux.org/alpine/aports/-/tree/master/community/micropython)

