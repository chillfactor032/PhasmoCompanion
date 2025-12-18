import re
from enum import Enum

class Map(Enum):
    TANGLEWOOD = 0
    BLEASDALE = 1
    GRAFTON = 2
    RIDGEVIEW = 3
    EDGEFIELD = 4
    WILLOW = 5
    BROWNSTONE = 6
    MAPLELODGE = 7
    PRISON = 8
    ASYLUM = 9
    
    def __str__(self):
        if(self == Map.TANGLEWOOD):
            return "Tanglewood Street House"
        elif(self == Map.BLEASDALE):
            return "Bleasdale Farmhouse"
        elif(self == Map.GRAFTON):
            return "Grafton Farmhouse"
        elif(self == Map.RIDGEVIEW):
            return "Ridgeview Road House"
        elif(self == Map.EDGEFIELD):
            return "Edgefield Street House"
        elif(self == Map.WILLOW):
            return "Willow Street House"
        elif(self == Map.BROWNSTONE):
            return "Brownstone High School"
        elif(self == Map.MAPLELODGE):
            return "Maple Lodge Campsite"
        elif(self == Map.PRISON):
            return "Prison"
        elif(self == Map.ASYLUM):
            return "Asylum"
        return "No Map Selected"
        
# Enum Class for Evidence Types
class Evidence(Enum):
    NOEVIDENCE = 0
    EMF5 = 1
    SPIRITBOX = 2
    FINGERPRINTS = 3
    GHOSTORB = 4
    GHOSTWRITING = 5
    FREEZINGTEMPS = 6
    DOTS = 7

    def __str__(self):
        if(self == Evidence.EMF5):
            return "EMF5"
        elif(self == Evidence.SPIRITBOX):
            return "Spirit Box"
        elif(self == Evidence.FINGERPRINTS):
            return "Ultraviolet"
        elif(self == Evidence.GHOSTORB):
            return "Orb"
        elif(self == Evidence.GHOSTWRITING):
            return "Writing"
        elif(self == Evidence.FREEZINGTEMPS):
            return "Freezing"
        elif(self == Evidence.DOTS):
            return "DOTS"
        return "No Evidence"

