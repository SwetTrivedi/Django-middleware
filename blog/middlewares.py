# This is function based middleware

def my_middleware(get_response):
    print("One time intiliaze")
    def my_function(request):
        print("this is before view")
        response=get_response(request)
        print("This is after view")
        return response
    return my_function




#This is class middleware
class Mymiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("This is one time Initilazation")
    def __call__(self,request):
        print("this is Before view ")
        response=self.get_response(request)
        print("this is after view ")
        return response
    




#This is multiple class middleware
    

class Brothermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("This is one time brother Initilazation")
    def __call__(self,request):
        print("this is Brother Before view ")
        response=self.get_response(request)
        print("this is  Brother after view ")
        return response
    
    
class Fathermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("This is one time father Initilazation")
    def __call__(self,request):
        print("this is father Before view ")
        response=self.get_response(request)
        print("this is father after view ")
        return response



class Mothermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("This is one time mother Initilazation")
    def __call__(self,request):
        print("this is mother Before view ")
        response=self.get_response(request)
        print("this is mother after view ")
        return response


