# bin/bash

rm main.zip
rm -rf ./data-reporting
wget https://github.com/freud-digital/frd-reporting/archive/refs/heads/main.zip
unzip main
mkdir data-reporting
mv frd-reporting-main/html/data/* ./data-reporting
rm -rf frd-reporting-main
rm main.zip
