#Import ElementTree 
import xml.etree.ElementTree as ET

#Define XML file
xml_file = "15Seconds_TulumNoPower_200Count.xml"

#Function to read the XML file and create a txt file
def extract_and_write_tags(xml_file):
    #Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    #List to store tag names
    tags = []

    #Extract tags from XML
    for elem in root.iter():
        tags.append(elem.tag)

    #Write tags to newly created text file
    with open("tags.txt", "w") as file:
        for tag in tags:
            file.write(tag + "\n")
    
    #Confirm the process completion
    print("Tags have been successfully written to tags.txt.")

#Execute the function
extract_and_write_tags(xml_file)