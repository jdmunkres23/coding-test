'''
코드 작성을 아주 논리적으로 잘 시작하셨네요! `while`문 안에 `for`문을 넣고 `break`를 활용하려는 접근은 전형적인 **그리디(Greedy)** 방식이라 아주 좋습니다.

다만, 몇 가지 치명적인 버그와 성능 문제가 보여서 이를 해결할 수 있는 피드백을 드릴게요.

---

### 1. 날짜 변환 방식의 오류 (`dec` 함수 관련)

현재 `sm + dec(sd)` 방식을 쓰셨는데, 이 방식은 위험합니다.

* **문제:** 3월 1일은 `3 + 0.1 = 3.1`이 되지만, 3월 10일은 `3 + 0.1 = 3.1`로 **동일해집니다.** (1일과 10일 구분 불가)
* **해결:** 월에 100을 곱해버리는 것이 가장 깔끔합니다.
> 예: 3월 8일 → $3 \times 100 + 8 = 308$ / 11월 30일 → $11 \times 100 + 30 = 1130$



### 2. 무한 루프와 중복 탐색 (성능 문제)

현재 `while`문 안에서 매번 `for i in bloom`을 처음부터 끝까지 다 돌고 있습니다.

* **문제:** $N$이 최대 10만이라서 매번 처음부터 돌면 $O(N^2)$이 되어 **시간 초과**가 납니다.
* **해결:** 리스트가 시작일 순으로 정렬되어 있으니, 이미 확인한 꽃은 다시 보지 않도록 **인덱스 변수**를 하나 두고 관리해야 합니다.

### 3. 로직 오류 (`i[1] < end` 부분)

* **문제:** `if i[0] <= end and i[1] < end:` 부분에서, 우리는 `end`를 **최대한 늘려야** 합니다. 즉, 지는 날(`i[1]`)이 현재 `end`보다 **큰** 꽃을 찾아야 하는데, 지금 코드는 작은 꽃을 찾고 있습니다.

---

### 💡 수정된 코드 제안

이해하기 쉽게 구조를 유지하면서 성능을 개선한 버전입니다.

```python
import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.read().split()
if not input:
    exit()

N = int(input[0])
flowers = []
idx = 1
for _ in range(N):
    # 날짜를 월*100 + 일 숫자로 변환 (예: 3월 1일 -> 301)
    sm, sd, em, ed = map(int, input[idx:idx+4])
    flowers.append((sm * 100 + sd, em * 100 + ed))
    idx += 4

# 1. 시작일 기준 오름차순 정렬
flowers.sort()

target_start = 301   # 현재 우리가 채워야 할 시작 지점
target_end = 1201    # 11월 30일까지 피어있으려면 12월 1일(1201)에 져야 함
current_end = 301    # 지금까지 선택한 꽃들로 커버 가능한 최대 끝 지점
count = 0
i = 0
result = 0

while current_end < target_end:
    max_end = 0
    found = False
    
    # 현재 커버 가능한 범위(target_start) 내에서 피는 꽃들 중 
    # 가장 늦게 지는 꽃을 찾음
    while i < N:
        if flowers[i][0] <= target_start:
            if flowers[i][1] > max_end:
                max_end = flowers[i][1]
                found = True
            i += 1 # 다음 꽃 확인
        else:
            # 시작일이 target_start보다 늦으면 더 이상 볼 필요 없음 (정렬되어 있으니까)
            break
            
    if not found: # 이어질 수 있는 꽃이 하나도 없으면 실패
        result = 0
        break
    
    count += 1
    target_start = max_end # 이제 다음 꽃은 이 꽃이 지기 전에만 피면 됨
    current_end = max_end # 현재까지 연결된 끝 지점 업데이트
    
    if current_end >= target_end:
        result = count
        break

print(result)

```

### 🧐 무엇이 달라졌나요?

1. **날짜 수치화:** `3.1` 같은 실수 대신 `301` 같은 정수를 써서 정확도를 높였습니다.
2. **투 포인터 방식:** `i`라는 인덱스 변수를 `while`문 밖에서 관리하여, `for`문이 매번 처음부터 도는 게 아니라 **이전 멈춘 곳부터 이어서** 검사합니다. (시간 복잡도 $O(N)$)
3. **그리디 조건:** 현재 꽃이 지기 전(`target_start` 이전)에 피는 꽃들 중 **가장 멀리 가는 꽃**(`max_end`)을 매번 선택합니다.
4. **종료 조건:** `current_end`가 `1201`(12월 1일) 이상이 되면 즉시 종료하고 횟수를 출력합니다.

이 코드로 다시 한 번 시도해 보세요! 훨씬 빠르고 정확하게 통과할 거예요. 궁금한 점 있으면 또 물어봐 주세요! :)
'''
import os
import sys


input_path = os.path.join(os.path.dirname(__file__), "4713.txt")

if os.path.exists(input_path):
    print("connected")
    sys.stdin = open(input_path, "r", encoding="utf-8")


