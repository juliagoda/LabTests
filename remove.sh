#! /bin/bash

cat files.txt | xargs sudo rm -rf
rm -rf /usr/bin/labtests
rm -rf /usr/share/labtests
rm -rf build 
rm -rf dist
rm -rf LabTests.egg-info
rm -rf labtests.spec
sudo rm -rf files.txt
