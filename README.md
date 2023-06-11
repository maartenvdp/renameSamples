# renameSamples

## Problem: Convert generic samplenames according to a list.


Problem description:

https://vi-control.net/community/threads/renaming-filenames-according-to-text-file.139140/


## Solution



One folder of samples alpahbetical organised. (implicit mapping)
List takes that order.


You have to setup the following directory structure:

    .
    ├── README.md
    ├── list_newnames.txt
    ├── rename.py
    └── samples
        ├── Sound1.wav
        ├── Sound2.wav
        ├── Sound3.wav
        ├── Sound4.wav
        └── Sound5.wav


For testing, create it in this way:

```bash
    mkdir samples
    cd samples
    for i in {1..5}; do  touch  "Sound$i.wav"; done
```



`list_newnames.txt` looks like this:

    white_bear
    san_junipero
    nosedive
    krill
    pria

Run the script:

    $ chmod 755 rename.py # not strictly necessary if you run it with python binary
    $ python3 rename.py 
    Sound1.wav converted to: white_bear.wav
    Sound2.wav converted to: san_junipero.wav
    Sound3.wav converted to: nosedive.wav
    Sound4.wav converted to: krill.wav
    Sound5.wav converted to: pria.wav

Check:

    $ tree -t
    .
    ├── samples
    │   ├── Sound1.wav
    │   ├── Sound2.wav
    │   ├── Sound3.wav
    │   ├── Sound4.wav
    │   └── Sound5.wav
    ├── list_newnames.txt
    ├── README.md
    ├── rename.py
    └── converted_samples
        ├── krill.wav
        ├── nosedive.wav
        ├── pria.wav
        ├── san_junipero.wav
        └── white_bear.wav

    3 directories, 13 files
