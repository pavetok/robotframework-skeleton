About
-----
This is skeleton for the functional tests on the Robot Framework.

On the tester machine should be installed:

- Docker
- Python 2.7
- Pip
- Virtualenv (optional)

Usage
-----
.. code:: bash

    $ cd /path/to/my/project
    $ git clone https://github.com/pavetok/robotframework-skeleton.git robotest
    $ cd robotest
    $ rm -r .git
    $ virtualenv venv27  # optional
    $ source venv27/bin/activate  # optional
    (venv27)$ pip install -U -r requirements/host-reqs.txt
    (venv27)$ cp stands/{desired_stand_name}/* .
    (venv27)$ rm -r stands
    (venv27)$ fig up
