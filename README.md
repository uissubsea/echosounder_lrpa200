# echosounder_lrpa200
A ROS publisher node for a tritech lrpa200 echosounding altimeter. This is currently in use on the UiS Subsea LOKE AUV.


This node publishes messages at 7Hz to "sensordata" topic, running a node named "altimeter".
Messages published have the following form; XXX.XXm; if no reading is obtained by the altimeter the published message is 000.00m.
