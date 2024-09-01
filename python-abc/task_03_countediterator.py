class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Initialize the iterator from the iterable
        self.counter = 0  

    def get_count(self):
        return self.counter  

    def __next__(self):
        try:
            item = next(self.iterator)  
            self.counter += 1
            return item  
        except StopIteration:
            raise StopIteration  

    def __iter__(self):
        return self
