# AP-CSP-Create-Task
The Create Performance Task I submitted for my 2023 AP Computer Science Principles test.

This code models a car dealership that is developing a website in order to automatically estimate the value of the vehicle a user hands in. They buy SUVs, Sedans, and Sports-cars and want the code to allow for adjusting the car types if the dealership wants to add/remove a new car-type to the list of vehicles they buy. The dealership also buys motorcycles.
**The method in which the dealership values each vehicle is:**
- If the vehicle is a car, specifically an SUV, the vehicle is valued at $20k and eligible for a 10% bonus if the car's model is after 2017.
- Otherwise, if the vehicle is another type of car, it is valued at $15k.
- If the vehicle is a bike, it is valued at $8k, and is eligible for a 20% bonus if it is a sport-bike whose model is 2020 or after.
Finally,
- If the vehicle has more than 100k miles, it loses 20% of the original value.
- If the vehicle is uninsured, it loses 10% of the original value.
- If the vehicle has been in an accident, it loses 10% of the original value.

*The AP CSP Task must contain at least 1 user-defined function and 1 array.*
