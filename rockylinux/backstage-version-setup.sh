#!/bin/bash

set -e

echo "Starting Backstage environment setup for Rocky Linux 8.10"

# 1. Install required system packages
echo "Installing development tools and dependencies"
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y gcc-c++ make wget curl git bzip2 zlib-devel readline-devel libffi-devel openssl-devel

# 2. Install Python 3.10
echo "Installing Python 3.10"
PYTHON_VERSION="3.10.14"
cd /usr/src
sudo wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
sudo tar xzf Python-$PYTHON_VERSION.tgz
cd Python-$PYTHON_VERSION
sudo ./configure --enable-optimizations
sudo make altinstall
python3.10 --version

# 3. Install GCC 12 and G++ 12
echo "Installing GCC and G++ version 12"
sudo dnf install -y epel-release
sudo dnf config-manager --set-enabled powertools || true
sudo dnf install -y centos-release-scl
sudo dnf install -y gcc-toolset-12
echo "source /opt/rh/gcc-toolset-12/enable" >> ~/.bashrc
source /opt/rh/gcc-toolset-12/enable
gcc --version
g++ --version

# 4. Install NVM and Node.js 20
echo "Installing NVM and Node.js 20"
export NVM_DIR="$HOME/.nvm"
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
export NVM_DIR="$HOME/.nvm"
source "$NVM_DIR/nvm.sh"
nvm install 20
nvm use 20
nvm alias default 20
node -v
npm -v

# 5. Enable Corepack and install Yarn 4.4.1
echo "Installing Yarn and activating version 4.4.1 with Corepack"
corepack enable
corepack prepare yarn@4.4.1 --activate
yarn --version

echo "Backstage environment setup is complete."