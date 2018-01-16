## summary
데스크탑OS를 ubuntu로 변경하면서 xshell이 그리워 만든 툴 입니다. (xshell이 리눅스 버전은 없더군요)

리눅스를 사용하면서 여러대의 서버를 관리하거나 기타 목적으로 여러대에 접속이 잦은 경우 많은 서버의 IP나 아이디, 
비밀번호를 기억하는 것은 쉽지 않습니다. 또한 결정적으로 프롬프트에서 매번 ssh 명령어를 치고 비밀번호 입력하는 것이
여간 불편한게 아닙니다. 그래서 자동 접속기를 만들어 봤습니다. 

누군가에게는 유용하게 쓰일 수 있기를 바랍니다.

## usage
    $ connect_ssh
  
명령어 실행시에 간단한 소개글을 확인할 수 있습니다. 사용경고 문구등을 삽입하면 알맞을 것 같군요.

<div style="width:50%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="image1.png">
</div>

OK를 누르면 접속 가능한 서버 목록을 보여줍니다. 선택하면 자동으로 해당 서버에 접속됩니다.

<div style="width:50%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="image2.png">
</div>


Shell script안에 비밀번호를 기록할 수 없는 서버의 경우를 위해 패스워드를 입력 받는 함수를 추가했습니다. 
`test.example.com`이 그 예제가 될 것입니다.
선택시에 아래와 같이 비밀번호를 묻는 창이 출력 됩니다. 서버에는 어떤 정보도 남기지 않습니다.

<div style="width:50%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="image3.png">
</div>

안심하고 사용하십시오. 모든 서버의 비밀번호를 동일하게 사용하고 있다면 `connect_ssh2` 사용도 고려해보시면 좋습니다.
`connect_ssh2`는 스크립트 내에 계정을 추가하는 포인트가 훨씬 적기 때문에 수정에 용이합니다.
