# ![image](./resources/Talend_PD_TalendBlues_SM.png) Assests for Twitter Heatmap Pipeline Workshop

### Pipeline Designer Trial Links
[APAC](https://iam.ap.cloud.talend.com/idp/trial-registration?product=pipelines&period=14&utm_medium=talendcommunity&utm_source=user_group)
[EMEA](https://iam.eu.cloud.talend.com/idp/trial-registration?product=pipelines&period=14&utm_medium=talendcommunity&utm_source=user_group)
[US](https://iam.us.cloud.talend.com/idp/trial-registration?product=pipelines&period=14&utm_medium=talendcommunity&utm_source=user_group)

### Instructions
You can either copy and paste from this main page or use the files for the different parts of the Pipeline Designer that you will see  you need in the workbook exersize.

### - Step 7: Avro Schema

The messages sent by the producer of tweeter feeds are formatted in Avro. The schema used is:

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

### - Step 29: Add the Python to the Pipeline

```python
# Here you can define your custom MAP transformations on the input
# The input record is available as the "input" variable
# The output record is available as the "output" variable
# The record columns are available as defined in your input/output schema
# The return statement is added automatically to the generated code,
# so there's no need to add it here
# Code Sample :
# output['col1'] = input['col1'] + 1234
# output['col2'] = "The " + input['col2'] + ":"
# output['col3'] = CustomTransformation(input['col3'])
output = json.loads("{}")
output['latitude']=None 
output['longitude']=None
output['location']=None
output['id']=input['id']
output['created_date']=input['created_date']
output['text']=input['text']
output['type']=input['type']
if input['gps_coords']==None:
    output['latitude']=(input['bounding_box'][0]['latitude']+input['bounding_box'][1]['latitude']+input['bounding_box'][2]['latitude']+input['bounding_box'][3]['latitude'])/4
    output['longitude']=(input['bounding_box'][0]['longitude']+input['bounding_box'][1]['longitude']+input['bounding_box'][2]['longitude']+input['bounding_box'][3]['longitude'])/4
    output['location']=str(output['latitude'])+','+str(output['longitude'])     
else:        
    output['latitude']=input['gps_coords']['latitude'] 
    output['longitude']=input['gps_coords']['longitude']
    output['location']=str(output['latitude'])+','+str(output['longitude'])    
    
```

### - Step 32 - 33: Create the ElasticSeach Index

```json

{  
   "settings":{  
      "number_of_shards":1
   },
   "mappings":{  
      "sm_loc":{  
         "properties":{  
            "latitude":{  
               "type":"double"
            },
            "longitude":{  
               "type":"double"
            },
            "location":{  
               "type":"geo_point"
            },
            "id":{  
               "type":"string"
            },
            "created_date":{  
               "type":"string"
            },
            "text":{  
               "type":"string"
            },
            "type":{  
               "type":"string"
            }
         }
      }
   }
}
```

