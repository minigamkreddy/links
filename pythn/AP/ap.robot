*** Settings ***
Library Remote
Library	../Utility/utility.py
Library	Collections
Library	XML
Library String

*** Variables ***
${CON_FILENAME}=	../Testbed/testbed.xml

*** keywords ***
ReadInfo
	${VAR}=	Parse XML	${CON_FILENAME}
	Set Global Variable	${VAR}
	${link}=	Get Element Test	${VAR}	STA/AP/link
	Set Global Variable	${link}	

*** Test Cases ***
TC_01
	[Documentation] the selenium
	ReadInfo
	${result}=	ap_login_ui	${link}
	Log To Console	${result}
	Shoule Be Equal As String	${result}	${True}

