import xml.etree.cElementTree as ET

def csv2xml(pdObj, batchId):
    root = ET.Element("ArrayOfDPScreeningRequest", 
        {"xmlns:xsd": "http://www.w3.org/2001/XMLSchema", 
         "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"})
    dpsr = ET.SubElement(root, "DPScreeningRequest")
    ET.SubElement(dpsr, "SourceSystemID").text = "4"
    ET.SubElement(dpsr, "SourceSystemName").text = "Pixos"

    ET.SubElement(dpsr, "SourceSystemBatchID").text = str(batchId)
    parties = ET.SubElement(dpsr, "PartiesToScreen")

    for index, row in pdObj.iterrows():
        if index == 0:
            continue
        party = ET.SubElement(parties, "DPPartyToScreen")
        ET.SubElement(party, "LinkageID").text = "0"
        ET.SubElement(party, "SourceSystemUniqueKey").text = row[3].strip() # HBL
        ET.SubElement(party, "SourceSystemSubKey").text = "VES"
        ET.SubElement(party, "PartyName").text = row[1].strip() # VesselName
        ET.SubElement(party, "CountryOfExport").text = row[2].strip() # POL
        ET.SubElement(party, "PartyCountryCode")

        party = ET.SubElement(parties, "DPPartyToScreen")
        ET.SubElement(party, "LinkageID").text = "0"
        ET.SubElement(party, "SourceSystemUniqueKey").text = row[3].strip() # HBL
        ET.SubElement(party, "SourceSystemSubKey").text = "S"
        ET.SubElement(party, "PartyName").text = row[4].strip() # Shipper
        ET.SubElement(party, "PartyCountryCode")

        party = ET.SubElement(parties, "DPPartyToScreen")
        ET.SubElement(party, "LinkageID").text = "0"
        ET.SubElement(party, "SourceSystemUniqueKey").text = row[3].strip() # HBL
        ET.SubElement(party, "SourceSystemSubKey").text = "S"
        ET.SubElement(party, "PartyName").text = row[7].strip() # Customer
        ET.SubElement(party, "PartyCountryCode")

        party = ET.SubElement(parties, "DPPartyToScreen")
        ET.SubElement(party, "LinkageID").text = "0"
        ET.SubElement(party, "SourceSystemUniqueKey").text = row[3].strip() # HBL
        ET.SubElement(party, "SourceSystemSubKey").text = "C"
        ET.SubElement(party, "PartyName").text = row[5].strip() # Consignee
        ET.SubElement(party, "PartyCountryCode")

        party = ET.SubElement(parties, "DPPartyToScreen")
        ET.SubElement(party, "LinkageID").text = "0"
        ET.SubElement(party, "SourceSystemUniqueKey").text = row[3].strip() # HBL
        ET.SubElement(party, "SourceSystemSubKey").text = "N"
        ET.SubElement(party, "PartyName").text = row[6].strip() # NotifyParty
        ET.SubElement(party, "PartyCountryCode")


    tree = ET.ElementTree(root)
    return tree
