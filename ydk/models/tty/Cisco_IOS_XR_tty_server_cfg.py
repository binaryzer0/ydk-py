""" Cisco_IOS_XR_tty_server_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package configuration.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes import TtyPagerEnum
from ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes import TtySessionTimeoutDirectionEnum
from ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes import TtyTransportProtocolEnum
from ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes import TtyTransportProtocolSelectEnum


class Tty(object):
    """
    TTY Line Configuration
    
    .. attribute:: tty_lines
    
    	TTY templates
    	**type**\: :py:class:`TtyLines <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines>`
    
    

    """

    _prefix = 'tty-server-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.tty_lines = Tty.TtyLines()
        self.tty_lines.parent = self


    class TtyLines(object):
        """
        TTY templates
        
        .. attribute:: tty_line
        
        	TTY Line,Use string 'console' to configure a console line,Use string 'default' to configure a default line,Use any string to configure a user defined template
        	**type**\: list of :py:class:`TtyLine <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine>`
        
        

        """

        _prefix = 'tty-server-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.tty_line = YList()
            self.tty_line.parent = self
            self.tty_line.name = 'tty_line'


        class TtyLine(object):
            """
            TTY Line,Use string 'console' to configure a
            console line,Use string 'default' to configure
            a default line,Use any string to configure a
            user defined template
            
            .. attribute:: name  <key>
            
            	Name of the template
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: general
            
            	TTY line general configuration
            	**type**\: :py:class:`General <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.General>`
            
            .. attribute:: telnet
            
            	Telnet protocol\-specific configuration
            	**type**\: :py:class:`Telnet <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Telnet>`
            
            .. attribute:: aaa
            
            	Container class for AAA related TTY configuration
            	**type**\: :py:class:`Aaa <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa>`
            
            .. attribute:: exec_
            
            	EXEC timeout and timestamp configurtion
            	**type**\: :py:class:`Exec <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Exec>`
            
            .. attribute:: connection
            
            	Management connection configuration
            	**type**\: :py:class:`Connection <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection>`
            
            .. attribute:: exec_mode
            
            	Exec Mode Pager  configurtion
            	**type**\: :py:class:`ExecMode <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.ExecMode>`
            
            

            """

            _prefix = 'tty-server-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.name = None
                self.general = Tty.TtyLines.TtyLine.General()
                self.general.parent = self
                self.telnet = Tty.TtyLines.TtyLine.Telnet()
                self.telnet.parent = self
                self.aaa = Tty.TtyLines.TtyLine.Aaa()
                self.aaa.parent = self
                self.exec_ = Tty.TtyLines.TtyLine.Exec()
                self.exec_.parent = self
                self.connection = Tty.TtyLines.TtyLine.Connection()
                self.connection.parent = self
                self.exec_mode = Tty.TtyLines.TtyLine.ExecMode()
                self.exec_mode.parent = self


            class General(object):
                """
                TTY line general configuration
                
                .. attribute:: length
                
                	Number of lines on a screen
                	**type**\: int
                
                	**range:** 0..512
                
                .. attribute:: absolute_timeout
                
                	Absolute timeout for line disconnection
                	**type**\: int
                
                	**range:** 0..10000
                
                .. attribute:: width
                
                	Number of characters on a screen line
                	**type**\: int
                
                	**range:** 0..512
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.length = None
                    self.absolute_timeout = None
                    self.width = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:general'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.length is not None:
                        return True

                    if self.absolute_timeout is not None:
                        return True

                    if self.width is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                    return meta._meta_table['Tty.TtyLines.TtyLine.General']['meta_info']


            class Telnet(object):
                """
                Telnet protocol\-specific configuration
                
                .. attribute:: transparent
                
                	Send a CR as a CR followed by a NULL instead of a CRfollowed by a LF
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.transparent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:telnet'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.transparent is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                    return meta._meta_table['Tty.TtyLines.TtyLine.Telnet']['meta_info']


            class Aaa(object):
                """
                Container class for AAA related TTY
                configuration
                
                .. attribute:: user_groups
                
                	Users characteristics
                	**type**\: :py:class:`UserGroups <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.UserGroups>`
                
                .. attribute:: authorization
                
                	Authorization parameters
                	**type**\: :py:class:`Authorization <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Authorization>`
                
                .. attribute:: authentication
                
                	Authentication parameters
                	**type**\: :py:class:`Authentication <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Authentication>`
                
                .. attribute:: accounting
                
                	Accounting parameters
                	**type**\: :py:class:`Accounting <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Accounting>`
                
                .. attribute:: login_timeout
                
                	Timeouts for any user input during login sequence
                	**type**\: int
                
                	**range:** 0..300
                
                .. attribute:: secret
                
                	Configure a secure one way encrypted password
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: password
                
                	Configure the password for the user
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.user_groups = Tty.TtyLines.TtyLine.Aaa.UserGroups()
                    self.user_groups.parent = self
                    self.authorization = Tty.TtyLines.TtyLine.Aaa.Authorization()
                    self.authorization.parent = self
                    self.authentication = Tty.TtyLines.TtyLine.Aaa.Authentication()
                    self.authentication.parent = self
                    self.accounting = Tty.TtyLines.TtyLine.Aaa.Accounting()
                    self.accounting.parent = self
                    self.login_timeout = None
                    self.secret = None
                    self.password = None


                class UserGroups(object):
                    """
                    Users characteristics
                    
                    .. attribute:: user_group
                    
                    	Group to which the user will belong
                    	**type**\: list of :py:class:`UserGroup <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup>`
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.user_group = YList()
                        self.user_group.parent = self
                        self.user_group.name = 'user_group'


                    class UserGroup(object):
                        """
                        Group to which the user will belong
                        
                        .. attribute:: name  <key>
                        
                        	Name of the group
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: category
                        
                        	Specify as 'root\-system' for root\-system group and 'other' for remaining groups
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tty-server-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.category = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYDataValidationError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:user-group[Cisco-IOS-XR-tty-server-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.name is not None:
                                return True

                            if self.category is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                            return meta._meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:user-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.user_group is not None:
                            for child_ref in self.user_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups']['meta_info']


                class Authorization(object):
                    """
                    Authorization parameters
                    
                    .. attribute:: exec_
                    
                    	For starting an exec (shell)
                    	**type**\: str
                    
                    .. attribute:: event_manager
                    
                    	Specify 'default' or use an authorization list with this name
                    	**type**\: str
                    
                    .. attribute:: commands
                    
                    	For exec (shell) configuration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.exec_ = None
                        self.event_manager = None
                        self.commands = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:authorization'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.exec_ is not None:
                            return True

                        if self.event_manager is not None:
                            return True

                        if self.commands is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Aaa.Authorization']['meta_info']


                class Authentication(object):
                    """
                    Authentication parameters
                    
                    .. attribute:: login
                    
                    	Authentication list name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.login = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:authentication'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.login is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Aaa.Authentication']['meta_info']


                class Accounting(object):
                    """
                    Accounting parameters
                    
                    .. attribute:: exec_
                    
                    	For starting an exec (shell)
                    	**type**\: str
                    
                    .. attribute:: commands
                    
                    	For exec (shell) configuration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.exec_ = None
                        self.commands = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:accounting'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.exec_ is not None:
                            return True

                        if self.commands is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Aaa.Accounting']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:aaa'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.user_groups is not None and self.user_groups._has_data():
                        return True

                    if self.authorization is not None and self.authorization._has_data():
                        return True

                    if self.authentication is not None and self.authentication._has_data():
                        return True

                    if self.accounting is not None and self.accounting._has_data():
                        return True

                    if self.login_timeout is not None:
                        return True

                    if self.secret is not None:
                        return True

                    if self.password is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                    return meta._meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']


            class Exec(object):
                """
                EXEC timeout and timestamp configurtion
                
                .. attribute:: timeout
                
                	EXEC Timeout
                	**type**\: :py:class:`Timeout <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Exec.Timeout>`
                
                .. attribute:: time_stamp
                
                	'True' to Enable & 'False' to Disable time stamp
                	**type**\: bool
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.timeout = None
                    self.time_stamp = None


                class Timeout(object):
                    """
                    EXEC Timeout
                    
                    .. attribute:: minutes
                    
                    	Timeout in minutes
                    	**type**\: int
                    
                    	**range:** 0..35791
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: seconds
                    
                    	Timeout in seconds
                    	**type**\: int
                    
                    	**range:** 0..2147483
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.minutes = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:timeout'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.minutes is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Exec.Timeout']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-server-cfg:exec'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.timeout is not None and self.timeout._has_data():
                        return True

                    if self.time_stamp is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                    return meta._meta_table['Tty.TtyLines.TtyLine.Exec']['meta_info']


            class Connection(object):
                """
                Management connection configuration
                
                .. attribute:: transport_input
                
                	Protocols to use when connecting to the terminal server
                	**type**\: :py:class:`TransportInput <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.TransportInput>`
                
                .. attribute:: transport_output
                
                	Protocols to use for outgoing connections
                	**type**\: :py:class:`TransportOutput <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.TransportOutput>`
                
                .. attribute:: session_timeout
                
                	Interval for closing connection when there is no input traffic
                	**type**\: :py:class:`SessionTimeout <ydk.models.tty.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.SessionTimeout>`
                
                .. attribute:: disconnect_character
                
                	Disconnect character's decimal equivalent value or Character 
                	**type**\: one of the below types:
                
                	**type**\: str
                
                	**pattern:** (\\p{IsBasicLatin}\|\\p{IsLatin\-1Supplement})\*
                
                
                ----
                	**type**\: int
                
                	**range:** 0..255
                
                
                ----
                .. attribute:: acl_in
                
                	ACL to filter ingoing connections
                	**type**\: str
                
                .. attribute:: acl_out
                
                	ACL to filter outgoing connections
                	**type**\: str
                
                .. attribute:: cli_white_space_completion
                
                	Command completion on whitespace
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: session_limit
                
                	The number of outgoing connections
                	**type**\: int
                
                	**range:** 0..20
                
                .. attribute:: escape_character
                
                	Escape character or ASCII decimal equivalent value orspecial strings NONE,DEFAULT,BREAK
                	**type**\: one of the below types:
                
                	**type**\: str
                
                	**pattern:** ((\\p{IsBasicLatin}\|\\p{IsLatin\-1Supplement})\*)\|(DEFAULT)\|(BREAK)\|(NONE)
                
                
                ----
                	**type**\: int
                
                	**range:** 0..255
                
                
                ----
                .. attribute:: transport_preferred
                
                	The preferred protocol to use
                	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                
                

                """

                _prefix = 'tty-management-cfg'
                _revision = '2015-09-25'

                def __init__(self):
                    self.parent = None
                    self.transport_input = Tty.TtyLines.TtyLine.Connection.TransportInput()
                    self.transport_input.parent = self
                    self.transport_output = None
                    self.session_timeout = None
                    self.disconnect_character = None
                    self.acl_in = None
                    self.acl_out = None
                    self.cli_white_space_completion = None
                    self.session_limit = None
                    self.escape_character = None
                    self.transport_preferred = None


                class TransportInput(object):
                    """
                    Protocols to use when connecting to the
                    terminal server
                    
                    .. attribute:: select
                    
                    	Choose transport protocols
                    	**type**\: :py:class:`TtyTransportProtocolSelectEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                    
                    .. attribute:: protocol1
                    
                    	Transport protocol1
                    	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                    
                    .. attribute:: protocol2
                    
                    	Transport protocol2
                    	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                    
                    .. attribute:: none
                    
                    	Not used
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2015-09-25'

                    def __init__(self):
                        self.parent = None
                        self.select = None
                        self.protocol1 = None
                        self.protocol2 = None
                        self.none = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-management-cfg:transport-input'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.select is not None:
                            return True

                        if self.protocol1 is not None:
                            return True

                        if self.protocol2 is not None:
                            return True

                        if self.none is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Connection.TransportInput']['meta_info']


                class TransportOutput(object):
                    """
                    Protocols to use for outgoing connections
                    
                    .. attribute:: select
                    
                    	Choose transport protocols
                    	**type**\: :py:class:`TtyTransportProtocolSelectEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelectEnum>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: protocol1
                    
                    	Transport protocol1
                    	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: protocol2
                    
                    	Transport protocol2
                    	**type**\: :py:class:`TtyTransportProtocolEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolEnum>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: none
                    
                    	Not used
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2015-09-25'

                    def __init__(self):
                        self.parent = None
                        self.select = None
                        self.protocol1 = None
                        self.protocol2 = None
                        self.none = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-management-cfg:transport-output'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.select is not None:
                            return True

                        if self.protocol1 is not None:
                            return True

                        if self.protocol2 is not None:
                            return True

                        if self.none is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Connection.TransportOutput']['meta_info']


                class SessionTimeout(object):
                    """
                    Interval for closing connection when there is
                    no input traffic
                    
                    .. attribute:: timeout
                    
                    	Session timeout interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..35791
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: direction
                    
                    	Include output traffic as well as input traffic
                    	**type**\: :py:class:`TtySessionTimeoutDirectionEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtySessionTimeoutDirectionEnum>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2015-09-25'

                    def __init__(self):
                        self.parent = None
                        self.timeout = None
                        self.direction = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tty-management-cfg:session-timeout'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.timeout is not None:
                            return True

                        if self.direction is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                        return meta._meta_table['Tty.TtyLines.TtyLine.Connection.SessionTimeout']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-management-cfg:connection'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.transport_input is not None and self.transport_input._has_data():
                        return True

                    if self.transport_output is not None and self.transport_output._has_data():
                        return True

                    if self.session_timeout is not None and self.session_timeout._has_data():
                        return True

                    if self.disconnect_character is not None:
                        return True

                    if self.acl_in is not None:
                        return True

                    if self.acl_out is not None:
                        return True

                    if self.cli_white_space_completion is not None:
                        return True

                    if self.session_limit is not None:
                        return True

                    if self.escape_character is not None:
                        return True

                    if self.transport_preferred is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                    return meta._meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info']


            class ExecMode(object):
                """
                Exec Mode Pager  configurtion
                
                .. attribute:: pager
                
                	Preferred Paging Utility
                	**type**\: :py:class:`TtyPagerEnum <ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes.TtyPagerEnum>`
                
                

                """

                _prefix = 'tty-management-cfg'
                _revision = '2015-09-25'

                def __init__(self):
                    self.parent = None
                    self.pager = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tty-management-cfg:exec-mode'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.pager is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                    return meta._meta_table['Tty.TtyLines.TtyLine.ExecMode']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/Cisco-IOS-XR-tty-server-cfg:tty/Cisco-IOS-XR-tty-server-cfg:tty-lines/Cisco-IOS-XR-tty-server-cfg:tty-line[Cisco-IOS-XR-tty-server-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.general is not None and self.general._has_data():
                    return True

                if self.telnet is not None and self.telnet._has_data():
                    return True

                if self.aaa is not None and self.aaa._has_data():
                    return True

                if self.exec_ is not None and self.exec_._has_data():
                    return True

                if self.connection is not None and self.connection._has_data():
                    return True

                if self.exec_mode is not None and self.exec_mode._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
                return meta._meta_table['Tty.TtyLines.TtyLine']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-server-cfg:tty/Cisco-IOS-XR-tty-server-cfg:tty-lines'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.tty_line is not None:
                for child_ref in self.tty_line:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
            return meta._meta_table['Tty.TtyLines']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tty-server-cfg:tty'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.tty_lines is not None and self.tty_lines._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.tty._meta import _Cisco_IOS_XR_tty_server_cfg as meta
        return meta._meta_table['Tty']['meta_info']


