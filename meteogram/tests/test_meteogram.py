"""Test use of the meteogram module."""

from meteogram import meteogram
from numpy.testing import assert_almost_equal

#
# Example starter test
#
def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup - none necessary

#
# Instructor led introductory examples
#

#
# Instructor led examples of numerical comparison
#

#
# Exercise 1
#
def test_build_asos_request_url_single_digit_datetimes():
    """
    Test building URL with single digit month and day.
    Setup
    Exercise
    Verify
    Cleanup
    """
    # Setup
    # station, start_date, end_date
    start = meteogram.datetime.datetime(2018, 1, 2, 3, 4)
    end = meteogram.datetime.datetime(2018, 5, 6, 7, 8)
    station = 'FSD'

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=01&day1=02&'
                 'hour1=03&minute1=04&year2=2018&month2=05&day2=06&hour2=07&'
                 'minute2=08&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&'
                 'vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')

    # Verify
    assert(result_url == truth_url)
    # Cleanup
    # none needed



def test_build_asos_request_url_double_digit_datetimes():
    """
    Test building URL with double digit month and day.
    """
    # Setup
    station = 'FSD'
    # two-digits in the datetime
    start = meteogram.datetime.datetime(2018, 11, 12, 13, 14)
    end = meteogram.datetime.datetime(2018, 11, 12, 15, 16)


    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=11&day1=12&'
                 'hour1=13&minute1=14&year2=2018&month2=11&day2=12&hour2=15&'
                 'minute2=16&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&'
                 'vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')

    # Verify
    assert(result_url == truth_url)
    # Cleanup
    # None

#
# Exercise 1 - Stop Here
#


#
# Exercise 2 - Add calculation tests here
#


def test_vector_addition():
    # Setup
    # directions - 0, 45, 360; windspeed 0
    speed = 0
    directions = meteogram.np.radians(meteogram.np.array([0, 45, 360]))

    truth = np.array([[-0*0., -0*1.],
                      [-0*1/np.sqrt(2), -0*1/np.sqrt(2)],
                      [-0*0, -0*1]])

    # Exercise
    for d in directions:
        u = -speed * meteogram.np.cos(d)
        v = -speed * meteogram.np.sin(d)


    # Verify
    # Cleanup


#
# Exercise 2 - Stop Here
#

#
# Instructor led mock example
#

#
# Exercise 3
#

#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
