#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) **O(n)**
because you need to iterate up to n^3, but you are going up by n^2 each time

b) **O(nlog(n))**
Outer loop goes up by n, inner loop iterates up by * 2 so it is log(n)

c) **O(n)**
Every input must be put recursively through the operation again, but the operation is to only add 2 or just return 0 eventually.

## Exercise II
To Minimize eggs dropped and broken:
- I place the egg on a scale (analog), with a camera recording. Build a device that drops a flat surface directly onto the egg, this surface can be loaded with variable mass. 
- I measure the size of the egg and reference online resources about how much force it takes on average to break that egg. 
(https://royalsocietypublishing.org/doi/10.1098/rsif.2016.0804) 
- Calibrate the device to apply half that much force to the egg, and execute.
    - Check how much damage the egg took. You can tell how deep a crack/scratch is relative to breaking point if you've cracked enough eggs while cooking. 
    - Document the force applied via camera review of the scale after impact
- Using your estimate of how much damage the egg took, adjust the force applied and swap eggs. 
    - If virutally no damage taken, move up by one standard deviation as determined by the study. If minimal damage taken, just add 1 gram until the egg is very NEAR breaking
    - Iterate as needed, no eggs are being dropped here.
- Armed with the knowledge of the force required to very nearly break an egg, measure the height of one story, and calculate the number of stories to reach the height where dropping the egg off would equate to that force. 
- Again, check damage but now iterate based off of standard deviations in the study. No damage => up 1.5 SD, Moderate damage => up by 0.5 SD, Severe damage but not broken => up by one floor. If broken, go down by 1 SD and repeat as needed.
This is O(3) ~ **O(1)** because it does not change with the number of floors. 


### Boring suboptimal answer
Use binary search: start at half the floors and go up by half the remaining floors if it doesn't break, or down half the remaining floors if it does break. Remaining, defined as the floors in between the values you tried.
This is **O(log(n))**



