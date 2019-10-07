# Adding_Report

This program calls the adding_report() function which repeatedly takes positive integer input until the user quits and then sums the integers and prints a "report".
The adding_report() function has 2 type of report:

"Q" or "q" used as the argument to adding_report() results in printing of all of the input integers and the total
"Quit" or "quit" used as the argument results in printing only the total

Sample input and output:
call adding_report() with "Q" or "q"  as argument (print all the integers entered and the total)
```
Input an integer to add to the total or "Q" to quit
Enter an integer or "Q": 3
Enter an integer or "Q": 6
Enter an integer or "Q": 24
Enter an integer or "Q": 17
Enter an integer or "Q": 61
Enter an integer or "Q": nine
nine is invalid input
Enter an integer or "Q": q

Items
3
6
24
17
61

Total
 111
call with "T"(print only the total)
```
call adding_report() with "Quit" or "quit" as argument (print all the integers entered and the total)
```
Input an integer to add to the total or "Q" to quit
Enter an integer or "Q": 5
Enter an integer or "Q": 7
Enter an integer or "Q": Quit

Total
 12
 ```
