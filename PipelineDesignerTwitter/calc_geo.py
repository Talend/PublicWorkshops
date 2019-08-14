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
