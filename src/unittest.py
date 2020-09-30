import sys


def test(did_pass):
    """  Print the result of a test.  """
    line_num = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = ("Test at line {0} FAILED.".format(line_num))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(abs(17) == 17)
    test(abs(-17) == 17)
    test(abs(0) == 0)
    test(abs(3.14) == 3.14)
    test(abs(-3.14) == 3.14)


test_suite()        # Here is the call to run the tests
