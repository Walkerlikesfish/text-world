
import random
from evennia import TICKER_HANDLER
from evennia import CmdSet, Command, DefaultRoom
from evennia import utils, create_object, search_object
from evennia import syscmdkeys, default_cmds
from evennia.contrib.text_sims.objects import LightSource, TutorialObject

# the system error-handling module is defined in the settings. We load the
# given setting here using utils.object_from_module. This way we can use
# it regardless of if we change settings later.
from django.conf import settings
_SEARCH_AT_RESULT = utils.object_from_module(settings.SEARCH_AT_RESULT)




# for the @detail command we inherit from MuxCommand, since
# we want to make use of MuxCommand's pre-parsing of '=' in the
# argument.
class CmdTutorialSetDetail(default_cmds.MuxCommand):
    """
    sets a detail on a room

    Usage:
        @detail <key> = <description>
        @detail <key>;<alias>;... = description

    Example:
        @detail walls = The walls are covered in ...
        @detail castle;ruin;tower = The distant ruin ...

    This sets a "detail" on the object this command is defined on
    (TutorialRoom for this tutorial). This detail can be accessed with
    the TutorialRoomLook command sitting on TutorialRoom objects (details
    are set as a simple dictionary on the room). This is a Builder command.

    We custom parse the key for the ;-separator in order to create
    multiple aliases to the detail all at once.
    """
    key = "@detail"
    locks = "cmd:perm(Builders)"
    help_category = "TutorialWorld"

    def func(self):
        """
        All this does is to check if the object has
        the set_detail method and uses it.
        """
        if not self.args or not self.rhs:
            self.caller.msg("Usage: @detail key = description")
            return
        if not hasattr(self.obj, "set_detail"):
            self.caller.msg("Details cannot be set on %s." % self.obj)
            return
        for key in self.lhs.split(";"):
            # loop over all aliases, if any (if not, this will just be
            # the one key to loop over)
            self.obj.set_detail(key, self.rhs)
        self.caller.msg("Detail set: '%s': '%s'" % (self.lhs, self.rhs))





class TutorialRoomCmdSet(CmdSet):
    """
    Implements the simple tutorial cmdset. This will overload the look
    command in the default CharacterCmdSet since it has a higher
    priority (ChracterCmdSet has prio 0)
    """
    key = "tutorial_cmdset"
    priority = 1

    def at_cmdset_creation(self):
        "add the tutorial-room commands"
        self.add(CmdTutorialSetDetail())



##### All rooms are derived from this ######
class TutorialRoom(DefaultRoom):

    def at_object_creation(self):
        "Called when room is first created"
        self.db.desc = "Hello from the Baseroom."
        self.cmdset.add_default(TutorialRoomCmdSet)

    def at_object_receive(self, new_arrival, source_location):
        """
        When an object enter a tutorial room we tell other objects in
        the room about it by trying to call a hook on them. The Mob object
        uses this to cheaply get notified of enemies without having
        to constantly scan for them.

        Args:
            new_arrival (Object): the object that just entered this room.
            source_location (Object): the previous location of new_arrival.

        """
        if new_arrival.has_player and not new_arrival.is_superuser:
            # this is a character
            for obj in self.contents_get(exclude=new_arrival):
                if hasattr(obj, "at_new_arrival"):
                    obj.at_new_arrival(new_arrival)

    def return_detail(self, detailkey):
        """
        This looks for an Attribute "obj_details" and possibly
        returns the value of it.

        Args:
            detailkey (str): The detail being looked at. This is
                case-insensitive.

        """
        details = self.db.details
        if details:
            return details.get(detailkey.lower(), None)

    def set_detail(self, detailkey, description):
        """
        This sets a new detail, using an Attribute "details".

        Args:
            detailkey (str): The detail identifier to add (for
                aliases you need to add multiple keys to the
                same description). Case-insensitive.
            description (str): The text to return when looking
                at the given detailkey.

        """
        print 'in set detail'
        if self.db.details:
            # to keep the descriptions of the room separate from object details
            if detailkey.startswith('desc'):
                if 'desc' not in self.db.details:
                    self.db.details['desc'] = {}
                self.db.details['desc'][detailkey] = description
            else:
                self.db.details[detailkey.lower()] = description
        else:
            self.db.details = {detailkey.lower(): description}

    def return_appearance(self, looker):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
        """
        if not looker:
            return
        # # get and identify all objects
        # visible = (con for con in self.contents if con != looker and
        #                                             con.access(looker, "view"))
        # exits, users, things = [], [], []
        # for con in visible:
        #     key = con.key
        #     if con.destination:
        #         exits.append(key)
        #     elif con.has_player:
        #         users.append("{c%s{n" % key)
        #     else:
        #         things.append(key)

        # get description, build string
        string = "{c%s{n\n" % self.key
        if self.db.details:
            randIndex = random.randint(0, len(self.db.details['desc'])-1)
            desc = self.db.details['desc'].values()[randIndex]
        else:
            desc = self.db.desc
        return desc