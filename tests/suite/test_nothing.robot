*** Settings ***
Resource        common.robot
Test Setup      Local setup test
Documentation   Suite documentation


*** Test Cases ***
Test nothing
    Keywords.My keyword
    RegisteredUser.login


*** Keywords ***
Local setup test
    Common.Setup test
    Log  Local setup test