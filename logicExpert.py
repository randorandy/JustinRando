from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places. 
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    Varia, GravitySuit, Wave, SpeedBooster, Spazer, Ice,
    Plasma, Screw, Charge, Grapple, SpaceJump, Energy, Reserve, Xray
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 1
)) 

energy300 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 14
))
hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun7 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))


missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 10
))
missile20 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 20
))

super4 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 4
))
super6 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 6
))
super12 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 12
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 30
))
powerBomb4 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb6 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
powerBomb8 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 4
))
powerBomb10 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 5
))
powerBomb12 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 6
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and #modified for yfaster
    (PowerBomb in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Super in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout)
))
canHighSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout) and
    (HiJump in loadout)
))
canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canSpeedOrFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout) or
    (SpeedBooster in loadout)
))

canHop = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (
        (Morph in loadout) and
        (Springball in loadout)
    )
))
grappleToCroc = LogicShortcut(lambda loadout: (
    (Missile in loadout) and
    (
        (Grapple in loadout) or
        (
            (GravitySuit in loadout) and
            (
                (Energy in loadout) or
                (Varia in loadout)
            )
        )
    )
))
upperNorfair = LogicShortcut(lambda loadout: (
    (Morph in loadout) or
    (grappleToCroc in loadout)
))
eastBrinstar = LogicShortcut(lambda loadout: (
    (Morph in loadout) or
    (grappleToCroc in loadout)
))
chozodia = LogicShortcut(lambda loadout: (
    (
        (upperNorfair in loadout) and
        (Morph in loadout)
    ) or
    (
        (SpeedBooster in loadout) and
        (canUseBombs in loadout)
    )
))
lnElevator = LogicShortcut(lambda loadout: (
    (upperNorfair in loadout) and
    (Morph in loadout) and
    (
        (SpeedBooster in loadout) or
        (Super in loadout)
    )
))
ln = LogicShortcut(lambda loadout: (
    (lnElevator in loadout) and
    (Super in loadout) and
    (Varia in loadout)
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


#Missile 22 in pool?
#Add PB73
#Add Missile 51
#Add missile 52


location_logic: LocationLogicType = {
    "Xray 1": lambda loadout: (
        True
    ),
    "Energy Tank 3": lambda loadout: (
        True
    ),
    "Missile 4": lambda loadout: (
        True
    ),
    "Missile 5": lambda loadout: (
        True
    ),
    "Missile 6": lambda loadout: (
        (Missile in loadout) #or backdoor
    ),
    "Missile 13": lambda loadout: (
        (grappleToCroc in loadout)
        #or backdoor
    ),
    "Wave Beam 14": lambda loadout: (
        (Morph in loadout) or
        (grappleToCroc in loadout)
    ),
    "Grapple Beam 8": lambda loadout: (
        (Missile in loadout)
    ),
    "Energy Tank 9": lambda loadout: (
        (Missile in loadout)
    ),
    "Missile 20": lambda loadout: (
        (upperNorfair in loadout) and
        (hellrun1 in loadout)
    ),
    "Missile 21": lambda loadout: (
        (upperNorfair in loadout) and
        (hellrun3 in loadout)
    ),
    "Energy Tank 15": lambda loadout: (
        (Super in loadout) and
        (upperNorfair in loadout)
    ),
    "Missile 17": lambda loadout: (
        (Morph in loadout) or
        (grappleToCroc in loadout)
    ),
    "Missile 67": lambda loadout: (
        (upperNorfair in loadout) and
        (Super in loadout) and #I think
        (hellrun5 in loadout) #todo test hellrun
    ),
    "Super Missile 68": lambda loadout: (
        (upperNorfair in loadout) and
        (Super in loadout) and #I think
        (hellrun5 in loadout) and #todo test hellrun
        (canBreakBlocks in loadout) and
        (Morph in loadout)
    ),
    "Missile 23": lambda loadout: (
        (upperNorfair in loadout) and
        (
            (HiJump in loadout) or
            (canSpeedOrFly in loadout)
        )
    ),
    "Missile 24": lambda loadout: (
        (upperNorfair in loadout)
    ),
    "Missile 25": lambda loadout: (
        (eastBrinstar in loadout)
    ),
    "Energy Tank 30": lambda loadout: (
        (eastBrinstar in loadout)
    ),
    "Morph Ball 31": lambda loadout: (
        (eastBrinstar in loadout)
    ),
    "Ice Beam 28": lambda loadout: (
        (eastBrinstar in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Missile 2": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Missile 66": lambda loadout: (
        (upperNorfair in loadout) 
    ),
    "Gravity Suit 33": lambda loadout: (
        (Morph in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
        )
    ),
    "Missile 254": lambda loadout: (
        (Morph in loadout) 
    ),
    "Missile 71": lambda loadout: (
        (chozodia in loadout) #includes morph
    ),
    "Missile 35": lambda loadout: (
        (Morph in loadout)
    ),
    "Missile 26": lambda loadout: (
        (eastBrinstar in loadout) and
        (Morph in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Missile 12": lambda loadout: (
        (Missile in loadout) and
        (Morph in loadout)
    ),
    "Missile 29": lambda loadout: (
        (eastBrinstar in loadout)
    ),
    "HiJump 19": lambda loadout: (
        (upperNorfair in loadout)
    ),
    "Energy Tank 34": lambda loadout: (
        (Morph in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
        )
    ),
    "Super Missile 38": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Missile 37": lambda loadout: (
        (Morph in loadout)
    ),
    "Charge Beam 255": lambda loadout: (
        (Morph in loadout)
    ),
    "Missile 32": lambda loadout: (
        (canUseBombs in loadout) and
        (Missile in loadout) # todo is it a missile door?
    ),
    "Super Missile 253": lambda loadout: (
        (lnElevator in loadout)
    ),
    "Power Bomb 0": lambda loadout: (
        (SpeedBooster in loadout) and
        (energy300 in loadout) #todo confirm
    ),
    "Energy Tank 10": lambda loadout: (
        (Missile in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile 41": lambda loadout: (
        (Missile in loadout) and
        (canUseBombs in loadout)
    ),
    "Missile 40": lambda loadout: (
        (Missile in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout)
    ),
    "Springball 42": lambda loadout: (
        (Missile in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (Springball in loadout)
    ),
    "Speed Booster 43": lambda loadout: (
        (Missile in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (
            (Springball in loadout) or
            (canUseBombs in loadout)
        )
    ),
    "Missile 77": lambda loadout: (
        (SpeedBooster in loadout) and
        (SpaceJump in loadout) and
        (Super in loadout) and
        (Missile in loadout) and
        (canUsePB in loadout)
    ),
    "Energy Tank 44": lambda loadout: (
        (Missile in loadout) and
        (Morph in loadout) and
        (GravitySuit in loadout) and
        (
            (Springball in loadout) or
            (canUseBombs in loadout) 
        )
    ),
    "Missile 69": lambda loadout: (
        (upperNorfair in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Varia Suit 70": lambda loadout: (
        (upperNorfair in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "Super Missile 74": lambda loadout: (
        (upperNorfair in loadout) and
        (Super in loadout) and
        (Morph in loadout) and
        (Varia in loadout)
    ),
    "Missile 16": lambda loadout: (
        (upperNorfair in loadout) and
        (Morph in loadout) and
        (Super in loadout) #todo I think, but this feels wrong
    ),
    "Energy Tank 46": lambda loadout: (
        (ln in loadout)
    ),
    "Missile 47": lambda loadout: (
        (ln in loadout)
    ),
    "Missile 50": lambda loadout: (
        (ln in loadout)
    ),
    "Missile 49": lambda loadout: (
        (ln in loadout) and
        (GravitySuit in loadout) and
        (canIBJ in loadout)
    ),
    "Missile 48": lambda loadout: (
        (ln in loadout) and
        (GravitySuit in loadout) and
        (canIBJ in loadout) and
        (super6 in loadout)
    ),
    "Missile 54": lambda loadout: (
        (ln in loadout) and
        (canUseBombs in loadout)
    ),
    "Missile 55": lambda loadout: (
        (ln in loadout) and
        (canUseBombs in loadout)
    ),
    "Missile 57": lambda loadout: (
        (ln in loadout)
    ),
    "Super Missile 60": lambda loadout: (
        (ln in loadout)
    ),
    "Energy Tank 53": lambda loadout: (
        (ln in loadout) and
        (canUseBombs in loadout)
    ),
    "Energy Tank 59": lambda loadout: (
        (ln in loadout) and
        (energy400 in loadout) and
        (Charge in loadout)
    ),
    "Space Jump 58": lambda loadout: (
        (ln in loadout) and
        (energy400 in loadout) and
        (Charge in loadout)
    ),
    "Missile 61": lambda loadout: (
        (ln in loadout)
    ),
    "Missile 62": lambda loadout: (
        (ln in loadout) and
        (GravitySuit in loadout)
    ),
    "Missile 63": lambda loadout: (
        (ln in loadout) and
        (GravitySuit in loadout) and
        (canUseBombs in loadout) #todo confirm
    ),
    "Missile 45": lambda loadout: (
        (ln in loadout)
    ),
    "Missile 72": lambda loadout: (
        (upperNorfair in loadout) and
        (super4 in loadout) and
        (Varia in loadout) and
        (GravitySuit in loadout) and
        (canUseBombs in loadout)
    ),
    "Bombs 81": lambda loadout: (
        (chozodia in loadout) and
        (Charge in loadout) and
        (canUseBombs in loadout)
    ),
    "Missile 79": lambda loadout: (
        (chozodia in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout)
    ),
    "Missile 78": lambda loadout: (
        (chozodia in loadout) and
        (canUseBombs in loadout)
    ),
    "Super Missile 80": lambda loadout: (
        (chozodia in loadout) and
        (SpaceJump in loadout) and
        (HiJump in loadout) and
        (SpeedBooster in loadout)
    ),
    "Spazer 64": lambda loadout: (
        (upperNorfair in loadout) and
        (Super in loadout)
    ),
    "Plasma Beam 84": lambda loadout: (
        (chozodia in loadout) and
        (canUsePB in loadout)
    ),
    "Missile 83": lambda loadout: (
        (Missile in loadout) and
        (canUseBombs in loadout)
    ),
    "Missile 11": lambda loadout: (
        (Missile in loadout) and
        (GravitySuit in loadout) and #todo I think it's underwater
        (SpeedBooster in loadout) and
        (Morph in loadout)
    ),
    "Power Bomb 76": lambda loadout: (
        (SpeedBooster in loadout) and
        (Super in loadout) and
        (Missile in loadout) and
        (canUsePB in loadout)
    ),
    "Missile 27": lambda loadout: (
        (eastBrinstar in loadout)
    ),
    "Missile 82": lambda loadout: (
        (Missile in loadout) and
        (canUsePB in loadout)
    ),
    "Super Missile 56": lambda loadout: (
        (ln in loadout) and
        (canUseBombs in loadout)
    ),
    "Missile 52": lambda loadout: (
        (ln in loadout) and
        (SpeedBooster in loadout) and
        (canUseBombs in loadout)
    ),
    "Missile 51": lambda loadout: (
        (ln in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout)
    ),
    "Missile 22": lambda loadout: (
        (upperNorfair in loadout) and
        (hellrun1 in loadout) #todo confirm hellrun
    ),
    "Missile 7": lambda loadout: (
        (Morph in loadout) and
        (Missile in loadout) #or backdoor brin elevator
    ),
    "Power Bomb 73": lambda loadout: (
        (upperNorfair in loadout) and
        (super4 in loadout) and
        (Varia in loadout) and
        (GravitySuit in loadout) and
        (Morph in loadout)
    ),
    "Missile 75": lambda loadout: (
        (upperNorfair in loadout) and
        (Super in loadout) and
        (Morph in loadout) and
        (Varia in loadout)
        #same as super 74
    ),
    "Missile 39": lambda loadout: (
        (Morph in loadout)
    ),



}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
