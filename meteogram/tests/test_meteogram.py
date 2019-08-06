"""Test use of the meteogram module."""

from meteogram import meteogram
from numpy.testing import assert_almost_equal, assert_array_almost_equal
from unittest.mock import patch
from meteogram import testing as mtesting

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


def test_wind_components_north():
    # Setup
    speed = 10
    direction = 0
    # Exercise
    u, v = meteogram.wind_components(speed, direction)
    # Verify
    true_u = 0
    true_v = -10
    assert_almost_equal(u, true_u)
    assert_almost_equal(v, true_v)
    # Cleanup - not needed


def test_wind_components_northeast():
    # Setup
    speed = 10
    direction = 45
    # Exercise
    u, v = meteogram.wind_components(speed, direction)
    # Verify
    true_u = -7.0710  # 10/sqrt(2)
    true_v = -7.0710  # 10/sqrt(2)
    assert_almost_equal(u, true_u, 4)
    assert_almost_equal(v, true_v, 4)
    # Cleanup - not needed


def test_wind_components_north360():
    # Setup
    speed = 10
    direction = 360

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = 0
    true_v = -10
    assert_almost_equal(u, true_u, 4)
    assert_almost_equal(v, true_v, 4)

    # Cleanup - not needed


def test_wind_components_speed0():
    # Setup
    speed = 0
    direction = 45
    # Exercise
    u, v = meteogram.wind_components(speed, direction)
    # Verify
    true_u = 0
    true_v = 0
    assert_almost_equal(u, true_u, 4)
    assert_almost_equal(v, true_v, 4)
    # Cleanup - not needed


def test_wind_components():
    # Setup
    speed = meteogram.np.array([10, 10, 10, 0])
    direction = meteogram.np.array([0, 45, 360, 45])

    # Exercise
    u, v = meteogram.wind_components(speed, direction)

    # Verify
    true_u = meteogram.np.array([0, -7.0710, 0, 0])
    true_v = meteogram.np.array([-10, -7.0710, -10, 0])
    assert_array_almost_equal(u, true_u, 3)
    assert_array_almost_equal(v, true_v, 3)
    # Cleanup
    # None

#
# Exercise 2 - Stop Here
#

#
# Instructor led mock example
#

#
# Exercise 3
#


# mock current utc time
def mocked_current_utc_time():
    """
    Mock our utc time function for testing with defaults
    because current_utc_time() never returns the same output twice!
    """
    # return a fixed datetime
    return meteogram.datetime.datetime(2018, 3, 26, 12)


# use a decorator to switch one function for another
@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_that_mock_works():
    """
    First, obviously, test that mock is being used correctly
    especially important for more complicated mocks!
    """
    # Setup - none

    # Exercise
    result = meteogram.current_utc_time()

    # Verify
    truth = meteogram.datetime.datetime(2018, 3, 26, 12)
    assert(result == truth)

    # Cleanup - none


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_with_defaults():
    """
    Test with no start or end date given
    """
    # Setup
    # station only
    station = 'FSD'

    # Exercise
    result_url = meteogram.build_asos_request_url(station)

    # test time: meteogram.datetime.datetime(2018, 3, 26, 12)
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=03&day1=25&'
                 'hour1=12&minute1=00&year2=2018&month2=03&day2=26&hour2=12'
                 '&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&'
                 'vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')
    # Verify
    assert(result_url == truth_url)
    # Cleanup
    # none needed


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_with_only_start_given():
    """
    Test with no end date given, only start date
    """
    # Setup
    station = 'FSD'
    start = meteogram.datetime.datetime(2018, 2, 16, 4)

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start)
    # test time: end date should be now, or datetime.datetime(2018, 3, 26, 12)
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=02&day1=16&'
                 'hour1=04&minute1=00&year2=2018&month2=03&day2=26&hour2=12&'
                 'minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&'
                 'vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')

    # Verify
    assert(result_url == truth_url)
    # Cleanup
    # none needed


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_build_asos_request_url_with_only_end_given():
    """
    Test with no end date given, only start date
    """
    # Setup
    station = 'FSD'
    end = meteogram.datetime.datetime(2018, 2, 16, 4)

    # Exercise
    result_url = meteogram.build_asos_request_url(station, None, end)

    # test time: 24 hrs before end -  datetime.datetime(2018, 2, 15, 4)
    truth_url = ('https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?'
                 'station%5B%5D=FSD&tz=UTC&year1=2018&month1=02&day1=15&'
                 'hour1=04&minute1=00&year2=2018&month2=02&day2=16&hour2=04&'
                 'minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&'
                 'vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes')
    # Verify
    assert(result_url == truth_url)
    # Cleanup
    # none needed


#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#


def test_current_utc_time():
    """
    Call it twice and ignore the microseconds part
    """
    # Setup - none

    # Exercise
    result = meteogram.current_utc_time()

    # Verify
    truth = meteogram.datetime.datetime.utcnow()
    delta = truth.timestamp() - result.timestamp()
    # test that less than 1/10000th of a second occurs between calls
    assert_almost_equal(delta, 0, 4)

    # Cleanup - none


def test_exner_function():
    # Setup
    pressure = 500
    # reference_pressure = 1000

    # Exercise
    result = meteogram.exner_function(pressure)

    # Verify
    truth = 0.8203833  # calculated by hand
    assert_almost_equal(result, truth, 4)

    # Cleanup - none


def test_potential_temperature():
    """
    As the docstring says:
      For inputs of 800 hPa and 273 Kelvin, output should be 290.96 K
    """
    # Setup
    pressure = 800
    temperature = 273

    # Exercise
    result = meteogram.potential_temperature(pressure, temperature)

    # Validate
    truth = 290.96
    assert_almost_equal(result, truth, 2)

    # Cleanup - none


@patch('meteogram.meteogram.current_utc_time', new=mocked_current_utc_time)
def test_download_asos_data():
    """Test downloading ASOS data."""
    # Setup
    url = meteogram.build_asos_request_url('AMW')

    # Exercise
    df = meteogram.download_asos_data(url)

    # Verify
    first_row_truth = mtesting.pd.Series(
        {'station_id': 'AMW',
         'station_name': 'Ames',
         'latitude_deg': 41.990439,
         'longitude_deg': -93.618515,
         'UTC': mtesting.pd.Timestamp('2018-03-25 12:00:00'),
         'temperature_degF': 29,
         'dewpoint_degF': 24,
         'wind_speed_knots': 8,
         'wind_direction_degrees': 113})

    mtesting.assert_dataseries_equal(df.iloc[0], first_row_truth)


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
