'''
1. 파일 실행 법
mkdir ./mkdir.ps1

2. 파일 실행 시 다음과 같은 에러 메시지 나는 경우

-----에러 메시지----
(중략)
+ CategoryInfo          : 보안 오류: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess
-------------------

다음의 코드를 터미널에서 실행 후 파일 실행 해야 함.

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

위의 코드는 임시 통행증을 끊어주는 것과 같다.
---- 코드 뜻 ----
Set-ExecutionPolicy: "실행 정책을 설정하겠다"는 핵심 명령어입니다.
    -ExecutionPolicy RemoteSigned: 어떤 수준으로 허용할지 결정하는 옵션입니다.
RemoteSigned: "내가 직접 만든 파일은 그냥 실행하고, 인터넷에서 받은 파일은 신뢰할 수 있는 서명이 있어야만 실행하겠다"는 뜻입니다. 가장 합리적인 보안 수준이죠.
    -Scope Process: 이 허락을 어디까지 적용할지 결정합니다.
Process: "지금 열려 있는 **이 터미널 창(VS Code 터미널)**이 닫힐 때까지만"이라는 뜻입니다. 창을 끄면 효력이 사라지므로 시스템 보안상 가장 안전합니다.
-----------------
'''

# 경로 지정
$P = ".\"
$D1 = "1st video - python syntax"
$D2 = "2nd video - greedy algorithm & implementation"
$D3 = "3th video - DFS&BFS"
$D4 = "4th video - sorting algorithm"
$D5 = "5th video - binary search"
$D6 = "6th video - dynamic programming"
$D7 = "7th video - shotest path algorithm"
$D8 = "8th video - other graph theory"

# 디렉토리 생성 및 이름 변경
mv "$P\1st video_pythonsyntax" "$P\$D1"
mv "$P\2nd video_greedy algorithm" "$P\$D2"
mkdir "$P\$D3", "$P\$D4", "$P\$D5", "$P\$D6", "$P\$D7", "$P\$D8" -ErrorAction SilentlyContinue

# 파일 이동
mv "$P\Lecture 12 ~ 13 Greedy algorithm.ipynb" "$P\$D2"
mv "$P\Lecture 14 ~ 15 Implementation - simulation and exhaustive search.ipynb" "$P\$D2"
mv "$P\Lecture 16 ~ 20 DFS & BFS.ipynb" "$P\$D3"
mv "$P\Lecture 21 ~ 25 Sorting algorithm.ipynb" "$P\$D4"
mv "$P\Lecture 26 ~ 27 Binary search.ipynb" "$P\$D5"
mv "$P\Lecture 28 ~ 29 Dynamic programming.ipynb" "$P\$D6"
mv "$P\Lecture 30 ~ 32 Shortest path algorithm.ipynb" "$P\$D7"
mv "$P\Lecture 33 ~ 36 Other graph theory.ipynb" "$P\$D8"