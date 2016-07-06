#!/usr/bin/env python
import os
import sys
import logging
import argparse
import requests
import ConfigParser

def parse_configuration_file(config_path):
    logging.debug("Checking %s for configuration options", config_path)
    if not os.path.exists(config_path):
        logging.critical("Config_path: %s doesn't exist! Exiting.", config_path)
        sys.exit(1)

    config = ConfigParser.ConfigParser()
    config.readfp(config_path)

    try:
        u = config.get("user", "username")
        p = config.get("user", "password")
        login_credentials = {"username": u, "password": p}
    except ConfigParser.NoOptionError as e:
        logging.critical("Error parsing user info. config_path: %s", config_path)
        logging.critical("%s", e.message)

    try:
        referer = config.get("kronos", "referer")
        login_page = config.get("kronos", "login")
        home_page = config.get("kronos", "homepage")
        timestamp_page = config.get("kronos", "timestamp")
        kronos_pages = {"login": login_page, "home": home_page,
                        "timestamp": timestamp_page, "referer": referer}
    except ConfigParser.NoOptionError as e:
        logging.critical("Error parsing kronos info. config_path: %s", config_path)
        logging.critical("%s", e.message)

    return login_credentials, kronos_pages

def timestamp(login_credentials, pages):

    with requests.Session() as session:
        session.get(pages['home'])
        cookies = requests.utils.dict_from_cookiejar(session.cookies)
        headers = dict(cookies.items() +
                       [('Referer', pages['referer'])])

        response = session.post(pages['login'], data=login_credentials,
                     headers=headers)

        response = session.post(pages['timestamp'], data={'transfer': ''})

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--config', action='store_true',
                        default=os.path.join(os.getcwd(), 'kronos.cfg'),
                        help="Path to configuration file")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Enable for debugging purposes")

    args = parser.parse_args()

    logformat = "%(asctime)s: %(levelname)s (Line: %(lineno)d) - %(message)s"
    logdateformat = "%I:%M:%S"
    loglevel = logging.INFO
    if args.verbose:
        loglevel = logging.DEBUG

    logfile = 'kronos_inout.log'
    logging.basicConfig(filename=logfile, filemode='w', level=loglevel,
                        format=logformat, datefmt=logdateformat)

    config_options = parse_configuration_file(args.config)
    time_stamp(*config_options)

if __name__ == "__main__":
    main()
