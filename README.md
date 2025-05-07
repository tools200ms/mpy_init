# MicroPython init system

This is a proposal for a Linux init system based on MicroPython.

## Design philosophy

Proposed MicroPython-based init system, called `mpy_init`, is designed to run on bare metal and in containers.

### Project assumptions:

0. **Cross-platform** – `mpy_init` inherits MicroPython's cross-platform nature, ensuring compatibility with all UNIX systems.

1. **Target-based** – `mpy_init` implements a current, target-based system initialization approach, similar to what is used in SystemD.

2. **In between OpenRC and SystemD** – `mpy_init` goes beyond the traditional scope of classic init systems like OpenRC and SysVinit. In addition to service initialization and control, it also manages: 

    a. **Time** – ensures OS runs with a correct time.

    b. **Network** – ensures applications are capable of communication (necessary also for time synchronization).

     c. **Periodic tasks** – provides cron functionality.
3. **Environment detection** - `myp_init` shall test if it is launched on bear-metal or in containerized environment. It affects a launch process (that is much simpler in the second case).

We believe that the above scope defines a good balance in what a modern init system should do, what not.

## Advantages

OS running MicroPython based Init system would bring following advantages: 

1. **Performance** - having MicroPython's VM already loaded makes scripts (compiled to bytecodes) to be run fast – VM is 'ready' at any time. Moreover, MicroPython is light-weight and optimized for resource-poor devices. Therefore, even in the case of running it on slow hardware, it should be a suitable solution.

2. **Efficient development: debug and testing tools** - unlike shell scripts, Python provides robust Development tools.

3. **More powerful shell** - traditional shell (bash, ash) can be replaced with [ipython](https://github.com/ipython/ipython) or [Xonsh](https://xon.sh/) - shells developed in Python. These projects keep compatibility with traditional shells (and theirs pros), while providing also Python features (even more Pros!).

# TODO

- Think about security.

