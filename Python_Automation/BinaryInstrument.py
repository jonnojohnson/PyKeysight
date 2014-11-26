from visa import *

## Requires VISA installed on Control PC
## 'http://www.agilent.com/find/visa'
## Requires PyVISA to use VISA in Python
## 'http://pyvisa.sourceforge.net/pyvisa/'

## DSO BinBlock Waveform xfer Example
## Originally Written by: John Dorhigi, Inside Application Engineer
## Modified for general use by: John-Michael O'Brien, Inside Application Engineer

## Revision History:
## 2/13/2014 JMO: Added readbinblk_raw to allow for binary transfers that are
##  kept strictly as a string.
## 2/5/2014 JMO: Reworked to avoid the use of low level VISA calls. Added generic
##  handling for binary blocks, improved memory usage, and extended utility
##  to include very large transfers (> 100MB)

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
## Copyright 2011-2014 Agilent Technologies Inc. All rights reserved.
##
## You have a royalty-free right to use, modify, reproduce and distribute this
## example files (and/or any modified version) in any way you find useful, provided
## that you agree that Agilent has no warranty, obligations or liability for any
## Sample Application Files.
##
##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class BinaryInstrument(Instrument):
    # This function takes two arguments. datatype is a single character that will
    # be passed to the struct.unpack function. Please see the Format Characters
    # section of the struct.unpack documentation for what characters are valid.
    def readbinblk(self,datatype="B",littleendian=False):
        data=self.read_raw() # Get the data
        startpos=data.find("#")
        if startpos < 0:
            raise IOError("No start of block found")
        lenlen = int(data[startpos+1:startpos+2]) # get the data length length

        # If it's a definite length binary block
        if lenlen > 0:
            # Get the length from the header
            offset = startpos+2+lenlen
            datalen = int(data[startpos+2:startpos+2+lenlen])
        else:
            # If it's an indefinite length binary block get the length from the transfer itself
            offset = startpos+2
            datalen = len(data)-offset-1

        if littleendian==True:
            orderchar="<"
        else:
            orderchar=">"

        # determine the length of the data being decoded.
        datatypelength = {'c':1,
                          'b':1,
                          'B':1,
                          '?':1,
                          'h':2,
                          'H':2,
                          'i':4,
                          'I':4,
                          'l':4,
                          'L':4,
                          'q':8,
                          'Q':8,
                          'f':4,
                          'd':8}[datatype]

        # Build the format string. (It will have a form like ">1024h")
        formatstring = orderchar+str(datalen/datatypelength)+datatype

        # Extract the data out into a list.
        return list(struct.unpack_from(formatstring,data,offset))
    def readbinblk_raw(self):
        data=self.read_raw() # Get the data
        startpos=data.find("#")
        if startpos < 0:
            raise IOError("No start of block found")
        lenlen = int(data[startpos+1:startpos+2]) # get the data length length

        # If it's a definite length binary block
        if lenlen > 0:
            # Get the length from the header
            offset = startpos+2+lenlen
            datalen = int(data[startpos+2:startpos+2+lenlen])
        else:
            # If it's an indefinite length binary block get the length from the transfer itself
            offset = startpos+2
            datalen = len(data)-offset-1

        # Extract the data out into a list.
        return data[offset:offset+datalen]
