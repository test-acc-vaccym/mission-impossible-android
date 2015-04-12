
# MIA - Mission Impossible: Android hardening

This project is a attempting to streamline the process of following the
guidelines from Mike Perry's post "Mission Impossible: Hardening Android for
Security and Privacy" on the [Tor Project Blog](https://blog.torproject.org/blog/mission-impossible-hardening-android-security-and-privacy).

It is currently a collection of scripts that require developer tools, that will
build and deploy an `update.zip` file to your connected device. It aspires for
be the basis for an installer for a custom Android ROM based on CyanogenMod.

Please keep in mind that this is experimental, and may not be functional at any
given moment. Also, it will likely wipe your Android device, and this is by
design!

**These tools come with no warranty. Test them on your own risk.**


## Requirements
* A supported device - see the compatibility table bellow.
* A linux/unix operating system - tested on: openSUSE and Ubuntu
* [Android SDK Tools](https://developer.android.com/sdk/index.html#Other) - with `adb` working globally.
* [Team Win Recovery Project](http://teamw.in/project/twrp2) bootloader installed onto your device.
* [Developer Options](https://developer.android.com/tools/device.html#developer-device-options) enabled on your device.
* [USB debugging](https://developer.android.com/tools/device.html#setting-up) enabled on your device.
* The MIA CLI tool - follow the setup instructions bellow.


## Usage
1.  Connect your device via USB, authorizing as necessary.

2.  Provide **temporary root access via ADB**, can be revoked later.

3.  Create a definition, customizing as necessary, see the template specific
    [README.md](templates/README.md), build a custom update.zip file and install onto the device:
    ```bash
    mia definition create my-phone
    mia build my-phone
    mia install my-phone
    ```

3.  After the installation completed open F-Droid and update the applications
    list.

4.  Open the *My App List* app, and install any desired applications from
    `misc-apps.xml`.


## MIA - CLI Tool

### Setup instructions for non-developers:
1.  Install Python if not already installed. Test using:
    `python --version`

2.  Install [`pip`](https://pip.pypa.io/en/latest/index.html) if not already installed. Test using:
    `pip --version`

3.  Install git if not already installed. Test using:
    `git --version`

4.  Install the `mia` CLI tool:
    ```bash
    sudo pip install git+https://github.com/mission-impossible-android/mission-impossible-android.git
    ```
    NOTE: You can follow the setup instructions for developers if you don't want
          to install the script globally or if you don't have `sudo` access.

5.  Test if the CLI tool is working properly.
    ```bash
    mia --help
    ```

### Setup instructions for developers:
1.  Install Python if not already installed. Test using:
    `python --version`

    NOTE: If you want to use Python 3 you will need to install the Python 3
          versions of the dependencies.

2.  (optional) Install development files for libyaml and libpython if you want
    to use LibYAML bindings for [pyyaml](http://pyyaml.org/wiki/PyYAML):

    * Using apt-get on Ubuntu:
      `apt-get install libyaml-dev libpython-dev`

    * Or using zypper on openSUSE:
      `zypper install libyaml-devel python-devel`

    NOTE: If you skip this step you'll see some warnings on the next step.

3.  Install the docopt and PyYAML modules:

    * Using Python Package Index [pip](https://pip.pypa.io/en/latest/index.html):
      `pip install docopt pyyaml`

    * Or using apt-get on Ubuntu:
      `apt-get install python-docopt python-yaml`

    * Or using zypper on openSUSE:
      `zypper install python-docopt python-PyYAML`

4.  Clone the repository:
    ```bash
    git clone https://github.com/mission-impossible-android/mission-impossible-android.git
    ```

5.  (optional) Add the tools folder to the PATH environment variable. This will
    let you run the tool from any folder in your system.
    `export PATH=$PATH:$HOME/mission-impossible-android/tools`

    * Make sure to replace `$HOME/mission-impossible-android/tools` with the
      actual path of the tools folder.
    * If you skip this step you will need to use an absolute or relative
      path to the CLI Tool. Eg: `./tools/mia` or
      `~/mission-impossible-android/tools/mia` instead of `mia`

6. Test if the tool is working properly.
    ```bash
    mia --help
    ```

### Setup instructions for developers (with virtualenv):
1.  Install Python if not already installed. Test using:
    `python --version`

2.  Install [`python-virtualenv`](https://virtualenv.pypa.io/en/latest/installation.html) if not already installed. Test using:
    `virtualenv --version`

3.  Clone the repository:
    ```bash
    git clone https://github.com/mission-impossible-android/mission-impossible-android.git
    ```

4.  Setup the virtual environment and install the dependencies:
    ```bash
    # Prepare the Python Virtual Environment.
    make prepare

    # Activate the newly created virtualenv.
    source bin/activate

    # Install mia once inside the Virtual Environment.
    pip install -e .
    ```

    NOTES:
    * Every time you need to use mia make sure you activate the virtualenv.
    * You can exit the virtualenv by executing `deactivate`
    * To recreate the virtual environment from scratch you can run:
      `deactivate && make clean`

5.  Test if the CLI tool is working properly:
    ```bash
    mia --help
    ```

6.  Now you can start changing files (python code or template files) and the
    changes will be visible next time you execute the `mia` command.


## Compatibility
Devices currently available for testing:

| Device | Codename | Testers | Actively tested? |
|--------|:--------:|:-------:|:----------------:|
| LG Nexus 4 | mako | patcon | no |
| LG Nexus 4 | mako | SchnWalter | yes |
| Asus Nexus 7 (wifi, 2012) | grouper | patcon | yes |
| Asus Nexus 7 (wifi, 2013) | flo | mikeperry-tor | yes |
| Motorola Moto G 4G | peregrine | mikeperry-tor | no |
| Samsung Galaxy S II | i9100 | SchnWalter | no |
| OnePlus One | bacon | SchnWalter | no |
| Sony Xperia Tablet Z (wifi) | pollux_windy | SchnWalter | yes |

NOTE: Other devices supported by CyanogenMod might also be compatible. If you
      test one, please report it in the [issue queue](https://github.com/mission-impossible-android/mission-impossible-android/issues).


## Links
* [updater-script syntax](http://forum.xda-developers.com/wiki/Edify_script_language)
* [TWRP for Android Emulator](http://teamw.in/project/twrp2/169)