ghosts_data = [
    {
        "name": "Spirit",
        "evidence": [
            Evidence.EMF5,
            Evidence.SPIRITBOX,
            Evidence.GHOSTWRITING
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "None.",
            "weakness": "Smudge sticks are more effective, preventing a hunt"
                        " for longer. ",
            "notes": ""
        }
    },
    {
        "name": "Wraith",
        "evidence": [
            Evidence.EMF5,
            Evidence.SPIRITBOX,
            Evidence.DOTS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Does not leave UV footprints after stepping in salt.",
            "weakness": "Will become more active if it steps in salt. ",
            "notes": ""
        }
    },
    {
        "name": "Phantom",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.FINGERPRINTS,
            Evidence.DOTS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Looking at a Phantom will lower the player's"
                        " sanity considerably.",
            "weakness": "Taking a photo of the Phantom will cause it to"
                        " briefly disappear. ",
            "notes": ""
        }
    },
    {
        "name": "Poltergeist",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.FINGERPRINTS,
            Evidence.GHOSTWRITING
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Capable of throwing multiple objects at once.",
            "weakness": "Becomes powerless with no throwables nearby.",
            "notes": ""
        }
    },
    {
        "name": "Banshee",
        "evidence": [
            Evidence.FINGERPRINTS,
            Evidence.GHOSTORB,
            Evidence.DOTS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Will target only one player at a time.",
            "weakness": "Crucifix effectiveness is increased to 5m against"
                        " one.",
            "notes": ""
        }
    },
    {
        "name": "Jinn",
        "evidence": [
            Evidence.EMF5,
            Evidence.FINGERPRINTS,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Travels at faster speeds if its victim is far away. ",
            "weakness": "Cannot use its ability if the site's fuse box is off.",
            "notes": ""
        }
    },
    {
        "name": "Mare",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.GHOSTORB,
            Evidence.GHOSTWRITING
        ],
        "hunt_threshold": "60",
        "data": {
            "strength": "Has an increased chance to attack in the dark. ",
            "weakness": "Turning the lights on will reduce the chance of an"
                        " attack. ",
            "notes": ""
        }
    },
    {
        "name": "Revenant",
        "evidence": [
            Evidence.GHOSTORB,
            Evidence.GHOSTWRITING,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Can travel significantly faster if a player is"
                        " spotted during a hunt.",
            "weakness": "Moves very slowly when not chasing a player. ",
            "notes": ""
        }
    },
    {
        "name": "Shade",
        "evidence": [
            Evidence.EMF5,
            Evidence.GHOSTWRITING,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "35",
        "data": {
            "strength": "Being shy makes it more difficult to locate and"
                        " obtain evidence.",
            "weakness": "Less likely to hunt if multiple people are nearby. ",
            "notes": ""
        }
    },
    {
        "name": "Demon",
        "evidence": [
            Evidence.FINGERPRINTS,
            Evidence.GHOSTWRITING,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "70",
        "data": {
            "strength": "Can initiate hunts more often. ",
            "weakness": "Using cursed possessions will lower sanity less. ",
            "notes": ""
        }
    },
    {
        "name": "Yurei",
        "evidence": [
            Evidence.GHOSTORB,
            Evidence.FREEZINGTEMPS,
            Evidence.DOTS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Has a stronger effect on sanity. ",
            "weakness": "Smudging the Yurei's ghost room will reduce how often"
                        " it wanders.",
            "notes": ""
        }
    },
    {
        "name": "Oni",
        "evidence": [
            Evidence.EMF5,
            Evidence.FREEZINGTEMPS,
            Evidence.DOTS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Increased activity and ghost events. ",
            "weakness": "An Oni's increased activity makes them"
                        "easier to find.",
            "notes": ""
        }
    },
    {
        "name": "Hantu",
        "evidence": [
            Evidence.FINGERPRINTS,
            Evidence.GHOSTORB,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Lower temperatures allow the Hantu to move faster. ",
            "weakness": "Warmer areas slow the Hantu's movement. ",
            "notes": ""
        }
    },
    {
        "name": "Yokai",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.GHOSTORB,
            Evidence.DOTS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Talking near the Yokai will anger it, increasing the"
                        " chance to attack. ",
            "weakness": "Can only hear voices close to it during a hunt. ",
            "notes": ""
        }
    },
    {
        "name": "Goryo",
        "evidence": [
            Evidence.EMF5,
            Evidence.FINGERPRINTS,
            Evidence.DOTS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Can only be seen interacting with D.O.T.S. through"
                        " a camera when nobody is nearby.",
            "weakness": "Tends to wander away less from its ghost room. ",
            "notes": ""
        }
    },
    {
        "name": "Myling",
        "evidence": [
            Evidence.EMF5,
            Evidence.FINGERPRINTS,
            Evidence.GHOSTWRITING
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Has quieter footsteps during a hunt.",
            "weakness": "Produces paranormal sounds more frequently.",
            "notes": ""
        }
    },
    {
        "name": "Onryo",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.GHOSTORB,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "60",
        "data": {
            "strength": "A flame extinguishing can cause an Onryo to attack.",
            "weakness": "The presence of flames reduces the Onryo's ability"
                        " to attack.",
            "notes": ""
        }
    },
    {
        "name": "The Twins",
        "evidence": [
            Evidence.EMF5,
            Evidence.SPIRITBOX,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Either Twin may start a hunt, though not at the same"
                        " time.",
            "weakness": "Will often interact with the environment at the same"
                        " time.",
            "notes": ""
        }
    },
    {
        "name": "Raiju",
        "evidence": [
            Evidence.EMF5,
            Evidence.GHOSTORB,
            Evidence.DOTS
        ],
        "hunt_threshold": "65",
        "data": {
            "strength": "Moves faster near electrical devices. ",
            "weakness": "Disrupts electronic equipment from further away when"
                        " it hunts.",
            "notes": ""
        }
    },
    {
        "name": "Obake",
        "evidence": [
            Evidence.EMF5,
            Evidence.FINGERPRINTS,
            Evidence.GHOSTORB
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "May leave fingerprints that disappear quicker. ",
            "weakness": "Has a small chance of leaving six-fingered"
                        " handprints.",
            "notes": ""
        }
    },
    {
        "name": "The Mimic",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.FINGERPRINTS,
            Evidence.FREEZINGTEMPS,
            Evidence.GHOSTORB
        ],
        "hunt_threshold": "?",
        "data": {
            "strength": "Can mimic the abilities and traits of other ghosts.",
            "weakness": "Will present Ghost Orbs as a secondary evidence.",
            "notes": ""
        }
    },
    {
        "name": "Moroi",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.GHOSTWRITING,
            Evidence.FREEZINGTEMPS
        ],
        "hunt_threshold": "50",
        "data": {
            "strength": "Weaker the victim the stronger it becomes.",
            "weakness": "Suffer from hyperosmia, weakening them for longer periods.",
            "notes": ""
        }
    },
    {
        "name": "Deogen",
        "evidence": [
            Evidence.SPIRITBOX,
            Evidence.GHOSTWRITING,
            Evidence.DOTS
        ],
        "hunt_threshold": "40",
        "data": {
            "strength": "Senses the living, run but cant hide",
            "weakness": "Require alot of energy to form, making them slow",
            "notes": ""
        }
    },
    {
        "name": "Thaye",
        "evidence": [
            Evidence.GHOSTORB,
            Evidence.GHOSTWRITING,
            Evidence.DOTS
        ],
        "hunt_threshold": "75",
        "data": {
            "strength": "Upon entering the location, it will become active, defensive, and agile",
            "weakness": "Weaken over time, making them weaker slower and less agressive.",
            "notes": ""
        }
    },
    {
        "name": "Dayan",
        "evidence": [
            Evidence.EMF5,
            Evidence.GHOSTORB,
            Evidence.SPIRITBOX
        ],
        "hunt_threshold": "65",
        "data": {
            "strength": "Upon entering the location, it will become active, defensive, and agile",
            "weakness": "Weaken over time, making them weaker slower and less agressive.",
            "notes": ""
        }
    },
    {
        "name": "Gallu",
        "evidence": [
            Evidence.EMF5,
            Evidence.FINGERPRINTS,
            Evidence.SPIRITBOX
        ],
        "hunt_threshold": "60",
        "data": {
            "strength": "Upon entering the location, it will become active, defensive, and agile",
            "weakness": "Weaken over time, making them weaker slower and less agressive.",
            "notes": ""
        }
    },
    {
        "name": "Obambo",
        "evidence": [
            Evidence.GHOSTWRITING,
            Evidence.FINGERPRINTS,
            Evidence.DOTS
        ],
        "hunt_threshold": "65",
        "data": {
            "strength": "Upon entering the location, it will become active, defensive, and agile",
            "weakness": "Weaken over time, making them weaker slower and less agressive.",
            "notes": ""
        }
    }
]
