# TappedOutUserParser
Basic parser for TappedOut. Used to get deck stats for single users.

## Usage

1. Install Python (see https://www.python.org/about/gettingstarted/)
2. Copy the script parse.py to your local machine (or clone the repository)
3. Run it with your options

python parse.py -p 7 -u "CommandersBrew" > commandersbrew.csv

## Options

-u, --user: The user to be parsed (get from tapped out at http://tappedout.net/users/CommandersBrew).  For this URL, the user is CommandCast

-p, --pages: The number of pages.  Go to the user's tapped out page and click decks.  See how many pages are listed.
http://tappedout.net/users/commandersbrew/mtg-decks/.  For this URL, there are 7 pages

-v, --verbose: The script can take awhile to run.  If you want to debug it or see what it's doing, set -v to true.  Verbose defaults to false.

## Results

Results in CSV form are in the results directory.

## Help!

No guarantees but you can comment on this repo or tweet at me.  https://twitter.com/Devil_Bug

# License

Copyright 2017 Nate Noonen

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
