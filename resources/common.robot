*** Settings ***
Library     String
Library     Collections

Library     SSHLibrary
Library     Selenium2Library

Library     externals/user.py
Library     internals/database.py
Library     services/entity_service.py
Library     pages/index_page.py

Resource    keywords.robot

Variables   variables.py


*** Keywords ***
Setup global
    Log  Setup global

Teardown global
    Log  Teardown global

Setup suite
    Log  Setup suite

Teardown suite
    Log  Teardown suite

Setup test
    Log  Setup test

Teardown test
    Log  Teardown test