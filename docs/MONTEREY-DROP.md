![](../images/macOS-12-Monterey.png)

With the release of OpenCore Legacy Patcher 0.1.7, support for macOS Monterey has been implemented. This page informs about regarding issues.

## Newly dropped hardware

With macOS Monterey, Apple continues their their somewhat ruthless march of dropping Intel hardware. This release saw the removal, and thus addition into OpenCore Legacy Patcher, of the following models:

* iMac14,4
* iMac15,1
* MacBook8,1
* MacBookAir6,1
* MacBookAir6,2
* MacBookPro11,1
* MacBookPro11,2
* MacBookPro11,3

::: details Model names

* iMac (21.5-inch, Mid 2014)
* iMac (Retina 5K, 27-inch, Late 2014)
* MacBook (Retina, 12-inch, Early 2015)
* MacBook Air (11-inch, Mid 2013)
* MacBook Air (13-inch, Mid 2013)
* MacBook Air (11-inch, Early 2014)
* MacBook Air (13-inch, Early 2014)
* MacBook Pro (Retina, 13-inch, Late 2013)
* MacBook Pro (Retina, 15-inch, Late 2013)
* MacBook Pro (Retina, 13-inch, Mid 2014)
* MacBook Pro (Retina, 15-inch, Mid 2014)

:::

All of these models now have support in OpenCore Legacy Patcher.

## Current macOS Monterey Issues

### MacBookPro11,3 booting issue without Kepler acceleration

Due to the display being routed through the NVIDIA Kepler card and macOS being rendered on the Intel iGPU, users have been experiencing issues booting without post-install patches applied ([see here for more info](https://github.com/dortania/OpenCore-Legacy-Patcher/issues/522).) Currently the only workaround is to install the patches in Safe Mode, by holding down `Shift` + `Enter` when you select macOS in the OpenCore Boot Picker.
