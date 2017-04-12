## summary
shell script안에 감춰진 바이너리를 실행 합니다.

## usage

기본적으로 `btos.sh`안에 binary가 포함되어 있어야 합니다. 포함시키는 가장 간단한 방법으로는 아래와 같은 형식이 있겠네요.

```bash
$ cat test.tgz >> btos.sh
```

이제 `btos.sh`안에 약간의 코드를 추가해서 셸스크립트를 실행만 해도 추가작업을 할 수 있도록 합니다. `DOIT()` 함수와 `FREE()` 함수를 수정하면 됩니다.

```bash
$ sh btos.sh
$
```
