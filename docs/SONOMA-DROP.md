![](../images/macOS-14-Sonoma.png)

*Well here we're again, it's always such a pleasure~*

Apple has yet again dropped a bunch of models, continuing their journey on discontinuing Intel Macs.
With the release of OpenCore Legacy Patcher 1.0.0, early support for macOS Sonoma has been implemented. This page informs about regarding issues.

## Versioning

With 1.0.0, we'll be switching to a proper major, minor and bug fix system ([Semantic Versioning](https://semver.org/)). This means the coming release will be version 1.0.0, and future releases plan to follow this scheme:

- First digit: Major changes, including new OS support, API changes, and significant patch set changes, etc
- Second digit: Minor changes, including incoming OS update fixes, minor patch set changes, etc
- Third digit: Bug fixes, primarily hot fixes either due to a regression in prior release or resolving issues in already released OS updates


## Newly dropped hardware

* MacBook10,1:       MacBook (Retina, 12-inch, 2017)
* MacBookPro14,1:    MacBook Pro (13-inch, 2017, Two Thunderbolt 3 ports)
* MacBookPro14,2:    MacBook Pro (13-inch, 2017, Four Thunderbolt 3 Ports)
* MacBookPro14,3:    MacBook Pro (15-inch, 2017)
* iMac18,1:          iMac (21.5-inch, 2017)
* iMac18,2:          iMac (Retina 4K, 21.5-inch, 2017)
* iMac18,3:          iMac (Retina 5K, 27-inch, 2017)

## Current status

OpenCore Legacy Patcher 1.0.0 will support macOS Sonoma for all models normally supported by the Patcher, however some challenges remain. You can find information about them below.

## Issues

* [Bluetooth](#bluetooth)
* [USB 1.1 (OHCI/UHCI) Support](#usb-11-ohciuhci-support)
* [Graphics support and issues](#graphics-support-and-issues)


### Bluetooth

Sometimes Bluetooth may not work after boot on pre-2012 models. Running NVRAM reset can alleviate it.

Dual boots may also bring the issue back even after the reset.

### USB 1.1 (OHCI/UHCI) Support

For Penryn systems, pre-2013 Mac Pros and Xserve, USB 1.1 support was outright removed in macOS Ventura and naturally this continues in macOS Sonoma.
While USB 1.1 may seem unimportant, it handles many important devices on your system. These include:

* Keyboard and Trackpad for laptops
* IR Receivers
* Bluetooth

OpenCore Legacy Patcher has basic support via Root Volume patching. However due to this, users will need to use a USB hub for installation and post-OS updates when patches are cleaned:

![](../images/usb11-chart.png)

::: warning The following systems rely on USB 1.1

* iMac10,x and older
* Macmini4,1 and older
* MacBook7,1 and older
* MacBookAir3,1 and older
* MacPro5,1 and older
* Xserve 3,1 and older
:::

[More information here](https://github.com/dortania/OpenCore-Legacy-Patcher/issues/1021)

### Graphics support and issues
This build includes both Legacy Metal and non-Metal patches for macOS Sonoma. Refer to the following links for more information about Legacy Metal and non-Metal support and their respective issues.

* [Legacy Metal](https://github.com/dortania/OpenCore-Legacy-Patcher/issues/1008)
* [Non-Metal](https://github.com/dortania/OpenCore-Legacy-Patcher/issues/108)
