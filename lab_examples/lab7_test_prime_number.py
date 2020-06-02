import unittest

class TestPrimeNumber(unittest.TestCase):
    def setUp(self):
        from prime import is_prime
        self.is_prime = is_prime

    def test_should_be_prime(self):
        known_prime_numbers = [2, 5, 7, 13, 19, 131071]
        for prime in known_prime_numbers:
            self.assertTrue(self.is_prime(prime))


    def test_should_be_nonprime(self):
        nonprimes = [4, 9, 12, 120, 2047]
        for nonprime in nonprimes:
            self.assertFalse(self.is_prime(nonprime))


    def test_negative_primes(self):
        primes = [-2, -5, -7, -131071]
        nonprimes = [-4, -9, -12, -120]
        for prime in primes:
            self.assertTrue(self.is_prime(prime))

        for nonprime in nonprimes:
            self.assertFalse(self.is_prime(nonprime))


    def test_one(self):
        self.assertFalse(self.is_prime(1))


if __name__ == '__main__':
    unittest.main()
