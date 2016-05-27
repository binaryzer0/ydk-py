""" Cisco_IOS_XR_infra_objmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-objmgr package configuration.

This module contains definitions
for the following management objects\:
  object\-group\: Object\-group configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EndPortEnum(Enum):
    """
    EndPortEnum

    End port

    .. data:: ECHO = 7

    	Echo (7)

    .. data:: DISCARD = 9

    	Discard (9)

    .. data:: DAYTIME = 13

    	Daytime (13)

    .. data:: CHARGEN = 19

    	Character generator (19)

    .. data:: FTP_DATA = 20

    	FTP data connections (used infrequently, 20)

    .. data:: FTP = 21

    	File Transfer Protocol (21)

    .. data:: SSH = 22

    	Secure Shell (22)

    .. data:: TELNET = 23

    	Telnet (23)

    .. data:: SMTP = 25

    	Simple Mail Transport Protocol (25)

    .. data:: TIME = 37

    	Time (37)

    .. data:: NICNAME = 43

    	Nicname (43)

    .. data:: TACACS = 49

    	TAC Access Control System (49)

    .. data:: DOMAIN = 53

    	Domain Name Service (53)

    .. data:: GOPHER = 70

    	Gopher (70)

    .. data:: FINGER = 79

    	Finger (79)

    .. data:: WWW = 80

    	World Wide Web (HTTP, 80)

    .. data:: HOST_NAME = 101

    	NIC hostname server (101)

    .. data:: POP2 = 109

    	Post Office Protocol v2 (109)

    .. data:: POP3 = 110

    	Post Office Protocol v3 (110)

    .. data:: SUN_RPC = 111

    	Sun Remote Procedure Call (111)

    .. data:: IDENT = 113

    	Ident Protocol (113)

    .. data:: NNTP = 119

    	Network News Transport Protocol (119)

    .. data:: BGP = 179

    	Border Gateway Protocol (179)

    .. data:: IRC = 194

    	Internet Relay Chat (194)

    .. data:: PIM_AUTO_RP = 496

    	PIM Auto-RP (496)

    .. data:: EXEC = 512

    	Exec (rsh, 512)

    .. data:: LOGIN = 513

    	Login (rlogin, 513)

    .. data:: CMD = 514

    	Remote commands (rcmd, 514)

    .. data:: LPD = 515

    	Printer service (515)

    .. data:: UUCP = 540

    	Unix-to-Unix Copy Program (540)

    .. data:: KLOGIN = 543

    	Kerberos login (543)

    .. data:: KSHELL = 544

    	Kerberos shell (544)

    .. data:: TALK = 517

    	Talk (517)

    .. data:: LDP = 646

    	LDP session connection attempts (MPLS, 646)

    """

    ECHO = 7

    DISCARD = 9

    DAYTIME = 13

    CHARGEN = 19

    FTP_DATA = 20

    FTP = 21

    SSH = 22

    TELNET = 23

    SMTP = 25

    TIME = 37

    NICNAME = 43

    TACACS = 49

    DOMAIN = 53

    GOPHER = 70

    FINGER = 79

    WWW = 80

    HOST_NAME = 101

    POP2 = 109

    POP3 = 110

    SUN_RPC = 111

    IDENT = 113

    NNTP = 119

    BGP = 179

    IRC = 194

    PIM_AUTO_RP = 496

    EXEC = 512

    LOGIN = 513

    CMD = 514

    LPD = 515

    UUCP = 540

    KLOGIN = 543

    KSHELL = 544

    TALK = 517

    LDP = 646


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
        return meta._meta_table['EndPortEnum']


class PortEnum(Enum):
    """
    PortEnum

    Port

    .. data:: ECHO = 7

    	Echo (7)

    .. data:: DISCARD = 9

    	Discard (9)

    .. data:: DAYTIME = 13

    	Daytime (13)

    .. data:: CHARGEN = 19

    	Character generator (19)

    .. data:: FTP_DATA = 20

    	FTP data connections (used infrequently, 20)

    .. data:: FTP = 21

    	File Transfer Protocol (21)

    .. data:: SSH = 22

    	Secure Shell (22)

    .. data:: TELNET = 23

    	Telnet (23)

    .. data:: SMTP = 25

    	Simple Mail Transport Protocol (25)

    .. data:: TIME = 37

    	Time (37)

    .. data:: NICNAME = 43

    	Nicname (43)

    .. data:: TACACS = 49

    	TAC Access Control System (49)

    .. data:: DOMAIN = 53

    	Domain Name Service (53)

    .. data:: GOPHER = 70

    	Gopher (70)

    .. data:: FINGER = 79

    	Finger (79)

    .. data:: WWW = 80

    	World Wide Web (HTTP, 80)

    .. data:: HOST_NAME = 101

    	NIC hostname server (101)

    .. data:: POP2 = 109

    	Post Office Protocol v2 (109)

    .. data:: POP3 = 110

    	Post Office Protocol v3 (110)

    .. data:: SUN_RPC = 111

    	Sun Remote Procedure Call (111)

    .. data:: IDENT = 113

    	Ident Protocol (113)

    .. data:: NNTP = 119

    	Network News Transport Protocol (119)

    .. data:: BGP = 179

    	Border Gateway Protocol (179)

    .. data:: IRC = 194

    	Internet Relay Chat (194)

    .. data:: PIM_AUTO_RP = 496

    	PIM Auto-RP (496)

    .. data:: EXEC = 512

    	Exec (rsh, 512)

    .. data:: LOGIN = 513

    	Login (rlogin, 513)

    .. data:: CMD = 514

    	Remote commands (rcmd, 514)

    .. data:: LPD = 515

    	Printer service (515)

    .. data:: UUCP = 540

    	Unix-to-Unix Copy Program (540)

    .. data:: KLOGIN = 543

    	Kerberos login (543)

    .. data:: KSHELL = 544

    	Kerberos shell (544)

    .. data:: TALK = 517

    	Talk (517)

    .. data:: LDP = 646

    	LDP session connection attempts (MPLS, 646)

    """

    ECHO = 7

    DISCARD = 9

    DAYTIME = 13

    CHARGEN = 19

    FTP_DATA = 20

    FTP = 21

    SSH = 22

    TELNET = 23

    SMTP = 25

    TIME = 37

    NICNAME = 43

    TACACS = 49

    DOMAIN = 53

    GOPHER = 70

    FINGER = 79

    WWW = 80

    HOST_NAME = 101

    POP2 = 109

    POP3 = 110

    SUN_RPC = 111

    IDENT = 113

    NNTP = 119

    BGP = 179

    IRC = 194

    PIM_AUTO_RP = 496

    EXEC = 512

    LOGIN = 513

    CMD = 514

    LPD = 515

    UUCP = 540

    KLOGIN = 543

    KSHELL = 544

    TALK = 517

    LDP = 646


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
        return meta._meta_table['PortEnum']


class PortOperatorEnum(Enum):
    """
    PortOperatorEnum

    Port operator

    .. data:: EQUAL = 0

    	Match packets on ports equal to entered port

    	number

    .. data:: NOT_EQUAL = 1

    	Match packets on ports not equal to entered

    	port number

    .. data:: GREATER_THAN = 2

    	Match packets on ports greater than entered

    	port number

    .. data:: LESS_THAN = 3

    	Match packets on ports less than entered port

    	number

    """

    EQUAL = 0

    NOT_EQUAL = 1

    GREATER_THAN = 2

    LESS_THAN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
        return meta._meta_table['PortOperatorEnum']


class StartPortEnum(Enum):
    """
    StartPortEnum

    Start port

    .. data:: ECHO = 7

    	Echo (7)

    .. data:: DISCARD = 9

    	Discard (9)

    .. data:: DAYTIME = 13

    	Daytime (13)

    .. data:: CHARGEN = 19

    	Character generator (19)

    .. data:: FTP_DATA = 20

    	FTP data connections (used infrequently, 20)

    .. data:: FTP = 21

    	File Transfer Protocol (21)

    .. data:: SSH = 22

    	Secure Shell (22)

    .. data:: TELNET = 23

    	Telnet (23)

    .. data:: SMTP = 25

    	Simple Mail Transport Protocol (25)

    .. data:: TIME = 37

    	Time (37)

    .. data:: NICNAME = 43

    	Nicname (43)

    .. data:: TACACS = 49

    	TAC Access Control System (49)

    .. data:: DOMAIN = 53

    	Domain Name Service (53)

    .. data:: GOPHER = 70

    	Gopher (70)

    .. data:: FINGER = 79

    	Finger (79)

    .. data:: WWW = 80

    	World Wide Web (HTTP, 80)

    .. data:: HOST_NAME = 101

    	NIC hostname server (101)

    .. data:: POP2 = 109

    	Post Office Protocol v2 (109)

    .. data:: POP3 = 110

    	Post Office Protocol v3 (110)

    .. data:: SUN_RPC = 111

    	Sun Remote Procedure Call (111)

    .. data:: IDENT = 113

    	Ident Protocol (113)

    .. data:: NNTP = 119

    	Network News Transport Protocol (119)

    .. data:: BGP = 179

    	Border Gateway Protocol (179)

    .. data:: IRC = 194

    	Internet Relay Chat (194)

    .. data:: PIM_AUTO_RP = 496

    	PIM Auto-RP (496)

    .. data:: EXEC = 512

    	Exec (rsh, 512)

    .. data:: LOGIN = 513

    	Login (rlogin, 513)

    .. data:: CMD = 514

    	Remote commands (rcmd, 514)

    .. data:: LPD = 515

    	Printer service (515)

    .. data:: UUCP = 540

    	Unix-to-Unix Copy Program (540)

    .. data:: KLOGIN = 543

    	Kerberos login (543)

    .. data:: KSHELL = 544

    	Kerberos shell (544)

    .. data:: TALK = 517

    	Talk (517)

    .. data:: LDP = 646

    	LDP session connection attempts (MPLS, 646)

    """

    ECHO = 7

    DISCARD = 9

    DAYTIME = 13

    CHARGEN = 19

    FTP_DATA = 20

    FTP = 21

    SSH = 22

    TELNET = 23

    SMTP = 25

    TIME = 37

    NICNAME = 43

    TACACS = 49

    DOMAIN = 53

    GOPHER = 70

    FINGER = 79

    WWW = 80

    HOST_NAME = 101

    POP2 = 109

    POP3 = 110

    SUN_RPC = 111

    IDENT = 113

    NNTP = 119

    BGP = 179

    IRC = 194

    PIM_AUTO_RP = 496

    EXEC = 512

    LOGIN = 513

    CMD = 514

    LPD = 515

    UUCP = 540

    KLOGIN = 543

    KSHELL = 544

    TALK = 517

    LDP = 646


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
        return meta._meta_table['StartPortEnum']



class ObjectGroup(object):
    """
    Object\-group configuration
    
    .. attribute:: port
    
    	Port object group
    	**type**\: :py:class:`Port <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port>`
    
    .. attribute:: network
    
    	Network object group
    	**type**\: :py:class:`Network <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network>`
    
    

    """

    _prefix = 'infra-objmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.port = ObjectGroup.Port()
        self.port.parent = self
        self.network = ObjectGroup.Network()
        self.network.parent = self


    class Port(object):
        """
        Port object group
        
        .. attribute:: objects
        
        	Table of port objects groups
        	**type**\: :py:class:`Objects <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects>`
        
        

        """

        _prefix = 'infra-objmgr-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.objects = ObjectGroup.Port.Objects()
            self.objects.parent = self


        class Objects(object):
            """
            Table of port objects groups
            
            .. attribute:: object
            
            	Port object group
            	**type**\: list of :py:class:`Object <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects.Object>`
            
            

            """

            _prefix = 'infra-objmgr-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.object = YList()
                self.object.parent = self
                self.object.name = 'object'


            class Object(object):
                """
                Port object group
                
                .. attribute:: object_name  <key>
                
                	Port object group name \- maximum 64 characters
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: operators
                
                	Table of port operators
                	**type**\: :py:class:`Operators <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects.Object.Operators>`
                
                .. attribute:: nested_groups
                
                	Table of nested port object groups
                	**type**\: :py:class:`NestedGroups <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects.Object.NestedGroups>`
                
                .. attribute:: port_ranges
                
                	Table of port range addresses
                	**type**\: :py:class:`PortRanges <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects.Object.PortRanges>`
                
                .. attribute:: description
                
                	Up to 100 characters describing this object
                	**type**\: str
                
                	**range:** 0..100
                
                

                """

                _prefix = 'infra-objmgr-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object_name = None
                    self.operators = ObjectGroup.Port.Objects.Object.Operators()
                    self.operators.parent = self
                    self.nested_groups = ObjectGroup.Port.Objects.Object.NestedGroups()
                    self.nested_groups.parent = self
                    self.port_ranges = ObjectGroup.Port.Objects.Object.PortRanges()
                    self.port_ranges.parent = self
                    self.description = None


                class Operators(object):
                    """
                    Table of port operators
                    
                    .. attribute:: operator
                    
                    	op class
                    	**type**\: list of :py:class:`Operator <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects.Object.Operators.Operator>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.operator = YList()
                        self.operator.parent = self
                        self.operator.name = 'operator'


                    class Operator(object):
                        """
                        op class
                        
                        .. attribute:: operator_type  <key>
                        
                        	operation for ports
                        	**type**\: :py:class:`PortOperatorEnum <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.PortOperatorEnum>`
                        
                        .. attribute:: port  <key>
                        
                        	Port number
                        	**type**\: one of the below types:
                        
                        	**type**\: :py:class:`PortEnum <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.PortEnum>`
                        
                        
                        ----
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.operator_type = None
                            self.port = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.operator_type is None:
                                raise YPYDataValidationError('Key property operator_type is None')
                            if self.port is None:
                                raise YPYDataValidationError('Key property port is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:operator[Cisco-IOS-XR-infra-objmgr-cfg:operator-type = ' + str(self.operator_type) + '][Cisco-IOS-XR-infra-objmgr-cfg:port = ' + str(self.port) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.operator_type is not None:
                                return True

                            if self.port is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Port.Objects.Object.Operators.Operator']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:operators'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.operator is not None:
                            for child_ref in self.operator:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                        return meta._meta_table['ObjectGroup.Port.Objects.Object.Operators']['meta_info']


                class NestedGroups(object):
                    """
                    Table of nested port object groups
                    
                    .. attribute:: nested_group
                    
                    	nested object group
                    	**type**\: list of :py:class:`NestedGroup <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.nested_group = YList()
                        self.nested_group.parent = self
                        self.nested_group.name = 'nested_group'


                    class NestedGroup(object):
                        """
                        nested object group
                        
                        .. attribute:: nested_group_name  <key>
                        
                        	Name of a nested object group
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nested_group_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.nested_group_name is None:
                                raise YPYDataValidationError('Key property nested_group_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:nested-group[Cisco-IOS-XR-infra-objmgr-cfg:nested-group-name = ' + str(self.nested_group_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.nested_group_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Port.Objects.Object.NestedGroups.NestedGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:nested-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.nested_group is not None:
                            for child_ref in self.nested_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                        return meta._meta_table['ObjectGroup.Port.Objects.Object.NestedGroups']['meta_info']


                class PortRanges(object):
                    """
                    Table of port range addresses
                    
                    .. attribute:: port_range
                    
                    	Match only packets on a given port range
                    	**type**\: list of :py:class:`PortRange <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Port.Objects.Object.PortRanges.PortRange>`
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.port_range = YList()
                        self.port_range.parent = self
                        self.port_range.name = 'port_range'


                    class PortRange(object):
                        """
                        Match only packets on a given port range
                        
                        .. attribute:: start_port  <key>
                        
                        	Port number
                        	**type**\: one of the below types:
                        
                        	**type**\: :py:class:`StartPortEnum <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.StartPortEnum>`
                        
                        
                        ----
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: end_port  <key>
                        
                        	Port number
                        	**type**\: one of the below types:
                        
                        	**type**\: :py:class:`EndPortEnum <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.EndPortEnum>`
                        
                        
                        ----
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.start_port = None
                            self.end_port = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.start_port is None:
                                raise YPYDataValidationError('Key property start_port is None')
                            if self.end_port is None:
                                raise YPYDataValidationError('Key property end_port is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:port-range[Cisco-IOS-XR-infra-objmgr-cfg:start-port = ' + str(self.start_port) + '][Cisco-IOS-XR-infra-objmgr-cfg:end-port = ' + str(self.end_port) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.start_port is not None:
                                return True

                            if self.end_port is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Port.Objects.Object.PortRanges.PortRange']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:port-ranges'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.port_range is not None:
                            for child_ref in self.port_range:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                        return meta._meta_table['ObjectGroup.Port.Objects.Object.PortRanges']['meta_info']

                @property
                def _common_path(self):
                    if self.object_name is None:
                        raise YPYDataValidationError('Key property object_name is None')

                    return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:port/Cisco-IOS-XR-infra-objmgr-cfg:objects/Cisco-IOS-XR-infra-objmgr-cfg:object[Cisco-IOS-XR-infra-objmgr-cfg:object-name = ' + str(self.object_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.object_name is not None:
                        return True

                    if self.operators is not None and self.operators._has_data():
                        return True

                    if self.nested_groups is not None and self.nested_groups._has_data():
                        return True

                    if self.port_ranges is not None and self.port_ranges._has_data():
                        return True

                    if self.description is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                    return meta._meta_table['ObjectGroup.Port.Objects.Object']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:port/Cisco-IOS-XR-infra-objmgr-cfg:objects'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.object is not None:
                    for child_ref in self.object:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                return meta._meta_table['ObjectGroup.Port.Objects']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:port'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.objects is not None and self.objects._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
            return meta._meta_table['ObjectGroup.Port']['meta_info']


    class Network(object):
        """
        Network object group
        
        .. attribute:: ipv6
        
        	IPv6 object group
        	**type**\: :py:class:`Ipv6 <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6>`
        
        .. attribute:: ipv4
        
        	IPv4 object group
        	**type**\: :py:class:`Ipv4 <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4>`
        
        

        """

        _prefix = 'infra-objmgr-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ipv6 = ObjectGroup.Network.Ipv6()
            self.ipv6.parent = self
            self.ipv4 = ObjectGroup.Network.Ipv4()
            self.ipv4.parent = self


        class Ipv6(object):
            """
            IPv6 object group
            
            .. attribute:: objects
            
            	Table of ipv6 object groups
            	**type**\: :py:class:`Objects <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.objects = ObjectGroup.Network.Ipv6.Objects()
                self.objects.parent = self


            class Objects(object):
                """
                Table of ipv6 object groups
                
                .. attribute:: object
                
                	IPv6 object group
                	**type**\: list of :py:class:`Object <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YList()
                    self.object.parent = self
                    self.object.name = 'object'


                class Object(object):
                    """
                    IPv6 object group
                    
                    .. attribute:: object_name  <key>
                    
                    	IPv6 object group name \- maximum 64 characters
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: nested_groups
                    
                    	Table of nested ipv6 object groups
                    	**type**\: :py:class:`NestedGroups <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups>`
                    
                    .. attribute:: address_ranges
                    
                    	Table of ipv6 address ranges
                    	**type**\: :py:class:`AddressRanges <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges>`
                    
                    .. attribute:: addresses
                    
                    	Table of ipv6 addresses
                    	**type**\: :py:class:`Addresses <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.Addresses>`
                    
                    .. attribute:: hosts
                    
                    	Table of ipv6 host addresses
                    	**type**\: :py:class:`Hosts <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.Hosts>`
                    
                    .. attribute:: description
                    
                    	Up to 100 characters describing this object
                    	**type**\: str
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.object_name = None
                        self.nested_groups = ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self.address_ranges = ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self.addresses = ObjectGroup.Network.Ipv6.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self.hosts = ObjectGroup.Network.Ipv6.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self.description = None


                    class NestedGroups(object):
                        """
                        Table of nested ipv6 object groups
                        
                        .. attribute:: nested_group
                        
                        	nested object group
                        	**type**\: list of :py:class:`NestedGroup <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nested_group = YList()
                            self.nested_group.parent = self
                            self.nested_group.name = 'nested_group'


                        class NestedGroup(object):
                            """
                            nested object group
                            
                            .. attribute:: nested_group_name  <key>
                            
                            	Enter the name of a nested object group
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.nested_group_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.nested_group_name is None:
                                    raise YPYDataValidationError('Key property nested_group_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:nested-group[Cisco-IOS-XR-infra-objmgr-cfg:nested-group-name = ' + str(self.nested_group_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.nested_group_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups.NestedGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:nested-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.nested_group is not None:
                                for child_ref in self.nested_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.NestedGroups']['meta_info']


                    class AddressRanges(object):
                        """
                        Table of ipv6 address ranges
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of :py:class:`AddressRange <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_range = YList()
                            self.address_range.parent = self
                            self.address_range.name = 'address_range'


                        class AddressRange(object):
                            """
                            Range of host addresses
                            
                            .. attribute:: start_address  <key>
                            
                            	IPv6 address
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: end_address  <key>
                            
                            	IPv6 address
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.start_address = None
                                self.end_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.start_address is None:
                                    raise YPYDataValidationError('Key property start_address is None')
                                if self.end_address is None:
                                    raise YPYDataValidationError('Key property end_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:address-range[Cisco-IOS-XR-infra-objmgr-cfg:start-address = ' + str(self.start_address) + '][Cisco-IOS-XR-infra-objmgr-cfg:end-address = ' + str(self.end_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.start_address is not None:
                                    return True

                                if self.end_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges.AddressRange']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:address-ranges'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address_range is not None:
                                for child_ref in self.address_range:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.AddressRanges']['meta_info']


                    class Addresses(object):
                        """
                        Table of ipv6 addresses
                        
                        .. attribute:: address
                        
                        	IPv6 address
                        	**type**\: list of :py:class:`Address <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = YList()
                            self.address.parent = self
                            self.address.name = 'address'


                        class Address(object):
                            """
                            IPv6 address
                            
                            .. attribute:: prefix  <key>
                            
                            	IPv6 prefix x\:x\:\:x/y
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: prefix_length  <key>
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..128
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.prefix = None
                                self.prefix_length = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.prefix is None:
                                    raise YPYDataValidationError('Key property prefix is None')
                                if self.prefix_length is None:
                                    raise YPYDataValidationError('Key property prefix_length is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:address[Cisco-IOS-XR-infra-objmgr-cfg:prefix = ' + str(self.prefix) + '][Cisco-IOS-XR-infra-objmgr-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.prefix is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses.Address']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                for child_ref in self.address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Addresses']['meta_info']


                    class Hosts(object):
                        """
                        Table of ipv6 host addresses
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of :py:class:`Host <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.host = YList()
                            self.host.parent = self
                            self.host.name = 'host'


                        class Host(object):
                            """
                            A single host address
                            
                            .. attribute:: host_address  <key>
                            
                            	host ipv6 address
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.host_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.host_address is None:
                                    raise YPYDataValidationError('Key property host_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:host[Cisco-IOS-XR-infra-objmgr-cfg:host-address = ' + str(self.host_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.host_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts.Host']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:hosts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.host is not None:
                                for child_ref in self.host:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object.Hosts']['meta_info']

                    @property
                    def _common_path(self):
                        if self.object_name is None:
                            raise YPYDataValidationError('Key property object_name is None')

                        return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:network/Cisco-IOS-XR-infra-objmgr-cfg:ipv6/Cisco-IOS-XR-infra-objmgr-cfg:objects/Cisco-IOS-XR-infra-objmgr-cfg:object[Cisco-IOS-XR-infra-objmgr-cfg:object-name = ' + str(self.object_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.object_name is not None:
                            return True

                        if self.nested_groups is not None and self.nested_groups._has_data():
                            return True

                        if self.address_ranges is not None and self.address_ranges._has_data():
                            return True

                        if self.addresses is not None and self.addresses._has_data():
                            return True

                        if self.hosts is not None and self.hosts._has_data():
                            return True

                        if self.description is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                        return meta._meta_table['ObjectGroup.Network.Ipv6.Objects.Object']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:network/Cisco-IOS-XR-infra-objmgr-cfg:ipv6/Cisco-IOS-XR-infra-objmgr-cfg:objects'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.object is not None:
                        for child_ref in self.object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                    return meta._meta_table['ObjectGroup.Network.Ipv6.Objects']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:network/Cisco-IOS-XR-infra-objmgr-cfg:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.objects is not None and self.objects._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                return meta._meta_table['ObjectGroup.Network.Ipv6']['meta_info']


        class Ipv4(object):
            """
            IPv4 object group
            
            .. attribute:: objects
            
            	Table of ipv4 object groups
            	**type**\: :py:class:`Objects <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects>`
            
            

            """

            _prefix = 'infra-objmgr-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.objects = ObjectGroup.Network.Ipv4.Objects()
                self.objects.parent = self


            class Objects(object):
                """
                Table of ipv4 object groups
                
                .. attribute:: object
                
                	IPv4 object group
                	**type**\: list of :py:class:`Object <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object>`
                
                

                """

                _prefix = 'infra-objmgr-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YList()
                    self.object.parent = self
                    self.object.name = 'object'


                class Object(object):
                    """
                    IPv4 object group
                    
                    .. attribute:: object_name  <key>
                    
                    	IPv4 object group name \- maximum 64 characters
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: nested_groups
                    
                    	Table of nested ipv4 object groups
                    	**type**\: :py:class:`NestedGroups <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups>`
                    
                    .. attribute:: address_ranges
                    
                    	Table of ipv4 host address ranges
                    	**type**\: :py:class:`AddressRanges <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges>`
                    
                    .. attribute:: addresses
                    
                    	Table of addresses
                    	**type**\: :py:class:`Addresses <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.Addresses>`
                    
                    .. attribute:: hosts
                    
                    	Table of host addresses
                    	**type**\: :py:class:`Hosts <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.Hosts>`
                    
                    .. attribute:: description
                    
                    	Up to 100 characters describing this object
                    	**type**\: str
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'infra-objmgr-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.object_name = None
                        self.nested_groups = ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups()
                        self.nested_groups.parent = self
                        self.address_ranges = ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges()
                        self.address_ranges.parent = self
                        self.addresses = ObjectGroup.Network.Ipv4.Objects.Object.Addresses()
                        self.addresses.parent = self
                        self.hosts = ObjectGroup.Network.Ipv4.Objects.Object.Hosts()
                        self.hosts.parent = self
                        self.description = None


                    class NestedGroups(object):
                        """
                        Table of nested ipv4 object groups
                        
                        .. attribute:: nested_group
                        
                        	Nested object group
                        	**type**\: list of :py:class:`NestedGroup <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nested_group = YList()
                            self.nested_group.parent = self
                            self.nested_group.name = 'nested_group'


                        class NestedGroup(object):
                            """
                            Nested object group
                            
                            .. attribute:: nested_group_name  <key>
                            
                            	Nested object group
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.nested_group_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.nested_group_name is None:
                                    raise YPYDataValidationError('Key property nested_group_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:nested-group[Cisco-IOS-XR-infra-objmgr-cfg:nested-group-name = ' + str(self.nested_group_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.nested_group_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups.NestedGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:nested-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.nested_group is not None:
                                for child_ref in self.nested_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.NestedGroups']['meta_info']


                    class AddressRanges(object):
                        """
                        Table of ipv4 host address ranges
                        
                        .. attribute:: address_range
                        
                        	Range of host addresses
                        	**type**\: list of :py:class:`AddressRange <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_range = YList()
                            self.address_range.parent = self
                            self.address_range.name = 'address_range'


                        class AddressRange(object):
                            """
                            Range of host addresses
                            
                            .. attribute:: start_address  <key>
                            
                            	IPv4 address
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: end_address  <key>
                            
                            	IPv4 address
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.start_address = None
                                self.end_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.start_address is None:
                                    raise YPYDataValidationError('Key property start_address is None')
                                if self.end_address is None:
                                    raise YPYDataValidationError('Key property end_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:address-range[Cisco-IOS-XR-infra-objmgr-cfg:start-address = ' + str(self.start_address) + '][Cisco-IOS-XR-infra-objmgr-cfg:end-address = ' + str(self.end_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.start_address is not None:
                                    return True

                                if self.end_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges.AddressRange']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:address-ranges'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address_range is not None:
                                for child_ref in self.address_range:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.AddressRanges']['meta_info']


                    class Addresses(object):
                        """
                        Table of addresses
                        
                        .. attribute:: address
                        
                        	IPv4 address
                        	**type**\: list of :py:class:`Address <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = YList()
                            self.address.parent = self
                            self.address.name = 'address'


                        class Address(object):
                            """
                            IPv4 address
                            
                            .. attribute:: prefix  <key>
                            
                            	IPv4 address/prefix
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: prefix_length  <key>
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.prefix = None
                                self.prefix_length = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.prefix is None:
                                    raise YPYDataValidationError('Key property prefix is None')
                                if self.prefix_length is None:
                                    raise YPYDataValidationError('Key property prefix_length is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:address[Cisco-IOS-XR-infra-objmgr-cfg:prefix = ' + str(self.prefix) + '][Cisco-IOS-XR-infra-objmgr-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.prefix is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses.Address']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                for child_ref in self.address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Addresses']['meta_info']


                    class Hosts(object):
                        """
                        Table of host addresses
                        
                        .. attribute:: host
                        
                        	A single host address
                        	**type**\: list of :py:class:`Host <ydk.models.infra.Cisco_IOS_XR_infra_objmgr_cfg.ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'infra-objmgr-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.host = YList()
                            self.host.parent = self
                            self.host.name = 'host'


                        class Host(object):
                            """
                            A single host address
                            
                            .. attribute:: host_address  <key>
                            
                            	Host ipv4 address
                            	**type**\: one of the below types:
                            
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'infra-objmgr-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.host_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.host_address is None:
                                    raise YPYDataValidationError('Key property host_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:host[Cisco-IOS-XR-infra-objmgr-cfg:host-address = ' + str(self.host_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.host_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                                return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts.Host']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-objmgr-cfg:hosts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.host is not None:
                                for child_ref in self.host:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                            return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object.Hosts']['meta_info']

                    @property
                    def _common_path(self):
                        if self.object_name is None:
                            raise YPYDataValidationError('Key property object_name is None')

                        return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:network/Cisco-IOS-XR-infra-objmgr-cfg:ipv4/Cisco-IOS-XR-infra-objmgr-cfg:objects/Cisco-IOS-XR-infra-objmgr-cfg:object[Cisco-IOS-XR-infra-objmgr-cfg:object-name = ' + str(self.object_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.object_name is not None:
                            return True

                        if self.nested_groups is not None and self.nested_groups._has_data():
                            return True

                        if self.address_ranges is not None and self.address_ranges._has_data():
                            return True

                        if self.addresses is not None and self.addresses._has_data():
                            return True

                        if self.hosts is not None and self.hosts._has_data():
                            return True

                        if self.description is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                        return meta._meta_table['ObjectGroup.Network.Ipv4.Objects.Object']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:network/Cisco-IOS-XR-infra-objmgr-cfg:ipv4/Cisco-IOS-XR-infra-objmgr-cfg:objects'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.object is not None:
                        for child_ref in self.object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                    return meta._meta_table['ObjectGroup.Network.Ipv4.Objects']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:network/Cisco-IOS-XR-infra-objmgr-cfg:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.objects is not None and self.objects._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
                return meta._meta_table['ObjectGroup.Network.Ipv4']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group/Cisco-IOS-XR-infra-objmgr-cfg:network'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
            return meta._meta_table['ObjectGroup.Network']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-objmgr-cfg:object-group'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.port is not None and self.port._has_data():
            return True

        if self.network is not None and self.network._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_objmgr_cfg as meta
        return meta._meta_table['ObjectGroup']['meta_info']


