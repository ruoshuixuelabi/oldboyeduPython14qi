class Foo(object):
    def __call__(self, *args, **kwargs):
        print("你执行了一个call")
        
    def __setattr__(self, key, value):
        object.__setattr__(self,key,value)
        
    
    # def __getattr__(self, item):
    
        
foo = Foo()

# foo["name"] = "666"  # setitem
foo.name = "777"  # setattr
print(foo.name)
# foo.name