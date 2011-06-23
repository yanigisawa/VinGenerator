import vin, unittest


class TestCases(unittest.TestCase):

    def test_Remainder10ConvertedToX(self):
        print "Test 1"
        c = vin.getCheckSumChar("3P3ES47Y1XHMTPGGR")
        self.assertEqual("X", c, "Should return \"X\" on a % 10 check sum")
    
    def test_VinGeneratorGeneratesValidVin(self):
        print "Test 2"
        v = vin.getRandomVin()
        self.assertEqual(vin.isValidVin(v), True, "Did not generate a valid vin: %s" % (v))

if __name__ == '__main__':
    unittest.main()
