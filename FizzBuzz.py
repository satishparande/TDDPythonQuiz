"""
Q1. Why is the report method untestable ? [2 pts]

report_file open and path is external collaborative (platform and system environment dependent) which is handled in the function so it is untestable.



Q2. How will you change the api of the report method to make it more testable ? [2 pts]



"""
class FizzBuzz(object):
    def report(self, numbers, fileWrapper):

        fileWrapper.open()
        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                msg += "buzz "
                fizzbuzz_found = True

            if fizzbuzz_found:
                fileWrapper.write(msg + "\n")

        fileWrapper.close()

if "__main__" == __name__:
    fb = FizzBuzz()
    fileWrapper = FileWrapper('temp.txt', 'w') # can create open wrapper  
    fb.report(range(100), fileWrapper)

class FileWrapper:
        def __init__(self, fname, mode):
            self.filename = fname
            self.mode = mode
            
        def open(self):
            self.filehandle = open (self.filename, self.mode)
            return self.filehandle
            
        def write(self, buff):
            self.filehandle.write(msg)\

        def close(self)
            self.filehandle.close()
            

            