import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.read().split()
if not input:
    exit()

N = int(input[0])
flowers = []
idx = 1
for _ in range(N):
    # 날짜를 월*100 + 일 숫자로 변환 (예: 3월 1일 -> 301)
    sm, sd, em, ed = map(int, input[idx:idx+4])
    flowers.append((sm * 100 + sd, em * 100 + ed))
    idx += 4

# 1. 시작일 기준 오름차순 정렬
flowers.sort()

target_start = 301   # 현재 우리가 채워야 할 시작 지점
target_end = 1201    # 11월 30일까지 피어있으려면 12월 1일(1201)에 져야 함
current_end = 301    # 지금까지 선택한 꽃들로 커버 가능한 최대 끝 지점
count = 0
i = 0
result = 0

while current_end < target_end:
    max_end = 0
    found = False
    
    # 현재 커버 가능한 범위(target_start) 내에서 피는 꽃들 중 
    # 가장 늦게 지는 꽃을 찾음
    while i < N:
        if flowers[i][0] <= target_start:
            if flowers[i][1] > max_end:
                max_end = flowers[i][1]
                found = True
            i += 1 # 다음 꽃 확인
        else:
            # 시작일이 target_start보다 늦으면 더 이상 볼 필요 없음 (정렬되어 있으니까)
            break
            
    if not found: # 이어질 수 있는 꽃이 하나도 없으면 실패
        result = 0
        break
    
    count += 1
    target_start = max_end # 이제 다음 꽃은 이 꽃이 지기 전에만 피면 됨
    current_end = max_end # 현재까지 연결된 끝 지점 업데이트
    
    if current_end >= target_end:
        result = count
        break

print(result)

'''
네, 알고리즘 성능 측면에서 보면 이 방식이 가장 효율적인 정해(Optimal Solution)에 가깝습니다.

그 이유를 세 가지 핵심 포인트로 정리해 드릴게요.

---

### 1. 시간 복잡도: $O(N \log N)$

이 문제의 효율성을 결정짓는 가장 큰 요소는 "모든 꽃을 몇 번 훑는가"입니다.

* **정렬:** `sort()` 함수를 사용하므로 $O(N \log N)$이 소요됩니다. (N=10만일 때 약 160만 번 연산)
* **탐색:** `while`문과 내부의 `while i < N` 문을 합쳐서 보면, 변수 `i`는 0부터 $N$까지 **딱 한 번만 증가**합니다. 즉, 탐색 부분은 $O(N)$입니다.
* **결과:** 전체 시간 복잡도는 정렬에 의해 $O(N \log N)$이 되며, 이는 $N=100,000$인 조건에서 제한 시간(보통 1~2초) 안에 들어올 수 있는 가장 빠른 방법입니다.

### 2. 공간 복잡도: $O(N)$

꽃의 정보를 리스트에 한 번 저장하기 때문에 메모리 사용량도 최소화되어 있습니다. 추가적인 거대 테이블(DP 테이블 등)을 만들지 않으므로 메모리 제한에도 안전합니다.

### 3. 그리디(Greedy)의 정당성

이 문제는 "현재 선택할 수 있는 꽃 중 가장 멀리 지는 것을 선택"하는 것이 항상 최선의 결과를 보장합니다. 이를 '구간 덮기(Interval Covering)' 문제라고 하는데, 정렬된 상태에서 탐색하는 그리디 알고리즘이 이 유형의 표준적인 해법입니다.

---

### 💡 더 최적화할 수 있는 사소한 부분 (Micro-optimization)

이미 충분히 훌륭하지만, 극단적인 성능 최적화가 필요하다면 아래와 같은 수정을 고려할 수 있습니다.

* **입력 속도:** `input()` 대신 `sys.stdin.readline`을 쓰면 입력 데이터가 많을 때 시간이 단축됩니다. (위 코드에서는 `read().split()`으로 처리하여 이미 빠릅니다.)
* **날짜 계산:** `301`, `1201` 같은 숫자 대신, 아예 모든 날짜를 1월 1일부터 며칠째인지(1~365)로 변환하여 계산하면 비교 연산이 미세하게 더 빨라질 수 있습니다. 하지만 월*100+일 방식이 가독성이 훨씬 좋아 권장되는 편입니다.
* **불필요한 꽃 제거:** 시작일이 12월 1일 이후이거나, 지는 날이 3월 1일 이전인 꽃들은 아예 입력 단계에서 무시하면 탐색 대상을 조금 줄일 수 있습니다.

### ⚠️ 주의할 점

작성하신 코드에서 `dec(sd)`를 써서 소수점으로 변환했던 방식은 **실수(float) 오차** 문제 때문에 알고리즘 테스트에서 오답 처리가 될 확률이 높습니다. 반드시 위 제안처럼 정수(int)로 변환해서 비교하는 방식을 사용하세요!

지금 코드가 로직적으로는 완성형이니, 날짜 변환 부분만 고쳐서 제출해 보시면 바로 통과하실 거예요. 화이팅입니다!
'''