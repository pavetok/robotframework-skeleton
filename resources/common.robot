*** Settings ***
# builtin
Library     String
Library     Collections
Library     OperatingSystem
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

Resource    admin.robot
Resource    fixtures.robot
Resource    keywords.robot

Variables   variables.py


*** Keywords ***
Setup global
    Admin.Create connections

Teardown global
    SSHLibrary.Close All Connections

Setup suite
    Log  Setup suite

Teardown suite
    Log  Teardown suite

Setup test
    Log  Setup test

Teardown test
    Log  Teardown test