# sequences

A sequence, in particular, is an
object that implements both **getitem** and **len**, and for this reason, it can be iterated over. Lists, tuples, and strings are examples of sequence objects in the standard library

### Building a wrapper around python sequence builtins

Suppose we are building a wrapper around list so delegate its methods to list

```py
   class Wrapper:
        def __getitem__(self, item):
            return self._values.__getitem__(item)
```

### Building your own sequence

- When indexing by a range, the result should be an instance of the same type of the class. Ex- if using a list then while slicing a[:] will return a list always. For tuple it is always tuple

- In the range provided by the slice, respect the semantics that Python uses, excluding the element at the end. For maintaining consistency. It will make other developers to feel like a pythonic way