# TIL-Python

## Generator

Generator(제너레이터)는 루프의 Iteration(반복) 동작을 제어할 수 있는 루틴 형태를 말한다.

예를 들어, 숫자 100만개를 만들어내 계산한다고 하면 메모리 어딘가에 100만개를 보관하고 있는 것이 아닌, 단순히 제네레이터만 생성해두고 필요할 때 언제든 숫자를 만들어낼 수 있다.
제너레이터를 리턴하려면 yield 구문을 사용하는데 이 때 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다.
다음 값을 생성하려면 next()로 추출할 수 있게 된다.

[예제](https://github.com/angrybirdpark/TIL/blob/main/Python/example/generator.py)


## range

제너레이터 방식을 활용하는 대표적인 함수, 주로 for 문에서 쓰인다.

```
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> range(5)
range(0, 5)
>>>type(range(5))
<class 'range'>
>>>for i in range(5):
        print(i, end=' ')
0 1 2 3 4
```

range()는 range 클래스를 리턴하며, for 문에서 사용할 경우 내부적으로는 제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성해내게 된다.

a = [n for n in range(1000000)]
b = range(1000000)

위와 같이 a, b를 선언하면 len()으로 길이 비교를 하면 동일한 100만 개가 출력되며, 비교 연산자에서도 True를 리턴한다.
a와 b의 차이점은 a에는 이미 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재한다.(제너레이터 방식)
그러므로 range 클래스를 갖고있는 b의 메모리 점유율이 훨씬 더 작다. (b가 100만 개가 아닌 1억 개라도 메모리 점유율은 같다.)


## enumerate

enumerate() 함수는 여러가지 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴한다.

```
>>> a = [1, 2, 3, 2, 45, 2, 5]
>>> a
[1, 2, 3, 2, 45, 2, 5]
>>> enumerate(a)
<enumerate object at 0x1010f83f0>
>>> list (enumerate(a))
[(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]
```

a = ['a1', 'b2', 'c3'] 과 같은 리스트가 있을 때 이 리스트의 인덱스와 값을 함께 출력하는 방법으로는 아래와 같다.

```
for i, v in enumerate(a):
    print(i, v)
```

## print

