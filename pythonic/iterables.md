### when we do `for e in object` what does python checks?

At a very higher level it checks the following things -

- If object contains one of the iterator methods - `__next__` or `__iter__`
- If object is a sequence and has `__len__` and `__getitem__`

### Behaviour in a iterable

- Once the iteration range is covered, the iterable will continue to be empty , hence raising `StopIteration` exception.
- This is the way iteration protocol works. An iterable constructs an iterator and this is done during the object creation(that's return self in `__iter__`).

This is the object which is iterated over

### Creating an iterable

Here, the for loop is starting a new iteration over our object. At this point, Python will call
the iter() function on it, which in turn will call the `__iter__` magic method. On this
method, it is defined to return self, indicating that the object is an iterable itself, so at that
point every step of the loop will call the next() function on that object, which delegates to
the `__next__`method. In this method, we decide how to produce the elements and return
one at a time. When there is nothing else to produce, we have to signal this to Python by
raising the StopIteration exception.


### tackling stop iteration and Container Iterable 
- To tackle we can create new object everytime during iteration.
- we can also make `__iter__` use a generator (which are iterator objects), which is being created every time. Everytime in the loop the generator object which is created everytime is iterated
