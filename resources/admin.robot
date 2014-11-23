*** Settings ***
Resource    common.robot


*** Keywords ***
Create fail directory
    Create Directory  ${HOST_FAIL_DIR}

Create test directory
    ${test_name} =  Replace String  ${TEST_NAME}  ${SPACE}  _
    ${HOST_TEST_FAIL_DIR} =  Normalize Path  ${HOST_FAIL_DIR}${/}${test_name}
    Create Directory  ${HOST_TEST_FAIL_DIR}
    Set Test Variable  ${HOST_TEST_FAIL_DIR}

Remember log lines count
    ${command} =  Catenate  cat ${APP_LOG_FILE} | wc -l
    ${APP_LOG_LINES_COUNT} =  Docker.Exec  ${STAND['app']['name']}  ${command}
    Set Test Variable  ${APP_LOG_LINES_COUNT}

Save log chunk
    ${from_line} =  Set Variable  ${APP_LOG_LINES_COUNT}
    ${command} =  Catenate  tail -n +${from_line} ${APP_LOG_FILE}
    ${app_log_during_test} =  Docker.Exec  ${STAND['app']['name']}  ${command}
    Create File  ${HOST_TEST_FAIL_DIR}/${STAND['app']['host']}_chunck.log
    ...  ${app_log_during_test}