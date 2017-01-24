#!/bin/bash
# Author: askeing
# Version: 0.0.1

LOG_FILE="bootstrap.log"

func_log_exec () {
    # It will only log the STDOUT result, and the return code will always be 0.
    $@ >> ${LOG_FILE}
}

func_log () {
    echo "$@" | tee -a ${LOG_FILE}
}

RET_SUCCESS="0"

func_log "[START] `date +%Y-%m-%d:%H:%M:%S`"

#####################
# Platform Checking #
#####################

# OS Platform
PLATFORM=`uname`
if [[ ${PLATFORM} == 'Linux' ]]; then
    func_log "[INFO] Your platform is Linux."
elif [[ ${PLATFORM} == 'Darwin' ]]; then
    func_log "[FAIL] Your platform is Mac OS X, not Linux."
    exit 1
else
    func_log "[FAIL] Your platform is $PLATFORM not Linux."
    exit 1
fi

################
# Prerequisite #
################

# Checking requirements
func_system_install () {
    echo "[EXEC] $@"
    $@
    if [[ ${RET_SUCCESS} != `echo $?` ]]; then
        func_log "[FAIL] Install failed."
        return 1
    fi
}

declare -a REQUIREMENTS=(
    "python"
    "pip"
    "virtualenv"
    "rabbitmqctl"
    )
declare -a REQUIREMENTS_INSTALL=(
    "sudo apt install -y --force-yes python python-dev"
    "sudo apt install -y --force-yes python-pip"
    "sudo apt install -y --force-yes python-virtualenv"
    "sudo apt install -y --force-yes rabbitmq-server"
    )

REQUIREMENTS_LENGTH=${#REQUIREMENTS[@]}

for (( i=1; i<${REQUIREMENTS_LENGTH}+1; i++ ));
do
    func_log "${i}/${REQUIREMENTS_LENGTH}: Check ${REQUIREMENTS[${i}-1]} ..."
    if [[ ${RET_SUCCESS} != `which ${REQUIREMENTS[${i}-1]} > /dev/null; echo $?` ]]; then
        func_log "[FAIL] No ${REQUIREMENTS[${i}-1]} installed."
        func_system_install ${REQUIREMENTS_INSTALL[${i}-1]}
        INSTALL_RET=$?
        if [[ ${RET_SUCCESS} != ${INSTALL_RET} ]]; then
            func_log "[FAIL] Install ${REQUIREMENTS[${i}-1]} failed."
        else
            func_log "[INFO] Install ${REQUIREMENTS[${i}-1]} done."
        fi
    fi
done
func_log "[PASS] Checking finished."

####################
# Virtualenv Setup #
####################

func_log "[INFO] Creating virtualenv ..."
rm -rf .env-python
virtualenv .env-python
func_log "[INFO] Activating virtualenv ..."
source .env-python/bin/activate

func_pip_install () {
    echo "[EXEC] $@"
    $@
    if [[ ${RET_SUCCESS} != `echo $?` ]]; then
        func_log "[FAIL] Install failed."
        return 1
    fi
}

declare -a PIP_PACKAGES=(
    "pip"
    "setuptools"
    )

PIP_PACKAGES_LENGTH=${#PIP_PACKAGES[@]}

func_log "[INFO] Installing packages into virtualenv ..."
for (( i=1; i<${PIP_PACKAGES_LENGTH}+1; i++ ));
do
    func_log "${i}/${PIP_PACKAGES_LENGTH}: Installing ${PIP_PACKAGES[${i}-1]} ..."
    func_system_install "pip install -U ${PIP_PACKAGES[${i}-1]}"
    INSTALL_RET=$?
    if [[ ${RET_SUCCESS} != ${INSTALL_RET} ]]; then
        func_log "[FAIL] Install ${PIP_PACKAGES[${i}-1]} failed."
    else
        func_log "[INFO] Install ${PIP_PACKAGES[${i}-1]} done."
    fi
done
func_log "[PASS] Install Python Prerequisite finished."

####################
# Controller Setup #
####################

func_log "[INFO] Python Setup Install ..."
pip install -r requirements.txt
python setup.py install
func_log "[PASS] Python Setup Install finished."

HOSTNAME=`hostname`
func_log "[INFO] The HOSTNAME is ${HOSTNAME}."

