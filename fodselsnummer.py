"""Functions for validation and generation of Norwegian fodselsnumbers"""

import re
from datetime import date, timedelta as td

# For Python 3 compability:
try:
    xrange
except NameError:
    xrange = range #pylint: disable=W0622, C0103

def check_fnr(fnr):
    """
    Check if a number is a valid fodselsnumber.

    Only checks the control digits, does not check if the
    individual numbers are used in the relevant year

    Args:
        fnr: A string containing the fodselsnummer to check
    Returns:
        True if it is a valid fodselsnummer, False otherwise.
    """
    if not re.match(r'\d{11}', fnr):
        return False
    generatedfnr = _generate_control_digits(fnr[0:9])
    if fnr == generatedfnr:
        return True
    else:
        return False

def generate_fnr_for_year(year, d_numbers):
    """
    Generates all the possible fodselsnumbers for a year.

    Args:
        year: The year to generate fodselsnummers for (integer)
        d_numbers: True if you want d-numbers as well, False otherwise.
    Returns:
        A list with all the possible fodselsnummers for that year.
    """
    allfnrs = []
    startdate = date(year, 1, 1)
    enddate = date(year, 12, 31)
    delta = enddate - startdate
    for i in xrange(delta.days + 1):
        allfnrs += generate_fnr_for_day(startdate + td(days=i), d_numbers)
    return allfnrs

def generate_fnr_for_day(day, d_numbers):
    """
    Generates all the possible fodselsnumbers for a day.

    Args:
        day: The day to generate fodslesnummers for (datetime)
        d_numbers: True if you want d-numbers as well, False otherwise.
    Returns:
        A list with all the possible fodselsnummers for that day.
    """
    thisdaysfnr = []
    stupid1900s = False
    datestring = day.strftime('%d%m%y')
    if d_numbers:
        dnrdatestring = str(int(datestring[0])+4) + datestring[1:]
    # ref:
    # http://www.kith.no/upload/5588/KITH1001-2010_Identifikatorer-for-personer_v1.pdf
    # Does not account for the 1800s, since this is for living persons
    # (this means that the 1800s list will be a little longer than necessary)
    if 1900 <= day.year <= 1999:
        individualmin = 000
        individualmax = 499
        if 1940 <= day.year <= 1999:
            stupid1900s = True
    else:
        individualmin = 500
        individualmax = 999
    for x in xrange(individualmin, individualmax+1):
        indivudalnr = str(x).zfill(3)
        fnr = _generate_control_digits(datestring + indivudalnr)
        if fnr != 'invalid':
            thisdaysfnr += [fnr]
        if d_numbers:
            dnr = _generate_control_digits(dnrdatestring + indivudalnr)
            if dnr != 'invalid':
                thisdaysfnr += [dnr]
    # Bonus round because of the stupid 1900s
    if stupid1900s:
        for x in xrange(900, 1000):
            indivudalnr = str(x).zfill(3)
            fnr = _generate_control_digits(datestring + indivudalnr)
            if fnr != 'invalid':
                thisdaysfnr += [fnr]
            if d_numbers:
                dnr = _generate_control_digits(dnrdatestring + indivudalnr)
                if dnr != 'invalid':
                    thisdaysfnr += [dnr]
    return thisdaysfnr

def _generate_control_digits(numbersofar):
    """Generates the magic control digits in a fodselsnumber"""
    staticnumbers1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1]
    staticnumbers2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    sum1 = 0
    for x in xrange(0, 9):
        sum1 += int(numbersofar[x]) * staticnumbers1[x]
    rest = sum1 % 11
    if rest == 0:
        control1 = 0
    else:
        if 11-rest != 10:
            control1 = 11-rest
        else:
            return 'invalid'
    numbersofar += str(control1)
    sum2 = 0
    for x in xrange(0, 10):
        sum2 += int(numbersofar[x]) * staticnumbers2[x]
    rest = sum2 % 11
    if rest == 0:
        control2 = 0
    else:
        if 11-rest != 10:
            control2 = 11-rest
        else:
            return 'invalid'
    numbersofar += str(control2)
    return numbersofar
