# 'mpy-init' – Unix init system developed in Python [Experimental code]

This is a Unix init system developed in Python. 

> **Q:**
> 
> What's the point of developing an init system using hi-level language that additionally requires VM (an overhead)? Init systems, after all, should be light and responsive pieces of software.
> 
> **A:**
> 
> Python in the form of **MicroPython** was successfully re-implemented to run on microcontrollers – small computers with very limited memory and CPU resources. 
> 
> Python is a flexible object-oriented language, great for expressing complexity – that Init System must deal with.

Project is developed with MicroPython limitations in mind (simplified modules and language API); therefore, it can be run on both - MicroPython and CPyhon.

Project's testing bench is AlpineLinux, however, porting it to another Linux distribution or unix system should be relatively straightforward.

## Project (planned) features

**MicroPython** - VM and modules, provide multiple functions making it a good base for building Init System but also more. Aim of this project is to use MicroPython potential as much as possible.

1. **In between OpenRC and SystemD** – `mpy_init` goes beyond the scope of classic init systems like OpenRC and SysVinit – that are designed to handle service start/stop/monitoring while delegating tasks such as loginng, cron to specialized demons. `mpy_init` approaches SystemD philosophy; that is to provide also essential services, `mpy_init` handles: 

    a. **Time** – ensures OS runs with a correct time.

    b. **Network** – ensures applications are capable of communication (necessary also for time synchronization).

     c. **Periodic tasks** – provides cron functionality.

     d. **SSD trimming** – Ensure partitions located on flash storage are mounted with a TRIM option, and/or periodic trims are enabled.
2. **Parallel boot** – boot services in parallel (if no dependency bound).
3. **Web API** – for initialization and management of machines over network.

Implementation of these features into a project makes it to 

## 'mpu_init' targets

`mpy_init` defines the following targets that are used to classify services by task and also determinate at what boot stage service is to be loaded. Below-defined targets and its scopes, targets are in order of actual boot: 

1. **init** – does initializations of special filesystems: devfs, procfs, sysfs, 
2. **launch** – cheks and mounts root and user filesystems, loads drivers, sets up hardware settings, launches logging capability
3. **network** – initializes network
4. **network.online** – brings up network services that require network access; fullfilling this target means that the machine is probably online
5. **system** – starts system services such as SSH server
6. **user** – runs user related services: login manager, task scheduler.

# References

- The MicroPython Project repository [link](https://github.com/micropython/micropython).
- Micropython [APK BUILD](https://gitlab.alpinelinux.org/alpine/aports/-/tree/master/community/micropython)

