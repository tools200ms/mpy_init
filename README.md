# 'yInit' – Unix init system developed in Python

This is (wh)YInit – Unix init system developed in Python. 

> **Q:**
> 
> What's the point of developing an init system using hi-level language that additionally requires VM (an overhead)? Init systems, after all, should be light and responsive pieces of software.
> 
> **A:**
> 
> Let's use **Cython!** 
> 
> Python is a flexible object-oriented language, great for expressing complexity – that Init System must deal with.
> 
> Currently, init systems go beyond simply being a launch platform. Tasks such as job scheduling, monitoring, log handling, reporting, remote control, and system integration are essential, regardless of whether the environment is a container or a bare-metal system.

Python - and inherently Cython provides a vast diversity of modules that can be used to build: 
- web control panel
- hardware support of hardware such as mini-displays and keypards (via GPIO - on boards such as Raspberry Pi)
- communication protocols for system integrations (via e.g. MQTT)

The goal is to develop a modern, feature-rich, and intuitive init system for Unix that integrates with both **bare-metal** and **containerized** environments.

## Flexibility

`YInit` can work as Cython compiled binary, or be launched in Python VM.

The first approach is actually the must for running fully flagged init system in an efficient way. 'Python VM' mode is designated for deploying Python projects that run in containers.

### Bare-metal

**For bare-metal setups:**
2. **Time** – Ensures OS runs with a correct time.
3. **Network** – Ensures applications are capable of communication (necessary also for a time synchronization).
4. **mDNS** – 'YInit' advertises it's IP using mDNS and provides MQTT for monitoring.
5. **SSD trimming** – Ensure partitions located on flash storage are mounted with a TRIM option, and/or periodic trims are enabled.
5. **GPIO support** – GPIO support to provide: display and keypad interface (for a selected hardware).

### Python modules
It provides the following modules: 

**For all setups (bare-metal & container VMs):**
1. **Task scheduler** – Provides cron functionality.
2. **Log handling** – 
3. **Web-configurator & REST API** – Administrative module for managing configuration over web/api.
4. **Messaging [e-mail, MQTT]** – 
5. Exception handling and automatic restarts of services

It can be thought as the platform for launching Python projects.


### 'yInit' features

Planned 'yInit' feature: 

- **Parallel boot** – boot services in parallel (if no dependency bound).

# References

[Cython Project page](https://cython.org/)
