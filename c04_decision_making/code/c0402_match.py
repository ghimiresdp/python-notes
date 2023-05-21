
# Simple pattern matching example
error_code = 500

match error_code:
    case 400:
        print('looks like something is missing in your input')
    case 404:
        print("Could not find what you're searching.")

    case 500:
        print('This is a server side error!!')
    case _:
        print('I could not find what the problem is!!')


# Pattern Matching with Or
error_code = 403

match error_code:
    case 400:
        print('looks like something is missing in your input')
    case 401 | 403:
        print("I think you have permission issues.")
    case _:
        print('I could not find what the problem is!!')


# pattern matching with wildcards
(x, y) = (5, 7)
match (x, y):
    case (0, 0):
        print("The point lies in the origin.")
    case (_, 0):
        print("The point lies in the x-axis.")
    case (0, _):
        print("The point lies in the y-axis.")
    case (_, _):
        print("The point lies somewhere between.")
