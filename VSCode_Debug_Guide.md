# VS Code `launch.json` 사용법

이 문서는 Python 알고리즘 문제를 VS Code에서 디버깅하는 방법을 설명합니다.

현재 프로젝트에는 아래 디버그 설정 파일이 있습니다.

```text
.vscode/launch.json
```

`launch.json`은 VS Code에서 `F5`를 눌렀을 때 어떤 파일을 어떤 방식으로 실행하고 디버깅할지 정하는 파일입니다.

## 1. 현재 설정

현재 `launch.json`에는 두 가지 실행 방식이 있습니다.

```text
Debug current Python file - integrated terminal
Debug current Python file - external terminal
```

첫 번째는 VS Code 아래쪽 터미널에서 실행합니다.

두 번째는 별도의 터미널 창을 열어서 실행합니다.

보통은 `integrated terminal`을 쓰면 되고, 터미널에 입력한 숫자가 안 보이면 `external terminal`을 쓰면 됩니다.

## 2. 각 옵션 설명

예시는 다음과 같습니다.

```jsonc
{
  "name": "Debug current Python file - integrated terminal",
  "type": "debugpy",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal",
  "justMyCode": true
}
```

### `"name"`

VS Code의 Run and Debug 메뉴에 표시되는 이름입니다.

예:

```jsonc
"name": "Debug current Python file - integrated terminal"
```

### `"type": "debugpy"`

Python 디버거를 사용하겠다는 뜻입니다.

VS Code의 Python 확장이 설치되어 있으면 보통 `debugpy`를 사용합니다.

### `"request": "launch"`

새 Python 프로그램을 실행하면서 디버깅하겠다는 뜻입니다.

### `"program": "${file}"`

현재 VS Code에서 열려 있는 파일을 실행한다는 뜻입니다.

예를 들어 [CODEUP/greedy/3120.py](CODEUP/greedy/3120.py)를 열고 `F5`를 누르면 그 파일이 실행됩니다.

다른 Python 파일을 열고 `F5`를 누르면 그 파일이 실행됩니다.

### `"console": "integratedTerminal"`

VS Code 아래쪽의 통합 터미널에서 실행합니다.

알고리즘 문제처럼 `input()`을 사용하는 코드는 이 설정이 편합니다.

```python
now, goal = map(int, input().split())
```

디버깅을 시작한 뒤 아래 터미널에 입력값을 직접 넣으면 됩니다.

```text
7 34
```

### `"console": "externalTerminal"`

VS Code 내부 터미널이 아니라 별도의 터미널 창에서 실행합니다.

통합 터미널에 숫자를 입력했는데 화면에 글자가 안 보이는 경우 이 설정을 사용하면 좋습니다.

### `"justMyCode": true`

내가 작성한 코드 위주로 디버깅합니다.

Python 내부 라이브러리 코드까지 깊게 들어가지 않게 해줍니다.

알고리즘 문제를 풀 때는 보통 `true`가 편합니다.

## 3. 기본 디버깅 방법

1. 디버깅하고 싶은 Python 파일을 엽니다.

   예:

   ```text
   CODEUP/greedy/3120.py
   ```

2. 멈추고 싶은 줄 왼쪽을 클릭해서 breakpoint를 찍습니다.

   빨간 점이 생기면 성공입니다.

3. 왼쪽 Run and Debug 패널을 엽니다.

4. 위쪽 실행 설정에서 하나를 선택합니다.

   ```text
   Debug current Python file - integrated terminal
   ```

5. `F5`를 누릅니다.

6. 프로그램이 `input()`에서 기다리면 아래 `TERMINAL` 탭에 입력값을 넣습니다.

   예:

   ```text
   7 34
   ```

7. Enter를 누릅니다.

8. breakpoint에 도착하면 코드 실행이 멈춥니다.

## 4. 입력값은 어디에 넣나요?

입력칸이 따로 뜨는 것이 아닙니다.

`integrated terminal` 설정을 사용할 때는 VS Code 아래쪽 패널의 `TERMINAL` 탭에 직접 입력합니다.

주의할 점은 `DEBUG CONSOLE`이 아니라 `TERMINAL`이라는 것입니다.

