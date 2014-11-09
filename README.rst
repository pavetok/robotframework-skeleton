About
-----
Skeleton for the functional tests on the Robot Framework.

Usage
-----
::

    git clone https://github.com/pavetok/robotframework-skeleton.git tests
    cd tests
    rm -r .git
    virtualenv venv  # optional
    source venv/bin/activate  # optional
    pip install -U -r host-requirements.txt
    cp stands/{stand_name}/* .
    fig up
