SELECT 
Format(actual_time,'MM-dd-yyy HH:mm') AS 'Test Timestamp', 
operator AS 'Test by', 
s_211_moisture AS 'Silo 211', 
s_221_moisture AS 'Silo 221', 
blender_wood_feeder_moisture AS 'SWF Feeder' 
FROM swf_sample_base 
ORDER BY actual_time desc