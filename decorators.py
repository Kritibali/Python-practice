def uppercase(func):
	def wrapper():
		original_result=func()
		modified_result=original_result.uppercase()
		return modified_result
	return wrapper
@uppercase
def greet():
    return 'Hello!'

print(greet)
