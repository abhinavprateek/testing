#!/bin/bash
apt-get update && apt-get -qq --yes --force-yes install nano python python-setuptools python-dev build-essential
easy_install requests
alias submit="python /home/user/testing/attempt_test_pass.py"
alias submit.="python /home/user/testing/attempt_test_fail.py"