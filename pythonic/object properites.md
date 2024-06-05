# Properties, attributes, and different types of methods for objects

- All of the properties and functions of an object are public in Python, which is different from other languages where properties can be public, private, or protected. That is, there is no
  point in preventing caller objects from invoking any attributes an object has.

- Convention -> An attribute that starts with
  an underscore is meant to be private to that object, and we expect that no external agent calls it (but again, there is nothing preventing this).

### Private properties
> Double underscores are a non-Pythonic approach. If you need to define attributes as private, use a single underscore, and respect the Pythonic convention that it is a private attribute.

```python
    class Connector:
        def __init__(self):
            self.__timeout = 60

    connector = Connector()
    print(connector.__timeout)
```

Here we will get an error \_\_timeout does not exist but we expect the error "timeout can't be accessed" or "it is private" in other languages

### Why we are getting __can't be accessed -> Name mangling??
What's actually happening is that with the double underscores, Python creates a different
name for the attribute (this is called name mangling). What it does is create the attribute with the following name instead: ```_<class-name>__<attribute-name>```
So the attribute exists with a different name only

```python
class Connector:
    def __init__(self):
        self.__timeout = 60

connector = Connector()
# print(connector.__timeout) ### error
print(connector._Connector__timeout) ### name mangling
```

### Properties
* Computation based on state of object and values of other attributes
* In other languages it is called getters and setters

* what does it solving when we can write methods such as set_email??
  It is actually creating confusion. Is the method is setting email, validating email,etc.