"""Run this file to run the development server"""

import argparse

from application import appfactory

app = appfactory.create_app()

app.secret_key = "dev"
app.config["DATABASE"] = "data/quizagator.db"

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d, --debug",
    dest="debug",
    default=False,
    action="store_true",
    help="set debug mode",
)
parser.add_argument(
    "--port",
    dest="port",
    type=int,
    default=5000,
    help="port to listen on (default: 5000)",
)
parser.add_argument(
    "--host",
    dest="host",
    type=str,
    default="0.0.0.0",
    help="host to serve from (default: 0.0.0.0)",
)

args = parser.parse_args()

app.debug = args.debug
app.run(args.host, args.port)
