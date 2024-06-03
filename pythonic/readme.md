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

# context managers

- When to run preconditions and postconditions then using context manager is a great way like during resource handling opening and closing allocated resource connections

- Context managers consist of two magic methods: **enter** and **exit**.

- We can also use contextlib for creating context managers either by utiling generator functions or by using a class.

### what if we returned True in **exit**?

If this method returns True, it means that the exception that was potentially raised; it will not propagate to the caller and will stop there. Sometimes, this is the desired effect, maybe even depending on the type of exception that was raised, but in general it is not a good idea to swallow the exception.
Remember: errors should never pass silently.
