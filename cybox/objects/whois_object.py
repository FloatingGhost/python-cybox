# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.whois_object as whois_binding

import cybox
from cybox.common import ObjectProperties, BaseProperty, String, DateTime, Date
from cybox.objects.address_object import Address, EmailAddress
from cybox.objects.uri_object import URI


class WhoisNameservers(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisNameserversType
    _binding_var = "Nameserver"
    _contained_type = URI
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisStatus(BaseProperty):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisStatusType
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"
    datatype = "string"


class WhoisStatuses(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisStatusesType
    _binding_var = "Status"
    _contained_type = WhoisStatus
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisContact(cybox.Entity):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisContactType
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"

    contact_type = fields.TypedField("contact_type")
    contact_id = fields.TypedField("Contact_ID", String)
    name = fields.TypedField("Name", String)
    address = fields.TypedField("Address", String)
    email_address = fields.TypedField("Email_Address", EmailAddress)
    phone_number = fields.TypedField("Phone_Number", String)
    fax_number = fields.TypedField("Fax_Number", String)
    organization = fields.TypedField("Organization", String)


class WhoisContacts(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisContactsType
    _binding_var = "Contact"
    _contained_type = WhoisContact
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisRegistrant(WhoisContact):
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"
    _binding = whois_binding
    _binding_class = whois_binding.WhoisRegistrantInfoType

    registrant_id = fields.TypedField("Registrant_ID", String)


class WhoisRegistrants(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisRegistrantsType
    _binding_var = "Registrant"
    _contained_type = WhoisRegistrant
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisRegistrar(cybox.Entity):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisRegistrarInfoType
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"

    registrar_id = fields.TypedField("Registrar_ID", String)
    registrar_guid = fields.TypedField("Registrar_GUID", String)
    name = fields.TypedField("Name", String)
    address = fields.TypedField("Address", String)
    email_address = fields.TypedField("Email_Address", EmailAddress)
    phone_number = fields.TypedField("Phone_Number", String)
    whois_server = fields.TypedField("Whois_Server", URI)
    referral_url = fields.TypedField("Referral_URL", URI)
    contacts = fields.TypedField("Contacts", WhoisContacts)


class WhoisEntry(ObjectProperties):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisObjectType
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"
    _XSI_NS = 'WhoisObj'
    _XSI_TYPE = 'WhoisObjectType'

    lookup_date = fields.TypedField("Lookup_Date", DateTime)
    remarks = fields.TypedField("Remarks", String)
    contact_info = fields.TypedField("Contact_Info", WhoisContact)
    domain_name = fields.TypedField("Domain_Name", URI)
    domain_id = fields.TypedField("Domain_ID", String)
    server_name = fields.TypedField("Server_Name", URI)
    ip_address = fields.TypedField("IP_Address", Address)
    dnssec = fields.TypedField("DNSSEC")
    nameservers = fields.TypedField("Nameservers", WhoisNameservers)
    status = fields.TypedField("Status", WhoisStatuses)
    updated_date = fields.TypedField("Updated_Date", Date)
    creation_date = fields.TypedField("Creation_Date", Date)
    expiration_date = fields.TypedField("Expiration_Date", Date)
    regional_internet_registry = fields.TypedField("Regional_Internet_Registry", String)
    sponsoring_registrar = fields.TypedField("Sponsoring_Registrar", String)
    registrar_info = fields.TypedField("Registrar_Info", WhoisRegistrar)
    registrants = fields.TypedField("Registrants", WhoisRegistrants)

    DNSSEC_SIGNED = "Signed"
    DNSSEC_UNSIGNED = "Unsigned"
