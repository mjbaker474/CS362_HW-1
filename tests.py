# Author: Matthew Baker
# Github: mjbaker474
# Email: bakerma2@oregonstate.edu
# Assignment: CS362 HW 1
# Description: Black Box test file for credit card validator.

import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    """Unit tests for credit_card_validator function."""

    def test_1(self):
        """Verifies  an empty input returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator(""))

    def test_2(self):
        """Verifies  input of invalid length of 14 numbers returns False.

        Picked using Category Partition Testing with TSL Generator
        """
        self.assertFalse(credit_card_validator("34309692356998"))

    def test_3(self):
        """Verifies  input of invalid length of 17 numbers returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("40240071442295225"))

    def test_4(self):
        """Verifies input of valid lenght containing characters returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("347785F60148522"))

    def test_5(self):
        """Verifies input of valid length and checksum with invalid prefix
        (i.e. Discover) returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("6011000991543426"))

    def test_6(self):
        """Verifies Visa of valid length and valid checksum returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("4532506055819135"))

    def test_7(self):
        """Verifies Visa of valid length but invalid checksum returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("4532507055819135"))

    def test_8(self):
        """Verifies Visa of invalid length and valid checksum returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("471631470134869"))

    def test_9(self):
        """Verifies Amex prefix 34 of valid length and valid checksum
        returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("342146104324189"))

    def test_10(self):
        """Verifies Amex prefix 34 of valid length but invalid checksum
          returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("349172073814442"))

    def test_11(self):
        """Verifies Amex prefix 34 of invalid length and valid checksum
          returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("3413773968849916"))

    def test_12(self):
        """Verifies Amex prefix 37 of valid length and valid checksum
          returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("377275905899863"))

    def test_13(self):
        """Verifies Amex prefix 37 of valid length but invalid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("373347543116662"))

    def test_14(self):
        """Verifies Amex prefix 37 of invalid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("3712208948430568"))

    def test_15(self):
        """Verifies invalid Amex prefix 36 of valid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("367858746772969"))

    def test_16(self):
        """Verifies Mastercard prefix 51 of valid length and valid checksum
        returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("5104128231187082"))

    def test_17(self):
        """Verifies Amex prefix 51 of valid length but invalid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("5104128231197082"))

    def test_18(self):
        """Verifies Amex prefix 51 of invalid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("510412823118708"))

    def test_19(self):
        """Verifies Mastercard prefix 53 of valid length and valid checksum
        returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("5380483430624061"))

    def test_20(self):
        """Verifies Mastercard prefix 53 of valid length but invalid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("5380483730624061"))

    def test_21(self):
        """Verifies Mastercard prefix 53 of invalid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("538048373062405"))

    def test_22(self):
        """Verifies Mastercard prefix 55 of valid length and valid checksum
        returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("5508509124753795"))

    def test_23(self):
        """Verifies Mastercard prefix 55 of valid length but invalid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("5508500124753795"))

    def test_24(self):
        """Verifies Mastercard prefix 55 of invalid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("550850012475374"))

    def test_25(self):
        """Verifies Mastercard prefix 2221 of valid length and valid checksum
        returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("2221463767450181"))

    def test_26(self):
        """Verifies Mastercard prefix 2221 of valid length but invalid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("2221463767450180"))

    def test_27(self):
        """Verifies Mastercard prefix 2221 of invalid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("222146376745017"))

    def test_28(self):
        """Verifies Mastercard prefix 2500 of valid length and valid checksum
        returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("2500569917935947"))

    def test_29(self):
        """Verifies Mastercard prefix 2500 of valid length but invalid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("2500569917435947"))

    def test_30(self):
        """Verifies Mastercard prefix 2500 of invalid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("250056991743591"))

    def test_31(self):
        """Verifies Mastercard prefix 2720 of valid length and valid checksum
        returns True.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertTrue(credit_card_validator("2720679350726192"))

    def test_32(self):
        """Verifies Mastercard prefix 2720 of valid length but invalid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("2720659350726192"))

    def test_33(self):
        """Verifies Mastercard prefix 2720 of invalid length and valid checksum
        returns False.

        Picked using Category Partition Testing with TSL Generator.
        """
        self.assertFalse(credit_card_validator("272065935072615"))

    def test_35(self):
        """Verifies invalid Amex prefix 35 of valid length and valid checksum
        returns False.

        Added to check boundary tests not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("359478142013734"))

    def test_36(self):
        """Verifies invalid Mastercard prefix 50 of valid length and valid
         checksum returns False.

        Added to check boundary tests not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("5024873210221785"))

    def test_37(self):
        """Verifies invalid Mastercard prefix 56 of valid length and valid
         checksum returns False.

        Added to check boundary tests not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("5624873210221789"))

    def test_38(self):
        """Verifies invalid Mastercard prefix 2220 of valid length and valid
         checksum returns False.

        Added to check boundary tests not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("2200873210221788"))

    def test_39(self):
        """Verifies invalid Mastercard prefix 2721 of valid length and valid
         checksum returns False.

        Added to check boundary tests not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("2721873210221788"))

    def test_40(self):
        """Verifies invalid prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error guessing test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("9521873210221785"))

    def test_41(self):
        """Verifies invalid prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error guessing test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("688524809611146"))

    def test_42(self):
        """Verifies None type returns False.

        Added as Error guessing test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator(None))

    def test_43(self):
        """Verifies Str of all characters returns False.

        Added as Error guessing test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("abcdefghijklmnop"))

    def test_44(self):
        """Verifies invalid 3 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("3933962240020468"))

    def test_45(self):
        """Verifies invalid 5 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("5933962240020463"))

    def test_46(self):
        """Verifies invalid 0 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("0831253539009159"))

    def test_47(self):
        """Verifies invalid 1 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("1831253539009157"))

    def test_48(self):
        """Verifies invalid 2 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("2831253539009155"))

    def test_49(self):
        """Verifies invalid 4 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("4831253539009151"))

    def test_50(self):
        """Verifies invalid 6 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("6831253539009156"))

    def test_51(self):
        """Verifies invalid 7 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("7831253539009154"))

    def test_52(self):
        """Verifies invalid 8 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("8831253539009152"))

    def test_53(self):
        """Verifies invalid 9 prefix of valid 16 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("9831253539009150"))

    def test_54(self):
        """Verifies invalid 0 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("097695398001306"))

    def test_55(self):
        """Verifies invalid 1 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("197695398001305"))

    def test_56(self):
        """Verifies invalid 2 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("297695398001304"))

    def test_57(self):
        """Verifies invalid 4 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("497695398001302"))

    def test_58(self):
        """Verifies invalid 5 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("597695398001301"))

    def test_59(self):
        """Verifies invalid 6 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("697695398001300"))

    def test_60(self):
        """Verifies invalid 7 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("797695398001309"))

    def test_61(self):
        """Verifies invalid 8 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("897695398001308"))

    def test_62(self):
        """Verifies invalid 9 prefix of valid 15 digit length and valid
         checksum returns False.

        Added as Error boundary test not covered by initial partition
        categories.
        """
        self.assertFalse(credit_card_validator("997695398001307"))


if __name__ == '__main__':
    unittest.main()
