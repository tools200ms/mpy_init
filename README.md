# 'yInit' – Unix init system developed in Python [Experimental code]

This is a Unix init system developed in Python. 

> **Q:**
> 
> What's the point of developing an init system using hi-level language that additionally requires VM (an overhead)? Init systems, after all, should be light and responsive pieces of software.
> 
> **A:**
> 
> Let's use Cython! 
> 
> Python is a flexible object-oriented language, great for expressing complexity – that Init System must deal with.
> 
> Currently, init systems go beyond simply being a launch platform. Tasks such as job scheduling, monitoring, log handling, reporting, remote control, and system integration are essential, regardless of whether the environment is a container or a bare-metal system.

Python - and inherently Cython provides a vast diversity of modules that can be used to build: 
- web control panel
- hardware support of hardware such as mini-displays and keypards (via GPIO - on boards such as Raspberry Pi)
- communication protocols for system integrations (via e.g. MQTT)

The concept is to develop an init system that handles administrative tasks and provides means for easy, and secure interactions.

## 'yInit' target applications
'yInit' aims to: 
- Init systems for apps running in a containtes
- Init system for bearmetal IoT servers

## yInit assumptions

`yInit` goes beyond the scope of classic init systems like OpenRC and SysVinit – that are designed to handle service start/stop/monitoring while delegating tasks such as loginng, cron to specialized demons. 

### 'yInit' cover range

`yInit` approaches SystemD philosophy; that is to provide also essential services, `yInit` handles: 

1. **Time** – ensures OS runs with a correct time.

2. **Network** – ensures applications are capable of communication (necessary also for time synchronization).

3. **Periodic tasks** – provides cron functionality.

4. **SSD trimming** – Ensure partitions located on flash storage are mounted with a TRIM option, and/or periodic trims are enabled.

### 'yInit' features (build-in services)

'yInit' provides: 

1. **Web Panel/API** – for initialization and management of machines over network.
2. **min-Display & key-pad** support – for GPIO featured devices for easy-build servers for IoT.
3. **integration** – for integrating witch other systems over MQTT.


### 'yInit' options

Planned 'yInit' options: 

- **Parallel boot** – boot services in parallel (if no dependency bound).


## Documentation

### 'yInit' targets

`yInit` defines the following targets that are used to classify services by task and also determinate at what boot stage service is to be loaded. Below-defined targets and its scopes, targets are in order of actual boot: 

1. **init** – does initializations of special filesystems: devfs, procfs, sysfs, 
2. **launch** – cheks and mounts root and user filesystems, loads drivers, sets up hardware settings, launches logging capability
3. **network** – initializes network
4. **network.online** – brings up network services that require network access; fullfilling this target means that the machine is probably online
5. **system** – starts system services such as SSH server
6. **user** – runs user related services: login manager, task scheduler.

