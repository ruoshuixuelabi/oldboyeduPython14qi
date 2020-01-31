def func():
    name = "alex"
    def inner():
        print(name)
    inner()
    print(inner.__closure__)
func()
