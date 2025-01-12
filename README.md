# iphone-android-migrate
A detailed guide to move your camera roll from iPhone to Android. Albums, edits and (most) dates included.

## You will need
- A computer with [python 3](https://www.python.org/) and pip installed (any OS will probably do, but I used Ubuntu Linux) and up to 2 times as much free storage as your iPhone uses for the camera roll. (ex: your iPhone uses 15GB for the camera roll, you computer will need around 15-30GB of free storage depending on how you albums are set up)
- An iPhone with some free space (things can be buggy without free space).
- An android phone and a cable to it connect to your computer.
- A cloud service which you can access from both your iPhone and your computer.

## Getting media from iPhone
**Any media uploaded to the cloud should probably be chosen to be uplaoded as "Current format" as such: [video link](https://github.com/objectiveSquid/iphone-android-migrate/blob/main/videos/current_format_example.mp4)**

* For each album (remember to copy the hidden one as well) in your iPhone upload all those photos/videos in a seperate folder on the cloud and download them to your computer.
* Then upload all your photos/videos from the camera again, even the ones already uploaded through albums. And downloaded them to your computer.
* Arrange all the photos/videos you've downloaded so they look like this on your filesystem:
  * DCIM/
    * all/
      * IMG_1234.JPG
      * IMG_2345.HEIC
      * IMG_5656.PNG
      * IMG_9090.JPG
    * albums/
      * cats/
        * IMG_1234.JPG
        * IMG_2345.HEIC
      * dogs/
        * IMG_5656.PNG
        * IMG_9090.JPG

## Moving media to Android
### Computer
* Process albums with `album.py`.
```sh
python3 scripts/album.py /path/to/your/DCIM
```
* Install adbsync from PyPI.
```sh
pip install adbsync
```

### Android phone
* Switch on developer options by clicking the build number in settings 7 times. Deeper explanation [here](https://developer.android.com/studio/debug/dev-options#enable).
* Enable USB debugging by clicking "USB debugging" in developer options. Deeper explanation [here](https://developer.android.com/studio/debug/dev-options#Enable-debugging).
* Connect your android phone to your computer with the cable.

### Computer
* Run `adbsync` to copy files to the android phone, your android phone might ask for permission to use USB debugging.
```sh
adbsync push /path/to/your/DCIM /storage/emulated/0
```

### Android phone
* Reboot the phone and the files will appear in the gallery.