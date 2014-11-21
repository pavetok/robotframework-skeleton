*** Settings ***
# builtin
Library     String
Library     Collections
# external
Library     SSHLibrary
Library     Selenium2Library

# actors
Library     RegisteredUser
# subsystems
Library     Database
Library     RestApi
# services
Library     EntityService
# pages
Library     IndexPage

Resource    fixtures.robot
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