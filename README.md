# Vennela
Screening Test for Full Stack Developer Position at TANDEMLOOP

Problem_1
-----------
1. The code defines a class named `calculator` to perform basic arithmetic operations.
2. The constructor `__init__` initializes two numbers and the operation type.
3. It stores the inputs as instance variables for later use.
4. The `calculate` method checks which operation to perform using `match-case`.
5. It supports four operations: add, subtract, multiply, and divide.
6. The operation input is converted to lowercase to avoid case mismatches.
7. If an unknown operation is entered, it returns an error message.
8. The program asks the user to input two numbers and the operation type.
9. It creates an object of the calculator class using the given inputs.
10. Finally, it calls the `calculate` method and prints the result.

Problem_2
----------
 1. A function is defined to generate a list of odd numbers.
2. It takes one input value, which determines how many odd numbers should be considered.
3. An empty list is created to store the odd numbers.
4. A loop runs from 0 up to twice the input value plus one.
5. Within the loop, each number is checked to see if it is odd using the modulus operator.
6. If the number is odd, it is added to the list.
7. After the loop ends, the list of odd numbers is returned.
8. The user is asked to enter a number.
9. The function is called with the user’s input.
10. The final result - the list of odd numbers - is printed.

Problem_3
----------
1. A function is defined to generate a specific series of odd numbers based on the given input.
2. The original input value is stored in a variable for processing.
3. The function checks if the input number is even.
4. If it's even, the number is reduced by 1 to make it odd.
5. A loop is used to generate numbers up to twice the adjusted number plus one.
6. Inside the loop, each number is checked to see if it is odd using the modulus operator.
7. If a number is odd, it is added to a result list.
8. After completing the loop, the list containing the odd number series is returned.
9. The user is asked to enter a number.
10. The function is called with the input, and the resulting series is printed.

Problem_4
----------
 1. A function is defined to count how many values in a list are divisible by numbers from 1 to 9.
2. An empty dictionary is initialized to store the results.
3. A loop runs through numbers 1 to 9, which act as divisors.
4. For each divisor, another loop checks each element in the input list.
5. If an element is divisible by the current divisor, the count for that divisor is increased.
6. After checking all elements, it verifies whether the divisor was added to the dictionary.
7. If a divisor is not present (i.e., no element was divisible by it), its count is set to zero.
8. The function finally returns the dictionary with counts for each divisor.
9. The user is prompted to enter comma-separated numbers.
10. The function is called with the user input and the result is displayed.