```text
TERMINAL 탭 클릭
7 34 입력
Enter
```

`3120.py`에는 입력 안내 문구가 없기 때문에, 프로그램이 멈춘 것처럼 보여도 사실은 입력을 기다리고 있을 수 있습니다.

## 5. 숫자를 입력했는데 터미널에 안 보여요

입력한 숫자가 화면에 보이지 않지만 Enter를 누르면 코드에 반영되는 경우가 있습니다.

이 경우는 Python 코드 문제가 아니라 VS Code 통합 터미널의 표시 문제일 가능성이 높습니다.

먼저 아래를 시도해보세요.

```text
Ctrl + Shift + P
Terminal: Kill All Terminals
```

그 다음 다시 `F5`를 눌러 실행합니다.

그래도 숫자가 안 보이면 외부 터미널 설정을 사용하세요.

1. 왼쪽 Run and Debug 패널을 엽니다.
2. 위쪽 실행 설정 드롭다운을 클릭합니다.
3. 아래 설정을 선택합니다.

   ```text
   Debug current Python file - external terminal
   ```

4. `F5`를 누릅니다.
5. 새로 뜨는 터미널 창에 입력값을 넣습니다.

   ```text
   7 34
   ```

외부 터미널은 별도 창에서 실행되기 때문에 입력한 숫자가 더 확실하게 보입니다.

## 6. breakpoint 위치 추천

`input()` 줄에 breakpoint를 찍으면 입력을 받기 전에 멈출 수 있습니다.

처음 연습할 때는 `input()` 다음 줄에 breakpoint를 찍는 것이 좋습니다.

예:

```python
now, goal = map(int, input().split())

t = now - goal
```

위 코드에서는 `t = now - goal` 줄에 breakpoint를 찍으면 좋습니다.

그러면 입력값을 넣은 뒤 `now`, `goal`, `t` 값을 차례로 확인할 수 있습니다.

## 7. 디버그 버튼 설명

디버깅 중에는 VS Code 위쪽에 작은 버튼들이 나타납니다.

### Continue

다음 breakpoint까지 계속 실행합니다.

단축키:

```text
F5
```

### Step Over

현재 줄을 실행하고 다음 줄로 이동합니다.

함수 호출이 있어도 함수 안으로 들어가지는 않습니다.

단축키:

```text
F10
```

### Step Into

함수 호출이 있으면 함수 안으로 들어갑니다.

단축키:

```text
F11
```

### Step Out

현재 함수 실행을 끝내고 함수를 호출한 위치로 돌아갑니다.

단축키:

```text
Shift + F11
```

### Stop

디버깅을 종료합니다.

단축키:

```text
Shift + F5
```

## 8. 변수 확인하기

디버깅 중 왼쪽 Run and Debug 패널에서 변수 값을 볼 수 있습니다.

예를 들어 `3120.py`에서는 이런 변수들을 확인할 수 있습니다.

```python
now
goal
t
count
unit
```

breakpoint에서 코드가 멈춘 상태라면, 마우스를 변수 위에 올려도 값을 볼 수 있습니다.

## 9. `3120.py` 디버깅 예시

현재 파일은 두 숫자를 입력받습니다.

```python
now, goal = map(int, input().split())
```

예를 들어 다음처럼 입력할 수 있습니다.

```text
7 34
```

그러면 `now`는 `7`, `goal`은 `34`가 됩니다.

디버깅할 때는 아래 줄에 breakpoint를 찍어보면 좋습니다.

```python
t = now - goal
```

이렇게 하면 `t`가 어떻게 바뀌는지, `count`가 언제 증가하는지 확인할 수 있습니다.

## 10. 정리

일반적인 흐름은 다음과 같습니다.

```text
Python 파일 열기
breakpoint 찍기
Run and Debug에서 실행 설정 선택하기
F5 누르기
TERMINAL 탭에 입력값 넣기
변수 값 확인하기
F10으로 한 줄씩 실행하기
```

입력한 숫자가 통합 터미널에 보이지 않으면 아래 설정을 선택해서 실행하세요.

```text
Debug current Python file - external terminal
```
