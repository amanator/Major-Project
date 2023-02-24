# This page is used to convert the collected data into the PIE Chart

import urllib.request
from urllib.parse import urlparse, quote
from quickchart import QuickChart

def createAndDownloadImage(countArray):
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.device_pixel_ratio = 2.0
    qc.config = {
        "type": "pie",
        "data": {
            "labels": ['angry', 'happy', 'sad', 'surprise', 'neutral'],
            "datasets": [{
                "label": "Foo",
                "data": countArray,
            }]
        },
        
    }

    qc.to_file('mychart.png')

    