
<h1 align="center">Simple Linear Regression From Scratch</h1>
<div>
  <p align="center">
    In this project, I break down the basic idea of Linear Regression with One Variable without using Scikit-Learn,  just simple to understand how the Simple Linear Regression works in the background. 
    <br/>
  </p>
</div>

<br/>
<div align="center">
  <a href="https://i.imgur.com/b8suQcK.png">
    <img src="https://i.imgur.com/b8suQcK.png" alt="Logo" width="860" height="444">
  </a>

<br/>
</div>

## Tech Stack

* **Python:** Version 3.10

* **NumPy:** Version 1.23.0

* **Pandas:**: Version 1.4.4

* **Matplotlib**: Version 3.5.3 

* **Spyder IDE**: Version 5.3.2

## Details

* I implemented here an algorithm from scratch to find the best fit line of a list of point[x,y]. I have applied 2 different datasets I found online, I draw the graphs of each one of them 2 graphs for each, on for the dataset with the fit line. and the second for the epochs and error, so you can understand how the error work and when it is not recommended to increase the iterations (as it will be waste of resources). So, as you see in the errors graphs almost the slope is Zero (There is no change in values).

* When you change your dataset and change the number of iterations and alpha value you might find the output as NaN or an Overflow Error. To solve this, multiply the dataset by 0.01 for example (This depends on the dataset), but this may solve the problem.

* For all the equation I used, why it is like this? How could you derive them also? Please check the References.

<br/>

## Figures
* [Figure 1 - Example 1 Fit Line - High Quality](https://i.imgur.com/7AyAf5i.png) 
* [Figure 2 - Example 1 Error - High Quality](https://i.imgur.com/5WeWQwC.png) 
 <div align="center">
  <a href="https://i.imgur.com/7AyAf5i.png">
    <img src="https://i.imgur.com/7AyAf5i.png" alt="Figure 1" width="488" height="500">
      <a href="https://i.imgur.com/5WeWQwC.png">
    <img src="https://i.imgur.com/5WeWQwC.png" alt="Figure 1" width="488" height="500">
  </a>
</div>

* [Figure 3 - Example 2 Fit Line - High Quality](https://i.imgur.com/XYcsOL4.png) 
* [Figure 4 - Example 2 Error - High Quality](https://i.imgur.com/5WeWQwC.png) 
 <div align="center">
  <a href="https://i.imgur.com/XYcsOL4.png">
    <img src="https://i.imgur.com/XYcsOL4.png" alt="Figure 1" width="500" height="440">
  <a href="https://i.imgur.com/cJEhQIA.png">
    <img src="https://i.imgur.com/cJEhQIA.png" alt="Figure 1" width="500" height="440">
  </a>
</div>
<br/>
<br/>



## Contributing
Contributions are what makes the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Do not forget to give the project a star! Thanks again!

<br/>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.





## References

*  This is important [Article](https://www.analyticsvidhya.com/blog/2021/04/gradient-descent-in-linear-regression/), as it illustrates how to deal the partial dervatives.

*  I recommend this article because it shows you an [Example using Python](https://www.geeksforgeeks.org/gradient-descent-in-linear-regression/)


## Contacts
* Via Email : Mahmoud.Nady@Ejust.edu.eg
* [Via FaceBook]( https://www.facebook.com/MND919/ ).







