# Assests for Twitter Heatmap Pipeline Workshop
![image](./resources/Talend_PD_TalendBlue.png)


###Instructions
The files are the code that you need to copy and paste into the different parts of the Pipeline Designer that you will find in the workbook exersize.

### - Step 7 Avro Schema

The messages sent by the producer are formatted in Avro. The schema used is :

```json
{
	"type": "record",
	"name": "outer_record_1952535649249628006",
	"namespace": "org.talend",
	"fields": [{
			"name": "geo_bounding_box",
			"type": {
				"type": "array",
				"items": {
					"type": "record",
					"name": "gps_coordinates",
					"namespace": "org.talend",
					"fields": [{
							"name": "latitude",
							"type": [
								"null",
								"double"
							]
						},
						{
							"name": "longitude",
							"type": [
								"null",
								"double"
							]
						}
					]
				}
			}
		},
		{
			"name": "gps_coords",
			"type": ["null", {
				"type": "record",
				"name": "gps_coordinatesx",
				"namespace": "org.talend",
				"fields": [{
						"name": "latitude",
						"type": [
							"null",
							"double"
						]
					},
					{
						"name": "longitude",
						"type": [
							"null",
							"double"
						]
					}
				]
			}]
		},
		{
			"name": "created_at",
			"type": [
				"null",
				"string"
			]
		},
		{
			"name": "text",
			"type": [
				"null",
				"string"
			]
		},
		{
			"name": "id",
			"type": [
				"null",
				"string"
			]
		},
		{
			"name": "type",
			"type": [
				"null",
				"string"
			]
		}
	]
}

```
