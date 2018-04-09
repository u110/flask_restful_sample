# flask RESTful-API を試した

```diff
(env) u110:~/Work/python_sandbox/flask-restful (master *=) $ make test
env/bin/pytest tests -v
================================================ test session starts =================================================
platform darwin -- Python 3.6.0b3, pytest-3.5.0, py-1.5.3, pluggy-0.6.0 -- /Users/u110/Work/python_sandbox/flask-restful/env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/u110/Work/python_sandbox/flask-restful, inifile:
collected 8 items

tests/test_endpoints.py::test_get[200-/] PASSED                                                                [ 12%]
tests/test_endpoints.py::test_get[200-/todos] PASSED                                                           [ 25%]
tests/test_endpoints.py::test_get[200-/todo/1] PASSED                                                          [ 37%]
tests/test_endpoints.py::test_get[200-/todo/2] PASSED                                                          [ 50%]
tests/test_endpoints.py::test_get[404-/todo/xxx] PASSED                                                        [ 62%]
tests/test_endpoints.py::test_post[200-/todo-payload0] PASSED                                                  [ 75%]
tests/test_endpoints.py::test_put[201-/todo/1-payload0] PASSED                                                 [ 87%]
tests/test_endpoints.py::test_put[404-/todo/xxx-payload1] PASSED                                               [100%]

============================================== 8 passed in 0.27 seconds ==============================================
```

