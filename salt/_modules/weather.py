# -*- coding: utf-8 -*-
'''
:depends: requests

Pulls current weather from the National Weather Service API

https://www.weather.gov/documentation/services-web-api

Credit:
    https://www.linode.com/docs/applications/configuration-management/create-a-salt-execution-module/
'''

# Python libraries
from __future__ import absolute_import
import logging

# Third-party libraries
try:
    from requests.exceptions import RequestException
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


log = logging.getLogger(__name__)


__virtual_name__ = 'weather'


def __virtual__():
    '''
    Only load weather if requests is available
    '''
    if HAS_REQUESTS:
        return __virtual_name__
    else:
        return False, 'The weather module cannot be loaded: requests package unavailable.'


def get(stations, fahrenheit=False):
    '''
    Gets the current weather

    :param stations: US weather station code or comma-separated list of stations

    :param fahrenheit: Show temperature in degrees Fahrenheit if True

    CLI Example:

    .. code-block:: bash

        salt minion weather.get KPHL

    This module also accepts multiple values in a comma seperated list:

    .. code-block:: bash

        salt minion weather.get KPHL,KACY

    '''
    log.debug(stations)

    return_value = {}

    stations = stations.split(',')

    for station in stations:
        return_value[station] = _observation_request(station, fahrenheit=fahrenheit)

    return return_value


def _observation_request(station, obsv_time='latest', fahrenheit=False):
    '''
    The function that makes the request for weather data from the National Weather Service.
    '''
    try:
        request = requests.get('https://api.weather.gov/stations/{0}/observations/{1}'.format(station, obsv_time))

        log.debug(request.text)

        temperature = float(request.json()['properties']['temperature']['value'])

        if fahrenheit:
            temperature = (temperature * (9/5)) + 32

        conditions = {
            'description': request.json()['properties']['textDescription'],
            'temperature': round(temperature, 1)
        }
    except RequestException as exc:
        log.debug(exc)
        conditions = 'Unable to contact the weather service API.'
    except (KeyError, ValueError, TypeError) as exc:
        log.debug(exc)
        conditions = 'Unable to parse API response.'

    return conditions
