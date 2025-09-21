import unittest
import math
import circle  # module name is "circle" so str/repr include "circle.Circle"

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        print("Setting up!")

    def tearDown(self):
        print("Tearing down!\n")


class TestCircleBasics(BaseTestCase):

    def test_add(self):
        c1 = circle.Circle(5)
        c2 = circle.Circle(6)
        result = c1 + c2
        print(f"Add {c1} + {c2} == {result}")
        self.assertIsInstance(result, circle.Circle)
        self.assertEqual(result.radius, 11)

    def test_area(self):
        c = circle.Circle(5)
        print(f"Circle with radius 5 has area {c.area}")
        self.assertAlmostEqual(c.area, math.pi * 25)

    def test_str(self):
        c = circle.Circle(5)
        print(c)
        self.assertEqual(str(c), "circle.Circle with radius: 5")

    def test_mul(self):
        c = circle.Circle(5)
        r1 = c * 5
        r2 = 5 * c
        print(f"Mult {c} * 5 == {r1}")
        self.assertEqual(r1.radius, 25)
        self.assertEqual(r2.radius, 25)

    def test_diameter(self):
        c = circle.Circle(5)
        print(f"Circle diameter with radius 5 is {c.diameter}")
        self.assertEqual(c.diameter, 10)

    def test_repr(self):
        c = circle.Circle(5)
        rep = repr(c)
        print(f"Circle repr is {rep}")
        self.assertEqual(rep, "circle.Circle(5)")
        d = eval(rep)
        self.assertIsInstance(d, circle.Circle)
        self.assertEqual(d.radius, 5)

    def test_set_diameter(self):
        c = circle.Circle(5)
        c.diameter = 8
        print(f"Circle with new diameter {c.diameter} has radius {c.radius}")
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)

    def test_str_module_prefix(self):
        c = circle.Circle(5)
        s = str(c)
        print(f"circle.Circle str is {s}")
        self.assertEqual(s, "circle.Circle with radius: 5")

    def test_from_diameter(self):
        c = circle.Circle.from_diameter(8)
        print(f"Circle FROM diameter {c.diameter} has radius {c.radius}")
        self.assertEqual(c.radius, 4)
        self.assertEqual(c.diameter, 8)

    def test_sorting(self):
        items = [circle.Circle(2), circle.Circle(1), circle.Circle(5), circle.Circle(4), circle.Circle(3)]
        print(f"unsorted circles {items}")
        items.sort()
        print(f"sorted circles {items}")
        self.assertEqual([c.radius for c in items], [1,2,3,4,5])


class TestSphere(BaseTestCase):

    def test_add(self):
        s1 = circle.Sphere(5)
        s2 = circle.Sphere(6)
        r = s1 + s2
        print(f"Add {s1} + {s2} == {r}")
        self.assertIsInstance(r, circle.Sphere)
        self.assertEqual(r.radius, 11)

    def test_area_surface(self):
        s = circle.Sphere(5)
        print(f"Sphere with radius 5 has area {s.area}")
        # surface area: 4πr^2
        self.assertAlmostEqual(s.area, 4 * math.pi * 25)

    def test_sorting(self):
        items = [circle.Sphere(2), circle.Sphere(3), circle.Sphere(1)]
        print(f"unsorted spheres {items}")
        items.sort()
        print(f"sorted spheres {items}")
        self.assertEqual([s.radius for s in items], [1,2,3])

    def test_volume(self):
        s = circle.Sphere(5)
        print(f"Sphere with radius 5 has volume {s.volume}")
        self.assertAlmostEqual(s.volume, (4/3) * math.pi * 125)


if __name__ == "__main__":
    unittest.main()
