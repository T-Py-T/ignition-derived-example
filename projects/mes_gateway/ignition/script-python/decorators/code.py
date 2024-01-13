from functools import wraps
from threading import Timer
import warnings
import inspect
import time
import traceback

# USING TO BRING IN SP ITEMS (ERROR LOGGING)
from scriptHeaders import ScriptHeaders
sh = ScriptHeaders()
db = sh.getDb()



#************************************ DO NOT EDIT BELOW THIS LINE *****************************************


def error_log(func): # Wrapper function log error writing (add above function call)
	@wraps(func)
	def errorCheck(*args, **kwargs): 
		try:
			retval = func(*args,**kwargs)
			return retval
		except Exception as Argument:
			logger = system.util.getLogger(func.__name__)
	        logger.warn(str(Argument)) #Log to wrapper (Java)
	        
	        # SET error trapping bits
	        badPaths, badValues = ["[default]Engine/ScriptFailed","[default]Engine/ScriptName","[default]Engine/ScriptError"],[True,str(func.__name__),str(Argument)]
	        system.tag.writeBlocking(badPaths, badValues)
	        
	        args_info = inspect.getargvalues(inspect.currentframe()).locals
	        log_to_database(Argument, func.__name__,  str(args_info['args']),str(args_info['kwargs']) ) # Log to DB
	        
	        print(func.__name__ +':  '+ traceback.format_exc())
			
			# NEED FURTHER TESTING ON HOW TO EXRACT LINE # FROM EXCEPTION
#			import traceback
#			from java.lang import Exception
#			
#			exceptionType, exception, stack = sys.exc_info()
#			if exceptionType == Exception:
#			    exception = exception.getCause()
#			
#			traceback_msg = traceback.format_exc()
#			line_number = traceback_msg.split("\n")[-2].split(",")[1].strip()
#			
#			logger.error("Exception occurred at line {}: {}".format(line_number, exception.getMessage()), exception)
			
			#raise
	return errorCheck



def timeit(func): # Wrapper function log execution time (add above function call)
	@wraps(func)
	def timed(*args,**kwargs):
		beg_ts = time.time()
		retval = func(*args, **kwargs)
		end_ts = time.time()
		print(func.__name__ + " elapsed time: %f" % (end_ts - beg_ts))
		return retval
	return timed



def dump_args(func): # This decorator dumps out the arguments passed to a function before calling it
	
	argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
	fname = func.func_name
	@wraps(func)
	def echo_func(*args,**kwargs):
		print fname, ":", ', '.join(
			'%s=%r' % entry 
			for entry in zip(argnames,args) + kwargs.items()
			)
		return func(*args, **kwargs)
	return echo_func



def cache_result(func): #Caches results of computationally intese functions for later.
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper



def retry(max_attempts=3, delay=1): #Used to attempt retrys with a timeout
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Attempt %d failed: %s" % (attempt, e))
                    time.sleep(delay)
            raise RuntimeError("Function {} failed after {} attempts.".format(func.__name__, max_attempts))
        return wrapper
    return decorator



def rate_limit(max_calls, interval): #Sets limit of call rate for wrapped function
    def decorator(func):
        call_times = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            call_times.append(current_time)

            # Remove old timestamps
            call_times[:] = [t for t in call_times if t > current_time - interval]

            if len(call_times) > max_calls:
                wait_time = interval - (current_time - call_times[0])
                time.sleep(wait_time)

            return func(*args, **kwargs)
        return wrapper
    return decorator



def debug(func): #used to debug the function and show 
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_info = inspect.getargvalues(inspect.currentframe()).locals
        print("Debug Info - Function: {}, Args: {}, Kwargs: {}".format(func.__name__, args_info['args'],args_info['kwargs']))
        result = func(*args, **kwargs)
        print("Debug Info - Function: {}, Result: {}".format(func.__name__, result))
        return result
    return wrapper



def deprecated(func): #shows warnings when dpricated functions are used.
	"""
	The deprecation wrapper helps manage the deprecation of a function by issuing warnings or raising exceptions when it is called. 
	It is helpful when you want to inform users about upcoming changes or deprecated functionality.
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		warnings.warn("Function {} is deprecated.".format(func.__name__), DeprecationWarning)
        return func(*args, **kwargs)
	return wrapper



## NOT WORKING (WOMP WOMP)
#def singleton(class_):
#    """
#    The singleton wrapper ensures that only one instance of a class is created and provides access to that instance across multiple function calls. 
#    It can be useful when you want to have a single shared instance of a class throughout your application.
#    """
#    instance = None
#    @wraps(class_)
#    def wrapper(*args, **kwargs):
#    	nonlocal instance
#        if instance is None:
#            instance = class_(*args, **kwargs)
#        return instance
#
#    return wrapper




#@timeit
#@error_log
@debug
def log_to_database(error, functionName, args, kwargs): # This is an SP call to log errors to the DB 
	""" gets line tagID needed for count history insert
		TODO: None
		Args:	#data fields from tag used for SPROC
			error (string): 
			functionName (string):
			args (string):
			kwargs (string):
	Returns:None      
	Testing: (script console)
		print(decorators.log_to_database(error, function_name, args, kwargs))
	"""
	call = system.db.createSProcCall("error.stp_InsertErrorLog", db)		
	call.registerInParam("functionName", system.db.VARCHAR, functionName)
	call.registerInParam("args", system.db.VARCHAR, args)
	call.registerInParam("kwargs", system.db.VARCHAR, kwargs)
	call.registerInParam("error_message", system.db.VARCHAR, error)
	system.db.execSProcCall(call)



#************************************ DO NOT EDIT ABOVE THIS LINE *****************************************

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     EXAMPLE IMPLEMENTATIONS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Using @error_log with @dump_args at the same time will cause problems with func.__name__
#	This will log "echo_func" instead of the actual function name that was called. 

#!!!!! MUST be used in this order if together
@timeit
@error_log
@dump_args
def f1(a,b,c): print a + b + c

#Ccalling the function
#f1(1, 2, 3)