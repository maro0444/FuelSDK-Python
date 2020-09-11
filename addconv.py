# Add a require statement to reference the Fuel SDK's functionality:
import FuelSDK
import ET_Client

print('>>>  Add a row to a data extension using CustomerKey')

# Next, create an instance of the ET_Client class:


try:
    # debug = False
    myClient = FuelSDK.ET_Client()
    # Create an instance of the object type we want to work with:
    de = FuelSDK.ET_DataExtension_Row()
    # Associate the ET_Client to the object using the auth_stub property:
    de.auth_stub = myClient

    de.CustomerKey = "2ECB6A6E-9A50-453C-9A3A-241AB39B0092"
    de.props = {"Email" : "you@cu.edu", "First" : "Gill", "Last" : "Roush", "EID" : "0678923", "Action" : "viewed financials"}
    # Utilize one of the ET_List methods:

    postResponse = de.post()

    # Print out the results for viewing
    print('Post Status: ' + str(postResponse.status))
    print('Code: ' + str(postResponse.code))
    print('Message: ' + str(postResponse.message))
    print('Results: ' + str(postResponse.results))

except Exception as e:
    print('Caught exception: ' + str(e.message))
    print(e)