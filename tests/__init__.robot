*** Settings ***
Resource        common.robot
Suite Setup     Common.Setup global
Suite Teardown  Common.Teardown global
Test Setup      Common.Setup test
Test Teardown   Common.Teardown test
Test Timeout    1 minute