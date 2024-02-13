# FUTDraftSimulator

Python-based project designed to simulate a Fifa-like Draft tournaments.


## Details

Simulation is based on logic used in pre-2014 FIFA games. The program is comparing each teams positions cumulative OVR to respective opponents positions OVR like in schema below: <br />
Forward : Defender <br />
Midfielder : Midfielder <br />
Defender : Forward <br />
The original algorithm used in FIFA games forced 3 goals to happen throughout the game. Our algorithm is based on probability and allows up to 6 goals, allowing games to end up a tie and be resolved using penalty kicks also based on probability system.
