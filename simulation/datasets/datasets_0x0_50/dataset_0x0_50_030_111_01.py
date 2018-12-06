from src.util import *
schedule = deque([
  (2512, 0, 0),
  (3595, 1, 2),
  (4753, 3, 0),
  (5823, 0, 0),
  (9462, 3, 1),
  (11751, 2, 1),
  (11902, 3, 0),
  (15623, 1, 2),
  (15974, 1, 2),
  (16312, 1, 1),
  (20733, 2, 0),
  (21088, 3, 0),
  (21652, 0, 1),
  (22098, 3, 2),
  (22438, 2, 1),
  (22975, 2, 2),
  (23348, 3, 2),
  (24464, 1, 0),
  (26640, 3, 1),
  (27660, 0, 2),
  (28597, 0, 0),
  (29295, 2, 1),
  (32385, 2, 1),
  (34253, 3, 1),
  (36553, 0, 0),
  (37086, 0, 2),
  (37110, 1, 0),
  (39087, 0, 0),
  (39441, 2, 0),
  (42565, 3, 2),
  (44269, 3, 1),
  (46097, 2, 2),
  (48707, 2, 2),
  (51655, 2, 0),
  (52517, 2, 1),
  (59276, 0, 1),
  (60277, 3, 0),
  (61329, 2, 2),
  (62003, 0, 1),
  (63976, 1, 2),
  (64417, 1, 0),
  (64533, 0, 2),
  (65219, 3, 2),
  (66102, 0, 1),
  (69165, 2, 0),
  (69324, 1, 2),
  (70447, 0, 1),
  (75541, 0, 2),
  (77733, 1, 2),
  (79582, 3, 2),
  (82970, 2, 2),
  (83755, 2, 0),
  (85991, 0, 2),
  (88850, 3, 1),
  (89860, 1, 1),
  (90246, 1, 1),
  (95969, 0, 1),
  (97224, 3, 1),
  (98997, 1, 0),
  (99229, 2, 0),
  (102867, 2, 2),
  (103170, 2, 2),
  (103774, 2, 0),
  (106267, 2, 0),
  (108769, 0, 1),
  (115384, 2, 2),
  (117717, 0, 2),
  (118365, 2, 1),
  (121296, 1, 0),
  (121298, 0, 2),
  (121688, 3, 1),
  (121823, 0, 2),
  (122604, 3, 0),
  (123570, 0, 1),
  (123588, 0, 0),
  (124274, 3, 2),
  (127200, 1, 0),
  (131118, 0, 1),
  (134699, 2, 1),
  (137921, 3, 0),
  (144345, 0, 2),
  (146028, 1, 2),
  (146890, 1, 1),
  (146909, 1, 1),
  (150728, 0, 1),
  (155033, 2, 2),
  (156817, 2, 2),
  (159400, 1, 2),
  (159954, 3, 1),
  (162329, 0, 0),
  (163174, 3, 0),
  (165996, 3, 0),
  (168452, 3, 2),
  (172234, 1, 1),
  (173263, 1, 2),
  (173354, 3, 2),
  (185434, 1, 1),
  (186058, 3, 2),
  (186426, 2, 1),
  (186609, 0, 0),
  (186718, 2, 0),
  (189803, 2, 1),
  (192488, 3, 1),
  (193997, 0, 2),
  (195849, 0, 0),
  (195972, 2, 1),
  (198476, 0, 1),
  (202367, 3, 1),
  (203582, 2, 0),
  (206181, 1, 2),
  (207392, 3, 1),
  (209816, 1, 2),
  (209994, 0, 0),
  (211779, 1, 2),
  (213950, 1, 1),
  (215990, 2, 0),
  (220293, 2, 1),
  (221022, 3, 2),
  (223818, 2, 2),
  (225515, 0, 1),
  (226584, 3, 1),
  (229621, 2, 0),
  (230436, 1, 2),
  (232354, 1, 0),
  (234446, 3, 0),
  (234624, 2, 2),
  (234989, 0, 0),
  (238857, 2, 2),
  (239708, 2, 2),
  (242033, 2, 2),
  (242619, 1, 0),
  (247283, 0, 2),
  (247323, 3, 0),
  (253382, 2, 0),
  (254094, 2, 2),
  (254621, 2, 2),
  (254901, 2, 2),
  (265192, 3, 1),
  (266145, 0, 0),
  (269892, 2, 1),
  (270879, 3, 2),
  (274510, 0, 0),
  (275680, 0, 2),
  (281790, 0, 1),
  (283222, 2, 0),
  (287340, 0, 0),
  (292726, 2, 0),
  (298383, 3, 1),
  (298845, 1, 0),
  (299537, 3, 0),
  (300291, 2, 0),
  (300358, 1, 1),
  (304468, 3, 2),
  (310017, 3, 2),
  (313010, 0, 1),
  (316734, 3, 0),
  (318520, 2, 0),
  (320430, 0, 0),
  (320508, 3, 2),
  (323667, 2, 1),
  (325001, 0, 2),
  (325734, 3, 0),
  (327961, 0, 1),
  (330368, 2, 2),
  (333890, 3, 2),
  (333930, 0, 1),
  (336935, 0, 2),
  (337036, 3, 1),
  (343903, 0, 1),
  (346352, 2, 0),
  (346787, 0, 0),
  (348245, 1, 1),
  (349309, 2, 1),
  (349680, 2, 0),
  (354284, 2, 1),
  (362895, 1, 2),
  (365513, 3, 2),
  (365927, 0, 0),
  (368062, 3, 2),
  (376246, 0, 0),
  (377568, 2, 1),
  (378093, 3, 1),
  (383480, 0, 1),
  (386582, 3, 2),
  (387537, 2, 1),
  (393669, 1, 1),
  (394935, 2, 0),
  (396604, 3, 2),
  (397645, 2, 1),
  (397829, 2, 2),
  (397830, 2, 1),
  (399294, 0, 2),
  (401032, 1, 0),
  (402397, 2, 1),
  (404738, 0, 2),
  (406111, 0, 2),
  (408663, 3, 2),
  (411537, 2, 2),
  (415181, 3, 2),
  (415500, 2, 2),
  (417038, 3, 1),
  (418381, 2, 0),
  (419062, 1, 0),
  (421919, 3, 1),
  (424864, 3, 2),
  (427322, 1, 1),
  (428128, 0, 1),
  (428464, 1, 0),
  (428895, 2, 0),
  (431399, 0, 1),
  (433705, 3, 0),
  (434865, 3, 0),
  (436953, 0, 1),
  (437190, 2, 0),
  (437955, 3, 2),
  (440266, 0, 0),
  (444108, 2, 2),
  (450400, 1, 2),
  (453991, 3, 0),
  (454273, 1, 2),
  (455449, 0, 1),
  (460104, 2, 1),
  (462580, 0, 0),
  (465614, 1, 2),
  (471153, 1, 1),
  (471375, 0, 2),
  (473101, 0, 1),
  (474360, 3, 2),
  (479371, 1, 0),
  (480208, 3, 0),
  (483551, 0, 0),
  (484411, 1, 2),
  (487900, 0, 1),
  (492556, 3, 2),
  (493250, 0, 2),
  (495635, 0, 1),
  (498996, 0, 1),
  (499933, 1, 1),
  (500023, 0, 1),
  (501579, 3, 2),
  (503896, 2, 2),
  (504492, 1, 0),
  (505695, 3, 1),
  (510346, 1, 1),
  (511610, 3, 2),
  (516220, 3, 1),
  (517357, 1, 2),
  (518967, 1, 2),
  (519369, 3, 1),
  (519808, 0, 2),
  (520564, 2, 0),
  (521569, 3, 0),
  (521894, 2, 1),
  (523474, 0, 0),
  (525347, 1, 2),
  (532278, 1, 0),
  (532596, 0, 1),
  (532735, 3, 1),
  (535143, 1, 1),
  (543049, 0, 2),
  (544139, 2, 2),
  (546143, 1, 1),
  (546397, 1, 2),
  (548649, 2, 1),
  (549784, 2, 2),
  (554842, 3, 2),
  (556123, 1, 2),
  (557235, 1, 1),
  (557821, 3, 1),
  (557976, 2, 0),
  (562060, 0, 1),
  (562806, 2, 1),
  (562909, 2, 2),
  (564074, 1, 1),
  (564692, 3, 0),
  (565062, 0, 0),
  (567137, 1, 2),
  (568885, 2, 0),
  (569331, 1, 2),
  (571554, 2, 1),
  (572598, 3, 1),
  (573969, 0, 1),
  (574252, 1, 0),
  (575504, 3, 1),
  (582437, 1, 1),
  (588411, 3, 1),
  (589833, 0, 1),
  (590688, 1, 2),
  (592747, 1, 0),
  (593018, 0, 2),
  (595814, 3, 2),
  (597189, 1, 2),
  (598001, 0, 0),
  (599720, 0, 1),
  (603439, 0, 2),
  (606999, 3, 2),
  (609338, 3, 2),
  (611518, 0, 1),
  (619584, 0, 0),
  (620342, 1, 0),
  (620671, 1, 1),
  (625000, 3, 1),
  (626236, 3, 0),
  (634703, 3, 0),
  (635203, 1, 0),
  (639042, 2, 2),
  (643072, 0, 0),
  (643369, 1, 0),
  (647493, 2, 0),
  (651033, 3, 0),
  (652256, 3, 1),
  (652455, 0, 2),
  (656327, 1, 1),
  (662324, 1, 1),
  (663798, 0, 2),
  (665241, 3, 0),
  (666285, 2, 0),
  (666330, 3, 1),
  (666511, 0, 2),
  (668992, 3, 0),
  (670641, 3, 2),
  (670879, 1, 0),
  (673081, 0, 0),
  (673151, 0, 1),
  (675010, 1, 2),
  (676767, 0, 1),
  (677007, 1, 0),
  (678657, 1, 1),
  (678824, 0, 2),
  (679991, 3, 1),
  (680380, 0, 1),
  (682790, 2, 1),
  (685301, 0, 0),
  (690504, 0, 0),
  (691429, 2, 1),
  (693197, 2, 2),
  (696249, 3, 2),
  (696832, 3, 0),
  (696840, 2, 1),
  (697927, 1, 1),
  (701592, 2, 2),
  (701880, 0, 0),
  (703877, 0, 1),
  (704925, 2, 2),
  (707600, 1, 1),
  (708191, 1, 1),
  (708748, 2, 1),
  (710492, 3, 0),
  (712563, 2, 1),
  (715561, 1, 2),
  (716110, 1, 0),
  (718194, 1, 0),
  (724404, 1, 1),
  (725553, 3, 2),
  (730520, 3, 0),
  (731469, 1, 2),
  (734930, 1, 1),
  (736391, 3, 1),
  (736787, 3, 1),
  (741207, 3, 0),
  (741544, 2, 0),
  (744684, 2, 2),
  (745373, 3, 2),
  (745695, 0, 2),
  (750469, 3, 1),
  (751602, 2, 0),
  (751672, 2, 2),
  (752551, 1, 2),
  (753711, 2, 0),
  (758513, 3, 2),
  (759265, 3, 2),
  (760011, 3, 0),
  (760074, 2, 1),
  (761500, 1, 2),
  (762262, 1, 1),
  (762304, 3, 0),
  (765387, 3, 1),
  (766665, 2, 0),
  (771093, 1, 2),
  (771124, 1, 2),
  (772516, 2, 2),
  (774711, 1, 2),
  (775091, 2, 2),
  (779994, 0, 1),
  (780336, 3, 1),
  (782210, 1, 0),
  (782511, 0, 1),
  (783680, 2, 1),
  (783884, 1, 0),
  (783916, 2, 0),
  (787495, 2, 1),
  (788549, 2, 0),
  (790970, 0, 2),
  (792819, 1, 0),
  (796198, 0, 2),
  (798877, 1, 1),
  (799236, 3, 2),
  (800294, 0, 2),
  (800981, 3, 0),
  (802031, 1, 0),
  (802789, 3, 0),
  (803413, 0, 1),
  (804150, 3, 2),
  (806344, 3, 1),
  (807065, 1, 1),
  (808853, 1, 2),
  (809074, 2, 1),
  (809996, 3, 1),
  (810224, 1, 1),
  (811854, 3, 0),
  (812861, 3, 0),
  (814556, 0, 0),
  (815939, 0, 2),
  (826686, 0, 2),
  (832605, 3, 0),
  (838509, 1, 0),
  (840846, 2, 2),
  (843502, 0, 1),
  (846798, 3, 0),
  (855058, 0, 2),
  (858423, 3, 2),
  (862374, 3, 2),
  (862973, 0, 1),
  (865970, 2, 2),
  (868783, 3, 1),
  (869155, 0, 0),
  (870514, 3, 0),
  (871687, 0, 2),
  (877310, 3, 1),
  (880808, 0, 2),
  (881138, 1, 0),
  (882161, 3, 2),
  (882301, 3, 0),
  (882453, 1, 0),
  (882990, 1, 2),
  (885094, 0, 1),
  (885173, 1, 1),
  (885241, 1, 2),
  (886269, 2, 0),
  (888526, 0, 2),
  (891053, 2, 1),
  (893956, 0, 0),
  (895123, 2, 1),
  (895672, 2, 2),
  (896268, 2, 0),
  (896604, 3, 0),
  (896849, 1, 0),
  (898590, 2, 1),
  (901561, 3, 2),
  (902067, 0, 2),
  (904987, 3, 0),
  (906839, 0, 0),
  (908836, 3, 0),
  (909246, 0, 0),
  (911730, 3, 0),
  (920019, 0, 0),
  (922012, 1, 1),
  (923129, 3, 1),
  (924067, 1, 0),
  (926855, 2, 2),
  (927618, 0, 2),
  (928348, 2, 0),
  (930249, 0, 0),
  (930828, 0, 2),
  (932486, 2, 0),
  (938127, 3, 0),
  (943649, 2, 2),
  (944209, 3, 2),
  (946332, 0, 0),
  (947042, 3, 1),
  (948649, 0, 0),
  (948874, 3, 1),
  (950137, 0, 0),
  (950408, 2, 1),
  (951779, 2, 0),
  (956828, 3, 2),
  (958108, 1, 0),
  (959332, 1, 0),
  (959649, 3, 2),
  (959739, 0, 1),
  (965033, 3, 2),
  (966946, 0, 0),
  (968642, 3, 2),
  (969953, 2, 2),
  (971779, 2, 0),
  (975073, 1, 2),
  (977921, 0, 1),
  (983856, 2, 2),
  (984449, 1, 0),
  (984642, 2, 2),
  (984749, 3, 0),
  (985407, 3, 2),
  (989651, 1, 1),
  (989896, 2, 0),
  (990314, 2, 2),
  (992494, 1, 1),
  (996587, 2, 1),
  (997368, 1, 1),
  (998352, 0, 0),
  (1000581, 2, 2),
  (1001879, 3, 0),
  (1002426, 2, 1),
  (1003548, 3, 2),
  (1004758, 1, 2),
  (1005184, 1, 1),
  (1007429, 3, 2),
  (1007598, 0, 2),
  (1007638, 3, 1),
  (1008005, 1, 0),
  (1012048, 1, 0),
  (1012771, 0, 2),
  (1013170, 2, 1),
  (1018482, 0, 0),
  (1023166, 1, 1),
  (1024618, 0, 2),
  (1026564, 0, 1),
  (1031223, 1, 0),
  (1034832, 2, 1),
  (1036447, 0, 1),
  (1036638, 3, 2),
  (1037058, 2, 2),
  (1038231, 0, 0),
  (1038597, 2, 1),
  (1043222, 2, 0),
  (1044617, 0, 0),
  (1044952, 3, 0),
  (1046322, 3, 2),
  (1046964, 2, 2),
  (1046988, 2, 0),
  (1049535, 1, 2),
  (1050094, 0, 2),
  (1053453, 2, 2),
  (1054231, 1, 2),
  (1061452, 2, 2),
  (1062415, 0, 2),
  (1064465, 2, 1),
  (1065293, 0, 0),
  (1065400, 1, 2),
  (1067370, 3, 1),
  (1067941, 0, 1),
  (1069960, 3, 1),
  (1072292, 1, 2),
  (1074814, 3, 1),
  (1076321, 2, 0),
  (1077380, 2, 2),
  (1078103, 1, 0),
  (1080243, 3, 0),
  (1087567, 2, 2),
  (1087722, 0, 1),
  (1089089, 3, 0),
  (1092130, 2, 1),
  (1092903, 1, 1),
  (1093683, 3, 0),
  (1094174, 0, 2),
  (1094963, 3, 0),
  (1097518, 1, 1),
  (1098865, 0, 0),
  (1099628, 2, 0),
  (1100200, 1, 1),
  (1100500, 1, 2),
  (1101955, 0, 1),
  (1103274, 3, 1),
  (1105966, 3, 2),
  (1107884, 1, 0),
  (1109723, 2, 1),
  (1111420, 3, 2),
  (1112630, 0, 1),
  (1123750, 1, 2),
  (1124807, 0, 1),
  (1130447, 1, 2),
  (1131129, 3, 0),
  (1133016, 0, 0),
  (1137071, 0, 1),
  (1142136, 1, 2),
  (1143771, 0, 2),
  (1144013, 1, 1),
  (1147264, 0, 1),
  (1148792, 2, 1),
  (1148907, 0, 0),
  (1151352, 1, 0),
  (1152230, 2, 1),
  (1153994, 1, 1),
  (1162827, 0, 0),
  (1165018, 3, 2),
  (1165221, 3, 1),
  (1165251, 0, 2),
  (1165924, 0, 0),
  (1166857, 0, 2),
  (1168056, 2, 0),
  (1168123, 1, 2),
  (1169729, 3, 2),
  (1172981, 2, 1),
  (1174101, 1, 0),
  (1175844, 0, 2),
  (1178037, 2, 1),
  (1179836, 1, 2),
  (1180564, 1, 0),
  (1181845, 3, 2),
  (1183754, 2, 0),
  (1186518, 1, 0),
  (1187931, 1, 1),
  (1187934, 1, 0),
  (1188123, 2, 2),
  (1188225, 0, 1),
  (1190078, 0, 1),
  (1191762, 1, 1),
  (1200398, 0, 0),
  (1203230, 0, 0),
  (1208399, 2, 2),
  (1209059, 2, 0),
  (1210705, 1, 1),
  (1213297, 1, 0),
  (1215941, 3, 0),
  (1217492, 1, 1),
  (1217938, 2, 1),
  (1218254, 0, 1),
  (1218467, 1, 1),
  (1221851, 1, 2),
  (1225324, 1, 1),
  (1227696, 2, 1),
  (1230091, 1, 2),
  (1234515, 0, 1),
  (1235318, 0, 1),
  (1235770, 1, 1),
  (1236439, 2, 0),
  (1237566, 3, 2),
  (1237574, 2, 1),
  (1237972, 2, 1),
  (1241138, 2, 2),
  (1241247, 0, 1),
  (1244105, 1, 2),
  (1247642, 3, 0),
  (1249889, 0, 2),
  (1252413, 3, 1),
  (1257606, 3, 1),
  (1258731, 1, 0),
  (1264377, 0, 0),
  (1265714, 3, 1),
  (1267563, 3, 0),
  (1267564, 1, 1),
  (1270440, 0, 2),
  (1270999, 1, 1),
  (1272689, 3, 0),
  (1275184, 3, 0),
  (1281230, 3, 0),
  (1283153, 2, 1),
  (1285496, 0, 1),
  (1287231, 1, 2),
  (1287561, 1, 2),
  (1288718, 2, 0),
  (1294392, 3, 0),
  (1294849, 2, 2),
  (1295580, 1, 2),
  (1298395, 2, 2),
  (1298521, 1, 2),
  (1298756, 0, 1),
  (1300952, 1, 0),
  (1301493, 2, 1),
  (1304483, 1, 2),
  (1312152, 2, 2),
  (1313105, 1, 2),
  (1313133, 3, 1),
  (1315307, 2, 1),
  (1315942, 2, 2),
  (1319936, 2, 2),
  (1320146, 0, 0),
  (1321864, 2, 2),
  (1324740, 1, 2),
  (1331051, 2, 2),
  (1332760, 2, 1),
  (1333246, 0, 0),
  (1335249, 3, 1),
  (1339271, 1, 1),
  (1339571, 2, 1),
  (1343578, 3, 2),
  (1343786, 3, 1),
  (1346500, 2, 1),
  (1346513, 1, 1),
  (1349007, 0, 1),
  (1349062, 2, 2),
  (1349407, 3, 2),
  (1350392, 0, 0),
  (1351229, 3, 0),
  (1351633, 0, 2),
  (1352362, 2, 0),
  (1352798, 1, 2),
  (1357537, 2, 2),
  (1358034, 0, 2),
  (1360967, 2, 1),
  (1363249, 3, 0),
  (1365009, 1, 0),
  (1369214, 1, 2),
  (1369328, 0, 2),
  (1370052, 1, 0),
  (1370371, 2, 2),
  (1370818, 3, 2),
  (1376700, 3, 2),
  (1379177, 2, 2),
  (1384384, 1, 2),
  (1385467, 2, 2),
  (1385754, 0, 1),
  (1386999, 1, 0),
  (1387692, 3, 1),
  (1387978, 3, 2),
  (1392478, 1, 1),
  (1394090, 1, 2),
  (1397559, 0, 2),
  (1399286, 0, 0),
  (1406301, 3, 2),
  (1408535, 2, 2),
  (1410141, 0, 0),
  (1410261, 0, 0),
  (1413638, 3, 1),
  (1415976, 1, 2),
  (1417344, 3, 2),
  (1419164, 1, 1),
  (1419424, 0, 1),
  (1422974, 1, 1),
  (1424773, 2, 0),
  (1431256, 1, 0),
  (1431599, 2, 0),
  (1435548, 1, 2),
  (1444081, 2, 0),
  (1446651, 3, 0),
  (1446677, 0, 1),
  (1448456, 2, 0),
  (1449043, 3, 2),
  (1450843, 0, 2),
  (1453749, 3, 0),
  (1458888, 2, 2),
  (1459479, 2, 0),
  (1460822, 1, 0),
  (1461187, 2, 1),
  (1462206, 3, 1),
  (1462255, 0, 0),
  (1466727, 3, 1),
  (1470186, 2, 1),
  (1471377, 3, 1),
  (1472161, 3, 2),
  (1472307, 0, 0),
  (1479022, 1, 0),
  (1489419, 1, 2),
  (1491968, 0, 1),
  (1492780, 2, 0),
  (1494546, 3, 2),
  (1497852, 2, 2),
  (1499494, 0, 1),
  (1500180, 2, 2),
  (1503201, 0, 1),
  (1503743, 0, 0),
  (1506397, 3, 1),
  (1508379, 0, 2),
  (1510542, 0, 1),
  (1516454, 1, 1),
  (1519112, 3, 2),
  (1519156, 0, 0),
  (1519808, 3, 2),
  (1521366, 3, 1),
  (1528477, 2, 1),
  (1531250, 0, 0),
  (1532659, 0, 2),
  (1534950, 0, 2),
  (1535411, 2, 1),
  (1538617, 1, 0),
  (1546447, 2, 2),
  (1548089, 1, 0),
  (1550772, 0, 0),
  (1552641, 1, 0),
  (1555007, 0, 1),
  (1555091, 0, 0),
  (1555118, 1, 2),
  (1563377, 0, 1),
  (1565469, 1, 2),
  (1580130, 2, 0),
  (1586251, 0, 1),
  (1587867, 2, 1),
  (1591911, 2, 2),
  (1594761, 3, 1),
  (1594839, 1, 1),
  (1595013, 2, 1),
  (1598748, 2, 2),
  (1600222, 1, 1),
  (1601983, 1, 1),
  (1603815, 3, 2),
  (1605164, 1, 0),
  (1612896, 1, 0),
  (1614558, 0, 2),
  (1615341, 1, 2),
  (1615637, 0, 1),
  (1617473, 0, 0),
  (1618463, 3, 0),
  (1619968, 3, 0),
  (1621352, 2, 1),
  (1624653, 3, 2),
  (1625621, 1, 0),
  (1626316, 0, 2),
  (1632460, 3, 1),
  (1633104, 3, 0),
  (1638623, 1, 0),
  (1639814, 0, 2),
  (1639837, 0, 2),
  (1646558, 1, 2),
  (1647599, 1, 1),
  (1648014, 2, 2),
  (1650523, 3, 0),
  (1652928, 1, 1),
  (1653787, 3, 0),
  (1654887, 2, 0),
  (1657055, 1, 1),
  (1659574, 1, 1),
  (1662496, 1, 2),
  (1663011, 0, 0),
  (1664460, 2, 0),
  (1666128, 0, 2),
  (1667448, 0, 2),
  (1671879, 1, 2),
  (1672055, 1, 0),
  (1673454, 0, 2),
  (1674408, 3, 1),
  (1681942, 1, 2),
  (1682426, 0, 1),
  (1682517, 1, 0),
  (1682786, 0, 2),
  (1684697, 3, 1),
  (1686457, 1, 0),
  (1688687, 0, 2),
  (1689093, 3, 1),
  (1689113, 1, 1),
  (1690034, 0, 2),
  (1690261, 1, 0),
  (1691185, 1, 2),
  (1693551, 2, 2),
  (1694731, 2, 1),
  (1700125, 1, 0),
  (1701650, 0, 1),
  (1703036, 2, 2),
  (1703607, 0, 0),
  (1710371, 0, 2),
  (1711865, 2, 0),
  (1712910, 2, 0),
  (1715133, 0, 1),
  (1715593, 3, 1),
  (1724264, 0, 2),
  (1725736, 1, 0),
  (1727020, 2, 1),
  (1728214, 2, 2),
  (1729443, 3, 2),
  (1729624, 3, 2),
  (1735403, 1, 2),
  (1737452, 1, 2),
  (1739981, 3, 1),
  (1742111, 3, 1),
  (1743809, 0, 2),
  (1747695, 0, 1),
  (1748270, 0, 2),
  (1751414, 0, 1),
  (1754068, 0, 0),
  (1754926, 1, 1),
  (1758517, 3, 2),
  (1761630, 1, 1),
  (1762464, 2, 1),
  (1765931, 0, 0),
  (1766714, 0, 1),
  (1767187, 0, 2),
  (1767278, 3, 0),
  (1773514, 1, 0),
  (1779137, 0, 1),
  (1779420, 1, 1),
  (1780143, 1, 1),
  (1780200, 2, 1),
  (1781279, 2, 1),
  (1782255, 2, 2),
  (1783320, 3, 0),
  (1784429, 0, 2),
  (1786695, 1, 0),
  (1786735, 3, 1),
  (1792323, 1, 2),
  (1794647, 1, 0),
  (1797056, 1, 2),
  (1799213, 1, 2),
  (1799756, 3, 0),
  (1801459, 1, 0),
  (1803787, 0, 0),
  (1807583, 2, 1),
  (1812016, 0, 0),
  (1813062, 3, 0),
  (1817802, 3, 2),
  (1819160, 3, 1),
  (1821684, 3, 2),
  (1823045, 2, 1),
  (1823752, 1, 2),
  (1825651, 2, 1),
  (1828277, 1, 1),
  (1828414, 2, 2),
  (1829651, 2, 2),
  (1830213, 3, 0),
  (1831625, 1, 2),
  (1831793, 3, 2),
  (1833179, 2, 1),
  (1835429, 1, 0),
  (1841970, 1, 2),
  (1842052, 0, 2),
  (1848038, 1, 2),
  (1849027, 2, 2),
  (1853030, 2, 1),
  (1853129, 1, 1),
  (1856212, 0, 1),
  (1858878, 2, 2),
  (1859574, 3, 1),
  (1860754, 2, 0),
  (1860865, 1, 1),
  (1860971, 2, 2),
  (1864427, 0, 2),
  (1866547, 3, 1),
  (1866603, 1, 0),
  (1867884, 2, 1),
  (1869057, 3, 1),
  (1870856, 2, 2),
  (1871780, 1, 2),
  (1875501, 2, 1),
  (1876147, 1, 0),
  (1876895, 1, 1),
  (1876976, 0, 0),
  (1881073, 1, 1),
  (1888260, 0, 0),
  (1888576, 2, 0),
  (1890358, 0, 0),
  (1891265, 1, 2),
  (1891371, 0, 1),
  (1892171, 0, 1),
  (1897788, 3, 2),
  (1899664, 3, 2),
  (1900372, 3, 2),
  (1903656, 2, 2),
  (1908971, 3, 2),
  (1909524, 3, 2),
  (1909545, 1, 2),
  (1909933, 3, 2),
  (1910373, 3, 2),
  (1912321, 3, 2),
  (1913211, 3, 2),
  (1914961, 3, 0),
  (1915225, 2, 1),
  (1915717, 3, 0),
  (1918034, 1, 1),
  (1918332, 3, 1),
  (1918370, 1, 2),
  (1919930, 3, 1),
  (1921728, 3, 0),
  (1922471, 0, 1),
  (1924571, 1, 1),
  (1928649, 2, 1),
  (1935753, 2, 0),
  (1938205, 1, 2),
  (1938310, 2, 0),
  (1944163, 0, 0),
  (1945249, 3, 1),
  (1948801, 1, 1),
  (1948992, 2, 1),
  (1953537, 3, 2),
  (1955092, 0, 1),
  (1955617, 3, 2),
  (1956825, 3, 0),
  (1957167, 0, 2),
  (1957620, 1, 0),
  (1958516, 1, 2),
  (1962209, 0, 2),
  (1968728, 3, 0),
  (1976199, 1, 2),
  (1976860, 0, 2),
  (1977412, 2, 2),
  (1983356, 1, 0),
  (1988816, 2, 0),
  (1991142, 3, 1),
  (1991842, 2, 0),
  (1992771, 2, 1),
  (1996192, 0, 2),
  (1998538, 3, 2),
  (2001001, 2, 1),
  (2002518, 0, 0),
  (2003760, 3, 0),
  (2005871, 1, 1),
  (2007829, 3, 1),
  (2008020, 2, 2),
  (2008245, 1, 1),
  (2008649, 2, 1),
  (2012840, 1, 1),
  (2013678, 0, 0),
  (2015612, 0, 1),
  (2015958, 2, 2),
  (2016706, 0, 0),
  (2019388, 2, 0),
  (2021169, 1, 2),
  (2025803, 0, 2),
  (2025815, 3, 0),
  (2027009, 1, 2),
  (2027901, 3, 1),
  (2029893, 2, 1),
  (2030729, 2, 2),
  (2031447, 3, 1),
  (2033265, 0, 2),
  (2033445, 2, 0),
  (2034479, 2, 2),
  (2037335, 2, 1),
  (2041940, 1, 1),
  (2044327, 2, 1),
  (2044545, 0, 2),
  (2045941, 2, 1),
  (2047454, 3, 2),
  (2048936, 0, 0),
  (2055757, 0, 1),
  (2057470, 0, 0),
  (2058846, 2, 0),
  (2059051, 1, 1),
  (2062442, 1, 2),
  (2064482, 0, 2),
  (2064558, 0, 0),
  (2067122, 1, 1),
  (2067176, 2, 1),
  (2067894, 3, 1),
  (2068565, 2, 0),
  (2069204, 0, 0),
  (2073165, 0, 1),
  (2077082, 0, 2),
  (2077245, 0, 1),
  (2082535, 1, 1),
  (2083454, 3, 1),
  (2083745, 3, 1),
  (2085881, 3, 2),
  (2087290, 1, 2),
  (2087377, 3, 0),
  (2088396, 1, 0),
  (2090244, 1, 1),
  (2092678, 3, 0),
  (2093874, 1, 0),
  (2094338, 3, 0),
  (2104121, 1, 1),
  (2104248, 1, 1),
  (2106411, 0, 2),
  (2106665, 3, 1),
  (2106983, 1, 0),
  (2107109, 2, 0),
  (2108751, 1, 2),
  (2110752, 0, 1),
  (2114599, 2, 1),
  (2114603, 1, 0),
  (2119388, 3, 2),
  (2121907, 2, 1),
  (2122115, 1, 2),
  (2125517, 1, 2),
  (2125631, 3, 2),
  (2126342, 3, 0),
  (2128309, 0, 1),
  (2129130, 1, 0),
  (2129800, 3, 2),
  (2132224, 0, 1),
  (2132813, 2, 0),
  (2134685, 2, 2),
  (2135498, 0, 1),
  (2136472, 0, 1),
  (2139741, 3, 2),
  (2140200, 1, 0),
  (2141932, 0, 0),
  (2142310, 3, 1),
  (2145013, 1, 0),
  (2146596, 1, 2),
  (2149001, 2, 1),
  (2150219, 1, 0),
  (2154060, 1, 0),
  (2161047, 1, 1),
  (2162439, 3, 0),
  (2165148, 0, 2),
  (2165221, 2, 1),
  (2167253, 1, 1),
  (2167471, 3, 0),
  (2168142, 3, 1),
  (2169870, 0, 1),
  (2172116, 3, 2),
  (2173243, 1, 1),
  (2177107, 0, 1),
  (2179980, 2, 2),
  (2184046, 1, 1),
  (2185955, 2, 0),
  (2186597, 2, 1),
  (2187698, 3, 1),
  (2190182, 1, 1),
  (2194003, 0, 2),
  (2197009, 0, 0),
  (2197113, 3, 2),
  (2197371, 2, 1),
  (2205537, 2, 1),
  (2206035, 0, 2),
  (2206125, 1, 2),
  (2206841, 2, 0),
  (2207073, 1, 0),
  (2208546, 2, 2),
  (2210439, 0, 2),
  (2210909, 0, 2),
  (2211277, 1, 1),
  (2212185, 2, 0),
  (2213234, 3, 2),
  (2214494, 0, 1),
  (2214912, 0, 1),
  (2215078, 3, 0),
  (2215485, 3, 2),
  (2216162, 1, 0),
  (2221298, 1, 1),
  (2222350, 0, 0),
  (2223537, 3, 2),
  (2225802, 0, 1),
  (2225966, 2, 0),
  (2226074, 0, 0),
  (2227298, 1, 0),
  (2229473, 0, 2),
  (2229491, 1, 0),
  (2235227, 3, 1),
  (2236878, 3, 2),
  (2236949, 1, 0),
  (2240349, 0, 1),
  (2240508, 2, 2),
  (2240667, 2, 0),
  (2244105, 0, 0),
  (2244125, 1, 1),
  (2249449, 2, 1),
  (2254084, 0, 2),
  (2256912, 0, 2),
  (2257986, 2, 0),
  (2258229, 0, 2),
  (2260055, 3, 1),
  (2262360, 1, 0),
  (2263109, 3, 1),
  (2265520, 3, 2),
  (2267964, 3, 2),
  (2268831, 1, 0),
  (2269876, 3, 2),
  (2275640, 3, 0),
  (2277010, 1, 1),
  (2277954, 0, 2),
  (2277970, 1, 1),
  (2283922, 3, 2),
  (2290943, 3, 0),
  (2291646, 3, 0),
  (2292248, 2, 0),
  (2294906, 2, 2),
  (2295008, 2, 2),
  (2295312, 0, 2),
  (2297102, 0, 0),
  (2303350, 2, 2),
  (2303361, 1, 2),
  (2304341, 0, 1),
  (2307213, 2, 1),
  (2308076, 2, 1),
  (2310693, 3, 0),
  (2312838, 1, 0),
  (2313770, 2, 0),
  (2314550, 2, 0),
  (2315302, 2, 0),
  (2315412, 3, 2),
  (2319546, 1, 0),
  (2321853, 0, 2),
  (2325641, 1, 0),
  (2328825, 3, 2),
  (2328925, 1, 0),
  (2329524, 0, 0),
  (2330440, 2, 0),
  (2330685, 3, 1),
  (2333538, 2, 2),
  (2334553, 3, 2),
  (2340047, 0, 0),
  (2342301, 2, 2),
  (2343130, 1, 1),
  (2346449, 3, 1),
  (2347800, 2, 1),
  (2351429, 3, 2),
  (2351522, 0, 1),
  (2354310, 1, 1),
  (2360757, 3, 0),
  (2366125, 2, 2),
  (2367787, 1, 2),
  (2369521, 3, 1),
  (2369751, 2, 1),
  (2371863, 1, 1),
  (2373030, 1, 1),
  (2373503, 2, 2),
  (2374201, 2, 1),
  (2374769, 1, 1),
  (2375187, 3, 2),
  (2375601, 1, 2),
  (2376328, 3, 2),
  (2381274, 1, 0),
  (2381435, 2, 1),
  (2386222, 2, 0),
  (2387188, 2, 1),
  (2388492, 2, 1),
  (2388556, 1, 0),
  (2389675, 2, 0),
  (2395057, 3, 1),
  (2397823, 2, 2),
  (2400713, 2, 1),
  (2404129, 2, 2),
  (2404388, 2, 2),
  (2404732, 2, 2),
  (2406083, 3, 2),
  (2406786, 1, 1),
  (2407806, 3, 2),
  (2409638, 2, 2),
  (2413622, 3, 2),
  (2416841, 3, 2),
  (2419439, 2, 1),
  (2420019, 3, 1),
  (2420034, 1, 2),
  (2426705, 1, 0),
  (2427818, 2, 0),
  (2427936, 1, 2),
  (2436054, 0, 2),
  (2436972, 0, 1),
  (2438120, 2, 0),
  (2439868, 1, 1),
  (2440217, 1, 1),
  (2443567, 2, 2),
  (2443568, 3, 2),
  (2444114, 0, 1),
  (2444141, 1, 1),
  (2444313, 2, 2),
  (2444530, 2, 1),
  (2451888, 1, 2),
  (2458997, 1, 0),
  (2460507, 3, 0),
  (2462446, 0, 2),
  (2463936, 1, 1),
  (2465122, 1, 1),
  (2467457, 1, 0),
  (2467656, 2, 0),
  (2469519, 2, 0),
  (2473951, 2, 2),
  (2475133, 1, 1),
  (2475974, 3, 1),
  (2477190, 2, 2),
  (2477621, 3, 0),
  (2480844, 3, 0),
  (2486971, 2, 1),
  (2487753, 0, 0),
  (2490356, 3, 1),
  (2490407, 0, 0),
  (2500753, 0, 1),
  (2502363, 3, 2),
  (2505325, 3, 2),
  (2508456, 0, 1),
  (2509723, 3, 2),
  (2513304, 0, 1),
  (2513436, 0, 1),
  (2513692, 0, 1),
  (2514478, 0, 1),
  (2514706, 1, 2),
  (2519019, 0, 1),
  (2521847, 0, 0),
  (2526785, 3, 2),
  (2527060, 3, 1),
  (2533112, 2, 0),
  (2533836, 3, 2),
  (2534177, 2, 0),
  (2536066, 1, 1),
  (2539591, 3, 1),
  (2546118, 1, 1),
  (2546192, 1, 0),
  (2547498, 3, 2),
  (2549945, 2, 0),
  (2552791, 3, 1),
  (2554093, 0, 2),
  (2554827, 2, 1),
  (2555506, 3, 0),
  (2557675, 0, 0),
  (2560487, 0, 1),
  (2562876, 1, 1),
  (2564983, 3, 2),
  (2565551, 0, 2),
  (2566288, 2, 2),
  (2570822, 0, 0),
  (2574426, 0, 1),
  (2574784, 1, 1),
  (2574921, 0, 1),
  (2579226, 3, 1),
  (2580198, 1, 1),
  (2580301, 3, 0),
  (2580345, 1, 2),
  (2581007, 1, 1),
  (2583814, 2, 0),
  (2584734, 2, 1),
  (2586309, 2, 1),
  (2587180, 0, 1),
  (2587769, 0, 2),
  (2595880, 1, 1),
  (2596843, 0, 1),
  (2598054, 1, 0),
  (2599578, 2, 0),
  (2604534, 1, 1),
  (2604579, 2, 0),
  (2605160, 2, 2),
  (2606853, 0, 2),
  (2612692, 0, 2),
  (2613582, 1, 1),
  (2616808, 2, 2),
  (2618488, 1, 2),
  (2620729, 0, 1),
  (2620915, 3, 2),
  (2620954, 3, 0),
  (2627358, 0, 2),
  (2632983, 2, 2),
  (2634666, 3, 2),
  (2635217, 2, 2),
  (2636031, 3, 0),
  (2637429, 2, 1),
  (2639994, 0, 2),
  (2640706, 0, 2),
  (2645970, 3, 2),
  (2647325, 2, 2),
  (2648133, 2, 0),
  (2648497, 0, 1),
  (2651355, 2, 0),
  (2658419, 1, 2),
  (2661149, 1, 0),
  (2661926, 1, 0),
  (2671554, 3, 2),
  (2674017, 0, 1),
  (2674940, 2, 1),
  (2676750, 1, 0),
  (2680111, 3, 2),
  (2684496, 3, 1),
  (2686515, 2, 1),
  (2689066, 2, 0),
  (2690153, 3, 2),
  (2690559, 3, 2),
  (2696115, 1, 1),
  (2699070, 3, 1),
  (2699799, 0, 2),
  (2703962, 0, 1),
  (2704349, 2, 2),
  (2706427, 2, 1),
  (2706455, 1, 2),
  (2708724, 3, 0),
  (2714846, 0, 2),
  (2716188, 2, 0),
  (2716235, 2, 2),
  (2717159, 1, 0),
  (2718623, 0, 2),
  (2721963, 2, 2),
  (2723438, 2, 0),
  (2724585, 1, 1),
  (2731201, 2, 2),
  (2735299, 2, 1),
  (2735433, 3, 2),
  (2735783, 1, 2),
  (2736373, 1, 0),
  (2741898, 0, 0),
  (2742208, 2, 2),
  (2743385, 3, 1),
  (2743501, 3, 1),
  (2744894, 0, 2),
  (2745430, 0, 2),
  (2746689, 2, 0),
  (2747820, 1, 0),
  (2754485, 2, 0),
  (2755838, 1, 0),
  (2757547, 0, 2),
  (2758787, 1, 1),
  (2759595, 3, 1),
  (2761105, 3, 0),
  (2769424, 0, 1),
  (2770993, 1, 2),
  (2772147, 2, 1),
  (2774934, 1, 1),
  (2781318, 0, 0),
  (2786360, 2, 0),
  (2786547, 2, 0),
  (2788233, 2, 0),
  (2788256, 0, 1),
  (2790639, 2, 1),
  (2791815, 1, 1),
  (2794737, 1, 2),
  (2798581, 3, 2),
  (2801242, 0, 2),
  (2801711, 2, 2),
  (2803378, 3, 2),
  (2806575, 0, 2),
  (2806832, 2, 1),
  (2811824, 0, 0),
  (2813319, 2, 2),
  (2815601, 1, 2),
  (2816772, 3, 1),
  (2817451, 1, 0),
  (2817597, 2, 0),
  (2818674, 1, 0),
  (2820518, 1, 1),
  (2821245, 0, 2),
  (2821252, 0, 2),
  (2821352, 1, 1),
  (2828205, 0, 1),
  (2828901, 0, 2),
  (2831233, 3, 0),
  (2831866, 0, 2),
  (2834556, 2, 2),
  (2834797, 0, 0),
  (2836316, 1, 2),
  (2837236, 1, 2),
  (2837335, 3, 2),
  (2840531, 0, 1),
  (2840695, 0, 2),
  (2841503, 3, 2),
  (2842139, 1, 1),
  (2845052, 2, 2),
  (2847650, 2, 2),
  (2847666, 2, 0),
  (2851269, 3, 0),
  (2853721, 2, 2),
  (2860430, 1, 2),
  (2861389, 2, 0),
  (2864940, 0, 1),
  (2868517, 1, 2),
  (2873215, 3, 2),
  (2873761, 1, 0),
  (2875372, 1, 1),
  (2883102, 2, 0),
  (2884402, 2, 0),
  (2884875, 1, 0),
  (2885391, 3, 2),
  (2888962, 0, 0),
  (2891021, 2, 2),
  (2893109, 0, 1),
  (2894842, 2, 0),
  (2896500, 0, 0),
  (2902461, 2, 0),
  (2905650, 2, 0),
  (2906895, 2, 1),
  (2908171, 1, 1),
  (2908730, 1, 1),
  (2909535, 0, 1),
  (2910012, 3, 1),
  (2911718, 2, 2),
  (2913684, 1, 2),
  (2914075, 3, 1),
  (2914801, 3, 0),
  (2916037, 2, 1),
  (2916124, 3, 1),
  (2916273, 3, 0),
  (2917019, 1, 0),
  (2920022, 1, 2),
  (2922232, 3, 0),
  (2922666, 0, 2),
  (2924402, 2, 1),
  (2925314, 0, 0),
  (2926598, 0, 2),
  (2929394, 3, 1),
  (2930771, 3, 1),
  (2932328, 2, 1),
  (2932453, 0, 0),
  (2938790, 1, 0),
  (2942859, 3, 0),
  (2946816, 2, 1),
  (2949295, 0, 2),
  (2952543, 3, 2),
  (2954560, 3, 0),
  (2956488, 2, 2),
  (2959348, 0, 1),
  (2964374, 3, 1),
  (2965574, 0, 1),
  (2969882, 1, 2),
  (2970060, 2, 1),
  (2971123, 2, 1),
  (2971979, 3, 1),
  (2974314, 1, 2),
  (2981471, 1, 2),
  (2983935, 2, 0),
  (2984087, 0, 2),
  (2989033, 2, 0),
  (2989401, 1, 0),
  (2992314, 2, 2),
  (2992981, 1, 0),
  (2999880, 1, 2),
  (3001066, 1, 1),
  (3001570, 3, 2),
  (3004155, 0, 2),
  (3006148, 0, 2),
  (3009780, 1, 1),
  (3010586, 1, 2),
  (3014933, 0, 1),
  (3014991, 3, 2),
  (3018206, 3, 2),
  (3019711, 3, 1),
  (3020150, 3, 1),
  (3023099, 3, 2),
  (3024028, 2, 1),
  (3025074, 3, 2),
  (3027597, 0, 2),
  (3030923, 0, 1),
  (3032575, 3, 0),
  (3034896, 3, 1),
  (3035014, 3, 1),
  (3043206, 2, 0),
  (3046287, 3, 1),
  (3052174, 3, 2),
  (3053413, 3, 0),
  (3055336, 2, 0),
  (3056236, 3, 1),
  (3056602, 0, 0),
  (3058150, 1, 1),
  (3058151, 3, 0),
  (3060007, 1, 1),
  (3063360, 0, 1),
  (3065551, 3, 0),
  (3066140, 3, 0),
  (3068379, 1, 0),
  (3068923, 0, 0),
  (3074562, 3, 1),
  (3076294, 3, 2),
  (3077546, 0, 1),
  (3081560, 1, 2),
  (3088711, 2, 1),
  (3089784, 0, 2),
  (3090720, 3, 0),
  (3090845, 1, 0),
  (3090957, 2, 1),
  (3091099, 2, 2),
  (3093125, 3, 1),
  (3094262, 0, 2),
  (3099071, 2, 0),
  (3099263, 1, 0),
  (3103989, 1, 2),
  (3106424, 1, 2),
  (3110290, 2, 1),
  (3110442, 1, 0),
  (3110900, 1, 0),
  (3112270, 0, 1),
  (3113114, 3, 1),
  (3115254, 3, 0),
  (3115865, 3, 2),
  (3120991, 1, 2),
  (3122354, 2, 1),
  (3127689, 0, 1),
  (3128257, 2, 2),
  (3129182, 1, 1),
  (3130671, 3, 0),
  (3133129, 2, 1),
  (3133682, 0, 2),
  (3134160, 2, 0),
  (3138101, 1, 1),
  (3138726, 3, 2),
  (3142059, 3, 2),
  (3146025, 3, 0),
  (3147549, 2, 1),
  (3148805, 2, 1),
  (3151195, 1, 0),
  (3155540, 2, 0),
  (3155570, 3, 1),
  (3156607, 1, 0),
  (3157599, 2, 0),
  (3160583, 2, 0),
  (3164524, 2, 0),
  (3165155, 0, 1),
  (3165851, 1, 1),
  (3166382, 3, 0),
  (3170832, 3, 0),
  (3170864, 2, 0),
  (3171121, 3, 1),
  (3172715, 3, 1),
  (3174371, 1, 0),
  (3175350, 2, 2),
  (3175436, 2, 0),
  (3177771, 0, 2),
  (3179375, 1, 0),
  (3180159, 0, 0),
  (3181705, 1, 0),
  (3181849, 3, 2),
  (3182153, 1, 2),
  (3183448, 3, 2),
  (3184765, 0, 1),
  (3185923, 2, 0),
  (3186501, 1, 0),
  (3186664, 2, 1),
  (3187285, 0, 2),
  (3189758, 3, 0),
  (3193235, 0, 2),
  (3193645, 1, 0),
  (3193889, 3, 1),
  (3195464, 1, 0),
  (3200953, 1, 2),
  (3205186, 0, 0),
  (3209974, 2, 2),
  (3210339, 0, 2),
  (3212496, 3, 1),
  (3213087, 1, 1),
  (3218247, 2, 0),
  (3218288, 2, 2),
  (3222224, 0, 2),
  (3222261, 3, 2),
  (3223499, 1, 1),
  (3226735, 3, 2),
  (3229702, 2, 2),
  (3237912, 0, 2),
  (3250869, 1, 2),
  (3251180, 2, 0),
  (3253189, 0, 1),
  (3254028, 1, 0),
  (3256957, 2, 1),
  (3261456, 3, 0),
  (3265707, 3, 2),
  (3267553, 1, 2),
  (3267950, 0, 2),
  (3270385, 2, 0),
  (3270699, 3, 2),
  (3271255, 2, 0),
  (3273326, 2, 0),
  (3274802, 2, 0),
  (3281516, 1, 2),
  (3281751, 1, 0),
  (3282364, 3, 0),
  (3282796, 1, 2),
  (3285792, 0, 0),
  (3292678, 2, 1),
  (3297715, 0, 0),
  (3299200, 3, 1),
  (3300360, 0, 1),
  (3302160, 3, 2),
  (3305866, 0, 1),
  (3306107, 3, 0),
  (3306536, 3, 1),
  (3307308, 2, 0),
  (3308396, 2, 2),
  (3308683, 0, 2),
  (3308974, 1, 2),
  (3310747, 3, 2),
  (3313008, 1, 0),
  (3317130, 1, 0),
  (3319037, 3, 0),
  (3320707, 0, 0),
  (3323296, 1, 1),
  (3325401, 3, 0),
  (3328984, 0, 0),
  (3329869, 1, 0),
  (3330519, 1, 1),
  (3330611, 3, 2),
  (3332198, 1, 2),
  (3335203, 0, 2),
  (3337417, 2, 0),
  (3337671, 3, 1),
  (3337827, 1, 0),
  (3339836, 3, 0),
  (3343081, 0, 1),
  (3343263, 1, 2),
  (3344481, 3, 0),
  (3344753, 1, 2),
  (3349563, 0, 0),
  (3351913, 0, 1),
  (3356614, 1, 2),
  (3357672, 2, 0),
  (3359975, 1, 2),
  (3361373, 2, 1),
  (3362527, 3, 1),
  (3364312, 3, 2),
  (3364748, 3, 2),
  (3365549, 1, 2),
  (3367005, 1, 0),
  (3367685, 2, 0),
  (3369565, 2, 2),
  (3369587, 0, 2),
  (3369858, 1, 0),
  (3373166, 0, 2),
  (3378026, 3, 2),
  (3378867, 0, 2),
  (3380834, 0, 1),
  (3383450, 2, 0),
  (3385636, 0, 0),
  (3389384, 2, 0),
  (3391266, 3, 1),
  (3392467, 1, 0),
  (3392751, 3, 2),
  (3392829, 2, 2),
  (3393590, 1, 0),
  (3395031, 1, 1),
  (3395873, 1, 0),
  (3399238, 1, 0),
  (3399449, 1, 1),
  (3400653, 3, 2),
  (3400874, 1, 1),
  (3401991, 2, 2),
  (3405971, 2, 2),
  (3406458, 0, 0),
  (3406510, 1, 1),
  (3407514, 2, 0),
  (3408124, 0, 1),
  (3409060, 0, 1),
  (3410345, 1, 0),
  (3413271, 2, 1),
  (3413610, 3, 2),
  (3413969, 2, 2),
  (3414117, 3, 1),
  (3417320, 3, 2),
  (3417927, 3, 0),
  (3419292, 3, 2),
  (3421785, 1, 2),
  (3424410, 1, 1),
  (3424548, 3, 2),
  (3431330, 2, 1),
  (3431502, 3, 0),
  (3432127, 3, 0),
  (3435486, 2, 0),
  (3435972, 3, 0),
  (3440093, 3, 1),
  (3442786, 1, 0),
  (3444694, 3, 2),
  (3446290, 0, 1),
  (3447531, 3, 2),
  (3449914, 1, 0),
  (3452290, 1, 1),
  (3452397, 3, 1),
  (3454049, 1, 0),
  (3456764, 1, 0),
  (3460349, 1, 0),
  (3464169, 1, 1),
  (3469433, 0, 0),
  (3470631, 1, 1),
  (3471082, 2, 0),
  (3471472, 1, 0),
  (3474094, 0, 0),
  (3474866, 2, 2),
  (3475043, 0, 2),
  (3475272, 3, 2),
  (3477154, 2, 1),
  (3478659, 1, 0),
  (3478750, 3, 1),
  (3480687, 2, 0),
  (3481600, 3, 2),
  (3482487, 1, 1),
  (3483695, 3, 2),
  (3484078, 3, 1),
  (3488208, 0, 1),
  (3492915, 1, 1),
  (3493199, 3, 1),
  (3494111, 3, 2),
  (3495720, 2, 1),
  (3495784, 2, 1),
  (3498422, 1, 1),
  (3499428, 0, 2),
  (3499556, 2, 0),
  (3502316, 0, 1),
  (3503634, 0, 1),
  (3505188, 0, 1),
  (3507099, 3, 0),
  (3507392, 2, 1),
  (3508212, 2, 1),
  (3518146, 0, 2),
  (3521746, 2, 0),
  (3522644, 2, 2),
  (3522865, 2, 2),
  (3523889, 3, 2),
  (3527262, 3, 1),
  (3527823, 1, 1),
  (3530518, 2, 1),
  (3533433, 3, 1),
  (3533464, 1, 1),
  (3535357, 1, 0),
  (3535611, 1, 0),
  (3536034, 0, 2),
  (3536655, 0, 2),
  (3536880, 1, 2),
  (3537302, 1, 0),
  (3539359, 1, 1),
  (3540366, 2, 2),
  (3541899, 3, 0),
  (3542370, 0, 1),
  (3543010, 0, 0),
  (3543942, 3, 2),
  (3548808, 0, 0),
  (3550895, 0, 2),
  (3554266, 1, 2),
  (3556362, 3, 0),
  (3556724, 2, 0),
  (3560939, 2, 1),
  (3561651, 0, 0),
  (3562638, 3, 0),
  (3564702, 0, 2),
  (3567078, 3, 1),
  (3567266, 2, 2),
  (3570536, 2, 1),
  (3571325, 1, 2),
  (3576411, 3, 1),
  (3578831, 0, 1),
  (3581251, 1, 2),
  (3581662, 0, 0),
  (3583601, 2, 0),
  (3583647, 2, 0),
  (3585254, 1, 0),
  (3588224, 3, 0),
  (3588839, 3, 0),
  (3592569, 1, 0),
  (3593900, 3, 2),
  (3594427, 2, 2),
  (3596430, 2, 2),
  (3597131, 3, 1),
  (3598769, 0, 1),
  (3599869, 0, 0),
])
