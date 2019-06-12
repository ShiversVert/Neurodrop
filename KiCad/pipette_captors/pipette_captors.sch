EESchema Schematic File Version 4
LIBS:pipette_captors-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:D_Photo D1
U 1 1 5CF7C901
P 3300 2350
F 0 "D1" H 3250 2645 50  0000 C CNN
F 1 "D_Photo" H 3250 2554 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 3250 2350 50  0001 C CNN
F 3 "~" H 3250 2350 50  0001 C CNN
	1    3300 2350
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J1
U 1 1 5CF7D654
P 2850 2150
F 0 "J1" H 2958 2331 50  0000 C CNN
F 1 "Conn_01x02_Male" H 2958 2240 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2850 2150 50  0001 C CNN
F 3 "~" H 2850 2150 50  0001 C CNN
	1    2850 2150
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male J2
U 1 1 5CF7E40E
P 4600 2350
F 0 "J2" H 4572 2232 50  0000 R CNN
F 1 "Conn_01x02_Male" H 4572 2323 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 4600 2350 50  0001 C CNN
F 3 "~" H 4600 2350 50  0001 C CNN
	1    4600 2350
	-1   0    0    1   
$EndComp
$Comp
L Device:D_Photo D2
U 1 1 5CF7CC31
P 3950 2350
F 0 "D2" H 3900 2645 50  0000 C CNN
F 1 "D_Photo" H 3900 2554 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 3900 2350 50  0001 C CNN
F 3 "~" H 3900 2350 50  0001 C CNN
	1    3950 2350
	0    1    1    0   
$EndComp
Wire Wire Line
	3950 2150 4400 2150
Wire Wire Line
	4400 2150 4400 2250
Wire Wire Line
	4400 2350 3950 2350
Wire Wire Line
	3950 2350 3950 2450
Wire Wire Line
	3300 2450 3050 2450
Wire Wire Line
	3050 2450 3050 2250
Wire Wire Line
	3050 2150 3300 2150
$Comp
L power:GND #PWR0101
U 1 1 5CF82AEC
P 4050 2850
F 0 "#PWR0101" H 4050 2600 50  0001 C CNN
F 1 "GND" H 4055 2677 50  0000 C CNN
F 2 "" H 4050 2850 50  0001 C CNN
F 3 "" H 4050 2850 50  0001 C CNN
	1    4050 2850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5CF82F87
P 2800 2850
F 0 "#PWR0102" H 2800 2600 50  0001 C CNN
F 1 "GND" H 2805 2677 50  0000 C CNN
F 2 "" H 2800 2850 50  0001 C CNN
F 3 "" H 2800 2850 50  0001 C CNN
	1    2800 2850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x01_Male J3
U 1 1 5CF83103
P 2600 2850
F 0 "J3" H 2708 3031 50  0000 C CNN
F 1 "Conn_01x01_Male" H 2708 2940 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x01_P2.54mm_Vertical" H 2600 2850 50  0001 C CNN
F 3 "~" H 2600 2850 50  0001 C CNN
	1    2600 2850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x01_Male J4
U 1 1 5CF83FB9
P 3850 2850
F 0 "J4" H 3958 3031 50  0000 C CNN
F 1 "Conn_01x01_Male" H 3958 2940 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x01_P2.54mm_Vertical" H 3850 2850 50  0001 C CNN
F 3 "~" H 3850 2850 50  0001 C CNN
	1    3850 2850
	1    0    0    -1  
$EndComp
$EndSCHEMATC
