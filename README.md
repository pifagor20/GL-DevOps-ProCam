The script can be executed in two ways:
1. Via Docker: 
git clone https://github.com/pifagor20/GL-DevOps-ProCam.git
docker build -t metrics_script .
docker run metrics_script
or
if we want to obtain some specific value "cpu" or "mem"
docker run metrics_script mem
docker run metrics_script cpu

2. Execute script directly:
before execution need to install lib psutil like below:
pip3 install -r requirements.txt

usage: ./metrics -cpu, ./metrics -mem

The script will print cpu and memory usage information.

optional arguments:
  -h, --help  show this help message and exit
  cpu        shows cpu metrics
  mem        shows mem metrics
