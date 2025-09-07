# Pseudocode Examples
An algorithm is a `procedure` for solving a problem in terms of the actions to be executed and the order in which those actions are to be executed. An algorithm is merely the sequence of steps taken to solve a problem. The steps are normally "sequence," "selection, " "iteration," and a case-type statement.

Pseudocode is an artificial and informal language that helps programmers develop algorithms. Pseudocode is a "text-based" detail (algorithmic) design tool.

The rules of Pseudocode are reasonably straightforward. All statements showing "dependency" are to be indented. These include while, do, for, if, switch. Examples below will illustrate this notion.

Examples:

```text
If student's grade is greater than or equal to 60
    Print "passed"
else
    Print "failed"
endif
```

```text
Set total to zero
Set grade counter to one
while grade counter is less than or equal to ten
    Input the next grade
    Add the grade into the total
endwhile
Set the class average to the total divided by ten
Print the class average.
```

```text
Initialize total to zero
Initialize counter to zero
Input the first grade
while the user has not as yet entered the sentinel
    add this grade into the running total
    add one to the grade counter
    input the next grade (possibly the sentinel)
endwhile
if the counter is not equal to zero
    set the average to the total divided by the counter
    print the average
else
    print 'no grades were entered'
endif
```

```text
initialize passes to zero
initialize failures to zero
initialize student to one
while student counter is less than or equal to ten
    input the next exam result
    if the student passed
        add one to passes
    else
        add one to failures
    endif
endwhile
add one to student counter
print the number of passes
print the number of failures
if eight or more students passed
    print "raise tuition"
endif
```

## Some keywords that should be used
For looping and selection, The keywords that are to be used include `Do While`...`EndDo`; `Do Until`...`Enddo`; `Case`...`EndCase`; `If`...`Endif`; `Call`... with `(parameters)`; `Call`; `Return` ....; `Return`; `When`; Always use scope terminators for loops and iteration.

As verbs, use the words `Generate`, `Compute`, `Process`, etc. Words such as `set`, `reset`, `increment`, `compute`, `calculate`, `add`, `sum`, `multiply`, ... `print`, `display`, `input`, `output`, `edit`, `test` , etc. with careful indentation tend to foster desirable pseudocode.

NOTE : Do not include data declarations in your pseudocode.

## Pseudocode standard
Common categories of actions include:
 - Input: `GET`, `READ`, `OBTAIN`
 - Output: `PRINT`, `DISPLAY`, `SHOW`
 - Compute: `COMPUTE`, `CALCULATE`, `DETERMINE`, `PROCESS`
 - Initialize: `SET`, `INIT`
 - Add One: `INCREMENT`, `BUMP`
 - Function: `PROCEDURE`


### Sequence: A series of instructions (list of actions) at the same level of indentation. Means complete one action and proceed to the next

Example:
```text
GET temperature value
GET weather type
PRINT “It is <temperature> degrees and <weather type> out right now”
``` 

### Control Flow => IF || THEN || ELSE 

A decision between two sequences based on some condition (NOTE: the indentation of the then and else sequences)
```text
GET num
IF num % 2 THEN
  PRINT “<num> is even!”
ELSE
  PRINT “<num> is odd!”
ENDIF
```

### While: 
As long as some condition is met, continuously run the same sequence (NOTE: once again we have the body of the while loop indented)
```text
DETERMINE buellerIsPresent
WHILE !buellerIsPresent
  PRINT “Bueller? …”
  DETERMINE buellerIsPresent
ENDWHILE
```

### Case: 
Like an if-else statement but matching on a particular value (NOTE: if we want our case statement to be comprehensive, we need to provide a default case under OTHER) 
```text
CASE temp OF:
  “Cold”: PRINT “Better stay indoors...”
  “Cool”: PRINT “Bring a jacket!”
  “Warm”: PRINT “Enjoy the sun!”
  OTHERS:
    PRINT: “Unknown temp! You’re on your own!”
ENDCASE
```

### Repeat:
```text
REPEAT:
  PRINT “Pete and Repete were sitting on a bridge. Pete fell off. Who was left?”
  GET userAnswer
UNTIL userAnswer != ‘Repete’
```

### For:
A for loop is just a specialized while loop that loops over elements of some collection
```text
GET limit
FOR each number up to limit
  IF number is divisible by 5 and 3 THEN
     PRINT “FizzBuzz”
  ELSE IF number is divisible by 3 THEN
    PRINT “Fizz”
  ELSE IF number is divisible by 5 THEN
    PRINT “Buzz”
  ELSE
    PRINT number
  ENDIF
ENDFOR
```

## Challenge

This activity will introduce students to several computer science concepts. Students will learn the necessity for thoroughness while programming and will be introduced to the often strange results of literalism. The overarching theme being introduced is that computers do what they are told and nothing more. The ability to read between the lines and determine what was meant rather than what was said is a skill computers lack.

Additionally, students are introduced to the concept of debugging through iterative attempts to program a computer to make a peanut butter and jelly sandwich.

```text
PROCEDURE MakeSandwich()

ENDPROCEDURE
```

[How to make peanut butter and jelly sandwich](https://www.youtube.com/watch?v=Ct-lOOUqmyY)
