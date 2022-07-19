# time_adder
### The following program requires no additional libraries to compile
This program calculates time in 12 Hour-format with weekdays and amount of days included alongwith adding time it can also decode time from 12 hour format to 24 hour format and vice versa by it's 2 methods namely `encode_time()` and `decode_time()`
To use this class we need to pass the input in 3 parts as follows:

`add_time(time,duration [amount of time you want to add], day of the week [optional])`

##### Duration must be in hours and minutes for example: 205:45 (means 205 hours and 45 minutes)


##### Time must be entered in 12 hour format if you want to enter in 24 hour format just encode the time into 12 hour format before using `add_time()`

