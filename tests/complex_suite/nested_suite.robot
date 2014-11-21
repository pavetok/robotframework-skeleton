*** Settings ***
Resource        common.robot
Test Setup      Local setup test
Documentation   Suite documentation


*** Test Cases ***
Integration test
    [Tags]  integration
    Keywords.My keyword
    RegisteredUser.login


*** Keywords ***
Local setup test
    Common.Setup test
    Log  Local setup test