*** Settings ***
Library     String
Library     Collections

Library     SSHLibrary
Library     Selenium2Library

Library     Database
Library     RestApi
Library     RegisteredUser
Library     EntityService
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