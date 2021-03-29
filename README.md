# filed

Django Web API that simulates the behavior of an audio file server while using a  SQL database.



Installation
------------

1. Install using ``pip install -r requirements.txt``.

2. run ``django-admin migrate``
3. run ``python manage.py runserver`` according to your enviorment. 

Endpoints
---------
1. POST http://127.0.0.1:8000/api/audio/create
2. GET http://127.0.0.1:8000/api/audio/song/
3. GET,DELETE,PUT http://127.0.0.1:8000/api/audio/song/1
4. GET http://127.0.0.1:8000/api/audio/podcast/
5. GET,DELETE,PUT http://127.0.0.1:8000/api/audio/podcast/1
6. GET http://127.0.0.1:8000/api/audio/audiobook/
7. GET,DELETE,PUT http://127.0.0.1:8000/api/audio/audiobook/1

HEADERS
--------
Content-Type: multipart/form-data; 

Example: of Song Data send through formData 
 {
	"audioFileType": "song",
	"audioFileMetadata" : {
		"name": "test name",
		"duration": "300"
	},
	audioFile: test.mp3
}
Example of podcast Data send through formData

{
    "audioFileType": "podcast",
    "audioFileMetadata": {
	  "name": "test.mp3",
    "duration": "400",
      "host": "hostname",
      "participants": "john,undertaker"
    },
    audioFile: test.mp3
}
Example of audiobook Data send through formData
{
    "audioFileType": "audiobook",
    "audioFileMetadata": {
	  "title": "title",
    "author": "author name",
	  "duration": "400",
    "narrator": "narrator name"
	  },
    audioFile: test.mp3
}

( These fields sends through formData audioFileType,audioFileMetadata,audioFile and mandatary Fields )

Please make media/audio folder inside filedtest/filedProject.
