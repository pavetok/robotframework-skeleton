*** Settings ***
Resource    common.robot


*** Keywords ***
Create connections
    ${user_name} =  OperatingSystem.Run  echo $USER
    ${home_dir} =  OperatingSystem.Run  echo $HOME
    SSHLibrary.Open Connection  localhost  port=2211  alias=root
    SSHLibrary.Login With Public Key   root  ${home_dir}/.ssh/id_rsa
    SSHLibrary.Set Client Configuration  timeout=10s  prompt=$