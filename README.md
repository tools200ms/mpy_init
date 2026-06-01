# 'yInit' – Unix init system developed in Python

This is YInit – Unix init system developed in Python. 

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
> Currently, init systems scope goes beyond simply being a service start/stop supervisors. Tasks such as job scheduling, monitoring and log handling are essential. Python - and inherently Cython comes with a solid module base that can be used by the init system.

The goal is to develop init system for Unix that provides flexibility to scaledown to be run in **contenerized enviroment [see 'Flexibility' section]**.

Moreover, Python is well-known form GPIO projects, see [README-raspberrypi.md](README-raspberrypi.md) to check out how `YInit` might be integrated with 
bare-metal hardware!

## Flexibility

`YInit` can work as Cython compiled binary, or be launched in Python VM.

The first approach is actually the must for running fully flagged init system in an efficient way. But, 'Python VM' mode is designated for deploying Python projects that run in containers.

Simply speaking, init system that runs in a container reuiers just a subset of features (host OS provides the rest). By developing project in Python YInit can work as a platform for deploing Python projects in containers.

### Enviroments
Containerized enviroment is a subset of bare-metal 

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
