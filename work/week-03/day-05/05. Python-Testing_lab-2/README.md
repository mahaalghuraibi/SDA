# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python unit testing lab

## Introduction

In this activity, we will use the test-driven development (TDD) approach to create a class that represents a simple circle. A `Circle` can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.<br/><br/>

Other abilities of a Circle instance:

- Compute the circle's area.
- Print the circle and get something nice.
- Be able to add two circles together.
- Be able to compare two circles to see which is bigger.
- Be able to compare to see if they are are equal.
- (follows from above) be able to put them in a list and sort them.

You will use:

- properties.
- a bunch of **magic methods**.
- a `classmethod`.

**General Instructions:**
For each step, write a couple of unit tests that test the new features.

- Run these tests (and they will fail the first time)
- Add the code required for your tests to pass.

**Step 1:**

- Create class called `Circle` – it’s signature should look like:
  ```python
  c = Circle(the_radius)
  ```
- The radius is a required parameter (can’t have a circle without one!)
- The resulting circle should have an attribute for the radius: `c.radius` So you can do:
    ```text
    >> c = Circle(4)
    >> print(c.radius)
    >> 4
    ```
- Remember: tests first!

**Step 2:**

- Add a **diameter** property, so the user can get the diameter of the circle:
   ```text
  >> c = Circle(4)
  >> print(c.diameter)
  >> 8
  ```

**Step 3:**

- Set up the diameter property so that the user can set the diameter of the circle:
  ```text
  >>c = Circle(4)
  >>c.diameter = 2
  >>print(c.diameter)
  >>2
  >>print(c.radius)
  >> 1
  ```
- NOTE that the radius has changed!

Important:

- Do not store both the radius and the diameter as attributes! If you do that, they could get out of sync. So store only one (the radius), and have the other calculated `on the fly` by the property.

**Step 4:**

- Add an area property so the user can get the area of the circle:
  ```text
  > c = Circle(2)
  >> print(c.area)
  >> 12.566370
  ```
- PI can be found in the math module.
- The user should not be able to set the area:
  ```text
  >> c = Circle(2)
  >> c.area = 42
  >> AttributeError
  ```

**Step 5:**

- Add an **alternate constructor** that lets the user create a Circle directly with the diameter:
  ```text
  >> c = Circle.from_diameter(8)
  >> print(c.diameter)
  8
  >> print(c.radius)
  4
  ```
- Hint: This is a good use case for a classmethod

**Step 6:**

- Every class should have a nice way to print it out values
- Add `__str__` and `__repr__` methods to your Circle class.
- Now you can print it:
  ```text
  c = Circle(4)
  
  print(c)
  Circle with radius: 4.000000
  
  repr(c)
  Out[4]: 'Circle(4)'
  
  d = eval(repr(c))
  
  d
  Out[6]: Circle(4)
  ```

**Step 7:**

- Add some of the numeric protocol to your Circle.
- You should be able to add two circles:
  ```text
  c1 = Circle(2)
  c2 = Circle(4)
  c1 + c2
  Out[9]: Circle(6)
  ```
- And multiply one by a number:
  ```text
  c2 * 3
  Out[16]: Circle(12)
  ```
- What happens with `3 * c2` ? – can you fix that?

**Step 8:**

- Add the ability to compare two circles:
  ```text
  c1 > c2
  Out[10]: False
  
  c1 < c2
  Out[11]: True
  
  c1 == c2
  Out[12]: False
  
  c3 = Circle(4)
  
  c2 == c3
  Out[14]: True
  ```
- Once the comparing is done, you should be able to sort a list of circles:
- print circles
  ```text
  [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
  ```
- Sort circles `circles.sort()`
  ```text
  [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
  ```
- NOTE: make sure to write unit tests for all of this! Ideally before writing the code.

**Step 9: Subclassing!**

- You’ve got a circle already – what if you needed a Sphere? They have a fair bit in common – both defined by a radius, same relationship of radius to diameter, etc.
- So we can get a pretty useful `Sphere` class by simply subclassing `Circle`, and adding and changing a couple things.

Create a `Sphere` Class that subclasses `Circle`.

- Override the `__str__` and `__repr__` methods to be appropriate for Spheres.
- Create a volume property that returns the volume (hint: volume of a sphere is: `4/3 pi r^3`).
- Override the area property so that it either computes the surface area of a sphere (what’s the formula for that???),
  or have it raise an exception: maybe `NotImplementedError`.
- Make sure to write some tests – maybe ahead of time! – that confirm that all this works. And the other things like
  addition, and sorting…
- Check that the `Sphere.from_diameter()` alternate constructor actually creates a Sphere! (you DO NOT have to write a
  new `classmethod` for that!) – pretty cool, eh?

### Expected output

```text
(venv) Sureshs-MBP:python-unit-testing-lab suresh$ python3 -m unittest test.unit.test_circle
Setting up!
Add circle.Circle with radius: 5 + circle.Circle with radius: 6 == circle.Circle with radius: 11
Tearing down!

.Setting up!
Circle with radius 5 has area 78.53981633974483
Tearing down!

.Setting up!
Circle with radius 5
Tearing down!

.Setting up!
Mult circle.Circle with radius: 5 * 5 == circle.Circle with radius: 25
Tearing down!

.Setting up!
Circle diameter with radius 5 is 10
Tearing down!

.Setting up!
Circle repr is circle.Circle(5)
Tearing down!

.Setting up!
Circle with new diameter 8.0 has radius 4.0
Tearing down!

.Setting up!
circle.Circle str is circle.Circle with radius: 5
Tearing down!

.Setting up!
Circle FROM diameter 8.0 has radius 4.0
Tearing down!

.Setting up!
unsorted circles [circle.Circle(2), circle.Circle(1), circle.Circle(5), circle.Circle(4), circle.Circle(3)]
sorted circles [circle.Circle(1), circle.Circle(2), circle.Circle(3), circle.Circle(4), circle.Circle(5)]
Tearing down!

.Setting up!
Add Sphere with radius: 5 + Sphere with radius: 6 == Sphere with radius: 11
Tearing down!

.Setting up!
Sphere with radius 5 has area 314.1592653589793
Tearing down!

.Setting up!
unsorted spheres [Sphere(2), Sphere(3), Sphere(1)]
sorted spheres [Sphere(1), Sphere(2), Sphere(3)]
Tearing down!

.Setting up!
Sphere with radius 5 has volume 523.5987755982989
Tearing down!

.
----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```
