{
  "targets": [
    {
      "target_name": "gstreamer-superficial",
      "sources": [ "gstreamer.cpp" ],
	  "include_dirs": [
		"<!(node -e \"require('nan')\")"
	  ],
	  "conditions" : [
		["OS=='linux'", {
			"include_dirs": [
				'<!@(pkg-config gstreamer-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)'
			],
			"libraries": [
				'<!@(pkg-config gstreamer-1.0 --libs)',
				'<!@(pkg-config gstreamer-app-1.0 --libs)',
				'<!@(pkg-config gstreamer-video-1.0 --libs)'
			]
		}],
		["OS=='win'", {
			"include_dirs": [
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)include/gstreamer-1.0",
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)include/glib-2.0",
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)include/libxml2"
			],
			"libraries": [
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)lib/gstreamer-1.0.lib",
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)lib/gstapp-1.0.lib",
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)lib/gstvideo-1.0.lib",
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)lib/gobject-2.0.lib",
				"<! ( echo %GSTREAMER_1_0_ROOT_X86_64%)lib/glib-2.0.lib"
			]
		}]
	  ]
    }
  ]
}
