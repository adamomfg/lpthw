#!/usr/bin/python
answers = """
True and True is True
False and True is False
1 == 1 and 2 == 1 is False
"test" == "test" is True
1 == 1 or 2 != 1 is True
True and 1 == 1 is True
False and 0 != 0 is False
True or 1 == 1 is True
"test" == "testing" is False
1 != 0 and 2 == 1 is False
"test" != "testing" is True
"test" == 1 is False
not (True and False) is True
not (1 == 1 and 0 != 1) is True
not (10 == 1 or 1000 = 1000) is False
not (1 != 10 or 3 == 4) is False
not ("testing" == "testing" and "Zed" == "Cool Guy") is True
1 == 1 and not ("testing" == 1 or 1 == 0) is True
"chunky" == "bacon" and not (3 == 4 or 3 == 3) is False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") is False
