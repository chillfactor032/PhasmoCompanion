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

map_data = {
    Map.TANGLEWOOD: """<b>Haunted Mirror:</b><br>
        The Haunted Mirror spawns on the wall next to the Master Bedroom door in the Living Room.
        <p>
        <b>Music Box:</b><br>
        The Music Box spawns on the shelf in the Nursery.
        <p>
        <b>Ouija Board:</b><br>
        The Ouija Board spawns on the coffee table at the far end of the Basement.
        <p>
        <b>Summoning Circle:</b><br>
        The Summoning Circle spawns near the stairs of the Basement.
        <p>
        <b>Tarot Cards:</b><br>
        The Tarot Cards spawn on the end table by the window in the Living Room.
        <p>
        <b>Voodoo Doll:</b><br>
        The Voodoo Doll spawns on the trash can in the Garage.
        """,
    Map.BLEASDALE: """<b>Ouija Board:</b><br>
        The Ouija Board spawns on the workbench in the Garage.
        <p>
        <b>Voodoo Doll:</b><br>
        The Voodoo Doll spawns on the couch in the Upstairs Hallway.
        <p>
        <b>Haunted Mirror:</b><br>
        The Haunted Mirror spawns on the wall in the Office.
        <p>
        <b>Summoning Circle:</b><br>
        The Summoning Circle spawns in the Attic.
        <p>
        <b>Tarot Cards:</b><br>
        The Tarot Cards spawn on the table in the Office.
        <p>
        <b>Music Box:</b><br>
        The Music Box spawns on the table with a lamp in the Living Room.
        """,
    Map.GRAFTON: """<b>Summoning Circle:</b><br>
        The Summoning Circle spawns in the Storage.
        <p>
        <b>Ouija Board:</b><br>
        The Ouija Board spawns in the Master Bedroom's closet.
        <p>
        <b>Music Box:</b><br>
        The Music Box spawns in the Foyer on one of the shelves.
        <p>
        <b>Haunted Mirror:</b><br>
        The Haunted Mirror spawns in the Living Room next to the Kitchen door.
        <p>
        <b>Tarot Cards:</b><br>
        The Tarot Cards spawn in the Dining Room on the dining table.
        <p>
        <b>Voodoo Doll:</b><br>
        The Voodoo Doll spawns in the Nursery on the chest.
        """,
    Map.RIDGEVIEW: """<b>Haunted Mirror:</b><br>
        The Haunted Mirror spawns above the lamp near the stairs in the Hallway.
        <p>
        <b>Music Box:</b><br>
        The Music Box spawns on the table in Girls Bedroom.
        <p>
        <b>Ouija Board:</b><br>
        The Ouija Board spawns on the shelf in the Utility.
        <p>
        <b>Summoning Circle:</b><br>
        The Summoning Circle spawns in front of the stairs in the Basement.
        <p>
        <b>Tarot Cards:</b><br>
        The Tarot Cards spawn on the table next to the entrance in the Foyer.
        <p>
        <b>Voodoo Doll:</b><br>
        The Voodoo Doll spawns on the bench in the Hallway.
        """,
    Map.EDGEFIELD: """<b>Haunted Mirror:</b><br>
        The Haunted Mirror spawns in front of the stairs leading up to the second floor in the Hallway.
        <p>
        <b>Music Box:</b><br>
        The Music Box spawns on the table with a lamp in the Living Room.
        <p>
        <b>Ouija Board:</b><br>
        The Ouija Board spawns under a metal rack in the Utility.
        <p>
        <b>Summoning Circle:</b><br>
        The Summoning Circle spawns in the segemented room of the Basement.
        <p>
        <b>Tarot Cards:</b><br>
        The Tarot Cards spawn on the table at the front of the Foyer.
        <p>
        <b>Voodoo Doll:</b><br>
        The Voodoo Doll spawns on the bed in the Large Blue Bedroom.
        """,
    Map.WILLOW: """<b>Ouija Board:</b><br>
        The Ouija Board spawns on top of the washing machines in the Garage.
        <p>
        <b>Tarot Cards:</b><br>
        The Tarot Cards spawn on the end table next to the couch in the Living Room.
        <p>
        <b>Voodoo Doll:</b><br>
        The Voodoo Doll spawns in the cabinet in the Boys Bedroom.
        <p>
        <b>Music Box:</b><br>
        The Music Box spawns on the table beside the entrance in the Living Room.
        <p>
        <b>Summoning Circle:</b><br>
        The Summoning Circle spawns in the Basement Hallway.
        <p>
        <b>Haunted Mirror:</b><br>
        The Haunted Mirror spawns in the corner beside the metal rack in the Garage.
        """,
    Map.BROWNSTONE: "All cursed possessions spawn in the Lobby or in the immediate vicinity in the hallway.",
    Map.MAPLELODGE: """<b>Ouija Board:</b><br>
        The Ouija Board spawns on the shelf in the Cleaning Closet.
        <p>
        <b>Haunted Mirror:</b><br>
        The Haunted Mirror spawns in the Blue Tent.
        <p>
        <b>Music Box:</b><br>
        The Music Box spawns outside the cabin on a metal table at the porch.
        <p>
        <b>Voodoo Doll:</b><br>
        The Voodoo Doll spawns at the Campfire beside a wine bottle.
        <p>
        <b>Tarot Cards:</b><br>
        The Tarot Cards spawn to the left side of the White Tent on a table.
        <p>
        <b>Summoning Circle:</b><br>
        The Summoning Circle spawns in the Cabin Kitchen.
        """,
    Map.PRISON: "All cursed possessions will spawn in the entrance hallway.",
    Map.ASYLUM: "All cursed possessions will spawn in the Reception."
}

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
        "hunt_threshold": "?",
        "data": {
            "strength": "Upon entering the location, it will become active, defensive, and agile",
            "weakness": "Weaken over time, making them weaker slower and less agressive.",
            "notes": ""
        }
    }
]

