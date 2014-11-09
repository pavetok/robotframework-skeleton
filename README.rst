About
-----
This is skeleton for the functional tests on the Robot Framework.

On the developer machine should be installed:

    - Docker
    - Python 2.7
    - Pip
    - Virtualenv (optional)

Usage
-----
::

    cd /path/to/my/project
    git clone https://github.com/pavetok/robotframework-skeleton.git tests
    cd tests
    rm -r .git
    virtualenv venv  # optional
    source venv/bin/activate  # optional
    pip install -U -r host-requirements.txt
    cp stands/{desired_stand_name}/* .
    rm -r stands
    fig up
