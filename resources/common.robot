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
# components
Library     Database
Library     RestApi
Library     AppLog
# services
Library     EntityService
# pages
Library     IndexPage

Resource    fixtures.robot
Resource    keywords.robot
Resource    admin.robot
Resource    docker.robot

Variables   variables.py


*** Keywords ***
Setup global
    Admin.Create fail directory

Teardown global
    SSHLibrary.Close All Connections

Setup suite
    Log  Setup suite

Teardown suite
    Log  Teardown suite

Setup test
    Admin.Remember log lines count

Teardown test
    Run Keyword If Test Failed  Run Keywords
    ...	Admin.Create test directory
    ...	Admin.Save log chunk