table_html = """
<html><head>
<style>
#styled-table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#styled-table td, #styled-table th {
  border: 1px solid #ddd;
  padding: 8px;
}

#styled-table tr:nth-child(even){background-color: #f2f2f2;}

#styled-table tr:hover {background-color: #ddd;}

#styled-table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  color: white;
}
</style></head>
<body>
NOTES
<table id="styled-table">
<tr>
    <th>Ghost</th>
    <th>Info</th>
</tr>
TABLECONTENTS
</table>
</body>
</html>
"""

class Ghost():
    name = ""
    evidence = []
    strength = ""
    weakness = ""

    def __init__(self, name, evidence, data):
        self.name = name
        self.evidence = evidence
        self.strength = data["strength"]
        self.weakness = data["weakness"]
        self.notes = data["notes"]

    def __str__(self):
        return self.name

    def is_possible(self, current_evidence):
        for ev in current_evidence:
            if(ev == Evidence.NOEVIDENCE):
                continue
            if(ev not in self.evidence):
                return False
        return True

    def get_remaining_evidence(self, evidence):
        tempEvidence = self.evidence.copy()
        for ev in self.evidence:
            if(ev in evidence):
                tempEvidence.remove(ev)
        return tempEvidence

    def get_name_with_evidence(self, current_evidence):
        remaining_evidence = self.get_remaining_evidence(current_evidence)
        if(len(remaining_evidence) == 0 or len(remaining_evidence) > 2):
            return self.name
        ev_list = []
        for ev in remaining_evidence:
            ev_list.append(str(ev))
        evidence_string = "(" + ",".join(ev_list) + ")"
        return self.name + " " + evidence_string


class Phasmo():
    ghosts = []
    possible_ghosts = []
    current_evidence = []
    mimic = None

    #    Initialize the list of ghosts in Phasmophobia
    #    ghosts_data contains ghost names and corresponding evidence
    #
    def __init__(self, ghosts_data):
        for ghost in ghosts_data:
            ghost_obj = Ghost(ghost["name"], ghost["evidence"], ghost["data"])
            self.ghosts.append(ghost_obj)
            if(ghost_obj.name == "The Mimic"):
                self.mimic = ghost_obj
        self.current_evidence = []

    #   Update a list of possible ghosts given the current provided evidence
    #
    def update_possible_ghosts(self):
        self.possible_ghosts.clear()
        for ghost in self.ghosts:
            if(ghost.is_possible(self.current_evidence)):
                self.possible_ghosts.append(ghost)

    def update_current_evidence(self, evidence):
        self.current_evidence = evidence
        self.update_possible_ghosts()

    def get_evidence_notes(self):
        notes = ""
        evidence_list = list(Evidence)
        possible_evidence = []
        eliminated_evidence = []
        for ghost in self.possible_ghosts:
            remaining_ev = ghost.get_remaining_evidence(self.current_evidence)
            for re in remaining_ev:
                if(re not in possible_evidence):
                    possible_evidence.append(re)
        for ev in evidence_list:
            if(ev not in possible_evidence and ev not in self.current_evidence):
                eliminated_evidence.append(str(ev))
        if(len(eliminated_evidence) > 0):
            notes += "<b>Eliminated Evidence:</b><br>"
            notes += ",".join(eliminated_evidence) + "<p>"
        return notes

    # Determin if The Mimic is possible due to a fake ghost orb
    #
    def mimic_possible(self):
        if(Evidence.GHOSTORB in self.current_evidence and
                len(self.current_evidence) > 1):
            temp_evidence = self.current_evidence.copy()
            temp_evidence.remove(Evidence.GHOSTORB)
            return self.mimic.is_possible(temp_evidence)

    # Get the remaining evidence to rule out if The Mimic is possible
    #
    def mimic_get_evidence(self):
        if(self.mimic_possible()):
            temp_evidence = self.current_evidence.copy()
            temp_evidence.remove(Evidence.GHOSTORB)
            return self.mimic.get_remaining_evidence(temp_evidence)
        else:
            return []
