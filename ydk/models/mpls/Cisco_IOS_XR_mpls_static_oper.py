""" Cisco_IOS_XR_mpls_static_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package operational data.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS STATIC operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class MgmtMplsStaticLabelMode_Enum(Enum):
    """
    MgmtMplsStaticLabelMode_Enum

    Mgmt mpls static label mode

    """

    """

    No Label Mode

    """
    NONE = 0

    """

    Per\-prefix Label

    """
    PER_PREFIX = 1

    """

    Per\-VRF label

    """
    PER_VRF = 2

    """

    Label with crossconnect

    """
    CROSS_CONNECT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtMplsStaticLabelMode_Enum']


class MgmtMplsStaticLabelStatus_Enum(Enum):
    """
    MgmtMplsStaticLabelStatus_Enum

    Mgmt mpls static label status

    """

    """

    Label Not Created

    """
    NOT_CREATED = 0

    """

    Label without active VRF

    """
    VRF_DOWN = 1

    """

    Rewrite without active VRF

    """
    REWRITE_VRF_DOWN = 2

    """

    LSD is disconnected

    """
    LSD_DISCONNECTED = 3

    """

    LSD operation failed

    """
    LSD_FAILED = 4

    """

    Waiting for LSD operation

    """
    WAIT_FOR_LSD_REPLY = 5

    """

    Label Created

    """
    LABEL_CREATED = 6

    """

    Label Creation Failed

    """
    LABEL_CREATE_FAILED = 7

    """

    Rewrite Creation Failed

    """
    LABEL_REWRITE_FAILED = 8

    """

    Rewrite NextHop Missing 

    """
    REWRITE_NEXT_HOP_INTERFACE_MISSING = 9

    """

    Label Discrepancy 

    """
    LABEL_DISCREPANCY = 10

    """

    Rewrite Discrepancy 

    """
    REWRITE_DISCREPANCY = 11

    """

    Label Status Unknown

    """
    LABEL_STATUS_UNKNOWN = 12


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtMplsStaticLabelStatus_Enum']


class MgmtStaticAddr_Enum(Enum):
    """
    MgmtStaticAddr_Enum

    Mgmt static addr

    """

    """

    IPv4

    """
    IPV4 = 0

    """

    IPv6

    """
    IPV6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticAddr_Enum']


class MgmtStaticNhLbl_Enum(Enum):
    """
    MgmtStaticNhLbl_Enum

    Mgmt static nh lbl

    """

    """

    Next\-Hop Label

    """
    OUT_LABEL = 0

    """

    Next\-Hop Pop

    """
    OUT_POP = 1

    """

    Next\-Hop Explicit\-Null

    """
    OUT_EXPLICIT_NULL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticNhLbl_Enum']


class MgmtStaticPath_Enum(Enum):
    """
    MgmtStaticPath_Enum

    Mgmt static path

    """

    """

    Crossconnect Path

    """
    CROSS_CONNECT_PATH = 0

    """

    Pop and Lookup Path

    """
    POP_LOOKUP_PATH = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticPath_Enum']



class MplsStatic(object):
    """
    MPLS STATIC operational data
    
    .. attribute:: local_labels
    
    	data for static local\-label table
    	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels>`
    
    .. attribute:: summary
    
    	MPLS STATIC summary data
    	**type**\: :py:class:`Summary <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Summary>`
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\: :py:class:`Vrfs <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs>`
    
    

    """

    _prefix = 'mpls-static-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.local_labels = MplsStatic.LocalLabels()
        self.local_labels.parent = self
        self.summary = MplsStatic.Summary()
        self.summary.parent = self
        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self


    class LocalLabels(object):
        """
        data for static local\-label table
        
        .. attribute:: local_label
        
        	Data for static label
        	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel>`
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.local_label = YList()
            self.local_label.parent = self
            self.local_label.name = 'local_label'


        class LocalLabel(object):
            """
            Data for static label
            
            .. attribute:: local_label_id
            
            	Local Label
            	**type**\: int
            
            	**range:** 16..1048575
            
            .. attribute:: label
            
            	Label value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: label_mode
            
            	Label Mode
            	**type**\: :py:class:`MgmtMplsStaticLabelMode_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode_Enum>`
            
            .. attribute:: label_status
            
            	Label Status
            	**type**\: :py:class:`MgmtMplsStaticLabelStatus_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus_Enum>`
            
            .. attribute:: path_info
            
            	Path Information
            	**type**\: list of :py:class:`PathInfo <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo>`
            
            .. attribute:: prefix
            
            	Prefix Information
            	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.local_label_id = None
                self.label = None
                self.label_mode = None
                self.label_status = None
                self.path_info = YList()
                self.path_info.parent = self
                self.path_info.name = 'path_info'
                self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix()
                self.prefix.parent = self
                self.vrf_name = None


            class PathInfo(object):
                """
                Path Information
                
                .. attribute:: next_hop_interface_name
                
                	Next\-Hop Interface Name
                	**type**\: str
                
                .. attribute:: next_hop_ipv4_address
                
                	Next\-Hop Ipv4 Address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: next_hop_ipv4_address_set
                
                	Next\-Hop Ipv4 Set
                	**type**\: bool
                
                .. attribute:: next_hop_label
                
                	Next\-Hop Label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_hop_label_type
                
                	Next\-Hop Label Type
                	**type**\: :py:class:`MgmtStaticNhLbl_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticNhLbl_Enum>`
                
                .. attribute:: path
                
                	Path Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Path Type
                	**type**\: :py:class:`MgmtStaticPath_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath_Enum>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.next_hop_interface_name = None
                    self.next_hop_ipv4_address = None
                    self.next_hop_ipv4_address_set = None
                    self.next_hop_label = None
                    self.next_hop_label_type = None
                    self.path = None
                    self.type = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:path-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.next_hop_interface_name is not None:
                        return True

                    if self.next_hop_ipv4_address is not None:
                        return True

                    if self.next_hop_ipv4_address_set is not None:
                        return True

                    if self.next_hop_label is not None:
                        return True

                    if self.next_hop_label_type is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.PathInfo']['meta_info']


            class Prefix(object):
                """
                Prefix Information
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix>`
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix()
                    self.prefix.parent = self
                    self.prefix_length = None


                class Prefix(object):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\: :py:class:`MgmtStaticAddr_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr_Enum>`
                    
                    .. attribute:: ipv4_prefix
                    
                    	IPv4 context
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_prefix
                    
                    	IPv6 context
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.ipv4_prefix = None
                        self.ipv6_prefix = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.af_name is not None:
                            return True

                        if self.ipv4_prefix is not None:
                            return True

                        if self.ipv6_prefix is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.prefix is not None and self.prefix._has_data():
                        return True

                    if self.prefix is not None and self.prefix.is_presence():
                        return True

                    if self.prefix_length is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix']['meta_info']

            @property
            def _common_path(self):
                if self.local_label_id is None:
                    raise YPYDataValidationError('Key property local_label_id is None')

                return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:local-labels/Cisco-IOS-XR-mpls-static-oper:local-label[Cisco-IOS-XR-mpls-static-oper:local-label-id = ' + str(self.local_label_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.local_label_id is not None:
                    return True

                if self.label is not None:
                    return True

                if self.label_mode is not None:
                    return True

                if self.label_status is not None:
                    return True

                if self.path_info is not None:
                    for child_ref in self.path_info:
                        if child_ref._has_data():
                            return True

                if self.prefix is not None and self.prefix._has_data():
                    return True

                if self.prefix is not None and self.prefix.is_presence():
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                return meta._meta_table['MplsStatic.LocalLabels.LocalLabel']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:local-labels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.local_label is not None:
                for child_ref in self.local_label:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.LocalLabels']['meta_info']


    class Summary(object):
        """
        MPLS STATIC summary data
        
        .. attribute:: active_vrf_count
        
        	Total Number of Active VRF Active
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: im_connected
        
        	IM is connected
        	**type**\: bool
        
        .. attribute:: interface_count
        
        	Total Number of Interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_foward_reference_count
        
        	Total Number of Active Interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_count
        
        	Total Number of Labels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_discrepancy_count
        
        	Total Number of Labels with Discrepancies
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_error_count
        
        	Total Number of Labels with Errors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lsd_connected
        
        	LSD connection is up
        	**type**\: bool
        
        .. attribute:: mpls_enabled_interface_count
        
        	Total Number of MPLS enabled Interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: rsi_connected
        
        	RSI is connected
        	**type**\: bool
        
        .. attribute:: vrf_count
        
        	Total Number of VRF configured
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.active_vrf_count = None
            self.im_connected = None
            self.interface_count = None
            self.interface_foward_reference_count = None
            self.label_count = None
            self.label_discrepancy_count = None
            self.label_error_count = None
            self.lsd_connected = None
            self.mpls_enabled_interface_count = None
            self.rsi_connected = None
            self.vrf_count = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.active_vrf_count is not None:
                return True

            if self.im_connected is not None:
                return True

            if self.interface_count is not None:
                return True

            if self.interface_foward_reference_count is not None:
                return True

            if self.label_count is not None:
                return True

            if self.label_discrepancy_count is not None:
                return True

            if self.label_error_count is not None:
                return True

            if self.lsd_connected is not None:
                return True

            if self.mpls_enabled_interface_count is not None:
                return True

            if self.rsi_connected is not None:
                return True

            if self.vrf_count is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.Summary']['meta_info']


    class Vrfs(object):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of :py:class:`Vrf <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF Name
            
            .. attribute:: vrf_name
            
            	VRF Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: local_labels
            
            	data for static local\-label table
            	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels>`
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.local_labels = MplsStatic.Vrfs.Vrf.LocalLabels()
                self.local_labels.parent = self


            class LocalLabels(object):
                """
                data for static local\-label table
                
                .. attribute:: local_label
                
                	Data for static label
                	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.local_label = YList()
                    self.local_label.parent = self
                    self.local_label.name = 'local_label'


                class LocalLabel(object):
                    """
                    Data for static label
                    
                    .. attribute:: local_label_id
                    
                    	Local Label
                    	**type**\: int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: label
                    
                    	Label value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_mode
                    
                    	Label Mode
                    	**type**\: :py:class:`MgmtMplsStaticLabelMode_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode_Enum>`
                    
                    .. attribute:: label_status
                    
                    	Label Status
                    	**type**\: :py:class:`MgmtMplsStaticLabelStatus_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus_Enum>`
                    
                    .. attribute:: path_info
                    
                    	Path Information
                    	**type**\: list of :py:class:`PathInfo <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo>`
                    
                    .. attribute:: prefix
                    
                    	Prefix Information
                    	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.local_label_id = None
                        self.label = None
                        self.label_mode = None
                        self.label_status = None
                        self.path_info = YList()
                        self.path_info.parent = self
                        self.path_info.name = 'path_info'
                        self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix()
                        self.prefix.parent = self
                        self.vrf_name = None


                    class PathInfo(object):
                        """
                        Path Information
                        
                        .. attribute:: next_hop_interface_name
                        
                        	Next\-Hop Interface Name
                        	**type**\: str
                        
                        .. attribute:: next_hop_ipv4_address
                        
                        	Next\-Hop Ipv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: next_hop_ipv4_address_set
                        
                        	Next\-Hop Ipv4 Set
                        	**type**\: bool
                        
                        .. attribute:: next_hop_label
                        
                        	Next\-Hop Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_label_type
                        
                        	Next\-Hop Label Type
                        	**type**\: :py:class:`MgmtStaticNhLbl_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticNhLbl_Enum>`
                        
                        .. attribute:: path
                        
                        	Path Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\: :py:class:`MgmtStaticPath_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath_Enum>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.next_hop_interface_name = None
                            self.next_hop_ipv4_address = None
                            self.next_hop_ipv4_address_set = None
                            self.next_hop_label = None
                            self.next_hop_label_type = None
                            self.path = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:path-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.next_hop_interface_name is not None:
                                return True

                            if self.next_hop_ipv4_address is not None:
                                return True

                            if self.next_hop_ipv4_address_set is not None:
                                return True

                            if self.next_hop_label is not None:
                                return True

                            if self.next_hop_label_type is not None:
                                return True

                            if self.path is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo']['meta_info']


                    class Prefix(object):
                        """
                        Prefix Information
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix()
                            self.prefix.parent = self
                            self.prefix_length = None


                        class Prefix(object):
                            """
                            Prefix
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\: :py:class:`MgmtStaticAddr_Enum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr_Enum>`
                            
                            .. attribute:: ipv4_prefix
                            
                            	IPv4 context
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_prefix
                            
                            	IPv6 context
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.af_name is not None:
                                    return True

                                if self.ipv4_prefix is not None:
                                    return True

                                if self.ipv6_prefix is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.prefix is not None and self.prefix._has_data():
                                return True

                            if self.prefix is not None and self.prefix.is_presence():
                                return True

                            if self.prefix_length is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.local_label_id is None:
                            raise YPYDataValidationError('Key property local_label_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:local-label[Cisco-IOS-XR-mpls-static-oper:local-label-id = ' + str(self.local_label_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.local_label_id is not None:
                            return True

                        if self.label is not None:
                            return True

                        if self.label_mode is not None:
                            return True

                        if self.label_status is not None:
                            return True

                        if self.path_info is not None:
                            for child_ref in self.path_info:
                                if child_ref._has_data():
                                    return True

                        if self.prefix is not None and self.prefix._has_data():
                            return True

                        if self.prefix is not None and self.prefix.is_presence():
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:local-labels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.local_label is not None:
                        for child_ref in self.local_label:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYDataValidationError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:vrfs/Cisco-IOS-XR-mpls-static-oper:vrf[Cisco-IOS-XR-mpls-static-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.vrf_name is not None:
                    return True

                if self.local_labels is not None and self.local_labels._has_data():
                    return True

                if self.local_labels is not None and self.local_labels.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                return meta._meta_table['MplsStatic.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-static-oper:mpls-static'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.local_labels is not None and self.local_labels._has_data():
            return True

        if self.local_labels is not None and self.local_labels.is_presence():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        if self.summary is not None and self.summary.is_presence():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        if self.vrfs is not None and self.vrfs.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MplsStatic']['meta_info']

