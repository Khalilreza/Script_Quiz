#Imports ElementTree module from library
import xml.etree.ElementTree as ET

#Define and assign XML file (holds the path of the file we want it to read)
xml_file = "15Seconds_TulumNoPower_200Count.xml"

#Function to read the XML file and create a txt file while extracting the tags
def extract_and_write_tags(xml_file):
    #Parse the XML file --> stored in the 'tree' variable. 
    #Use the 'getroot' method to obtain root element from the xml
    tree = ET.parse(xml_file)
    root = tree.getroot()

    #List to store tag names
    tags = []

    #Extract tags from XML
    #Loop iterates over all elements and retrieves the tag name using 'tag'
    for elem in root.iter():
        tags.append(elem.tag)

    #Write tags to newly created text file
    #Loop through each tag and write it to the text file 
    with open("tags.txt", "w") as file:
        for tag in tags:
            file.write(tag + "\n")
    
    #Confirm the process completion
    print("Tags have been successfully written to tags.txt.")

#Execute the function and pass it to the xml file
extract_and_write_tags(xml_file)