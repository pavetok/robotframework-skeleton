*** Settings ***
Resource    common.robot


*** Keywords ***
Exec
    [Arguments]  ${container}  ${cmd}
    ${result} =  Run  docker exec ${container} ${cmd}
    [Return]  ${result}
