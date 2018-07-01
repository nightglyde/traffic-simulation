from util import *
schedule = deque([
  (266, 5, 1),
  (5067, 0, 7),
  (6612, 7, 7),
  (7198, 0, 6),
  (8199, 2, 7),
  (8990, 7, 7),
  (11635, 6, 7),
  (15331, 2, 7),
  (17235, 6, 7),
  (24026, 6, 7),
  (24131, 1, 5),
  (25070, 2, 3),
  (27760, 6, 7),
  (31138, 2, 7),
  (35617, 5, 3),
  (37332, 1, 7),
  (37334, 0, 7),
  (41650, 2, 4),
  (44843, 6, 7),
  (46531, 2, 4),
  (47265, 4, 7),
  (48245, 6, 7),
  (48736, 7, 7),
  (52022, 6, 7),
  (60442, 4, 7),
  (61131, 5, 5),
  (65502, 7, 7),
  (69375, 3, 7),
  (70964, 4, 3),
  (71667, 2, 7),
  (74632, 3, 7),
  (77867, 2, 6),
  (80460, 5, 7),
  (83880, 5, 3),
  (90238, 3, 7),
  (92691, 3, 7),
  (93557, 0, 7),
  (93614, 5, 6),
  (94558, 1, 7),
  (96133, 0, 7),
  (100401, 4, 3),
  (108286, 5, 2),
  (108919, 1, 7),
  (110244, 3, 2),
  (110473, 2, 7),
  (116706, 7, 7),
  (117794, 1, 4),
  (118278, 1, 4),
  (119257, 3, 7),
  (120883, 6, 7),
  (121328, 4, 6),
  (123169, 1, 7),
  (126160, 1, 4),
  (127365, 3, 6),
  (128185, 6, 4),
  (131153, 5, 7),
  (132784, 7, 7),
  (138654, 7, 7),
  (139153, 1, 5),
  (142039, 6, 7),
  (143100, 6, 6),
  (144653, 1, 7),
  (149031, 7, 0),
  (156123, 5, 7),
  (158168, 6, 5),
  (161148, 7, 7),
  (163062, 7, 6),
  (163150, 4, 7),
  (164664, 5, 3),
  (165098, 0, 7),
  (166068, 4, 5),
  (167079, 5, 7),
  (167724, 0, 7),
  (168830, 0, 0),
  (169332, 6, 7),
  (171711, 3, 2),
  (175890, 0, 0),
  (178244, 3, 7),
  (178385, 4, 6),
  (179960, 0, 7),
  (180503, 0, 0),
  (180853, 5, 7),
  (182339, 1, 0),
  (182432, 5, 7),
  (182541, 6, 7),
  (182678, 1, 7),
  (186704, 7, 0),
  (189732, 2, 7),
  (193489, 7, 6),
  (194904, 5, 7),
  (195027, 5, 6),
  (197219, 5, 7),
  (197877, 4, 2),
  (198917, 3, 7),
  (199343, 1, 0),
  (199870, 4, 3),
  (200110, 4, 7),
  (200927, 1, 7),
  (201385, 6, 7),
  (202054, 3, 3),
  (202439, 4, 7),
  (206245, 1, 7),
  (206700, 5, 7),
  (206765, 1, 7),
  (209963, 4, 3),
  (212258, 1, 7),
  (215030, 0, 0),
  (215312, 3, 5),
  (215608, 6, 7),
  (215678, 5, 3),
  (217656, 3, 7),
  (223772, 7, 7),
  (225576, 1, 7),
  (237080, 4, 7),
  (237764, 3, 7),
  (238380, 2, 7),
  (240681, 6, 3),
  (241135, 2, 7),
  (252544, 7, 7),
  (253941, 5, 7),
  (254370, 6, 3),
  (255230, 3, 7),
  (255249, 1, 6),
  (256031, 3, 5),
  (258058, 3, 7),
  (261892, 4, 6),
  (267214, 5, 7),
  (267506, 2, 7),
  (268686, 0, 7),
  (281423, 5, 7),
  (282740, 3, 7),
  (287438, 7, 7),
  (289293, 1, 7),
  (289759, 7, 7),
  (292464, 7, 0),
  (292706, 7, 7),
  (293801, 1, 7),
  (294081, 0, 7),
  (297892, 6, 7),
  (298343, 7, 7),
  (298661, 4, 7),
  (299342, 2, 2),
  (299859, 1, 3),
  (302842, 4, 7),
  (306743, 6, 7),
  (308097, 5, 7),
  (309483, 3, 7),
  (312190, 2, 7),
  (312543, 7, 2),
  (316419, 2, 3),
  (318045, 6, 7),
  (318391, 2, 6),
  (319987, 3, 7),
  (321225, 2, 5),
  (322453, 0, 0),
  (329896, 1, 7),
  (334299, 6, 0),
  (337465, 0, 7),
  (338634, 7, 4),
  (345826, 2, 2),
  (348336, 0, 7),
  (349394, 1, 6),
  (350538, 0, 7),
  (359933, 3, 6),
  (360300, 6, 0),
  (366233, 3, 6),
  (367103, 2, 5),
  (369334, 1, 7),
  (370283, 6, 3),
  (373822, 0, 7),
  (374728, 7, 7),
  (374886, 1, 4),
  (379548, 1, 7),
  (379835, 5, 7),
  (380815, 0, 0),
  (381346, 2, 7),
  (382857, 1, 7),
  (383649, 2, 2),
  (384783, 4, 7),
  (388008, 0, 0),
  (390088, 7, 6),
  (391042, 5, 3),
  (391917, 0, 4),
  (393056, 7, 7),
  (395930, 3, 7),
  (398775, 1, 7),
  (398902, 0, 7),
  (401219, 6, 7),
  (405540, 6, 7),
  (407915, 3, 7),
  (407989, 0, 7),
  (408612, 0, 7),
  (409233, 1, 7),
  (413613, 5, 7),
  (417753, 2, 7),
  (418399, 0, 7),
  (418736, 5, 2),
  (421923, 0, 0),
  (423990, 2, 7),
  (424576, 1, 7),
  (428653, 5, 5),
  (429985, 4, 6),
  (430273, 7, 7),
  (433433, 3, 7),
  (434206, 4, 7),
  (441674, 0, 7),
  (445488, 2, 2),
  (446658, 1, 0),
  (448665, 6, 0),
  (450498, 6, 3),
  (450775, 2, 7),
  (451458, 6, 7),
  (451886, 3, 6),
  (451927, 1, 7),
  (452772, 5, 6),
  (456577, 5, 2),
  (457411, 0, 7),
  (460687, 4, 5),
  (460758, 3, 3),
  (469344, 1, 7),
  (473206, 4, 0),
  (474737, 5, 7),
  (475780, 2, 6),
  (475828, 6, 4),
  (478024, 6, 7),
  (481439, 0, 4),
  (489991, 1, 0),
  (491318, 0, 4),
  (491938, 6, 7),
  (494795, 0, 7),
  (498250, 7, 7),
  (501778, 4, 6),
  (502068, 3, 6),
  (504372, 5, 7),
  (506094, 4, 7),
  (506267, 0, 4),
  (512798, 4, 6),
  (513858, 2, 7),
  (518745, 4, 7),
  (521160, 0, 7),
  (523825, 3, 7),
  (523949, 7, 0),
  (524058, 5, 5),
  (525469, 3, 7),
  (527097, 2, 7),
  (527880, 0, 3),
  (527979, 2, 7),
  (528070, 5, 7),
  (529465, 4, 7),
  (530757, 0, 7),
  (535200, 5, 7),
  (535861, 0, 7),
  (537386, 1, 0),
  (538975, 3, 7),
  (541465, 6, 7),
  (541803, 6, 7),
  (542599, 5, 7),
  (543859, 4, 7),
  (546563, 5, 7),
  (546881, 2, 7),
  (549041, 6, 3),
  (550078, 0, 7),
  (551646, 3, 2),
  (552103, 0, 4),
  (552156, 4, 7),
  (554019, 0, 7),
  (554777, 1, 3),
  (555186, 0, 7),
  (555484, 3, 3),
  (557516, 1, 7),
  (559092, 7, 7),
  (560086, 7, 7),
  (560913, 5, 6),
  (564269, 6, 3),
  (564879, 5, 7),
  (565089, 3, 3),
  (565542, 2, 7),
  (566159, 3, 7),
  (567222, 0, 7),
  (571416, 3, 5),
  (573475, 4, 7),
  (578717, 3, 7),
  (588640, 4, 7),
  (589205, 0, 7),
  (589721, 2, 7),
  (594165, 2, 6),
  (596629, 5, 7),
  (601858, 1, 7),
  (605364, 2, 2),
  (606245, 1, 0),
  (606929, 6, 7),
  (611171, 2, 7),
  (612162, 7, 7),
  (618093, 1, 7),
  (623496, 5, 7),
  (630505, 0, 6),
  (632219, 7, 7),
  (644035, 2, 7),
  (647273, 2, 7),
  (648938, 5, 7),
  (650123, 3, 2),
  (656717, 6, 7),
  (656891, 7, 0),
  (659493, 6, 7),
  (660517, 2, 7),
  (661717, 3, 6),
  (666035, 4, 6),
  (667943, 6, 6),
  (669315, 0, 7),
  (674699, 4, 7),
  (674981, 6, 7),
  (676433, 4, 6),
  (676639, 1, 5),
  (676677, 0, 7),
  (678246, 6, 7),
  (679532, 0, 7),
  (684084, 2, 7),
  (684983, 4, 7),
  (685156, 7, 7),
  (691153, 6, 4),
  (691762, 4, 7),
  (696729, 2, 2),
  (698750, 6, 3),
  (701539, 2, 7),
  (702122, 0, 7),
  (704882, 2, 7),
  (706722, 7, 0),
  (710651, 2, 1),
  (711504, 2, 7),
  (712955, 7, 7),
  (715741, 3, 7),
  (717483, 1, 7),
  (720175, 6, 7),
  (721138, 4, 7),
  (722455, 7, 0),
  (727265, 5, 7),
  (728315, 7, 7),
  (728560, 2, 5),
  (728876, 2, 2),
  (730069, 3, 7),
  (734126, 2, 7),
  (740044, 1, 0),
  (743191, 6, 7),
  (744320, 3, 7),
  (746274, 7, 7),
  (748212, 3, 7),
  (751284, 2, 4),
  (752587, 1, 7),
  (753435, 7, 7),
  (753478, 1, 7),
  (754672, 0, 7),
  (756236, 5, 7),
  (756832, 0, 3),
  (757832, 0, 5),
  (761525, 3, 7),
  (765153, 5, 7),
  (765893, 7, 7),
  (768731, 6, 4),
  (769631, 7, 7),
  (769895, 1, 7),
  (771799, 5, 7),
  (773155, 4, 7),
  (775709, 6, 2),
  (785786, 2, 3),
  (788707, 1, 7),
  (791018, 6, 7),
  (796981, 0, 0),
  (798995, 3, 7),
  (802749, 3, 7),
  (804907, 0, 4),
  (808428, 7, 7),
  (810340, 4, 2),
  (812287, 6, 3),
  (813596, 0, 7),
  (814236, 4, 7),
  (815225, 6, 7),
  (815813, 1, 7),
  (816242, 3, 7),
  (822248, 6, 0),
  (822494, 0, 7),
  (825384, 3, 7),
  (826528, 4, 7),
  (828124, 4, 5),
  (828185, 0, 7),
  (828348, 6, 4),
  (829911, 5, 7),
  (837726, 1, 0),
  (838623, 6, 4),
  (839264, 4, 5),
  (839783, 2, 7),
  (842829, 4, 7),
  (846192, 3, 2),
  (849783, 6, 0),
  (851056, 6, 4),
  (854057, 0, 0),
  (855494, 3, 7),
  (855553, 7, 4),
  (855780, 5, 7),
  (856210, 7, 7),
  (856839, 4, 2),
  (857018, 3, 7),
  (858853, 4, 7),
  (859734, 5, 2),
  (863244, 5, 7),
  (865528, 2, 7),
  (868526, 5, 2),
  (870403, 3, 5),
  (871798, 5, 7),
  (873887, 2, 3),
  (880357, 3, 7),
  (881215, 6, 0),
  (882536, 6, 6),
  (884550, 0, 7),
  (885603, 3, 7),
  (888249, 3, 7),
  (890411, 3, 3),
  (891460, 1, 7),
  (892165, 1, 7),
  (892513, 0, 7),
  (895924, 2, 7),
  (896569, 0, 0),
  (897411, 7, 7),
  (899549, 4, 5),
  (899908, 3, 6),
  (900771, 1, 3),
  (901747, 4, 2),
  (903146, 2, 7),
  (904530, 7, 7),
  (905590, 5, 7),
  (907924, 5, 3),
  (911518, 3, 7),
  (911843, 2, 7),
  (912807, 0, 7),
  (913262, 2, 2),
  (914171, 6, 7),
  (915369, 0, 7),
  (919895, 3, 7),
  (920503, 5, 3),
  (921673, 2, 7),
  (924202, 4, 7),
  (925319, 3, 7),
  (925820, 3, 7),
  (926033, 6, 7),
  (927938, 5, 2),
  (928544, 3, 2),
  (929025, 7, 7),
  (931796, 5, 7),
  (933449, 3, 6),
  (935707, 6, 4),
  (935801, 0, 0),
  (935818, 0, 7),
  (936192, 5, 5),
  (938368, 1, 7),
  (940385, 4, 7),
  (941914, 6, 7),
  (944877, 4, 3),
  (945311, 7, 7),
  (952352, 5, 7),
  (956632, 2, 2),
  (956743, 6, 7),
  (960162, 1, 7),
  (960353, 6, 0),
  (961489, 4, 3),
  (962031, 4, 7),
  (962250, 2, 7),
  (967679, 1, 7),
  (967926, 3, 5),
  (968141, 4, 5),
  (970099, 3, 2),
  (983205, 1, 7),
  (983527, 1, 7),
  (984379, 1, 7),
  (986442, 7, 7),
  (988545, 5, 7),
  (994114, 2, 7),
  (994736, 0, 3),
  (995825, 2, 7),
  (995968, 0, 7),
  (998546, 5, 7),
  (1003350, 7, 7),
  (1004340, 3, 7),
  (1004689, 4, 7),
  (1005684, 6, 7),
  (1005930, 6, 7),
  (1007802, 3, 7),
  (1013018, 1, 7),
  (1017184, 3, 6),
  (1018232, 1, 3),
  (1018659, 4, 6),
  (1019840, 0, 7),
  (1028265, 4, 7),
  (1030511, 2, 7),
  (1031344, 6, 0),
  (1031610, 3, 7),
  (1032079, 4, 2),
  (1034715, 5, 7),
  (1036322, 2, 3),
  (1037279, 0, 7),
  (1037357, 2, 2),
  (1038087, 1, 7),
  (1043436, 0, 7),
  (1045205, 5, 5),
  (1045634, 6, 7),
  (1049718, 0, 4),
  (1051766, 4, 7),
  (1052774, 2, 7),
  (1055137, 0, 7),
  (1057003, 1, 7),
  (1062385, 7, 3),
  (1062811, 7, 7),
  (1067000, 3, 3),
  (1067794, 7, 0),
  (1070176, 2, 7),
  (1071286, 7, 7),
  (1072947, 4, 6),
  (1075558, 3, 7),
  (1075816, 1, 7),
  (1077239, 7, 7),
  (1078192, 5, 7),
  (1081408, 1, 0),
  (1086345, 3, 7),
  (1086875, 2, 7),
  (1087045, 4, 7),
  (1088523, 4, 1),
  (1089256, 7, 3),
  (1090407, 4, 7),
  (1095192, 1, 7),
  (1097033, 2, 2),
  (1098066, 2, 7),
  (1101155, 3, 3),
  (1101583, 0, 7),
  (1101933, 6, 7),
  (1117674, 1, 7),
  (1117986, 7, 0),
  (1120799, 0, 3),
  (1122733, 0, 7),
  (1123234, 4, 3),
  (1127772, 3, 7),
  (1127927, 5, 7),
  (1132143, 7, 2),
  (1133030, 7, 0),
  (1140257, 2, 7),
  (1140694, 0, 7),
  (1143575, 2, 7),
  (1145253, 2, 7),
  (1145271, 0, 0),
  (1145664, 6, 0),
  (1146859, 1, 5),
  (1147101, 4, 6),
  (1151763, 3, 7),
  (1153923, 2, 7),
  (1155640, 7, 3),
  (1157834, 2, 7),
  (1158713, 4, 7),
  (1164524, 6, 7),
  (1165058, 6, 4),
  (1166225, 7, 4),
  (1167788, 2, 7),
  (1168660, 5, 5),
  (1169559, 5, 7),
  (1171600, 5, 2),
  (1171872, 6, 7),
  (1172985, 1, 4),
  (1175857, 2, 7),
  (1176934, 6, 7),
  (1177440, 0, 4),
  (1178136, 6, 6),
  (1179154, 4, 7),
  (1181588, 7, 7),
  (1181930, 5, 2),
  (1187982, 6, 7),
  (1188764, 6, 7),
  (1189943, 1, 7),
  (1191153, 1, 0),
  (1191298, 3, 7),
  (1191992, 1, 7),
  (1192750, 3, 4),
  (1195272, 7, 7),
  (1196536, 3, 2),
  (1201282, 3, 3),
  (1203132, 7, 4),
  (1205018, 7, 7),
  (1205452, 6, 7),
  (1207135, 6, 7),
  (1207601, 3, 7),
  (1210068, 3, 7),
  (1210919, 7, 0),
  (1212678, 0, 4),
  (1213252, 1, 7),
  (1214825, 2, 7),
  (1217267, 4, 7),
  (1219197, 0, 7),
  (1224799, 4, 3),
  (1225131, 5, 2),
  (1227020, 3, 3),
  (1227566, 1, 7),
  (1228324, 3, 7),
  (1233564, 3, 7),
  (1234854, 7, 6),
  (1240823, 3, 7),
  (1240866, 4, 7),
  (1244270, 7, 4),
  (1244453, 4, 7),
  (1246476, 7, 3),
  (1249825, 6, 6),
  (1251797, 6, 6),
  (1252225, 0, 3),
  (1254286, 0, 6),
  (1256619, 7, 7),
  (1256673, 0, 0),
  (1257535, 4, 2),
  (1262281, 5, 5),
  (1262787, 6, 7),
  (1263991, 0, 0),
  (1269630, 7, 3),
  (1272832, 7, 7),
  (1273490, 7, 4),
  (1275431, 0, 7),
  (1279177, 4, 7),
  (1282455, 5, 6),
  (1282984, 7, 7),
  (1283287, 5, 3),
  (1284930, 5, 7),
  (1285481, 5, 7),
  (1285870, 7, 7),
  (1287128, 2, 4),
  (1289722, 4, 5),
  (1292332, 7, 0),
  (1300851, 7, 0),
  (1306444, 4, 7),
  (1309600, 2, 7),
  (1309818, 4, 7),
  (1310044, 4, 6),
  (1314309, 3, 7),
  (1314576, 7, 0),
  (1315985, 2, 3),
  (1316801, 2, 7),
  (1322338, 2, 7),
  (1322895, 3, 7),
  (1323871, 7, 7),
  (1326197, 2, 7),
  (1326792, 2, 7),
  (1327408, 1, 7),
  (1329843, 0, 4),
  (1331025, 5, 7),
  (1335231, 2, 4),
  (1336674, 0, 3),
  (1342116, 7, 7),
  (1344495, 0, 4),
  (1347642, 7, 4),
  (1347646, 4, 7),
  (1348080, 2, 0),
  (1350750, 3, 7),
  (1351036, 3, 7),
  (1352530, 6, 0),
  (1353031, 6, 7),
  (1354330, 7, 6),
  (1360982, 7, 4),
  (1367278, 7, 6),
  (1370115, 0, 6),
  (1371406, 3, 7),
  (1378501, 1, 7),
  (1379580, 6, 7),
  (1383006, 0, 7),
  (1383016, 7, 7),
  (1383247, 3, 5),
  (1385437, 2, 6),
  (1387557, 4, 7),
  (1391205, 7, 7),
  (1391231, 1, 7),
  (1398543, 5, 5),
  (1399283, 6, 7),
  (1403687, 1, 0),
  (1406677, 6, 7),
  (1411732, 0, 3),
  (1418451, 2, 3),
  (1419015, 6, 7),
  (1420100, 0, 7),
  (1421007, 2, 7),
  (1421547, 6, 7),
  (1422658, 1, 6),
  (1424300, 0, 7),
  (1425786, 4, 7),
  (1426301, 0, 7),
  (1427358, 0, 7),
  (1428235, 5, 6),
  (1429043, 6, 7),
  (1433536, 5, 7),
  (1434565, 0, 7),
  (1434575, 7, 6),
  (1434731, 4, 7),
  (1434824, 1, 7),
  (1434835, 1, 7),
  (1435039, 2, 7),
  (1436416, 1, 4),
  (1438259, 6, 3),
  (1444693, 0, 2),
  (1445234, 1, 7),
  (1445354, 6, 7),
  (1446337, 2, 7),
  (1451549, 3, 7),
  (1453331, 3, 3),
  (1458032, 2, 7),
  (1458812, 6, 7),
  (1462268, 6, 5),
  (1463996, 0, 7),
  (1465188, 3, 5),
  (1468489, 3, 7),
  (1473499, 7, 0),
  (1473783, 0, 3),
  (1478452, 0, 3),
  (1479226, 5, 7),
  (1479575, 6, 7),
  (1481593, 1, 7),
  (1485371, 6, 7),
  (1486424, 0, 7),
  (1487525, 1, 7),
  (1489017, 6, 7),
  (1491037, 3, 7),
  (1495298, 0, 7),
  (1495591, 1, 7),
  (1496589, 2, 7),
  (1499057, 3, 2),
  (1499559, 1, 6),
  (1502660, 7, 7),
  (1502683, 5, 7),
  (1503857, 5, 7),
  (1505222, 2, 3),
  (1505328, 4, 7),
  (1506555, 3, 7),
  (1506970, 0, 4),
  (1507503, 5, 6),
  (1509817, 4, 2),
  (1509899, 0, 7),
  (1510892, 5, 7),
  (1511415, 6, 7),
  (1513215, 4, 3),
  (1513478, 6, 7),
  (1513564, 3, 4),
  (1515217, 3, 7),
  (1515274, 7, 0),
  (1515691, 0, 7),
  (1516941, 5, 7),
  (1518639, 7, 3),
  (1520664, 7, 0),
  (1522744, 6, 4),
  (1523056, 1, 0),
  (1524205, 6, 6),
  (1527221, 5, 7),
  (1528793, 2, 7),
  (1531693, 4, 7),
  (1531834, 4, 7),
  (1536708, 5, 7),
  (1538680, 3, 7),
  (1539362, 3, 7),
  (1541365, 6, 7),
  (1543236, 4, 7),
  (1543709, 4, 7),
  (1545322, 1, 5),
  (1546326, 7, 0),
  (1548311, 6, 5),
  (1550643, 6, 7),
  (1550752, 2, 3),
  (1551301, 7, 6),
  (1555123, 6, 7),
  (1557084, 7, 7),
  (1558202, 4, 7),
  (1559323, 2, 6),
  (1568572, 4, 7),
  (1568810, 4, 7),
  (1569688, 4, 1),
  (1569885, 7, 7),
  (1571412, 3, 3),
  (1571676, 3, 5),
  (1575030, 2, 2),
  (1576933, 6, 7),
  (1577810, 5, 6),
  (1579707, 6, 7),
  (1579906, 6, 7),
  (1586877, 6, 7),
  (1587059, 0, 7),
  (1592408, 1, 7),
  (1593551, 3, 7),
  (1595147, 0, 7),
  (1605340, 3, 7),
  (1606633, 4, 7),
  (1607121, 5, 7),
  (1610166, 7, 7),
  (1610853, 5, 7),
  (1611347, 6, 7),
  (1612254, 5, 7),
  (1614593, 2, 7),
  (1616328, 7, 0),
  (1619532, 4, 6),
  (1620218, 2, 7),
  (1620374, 6, 7),
  (1621251, 1, 2),
  (1625249, 7, 0),
  (1628830, 0, 5),
  (1630146, 5, 7),
  (1631041, 0, 7),
  (1633527, 3, 3),
  (1636573, 7, 7),
  (1637609, 5, 5),
  (1638493, 0, 7),
  (1639607, 6, 7),
  (1640598, 3, 7),
  (1640825, 1, 7),
  (1641180, 5, 5),
  (1641826, 6, 7),
  (1642367, 4, 7),
  (1642472, 0, 7),
  (1643832, 0, 6),
  (1643845, 4, 7),
  (1643995, 3, 7),
  (1651097, 5, 5),
  (1651489, 1, 4),
  (1653711, 1, 4),
  (1657988, 0, 7),
  (1659024, 6, 7),
  (1659988, 5, 7),
  (1660629, 5, 7),
  (1661216, 4, 7),
  (1662776, 1, 7),
  (1664317, 1, 7),
  (1664702, 5, 7),
  (1671455, 6, 7),
  (1672095, 1, 0),
  (1676889, 1, 7),
  (1679035, 2, 7),
  (1686500, 6, 0),
  (1689180, 0, 0),
  (1689767, 3, 2),
  (1690379, 1, 6),
  (1691269, 6, 7),
  (1694732, 1, 4),
  (1695873, 5, 7),
  (1701249, 5, 3),
  (1704540, 1, 7),
  (1705822, 1, 7),
  (1707016, 0, 7),
  (1708001, 6, 7),
  (1714147, 2, 7),
  (1715343, 3, 7),
  (1720915, 7, 7),
  (1721101, 2, 7),
  (1721581, 1, 6),
  (1722434, 0, 7),
  (1722528, 0, 7),
  (1724406, 7, 3),
  (1724775, 0, 7),
  (1726721, 7, 7),
  (1727892, 0, 3),
  (1729004, 4, 3),
  (1730696, 2, 7),
  (1731508, 5, 2),
  (1732641, 0, 7),
  (1737594, 1, 7),
  (1739007, 4, 6),
  (1740311, 4, 7),
  (1741837, 7, 7),
  (1741988, 4, 6),
  (1742788, 0, 0),
  (1746887, 6, 7),
  (1747405, 3, 6),
  (1748558, 7, 7),
  (1748660, 6, 0),
  (1750586, 7, 7),
  (1751348, 6, 7),
  (1757595, 5, 7),
  (1762659, 5, 7),
  (1764369, 3, 7),
  (1767860, 1, 0),
  (1771094, 5, 7),
  (1771726, 1, 7),
  (1773262, 5, 6),
  (1774014, 1, 0),
  (1779055, 3, 6),
  (1779210, 2, 7),
  (1779665, 6, 7),
  (1780488, 1, 0),
  (1780533, 6, 7),
  (1782984, 1, 7),
  (1783862, 5, 2),
  (1783905, 4, 5),
  (1784122, 2, 7),
  (1789664, 5, 3),
  (1793309, 3, 7),
  (1795766, 6, 6),
  (1797315, 0, 7),
  (1800584, 5, 7),
  (1801345, 7, 0),
  (1811678, 1, 7),
  (1812878, 0, 3),
  (1812948, 6, 7),
  (1815745, 4, 6),
  (1818137, 6, 0),
  (1822863, 7, 7),
  (1822938, 5, 7),
  (1824984, 0, 7),
  (1825619, 6, 0),
  (1826417, 4, 7),
  (1829340, 2, 7),
  (1832953, 3, 2),
  (1833956, 0, 7),
  (1835094, 2, 7),
  (1836447, 3, 2),
  (1838649, 7, 7),
  (1841883, 2, 3),
  (1843500, 0, 7),
  (1844432, 6, 7),
  (1846367, 4, 7),
  (1848051, 0, 7),
  (1850550, 6, 6),
  (1851019, 2, 2),
  (1854584, 2, 7),
  (1858050, 7, 4),
  (1859041, 6, 5),
  (1864355, 6, 6),
  (1865404, 1, 0),
  (1866263, 1, 4),
  (1866426, 2, 7),
  (1867032, 2, 7),
  (1869262, 0, 7),
  (1875217, 6, 7),
  (1877367, 1, 0),
  (1885531, 4, 7),
  (1885993, 4, 2),
  (1887169, 1, 7),
  (1890356, 3, 7),
  (1893541, 0, 7),
  (1895119, 1, 7),
  (1895612, 7, 3),
  (1896127, 5, 6),
  (1898618, 3, 3),
  (1899324, 3, 7),
  (1900112, 7, 7),
  (1902186, 5, 7),
  (1903987, 4, 7),
  (1904449, 2, 7),
  (1908470, 1, 3),
  (1909367, 5, 6),
  (1910693, 2, 5),
  (1911226, 7, 7),
  (1913542, 3, 5),
  (1916998, 6, 3),
  (1917648, 2, 7),
  (1918830, 1, 2),
  (1921341, 5, 6),
  (1923165, 0, 7),
  (1925414, 3, 2),
  (1928619, 2, 7),
  (1934436, 7, 3),
  (1935332, 2, 6),
  (1941062, 5, 2),
  (1942208, 5, 7),
  (1946485, 1, 7),
  (1948222, 2, 3),
  (1949979, 6, 7),
  (1950640, 1, 0),
  (1955511, 5, 2),
  (1956937, 6, 4),
  (1957252, 7, 3),
  (1958328, 6, 7),
  (1958569, 6, 7),
  (1959100, 3, 7),
  (1960294, 5, 7),
  (1967636, 2, 7),
  (1970508, 4, 7),
  (1971212, 0, 0),
  (1973647, 3, 2),
  (1977728, 4, 7),
  (1978848, 3, 7),
  (1979285, 4, 7),
  (1980628, 7, 7),
  (1982432, 4, 6),
  (1987301, 6, 7),
  (1990154, 0, 0),
  (1990336, 3, 7),
  (1990934, 7, 7),
  (1991413, 2, 3),
  (1991642, 1, 7),
  (1992008, 2, 7),
  (1994233, 5, 2),
  (1995476, 3, 7),
  (1995851, 5, 7),
  (1998359, 4, 6),
  (2000801, 3, 3),
  (2001724, 1, 2),
  (2004843, 7, 5),
  (2004867, 1, 7),
  (2008898, 3, 5),
  (2009647, 7, 7),
  (2010106, 1, 6),
  (2010551, 4, 7),
  (2011490, 6, 5),
  (2012055, 1, 4),
  (2012845, 4, 6),
  (2014655, 6, 0),
  (2015467, 5, 7),
  (2015703, 2, 2),
  (2016940, 6, 3),
  (2017899, 0, 6),
  (2019110, 3, 5),
  (2024873, 4, 1),
  (2025659, 0, 7),
  (2026475, 0, 7),
  (2027339, 0, 7),
  (2027966, 6, 0),
  (2028340, 4, 7),
  (2029568, 3, 7),
  (2031813, 2, 7),
  (2032808, 4, 7),
  (2033182, 4, 7),
  (2035720, 4, 7),
  (2038885, 0, 3),
  (2040212, 2, 5),
  (2040285, 6, 7),
  (2041835, 2, 6),
  (2042820, 3, 7),
  (2043592, 4, 3),
  (2045791, 1, 6),
  (2046643, 0, 0),
  (2046911, 0, 7),
  (2051033, 1, 7),
  (2051634, 0, 7),
  (2052541, 0, 7),
  (2053031, 4, 7),
  (2053320, 5, 2),
  (2055808, 2, 7),
  (2056688, 7, 7),
  (2057132, 4, 1),
  (2057883, 4, 7),
  (2058000, 3, 7),
  (2061673, 3, 6),
  (2062323, 5, 7),
  (2063274, 0, 7),
  (2063672, 0, 4),
  (2065466, 0, 7),
  (2066203, 7, 3),
  (2069661, 4, 3),
  (2072496, 4, 2),
  (2078760, 0, 7),
  (2079633, 5, 5),
  (2081616, 6, 7),
  (2087785, 3, 7),
  (2087929, 6, 3),
  (2090703, 4, 7),
  (2094075, 0, 7),
  (2096098, 4, 7),
  (2098685, 4, 7),
  (2100148, 0, 0),
  (2100520, 5, 7),
  (2100673, 1, 0),
  (2102182, 6, 3),
  (2102845, 5, 7),
  (2103527, 3, 3),
  (2104614, 6, 6),
  (2105590, 7, 7),
  (2107786, 6, 7),
  (2108525, 1, 4),
  (2112221, 3, 3),
  (2112340, 0, 4),
  (2116244, 5, 7),
  (2117495, 7, 6),
  (2119416, 2, 6),
  (2122385, 4, 7),
  (2123693, 7, 7),
  (2124323, 0, 6),
  (2124897, 5, 7),
  (2126420, 1, 0),
  (2128578, 0, 7),
  (2129368, 2, 7),
  (2132153, 4, 3),
  (2132422, 3, 7),
  (2136680, 7, 7),
  (2140480, 4, 7),
  (2141179, 4, 7),
  (2144418, 7, 7),
  (2145527, 6, 3),
  (2151159, 5, 5),
  (2153042, 3, 7),
  (2154463, 4, 7),
  (2160417, 0, 6),
  (2162821, 6, 4),
  (2163831, 2, 2),
  (2163883, 0, 0),
  (2167799, 7, 0),
  (2169253, 5, 7),
  (2170040, 4, 7),
  (2172556, 6, 7),
  (2172765, 2, 3),
  (2174312, 0, 7),
  (2177865, 6, 7),
  (2180159, 6, 7),
  (2183418, 5, 7),
  (2185452, 4, 6),
  (2186033, 7, 3),
  (2188147, 5, 2),
  (2194098, 7, 4),
  (2195132, 0, 7),
  (2198818, 6, 4),
  (2200460, 1, 7),
  (2207661, 4, 5),
  (2209079, 4, 7),
  (2212354, 3, 3),
  (2212843, 0, 7),
  (2214641, 2, 3),
  (2216937, 6, 0),
  (2217962, 2, 5),
  (2219512, 4, 6),
  (2219798, 7, 5),
  (2219940, 0, 7),
  (2221043, 2, 7),
  (2226007, 0, 7),
  (2234168, 7, 7),
  (2238264, 4, 2),
  (2240915, 3, 5),
  (2244666, 1, 7),
  (2247804, 7, 7),
  (2251492, 2, 2),
  (2253724, 6, 4),
  (2260071, 3, 2),
  (2260695, 2, 7),
  (2261690, 3, 2),
  (2264713, 4, 5),
  (2265080, 7, 0),
  (2270527, 7, 7),
  (2270765, 6, 7),
  (2270974, 5, 7),
  (2271529, 6, 7),
  (2272884, 2, 7),
  (2273965, 3, 3),
  (2274534, 2, 7),
  (2275324, 1, 4),
  (2275631, 7, 6),
  (2275678, 4, 7),
  (2276466, 7, 7),
  (2278186, 3, 2),
  (2278250, 7, 7),
  (2278689, 5, 7),
  (2283819, 5, 7),
  (2285025, 0, 7),
  (2285761, 5, 7),
  (2291200, 5, 7),
  (2292068, 7, 7),
  (2295550, 4, 7),
  (2296406, 4, 7),
  (2297285, 7, 4),
  (2297313, 1, 7),
  (2298397, 1, 6),
  (2299549, 1, 7),
  (2300705, 6, 3),
  (2301937, 2, 7),
  (2304427, 5, 1),
  (2306777, 4, 7),
  (2308327, 7, 5),
  (2309160, 7, 2),
  (2312141, 2, 1),
  (2314516, 1, 7),
  (2315720, 7, 7),
  (2316566, 3, 2),
  (2325170, 6, 4),
  (2327201, 3, 7),
  (2329389, 5, 7),
  (2330685, 3, 7),
  (2333252, 5, 7),
  (2337859, 1, 7),
  (2339650, 0, 4),
  (2342183, 0, 3),
  (2342835, 3, 7),
  (2346950, 2, 7),
  (2348569, 7, 3),
  (2352032, 6, 4),
  (2352459, 1, 7),
  (2352979, 5, 2),
  (2353362, 3, 7),
  (2355419, 4, 7),
  (2356983, 7, 7),
  (2360051, 0, 0),
  (2360136, 3, 7),
  (2362819, 3, 7),
  (2363141, 5, 7),
  (2367885, 1, 7),
  (2368411, 4, 7),
  (2369124, 2, 6),
  (2369506, 6, 7),
  (2371327, 1, 7),
  (2371650, 1, 4),
  (2371755, 5, 7),
  (2372769, 1, 7),
  (2376428, 3, 6),
  (2377059, 1, 4),
  (2380259, 5, 6),
  (2382581, 3, 7),
  (2383313, 6, 7),
  (2384719, 2, 7),
  (2385536, 4, 3),
  (2386142, 5, 7),
  (2387048, 0, 7),
  (2387239, 3, 7),
  (2387369, 0, 7),
  (2391951, 7, 6),
  (2394373, 0, 7),
  (2394999, 7, 0),
  (2404126, 3, 5),
  (2405061, 1, 7),
  (2407127, 2, 3),
  (2410745, 1, 0),
  (2412360, 4, 7),
  (2414275, 3, 5),
  (2416816, 0, 6),
  (2420960, 7, 4),
  (2421337, 4, 7),
  (2425430, 5, 3),
  (2428822, 2, 1),
  (2428858, 1, 3),
  (2430732, 5, 7),
  (2431608, 1, 3),
  (2432429, 7, 5),
  (2433382, 6, 6),
  (2433621, 3, 3),
  (2433669, 4, 0),
  (2433828, 0, 4),
  (2435510, 0, 7),
  (2441317, 1, 7),
  (2449247, 7, 3),
  (2450762, 7, 7),
  (2455272, 6, 7),
  (2455956, 6, 6),
  (2456769, 0, 7),
  (2458924, 2, 7),
  (2458953, 0, 7),
  (2460925, 6, 7),
  (2463289, 1, 0),
  (2463694, 4, 7),
  (2466337, 3, 6),
  (2471423, 5, 7),
  (2471941, 1, 0),
  (2472523, 6, 7),
  (2475595, 1, 7),
  (2478941, 7, 4),
  (2479853, 0, 7),
  (2480003, 6, 6),
  (2480051, 1, 3),
  (2480118, 5, 3),
  (2480838, 4, 7),
  (2485303, 0, 7),
  (2487073, 7, 0),
  (2495268, 6, 7),
  (2496723, 3, 7),
  (2497452, 4, 3),
  (2500132, 5, 7),
  (2504972, 6, 7),
  (2510995, 3, 6),
  (2514702, 4, 7),
  (2514822, 4, 3),
  (2515075, 1, 0),
  (2516259, 2, 2),
  (2518208, 7, 7),
  (2518578, 5, 7),
  (2518693, 3, 6),
  (2519266, 5, 3),
  (2520559, 4, 7),
  (2521077, 0, 7),
  (2521235, 6, 7),
  (2522269, 7, 7),
  (2525405, 7, 7),
  (2525865, 3, 7),
  (2526497, 2, 7),
  (2527475, 6, 2),
  (2529825, 2, 7),
  (2533394, 2, 7),
  (2534293, 0, 7),
  (2537484, 0, 7),
  (2538494, 0, 7),
  (2539980, 6, 7),
  (2540079, 2, 7),
  (2546318, 4, 2),
  (2547335, 5, 6),
  (2554940, 3, 6),
  (2555097, 4, 3),
  (2555939, 7, 7),
  (2556292, 7, 7),
  (2560113, 7, 4),
  (2560463, 1, 7),
  (2562587, 6, 6),
  (2564174, 4, 7),
  (2566572, 0, 6),
  (2567875, 6, 7),
  (2569022, 4, 7),
  (2570016, 2, 7),
  (2576100, 6, 0),
  (2577889, 1, 3),
  (2578849, 6, 7),
  (2579375, 6, 7),
  (2580008, 0, 0),
  (2580783, 4, 7),
  (2584088, 7, 4),
  (2584557, 1, 0),
  (2586050, 4, 2),
  (2587735, 0, 4),
  (2587808, 6, 7),
  (2588287, 2, 3),
  (2589487, 4, 6),
  (2593350, 7, 3),
  (2596067, 3, 7),
  (2596143, 4, 7),
  (2596820, 5, 7),
  (2596933, 5, 7),
  (2598227, 1, 3),
  (2603103, 5, 3),
  (2607103, 5, 7),
  (2608013, 0, 7),
  (2615547, 1, 7),
  (2615964, 5, 7),
  (2619412, 5, 5),
  (2620275, 4, 7),
  (2620624, 0, 7),
  (2622212, 6, 7),
  (2623115, 1, 7),
  (2624053, 0, 7),
  (2626501, 6, 7),
  (2627332, 3, 7),
  (2628094, 6, 3),
  (2631500, 1, 7),
  (2640175, 4, 6),
  (2640245, 6, 6),
  (2640435, 5, 7),
  (2641234, 0, 7),
  (2641804, 1, 6),
  (2647234, 6, 0),
  (2648373, 6, 7),
  (2649117, 7, 0),
  (2651213, 7, 7),
  (2653402, 2, 7),
  (2655055, 3, 7),
  (2655670, 1, 7),
  (2656148, 7, 3),
  (2656344, 0, 6),
  (2656708, 6, 4),
  (2659592, 2, 7),
  (2659972, 4, 3),
  (2661217, 6, 7),
  (2664796, 1, 7),
  (2665355, 1, 0),
  (2668222, 2, 7),
  (2668576, 4, 3),
  (2675365, 5, 7),
  (2676215, 2, 2),
  (2684229, 4, 7),
  (2685600, 7, 7),
  (2689417, 6, 4),
  (2690475, 0, 7),
  (2700403, 4, 7),
  (2702195, 5, 7),
  (2704672, 6, 4),
  (2706892, 5, 7),
  (2709544, 2, 7),
  (2710070, 2, 2),
  (2710607, 5, 2),
  (2711543, 1, 7),
  (2714546, 5, 7),
  (2715664, 5, 7),
  (2715916, 5, 6),
  (2718892, 4, 7),
  (2721273, 1, 7),
  (2723156, 1, 7),
  (2723671, 6, 7),
  (2725563, 7, 7),
  (2726566, 0, 7),
  (2726977, 5, 7),
  (2728584, 6, 7),
  (2728801, 4, 6),
  (2731597, 4, 7),
  (2734061, 2, 7),
  (2737133, 2, 7),
  (2740194, 1, 7),
  (2743694, 1, 0),
  (2748512, 5, 2),
  (2749074, 6, 7),
  (2750142, 0, 3),
  (2753121, 1, 7),
  (2753786, 5, 3),
  (2757950, 0, 4),
  (2758988, 1, 7),
  (2759621, 6, 7),
  (2761787, 6, 0),
  (2763690, 3, 3),
  (2764139, 3, 5),
  (2766806, 4, 5),
  (2773484, 6, 3),
  (2776444, 2, 7),
  (2780340, 2, 7),
  (2784857, 6, 5),
  (2786541, 4, 7),
  (2789096, 5, 5),
  (2789649, 4, 7),
  (2792164, 3, 7),
  (2793185, 3, 7),
  (2795095, 6, 4),
  (2795499, 3, 7),
  (2799813, 4, 7),
  (2802178, 7, 7),
  (2802953, 4, 5),
  (2805741, 6, 7),
  (2809127, 6, 3),
  (2810256, 4, 5),
  (2810631, 5, 7),
  (2813616, 0, 3),
  (2814047, 6, 7),
  (2818410, 2, 7),
  (2818563, 2, 7),
  (2819350, 1, 7),
  (2820061, 2, 7),
  (2820278, 7, 7),
  (2822481, 4, 7),
  (2823412, 0, 4),
  (2826501, 3, 7),
  (2826933, 4, 1),
  (2827240, 2, 2),
  (2827305, 2, 7),
  (2831057, 0, 0),
  (2833873, 2, 7),
  (2833964, 2, 7),
  (2834312, 6, 7),
  (2835004, 6, 4),
  (2840877, 5, 3),
  (2841732, 7, 3),
  (2845901, 4, 2),
  (2848485, 2, 3),
  (2849029, 7, 7),
  (2854140, 4, 3),
  (2854700, 3, 7),
  (2858644, 3, 6),
  (2860449, 4, 3),
  (2860531, 6, 7),
  (2860564, 2, 6),
  (2862323, 4, 3),
  (2862707, 4, 6),
  (2865925, 3, 7),
  (2866302, 5, 2),
  (2869471, 1, 3),
  (2871364, 5, 7),
  (2873265, 2, 3),
  (2875180, 4, 3),
  (2875890, 1, 0),
  (2876741, 1, 7),
  (2880626, 1, 7),
  (2884893, 2, 7),
  (2885272, 3, 7),
  (2886505, 3, 7),
  (2887314, 0, 7),
  (2890171, 4, 6),
  (2893025, 7, 7),
  (2894465, 1, 7),
  (2895693, 4, 7),
  (2900238, 2, 5),
  (2902547, 2, 7),
  (2904337, 7, 7),
  (2904700, 4, 7),
  (2904758, 0, 2),
  (2905121, 2, 5),
  (2912760, 5, 7),
  (2914065, 5, 2),
  (2914893, 4, 7),
  (2915890, 0, 7),
  (2920181, 7, 7),
  (2924283, 0, 7),
  (2926128, 2, 7),
  (2927820, 6, 6),
  (2933739, 5, 6),
  (2942499, 3, 3),
  (2944260, 0, 7),
  (2944609, 4, 7),
  (2946174, 3, 2),
  (2948683, 3, 7),
  (2950621, 5, 7),
  (2954173, 4, 7),
  (2956735, 0, 7),
  (2956864, 0, 7),
  (2958164, 6, 6),
  (2959283, 7, 7),
  (2960085, 6, 4),
  (2964702, 7, 7),
  (2965365, 4, 7),
  (2965619, 4, 7),
  (2970966, 3, 2),
  (2973677, 7, 7),
  (2976524, 7, 7),
  (2977389, 5, 3),
  (2978720, 4, 6),
  (2982381, 6, 7),
  (2986381, 3, 7),
  (2987376, 1, 6),
  (2992284, 4, 4),
  (2992378, 0, 7),
  (2993384, 2, 2),
  (2994008, 1, 4),
  (2996275, 5, 7),
  (3005421, 1, 0),
  (3007172, 7, 7),
  (3010827, 6, 7),
  (3011330, 3, 7),
  (3011585, 2, 7),
  (3014697, 3, 7),
  (3015908, 3, 7),
  (3019131, 7, 4),
  (3021471, 0, 0),
  (3023573, 0, 7),
  (3025343, 4, 7),
  (3025698, 0, 7),
  (3025730, 5, 7),
  (3027763, 4, 2),
  (3031839, 7, 7),
  (3033192, 5, 7),
  (3035547, 0, 7),
  (3035934, 2, 2),
  (3037792, 5, 7),
  (3038139, 4, 7),
  (3042130, 0, 7),
  (3042165, 0, 7),
  (3044432, 3, 5),
  (3049038, 7, 7),
  (3049167, 1, 7),
  (3049774, 6, 7),
  (3050142, 5, 3),
  (3050398, 4, 7),
  (3051129, 1, 4),
  (3053734, 7, 4),
  (3060575, 1, 7),
  (3061957, 0, 6),
  (3062138, 2, 7),
  (3066192, 0, 7),
  (3066694, 7, 7),
  (3066771, 5, 2),
  (3072450, 3, 7),
  (3074718, 6, 7),
  (3081306, 0, 7),
  (3083779, 5, 3),
  (3092956, 3, 7),
  (3095645, 4, 7),
  (3099509, 7, 7),
  (3099510, 4, 5),
  (3100692, 2, 7),
  (3100947, 2, 3),
  (3101832, 0, 7),
  (3107160, 2, 7),
  (3109303, 7, 7),
  (3109818, 2, 3),
  (3110027, 7, 7),
  (3110093, 1, 3),
  (3115793, 1, 7),
  (3117954, 5, 7),
  (3122168, 2, 7),
  (3122319, 6, 7),
  (3122852, 0, 2),
  (3124426, 2, 7),
  (3125732, 5, 7),
  (3126401, 1, 7),
  (3131162, 5, 3),
  (3132363, 2, 6),
  (3132829, 4, 7),
  (3133437, 0, 7),
  (3134409, 0, 0),
  (3135913, 1, 7),
  (3136261, 7, 7),
  (3137471, 2, 7),
  (3138938, 5, 3),
  (3141421, 0, 6),
  (3142603, 1, 7),
  (3143127, 7, 0),
  (3144260, 3, 7),
  (3145159, 7, 0),
  (3149630, 2, 7),
  (3153173, 5, 5),
  (3154041, 7, 5),
  (3158914, 1, 4),
  (3160700, 0, 7),
  (3162565, 7, 0),
  (3163204, 7, 7),
  (3171042, 0, 0),
  (3171547, 3, 2),
  (3171730, 7, 4),
  (3171851, 1, 7),
  (3176007, 4, 7),
  (3178134, 7, 7),
  (3179071, 2, 7),
  (3180937, 2, 7),
  (3182328, 2, 3),
  (3185456, 3, 7),
  (3186992, 2, 7),
  (3188763, 3, 2),
  (3189184, 7, 0),
  (3189964, 2, 7),
  (3196390, 5, 7),
  (3197440, 2, 6),
  (3198634, 5, 7),
  (3201951, 7, 7),
  (3203010, 4, 5),
  (3204545, 1, 7),
  (3205681, 3, 7),
  (3206294, 3, 7),
  (3209197, 6, 3),
  (3214838, 7, 7),
  (3216100, 6, 7),
  (3219345, 5, 3),
  (3220367, 3, 7),
  (3221280, 6, 3),
  (3221586, 3, 3),
  (3223013, 7, 7),
  (3225736, 2, 7),
  (3226458, 2, 7),
  (3226774, 7, 7),
  (3228365, 7, 7),
  (3231204, 7, 7),
  (3232359, 1, 7),
  (3233806, 5, 7),
  (3236362, 5, 5),
  (3237817, 1, 7),
  (3241338, 3, 7),
  (3242426, 5, 7),
  (3243928, 2, 2),
  (3245927, 1, 0),
  (3246980, 6, 7),
  (3247012, 5, 2),
  (3249130, 4, 7),
  (3252285, 4, 7),
  (3254788, 3, 7),
  (3255013, 4, 7),
  (3256142, 5, 7),
  (3260875, 5, 6),
  (3261037, 1, 3),
  (3265189, 6, 5),
  (3265405, 6, 7),
  (3267542, 1, 7),
  (3269759, 4, 2),
  (3270521, 2, 3),
  (3273882, 3, 2),
  (3275686, 5, 1),
  (3278527, 2, 7),
  (3281741, 5, 7),
  (3282615, 6, 0),
  (3285224, 6, 7),
  (3286890, 3, 7),
  (3287378, 5, 7),
  (3288189, 1, 0),
  (3290503, 2, 7),
  (3290510, 1, 0),
  (3294441, 0, 7),
  (3294635, 1, 7),
  (3298516, 3, 3),
  (3302710, 0, 7),
  (3304902, 2, 7),
  (3307897, 3, 7),
  (3313528, 7, 4),
  (3316524, 5, 7),
  (3317866, 6, 7),
  (3319067, 4, 7),
  (3322499, 5, 5),
  (3323949, 6, 0),
  (3324261, 2, 7),
  (3326073, 1, 4),
  (3326599, 1, 0),
  (3329271, 4, 3),
  (3330228, 1, 7),
  (3330437, 7, 7),
  (3335832, 5, 3),
  (3336335, 7, 7),
  (3336633, 4, 3),
  (3336940, 2, 7),
  (3338025, 5, 7),
  (3339210, 6, 7),
  (3350724, 7, 7),
  (3354043, 1, 7),
  (3357136, 5, 7),
  (3359403, 2, 7),
  (3359631, 6, 0),
  (3359770, 5, 7),
  (3361542, 6, 7),
  (3362234, 4, 6),
  (3362316, 7, 2),
  (3363723, 5, 7),
  (3363745, 6, 7),
  (3365594, 3, 7),
  (3365710, 3, 2),
  (3369205, 3, 2),
  (3369507, 4, 7),
  (3370715, 6, 6),
  (3379619, 6, 7),
  (3380474, 3, 7),
  (3383962, 2, 7),
  (3384046, 1, 3),
  (3387993, 0, 3),
  (3389425, 6, 0),
  (3389976, 4, 7),
  (3391408, 1, 7),
  (3392936, 3, 3),
  (3395905, 0, 0),
  (3397920, 4, 2),
  (3398207, 0, 7),
  (3403180, 5, 7),
  (3404454, 4, 5),
  (3407222, 2, 7),
  (3413014, 5, 6),
  (3416337, 0, 7),
  (3417557, 6, 4),
  (3418763, 1, 4),
  (3420924, 2, 7),
  (3421967, 1, 7),
  (3423585, 6, 4),
  (3423782, 6, 1),
  (3424146, 3, 7),
  (3429600, 3, 7),
  (3430458, 7, 7),
  (3433525, 4, 7),
  (3434443, 4, 7),
  (3434586, 6, 7),
  (3435701, 1, 3),
  (3435724, 1, 6),
  (3436467, 0, 0),
  (3436618, 6, 4),
  (3438616, 3, 5),
  (3438636, 4, 7),
  (3440746, 7, 6),
  (3440761, 2, 7),
  (3443622, 3, 7),
  (3444379, 7, 0),
  (3444544, 2, 7),
  (3444647, 7, 7),
  (3444675, 4, 3),
  (3446106, 5, 7),
  (3446962, 3, 2),
  (3447719, 2, 2),
  (3453026, 4, 2),
  (3457080, 3, 3),
  (3460084, 2, 4),
  (3467153, 7, 0),
  (3470719, 7, 4),
  (3471713, 5, 7),
  (3479047, 2, 6),
  (3480504, 7, 7),
  (3480560, 5, 7),
  (3485501, 5, 6),
  (3485752, 0, 0),
  (3486324, 3, 5),
  (3487970, 4, 5),
  (3489338, 0, 7),
  (3489974, 5, 3),
  (3491160, 7, 0),
  (3491464, 6, 6),
  (3491774, 7, 0),
  (3493950, 5, 6),
  (3494210, 5, 7),
  (3499823, 6, 4),
  (3502248, 0, 7),
  (3502286, 1, 7),
  (3505479, 4, 5),
  (3510515, 2, 7),
  (3511289, 4, 7),
  (3512658, 5, 7),
  (3513888, 1, 7),
  (3519218, 5, 7),
  (3519549, 2, 7),
  (3523681, 4, 7),
  (3524839, 6, 3),
  (3528609, 7, 7),
  (3532377, 6, 7),
  (3534046, 1, 1),
  (3534765, 5, 7),
  (3535317, 3, 7),
  (3538898, 1, 7),
  (3543165, 5, 5),
  (3546770, 1, 0),
  (3549170, 2, 7),
  (3552389, 0, 3),
  (3552578, 2, 7),
  (3555254, 2, 7),
  (3559810, 4, 1),
  (3561025, 0, 7),
  (3567390, 3, 7),
  (3569942, 4, 1),
  (3571190, 0, 7),
  (3574492, 0, 7),
  (3575927, 5, 7),
  (3577591, 6, 7),
  (3579262, 3, 7),
  (3582805, 6, 5),
  (3583366, 1, 7),
  (3585167, 6, 7),
  (3586535, 6, 7),
  (3589561, 3, 6),
  (3590466, 2, 2),
  (3595068, 7, 7),
  (3595208, 4, 3),
  (3595213, 7, 7),
  (3595223, 3, 7),
  (3597714, 6, 3),
  (3598716, 5, 7),
  (3599394, 3, 7),
])