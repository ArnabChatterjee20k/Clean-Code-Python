# context managers

- When to run preconditions and postconditions then using context manager is a great way like during resource handling opening and closing allocated resource connections

- Context managers consist of two magic methods: **enter** and **exit**.

- We can also use contextlib for creating context managers either by utiling generator functions or by using a class.

### what if we returned True in **exit**?

If this method returns True, it means that the exception that was potentially raised; it will not propagate to the caller and will stop there. Sometimes, this is the desired effect, maybe even depending on the type of exception that was raised, but in general it is not a good idea to swallow the exception.
Remember: errors should never pass silently.
