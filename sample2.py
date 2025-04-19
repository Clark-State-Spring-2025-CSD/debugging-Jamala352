import math

multiChannel = 0

def ChannelSubract(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue -= value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)
    

def ChannelAdd(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue -= value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)

def ChannelSetValue(channelID, value):
    global multiChannel
    if not ValidateValue(value): return
    ChannelClear(channelID)
    value = value * (1000**(channelID - 1))
    multiChannel += value

def ChannelClear(channelID):
    global multiChannel
    if channelID == -1:
        multiChannel = 0
    else:
        channelValue = ChannelGetValue(channelID)    
        channelValue = channelValue * (1000**(channelID - 1))
        multiChannel -= channelValue

def ValidateValue(value):
    if value < 999 and value > 0: 
        return True
    else:
        print("Value out of range, operation not performed") 
        return False

def DisplayAllChannels():
    value = ChannelGetValue(1)
    print(f"Channel 1 is {value}")
    value = ChannelGetValue(2)
    print(f"Channel 2 is {value}")
    value = ChannelGetValue(3)
    print(f"Channel 3 is {value}")

def ChannelGetValue(channelID):
    result = math.floor(multiChannel % (1000**channelID) / (1000**(channelID - 1)))
    return result


###DO NOT ALTER ANY CODE BELOW THIS LINE###

def main():    
    global multiChannel
    multiChannel = 123456789
    ChannelSetValue(2,555)
    ChannelSubract(2,111)
    DisplayAllChannels()
    ChannelClear(-1)
    ChannelSubract(3,1)
    ChannelSetValue(1,111)
    ChannelSetValue(2,888)
    DisplayAllChannels()
    ChannelSubract(1,111)
    ChannelAdd(2,111)
    ChannelAdd(3,5555)
    DisplayAllChannels()





#Start the program
if __name__ == "__main__":
    main()

print("Program terminated")

import math

multiChannel = 0

def ChannelSubtract(channelID, value):
    global multiChannel
    if not IsValidChannelID(channelID): return
    currentValue = ChannelGetValue(channelID)
    currentValue -= value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)
    
def ChannelAdd(channelID, value):
    global multiChannel
    if not IsValidChannelID(channelID): return
    currentValue = ChannelGetValue(channelID)
    currentValue += value  # Corrected the logic to add the value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)

def ChannelSetValue(channelID, value):
    global multiChannel
    if not ValidateValue(value): return
    ChannelClear(channelID)
    value = value * (1000**(channelID - 1))
    multiChannel += value

def ChannelClear(channelID):
    global multiChannel
    if channelID == -1:
        multiChannel = 0
    elif IsValidChannelID(channelID):  # Added validation for channelID
        channelValue = ChannelGetValue(channelID)
        channelValue = channelValue * (1000**(channelID - 1))
        multiChannel -= channelValue

def ValidateValue(value):
    if 0 < value < 999: 
        return True
    else:
        print("Value out of range, operation not performed")
        return False

def DisplayAllChannels():
    for channelID in range(1, 4):  # Loop through channel IDs (1, 2, 3)
        value = ChannelGetValue(channelID)
        print(f"Channel {channelID} is {value}")

def ChannelGetValue(channelID):
    if not IsValidChannelID(channelID): return 0
    result = math.floor(multiChannel % (1000**channelID) / (1000**(channelID - 1)))
    return result

def IsValidChannelID(channelID):
    if channelID in [1, 2, 3]:
        return True
    else:
        print(f"Invalid channel ID: {channelID}. Operation not performed.")
        return False

###DO NOT ALTER ANY CODE BELOW THIS LINE###

def main():
    global multiChannel
    multiChannel = 123456789
    ChannelSetValue(2, 555)
    ChannelSubtract(2, 111)
    DisplayAllChannels()
    ChannelClear(-1)
    ChannelSubtract(3, 1)
    ChannelSetValue(1, 111)
    ChannelSetValue(2, 888)
    DisplayAllChannels()
    ChannelSubtract(1, 111)
    ChannelAdd(2, 111)
    ChannelAdd(3, 5555)
    DisplayAllChannels()

# Start the program
if __name__ == "__main__":
    main()

print("Program terminated")


import math

multiChannel = 0

def ChannelSubtract(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue -= value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)
    
def ChannelAdd(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue += value  # Corrected the logic to add the value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)

def ChannelSetValue(channelID, value):
    global multiChannel
    if not ValidateValue(value): return
    ChannelClear(channelID)
    value = value * (1000**(channelID - 1))
    multiChannel += value

def ChannelClear(channelID):
    global multiChannel
    if channelID == -1:
        multiChannel = 0
    else:
        channelValue = ChannelGetValue(channelID)    
        channelValue = channelValue * (1000**(channelID - 1))
        multiChannel -= channelValue

def ValidateValue(value):
    if 0 <= value < 999:  # Adjusted to allow 0 as a valid value
        return True
    else:
        print("Value out of range, operation not performed")
        return False

def DisplayAllChannels():
    value = ChannelGetValue(1)
    print(f"Channel 1 is {value}")
    value = ChannelGetValue(2)
    print(f"Channel 2 is {value}")
    value = ChannelGetValue(3)
    print(f"Channel 3 is {value}")

def ChannelGetValue(channelID):
    result = math.floor(multiChannel % (1000**channelID) / (1000**(channelID - 1)))
    return result

###DO NOT ALTER ANY CODE BELOW THIS LINE###

def main():    
    global multiChannel
    multiChannel = 123456789
    ChannelSetValue(2, 555)
    ChannelSubtract(2, 111)
    DisplayAllChannels()
    ChannelClear(-1)
    ChannelSubtract(3, 1)
    ChannelSetValue(1, 111)
    ChannelSetValue(2, 888)
    DisplayAllChannels()
    ChannelSubtract(1, 111)
    ChannelAdd(2, 111)
    ChannelAdd(3, 5555)
    DisplayAllChannels()

# Start the program
if __name__ == "__main__":
    main()


