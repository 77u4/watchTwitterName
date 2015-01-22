#!/bin/bash

#get current working directory
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

#install python futures
echo ">> downloading python futures from Google Code"
curl -o futures.tar.gz https://pypi.python.org/packages/source/f/futures/futures-2.2.0.tar.gz

echo ">> unzipping/taring/gzipping (wtf) python futures package"
tar xfvz futures.tar.gz
echo ">> cleaning up folder: deleting archive"
rm futures.tar.gz

echo ">> generating manifest"
cd futures-2.2.0
sudo python setup.py install

echo ">> cleaning up folder: deleting futures.2.2.0 folder"
cd ..
sudo rm -rf futures-2.2.0

echo ">> successfully installed python futures"

#install urlwatch
echo ">> downloading urlwatch from GitHub repository"
curl -o urlwatch.zip https://codeload.github.com/thp/urlwatch/zip/master

echo ">> unzipping urlwatch package"
unzip urlwatch
echo ">> cleaning up folder: deleting archive"
rm urlwatch.zip

echo ">> generating manifest"
cd urlwatch-master
python setup.py sdist
sudo python setup.py install

echo ">> cleaning up folder: deleting urlwatch-master folder"
cd ..
sudo rm -rf urlwatch-master
echo ">> urlwatch installed successfully"

#define filename of hooks-backup
BACKUPFILE=$HOME/.urlwatch/lib/hooks-backup-$(date).py
URLSFILE=$HOME/.urlwatch/urls.txt

echo ">> creating urls.txt file"
touch "$URLSFILE"
echo "https://twitter.com/username" > "$URLSFILE"
echo ">> ...done"

echo ">> generating directories"
urlwatch
echo ">> ...done"

#copy backup-file to $BACKUPFILE
cp "$HOME/.urlwatch/lib/hooks.py" "$BACKUPFILE"
echo ">> hooks.py backup is located at $BACKUPFILE"

#copy nre hooks.py to the configuration directory
cp "$DIR/hooks.py" "$HOME/.urlwatch/lib/hooks.py"
echo ">> new hooks file successfully copied"
