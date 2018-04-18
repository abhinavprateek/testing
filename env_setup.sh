#!/bin/bash
apt-get -qq update && apt-get -qq --yes --force-yes install nano python python-setuptools python-dev build-essential
easy_install requests
alais submit="python /home/user/testing/attempt_test_pass.py"
alais submit.="python /home/user/testing/attempt_test_fail.py"