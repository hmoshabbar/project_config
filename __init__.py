

UPLOAD_DIR="upload"
PLIST_TEMPLATE="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>items</key>
   <array>
       <dict>
           <key>assets</key>
           <array>
               <dict>
                   <key>kind</key>
                   <string>software-package</string>
                   <key>url</key>
                   <string>{{ipaUrl}}</string>
                </dict>
                <dict>
                   <key>kind</key>
                   <string>display-image</string>
                   <key>needs-shine</key>
                   <true/>
                   <key>url</key>
                   <string>{{iconSmallUrl}}</string>
                </dict>
            <dict>
                   <key>kind</key>
                   <string>full-size-image</string>
                   <key>needs-shine</key>
                   <true/>
                   <key>url</key>
                   <string>{{iconBigUrl}}</string>
            </dict>
            </array><key>metadata</key>
               <dict>
               <key>bundle-identifier</key>
               <string>{{idfix}}</string>
               <key>bundle-version</key>
               <string>{{versionName}}</string>
               <key>kind</key>
               <string>software</string>
               <key>subtitle</key>
               <string>{{name}}</string>
               <key>title</key>
               <string>{{name}}</string>
            </dict>
       </dict>
    </array>
</dict>
</plist>
"""