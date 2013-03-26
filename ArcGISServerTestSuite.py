import agsutil
import urllib


def testSecurityAddUser():
    return

def testPublishMapService():
    return

def testServiceRestart():
    
    # Get current status
    # http://sssgisapp1:6080/arcgis/admin/services/RevBase.MapServer/status?f=json
    # configuredState "STARTED" "STOPPED"
    # realTimeState "STARTED" "STOPPED"
    
    # If stopped, skip and log
    # If started, stop then start

# Tests for type GeometryServer
## Check for existence. Create if not existing and log.
## Restart.
## Validate ItemInfo Tags
## Delete if did not exist.

# Tests for type ImageServer
## Publish As Raster
## Build Cache?
## Validate Item Info
## Validate Thumbnail
## Validate Histograms
## Validate Key Properties
def testISExportImage():
    return
def testISQuery():
    return
def testISIdentify():
    return
def testISComputeHistograms():
    return

# Tests for type MapServer
def testMSMap():
    return
def testMSQuery():
    return
def testMSData():
    return
# Tests for type GeocodeServer
# Tests for type GeoDataServer
# Tests for type GPServer
## Test PrintingTools?
# Tests for type GlobeServer
# Tests for type SearchServer
## Check for existence. Create if not existing and log.
## Restart.
## Delete if did not exist.

# Extension tests
## Tests for extension KmlServer
## SingleImage Test
## SeparateImages Test
## Vectors Test
# Tests for extension FeatureServer
## Query Test
## Editing Test
# Tests for extension NAServer
# Tests for extension WCSServer
# Tests for extension WFSServer
# Tests for extension WMSServer
# Tests for extension MobileServer
# Tests for extension JPIPServer


#TODO Start and stop each service
#TODO Create test user
#TODO Create test folder
#TODO Publish one of each type of service
#TODO Run through operations on each service

#TODO Cleanup
#TODO   Delete all services
#TODO   Delete test folder
#TODO   Delete test user
