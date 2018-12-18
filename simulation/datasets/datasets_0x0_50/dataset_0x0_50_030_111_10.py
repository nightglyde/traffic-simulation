from src.util import *
schedule = deque([
  (4748, 0, 1),
  (6718, 3, 1),
  (8783, 0, 0),
  (11664, 0, 0),
  (12191, 2, 0),
  (13290, 0, 0),
  (15101, 3, 0),
  (15182, 0, 2),
  (16194, 3, 2),
  (18604, 1, 2),
  (22821, 2, 1),
  (23002, 0, 0),
  (23042, 2, 2),
  (25543, 1, 0),
  (29745, 2, 0),
  (33215, 3, 0),
  (37601, 1, 0),
  (38215, 2, 0),
  (39654, 1, 2),
  (45504, 0, 1),
  (46522, 0, 0),
  (46991, 0, 2),
  (47140, 2, 0),
  (49387, 0, 1),
  (51766, 2, 1),
  (56156, 2, 1),
  (56474, 3, 0),
  (59462, 0, 0),
  (59944, 3, 0),
  (60448, 3, 0),
  (60579, 1, 0),
  (63339, 1, 0),
  (66431, 3, 2),
  (66721, 3, 1),
  (67171, 2, 1),
  (72571, 1, 1),
  (76039, 0, 2),
  (76084, 3, 1),
  (77690, 0, 1),
  (82479, 0, 2),
  (84516, 0, 2),
  (85395, 2, 2),
  (85676, 1, 0),
  (86551, 0, 0),
  (92918, 1, 0),
  (93430, 2, 1),
  (93544, 1, 2),
  (93830, 2, 0),
  (97442, 3, 1),
  (101340, 3, 1),
  (101691, 0, 1),
  (102347, 0, 1),
  (104628, 1, 2),
  (106298, 0, 1),
  (113573, 0, 0),
  (113638, 2, 2),
  (114133, 0, 0),
  (114479, 2, 2),
  (117118, 0, 0),
  (118392, 3, 0),
  (118891, 3, 0),
  (118971, 0, 1),
  (125457, 3, 2),
  (127007, 1, 1),
  (127307, 0, 0),
  (129770, 2, 1),
  (130703, 0, 0),
  (131340, 2, 2),
  (133685, 3, 2),
  (135299, 0, 1),
  (135471, 2, 1),
  (138238, 2, 2),
  (140408, 0, 0),
  (140502, 1, 1),
  (145073, 0, 1),
  (147430, 3, 1),
  (148930, 1, 1),
  (149499, 3, 1),
  (157561, 3, 2),
  (158376, 1, 0),
  (161094, 0, 2),
  (162830, 0, 0),
  (169957, 2, 2),
  (172813, 3, 2),
  (173720, 2, 0),
  (175072, 1, 0),
  (177908, 1, 2),
  (179207, 3, 2),
  (179625, 3, 0),
  (181589, 0, 2),
  (184047, 2, 0),
  (185029, 2, 2),
  (185731, 1, 0),
  (188128, 3, 1),
  (189795, 2, 1),
  (189917, 1, 0),
  (190411, 1, 1),
  (193966, 1, 0),
  (195784, 3, 1),
  (197538, 0, 0),
  (199347, 3, 2),
  (202077, 1, 1),
  (203706, 2, 1),
  (210173, 2, 1),
  (210290, 3, 1),
  (213138, 0, 2),
  (213431, 1, 2),
  (217389, 2, 2),
  (217777, 0, 0),
  (218472, 1, 0),
  (219467, 1, 0),
  (219884, 2, 0),
  (220158, 2, 1),
  (226046, 3, 2),
  (226464, 2, 2),
  (230014, 1, 0),
  (230238, 0, 2),
  (232996, 0, 2),
  (234755, 2, 1),
  (235844, 1, 1),
  (236514, 3, 1),
  (238480, 2, 1),
  (243280, 1, 2),
  (246030, 1, 1),
  (250406, 2, 0),
  (252866, 1, 0),
  (258838, 3, 0),
  (262965, 1, 0),
  (269478, 0, 2),
  (272754, 3, 2),
  (273599, 1, 1),
  (274875, 3, 2),
  (275581, 0, 0),
  (275854, 0, 2),
  (278867, 1, 2),
  (279458, 2, 2),
  (281598, 0, 2),
  (287186, 3, 1),
  (288152, 2, 1),
  (290600, 3, 2),
  (292064, 0, 1),
  (295484, 0, 0),
  (296481, 0, 0),
  (298653, 3, 0),
  (301419, 3, 1),
  (301731, 2, 2),
  (302851, 2, 1),
  (317268, 3, 0),
  (317342, 2, 1),
  (317916, 2, 2),
  (319417, 0, 1),
  (320876, 0, 1),
  (323858, 2, 1),
  (324804, 0, 2),
  (325183, 0, 2),
  (326295, 2, 1),
  (328534, 3, 0),
  (329396, 1, 1),
  (332887, 0, 2),
  (332902, 1, 0),
  (332981, 1, 0),
  (333841, 1, 0),
  (339288, 0, 0),
  (339930, 0, 2),
  (340477, 0, 2),
  (342256, 2, 2),
  (345004, 2, 1),
  (345180, 0, 2),
  (345741, 2, 1),
  (351556, 0, 0),
  (355743, 3, 1),
  (356405, 2, 0),
  (357321, 1, 1),
  (358203, 3, 2),
  (359919, 3, 1),
  (362025, 3, 1),
  (368263, 3, 0),
  (370886, 3, 2),
  (374771, 3, 1),
  (376808, 2, 0),
  (376972, 0, 2),
  (382391, 3, 2),
  (388353, 3, 1),
  (388424, 3, 1),
  (388437, 2, 0),
  (393494, 2, 1),
  (393608, 2, 1),
  (394026, 0, 0),
  (395448, 1, 0),
  (396174, 1, 1),
  (396625, 0, 0),
  (400866, 2, 2),
  (400884, 2, 1),
  (400926, 0, 0),
  (401295, 0, 1),
  (402811, 2, 1),
  (402895, 1, 2),
  (403929, 3, 0),
  (410498, 1, 2),
  (412136, 2, 0),
  (415307, 3, 2),
  (418490, 2, 2),
  (424289, 3, 1),
  (426715, 2, 0),
  (429818, 1, 0),
  (430352, 3, 1),
  (437747, 3, 2),
  (439303, 3, 1),
  (440517, 2, 0),
  (442703, 2, 0),
  (447172, 0, 1),
  (448835, 3, 0),
  (449150, 1, 0),
  (449504, 2, 0),
  (452372, 2, 0),
  (453070, 3, 0),
  (454080, 0, 1),
  (455782, 1, 2),
  (455835, 2, 0),
  (456529, 2, 1),
  (459337, 1, 0),
  (461940, 0, 1),
  (462455, 3, 0),
  (462623, 0, 2),
  (464354, 3, 2),
  (468527, 0, 0),
  (468758, 0, 1),
  (470864, 1, 1),
  (473031, 3, 0),
  (475548, 1, 1),
  (476019, 0, 0),
  (481368, 3, 0),
  (483842, 0, 0),
  (484797, 0, 1),
  (484840, 1, 0),
  (484958, 0, 1),
  (486906, 0, 0),
  (487812, 3, 1),
  (489757, 0, 0),
  (489828, 2, 1),
  (490988, 3, 0),
  (493604, 2, 2),
  (494949, 2, 0),
  (503336, 2, 0),
  (507818, 1, 1),
  (510670, 3, 1),
  (513216, 3, 0),
  (514111, 3, 2),
  (514243, 1, 1),
  (515298, 2, 1),
  (519090, 2, 1),
  (519391, 0, 1),
  (527053, 1, 1),
  (528165, 0, 1),
  (529460, 2, 1),
  (533572, 1, 1),
  (533887, 2, 2),
  (534914, 3, 0),
  (536509, 1, 0),
  (536790, 1, 0),
  (537900, 1, 0),
  (538638, 0, 1),
  (539564, 2, 2),
  (539619, 0, 1),
  (545527, 0, 1),
  (547100, 1, 2),
  (549536, 2, 0),
  (550094, 2, 1),
  (550637, 0, 1),
  (551397, 2, 1),
  (554811, 1, 2),
  (557573, 2, 1),
  (558230, 1, 2),
  (558266, 1, 2),
  (559725, 1, 0),
  (563698, 0, 1),
  (564627, 3, 1),
  (567388, 0, 0),
  (569531, 2, 1),
  (570119, 2, 0),
  (571239, 1, 0),
  (571701, 0, 1),
  (573647, 0, 2),
  (574941, 2, 1),
  (576097, 0, 2),
  (581705, 0, 0),
  (585108, 2, 1),
  (585130, 3, 0),
  (594154, 3, 0),
  (597751, 3, 0),
  (597798, 3, 2),
  (597866, 1, 0),
  (599375, 3, 1),
  (599448, 3, 0),
  (601538, 0, 2),
  (603232, 0, 2),
  (607071, 3, 2),
  (609498, 3, 1),
  (611807, 1, 0),
  (611830, 2, 0),
  (613018, 1, 2),
  (614231, 3, 1),
  (615233, 1, 2),
  (615727, 2, 1),
  (616085, 0, 2),
  (619758, 0, 0),
  (620101, 1, 1),
  (622972, 2, 2),
  (625494, 1, 0),
  (626323, 2, 2),
  (626927, 2, 2),
  (628554, 3, 2),
  (629566, 0, 0),
  (635175, 3, 0),
  (635754, 2, 1),
  (639879, 1, 2),
  (640804, 0, 1),
  (645215, 2, 2),
  (645533, 0, 0),
  (649405, 3, 1),
  (650771, 0, 2),
  (653205, 3, 0),
  (654668, 0, 1),
  (656415, 3, 0),
  (658649, 0, 1),
  (659986, 1, 2),
  (664414, 3, 2),
  (666399, 0, 0),
  (671623, 2, 1),
  (674260, 3, 2),
  (674434, 1, 2),
  (675122, 1, 2),
  (676795, 1, 2),
  (680649, 3, 0),
  (681684, 3, 1),
  (685569, 2, 0),
  (686551, 1, 1),
  (688128, 0, 0),
  (692724, 0, 2),
  (702878, 2, 1),
  (703002, 2, 1),
  (706985, 0, 1),
  (706998, 2, 1),
  (709885, 1, 0),
  (717063, 2, 2),
  (721149, 0, 0),
  (721823, 2, 1),
  (727621, 1, 1),
  (728581, 0, 2),
  (729228, 1, 2),
  (732277, 3, 0),
  (733169, 0, 1),
  (733991, 1, 0),
  (737415, 0, 1),
  (738273, 3, 0),
  (739420, 3, 1),
  (740935, 0, 1),
  (741049, 3, 1),
  (747017, 3, 0),
  (749973, 2, 1),
  (750124, 0, 0),
  (756520, 0, 0),
  (757039, 2, 2),
  (762019, 0, 1),
  (767889, 3, 1),
  (768320, 3, 1),
  (768711, 0, 1),
  (770981, 3, 2),
  (773386, 2, 0),
  (773676, 0, 2),
  (775610, 2, 1),
  (776069, 1, 0),
  (778118, 3, 1),
  (778440, 2, 0),
  (778789, 3, 0),
  (779348, 2, 0),
  (779724, 1, 0),
  (781877, 0, 2),
  (782835, 1, 0),
  (783208, 2, 0),
  (793073, 0, 2),
  (795221, 0, 2),
  (795569, 3, 0),
  (797684, 1, 1),
  (799619, 3, 0),
  (802158, 1, 0),
  (804557, 1, 2),
  (806760, 3, 2),
  (808379, 3, 0),
  (811271, 2, 2),
  (814752, 1, 1),
  (815044, 3, 1),
  (816730, 0, 1),
  (816867, 1, 1),
  (817144, 3, 0),
  (817599, 1, 0),
  (821197, 0, 1),
  (821345, 0, 0),
  (822294, 1, 1),
  (824048, 1, 1),
  (824073, 3, 0),
  (826589, 0, 1),
  (833824, 1, 2),
  (834252, 1, 2),
  (837544, 1, 0),
  (839701, 3, 2),
  (844205, 2, 2),
  (844225, 2, 2),
  (845065, 2, 0),
  (845395, 3, 0),
  (846279, 1, 1),
  (847231, 1, 2),
  (847473, 0, 2),
  (851578, 2, 2),
  (854152, 1, 0),
  (856572, 1, 1),
  (856687, 3, 1),
  (858346, 1, 0),
  (858993, 0, 1),
  (860706, 3, 1),
  (864730, 1, 1),
  (870706, 2, 2),
  (873916, 1, 0),
  (875004, 1, 0),
  (877291, 2, 1),
  (878594, 1, 2),
  (880003, 2, 1),
  (883492, 3, 1),
  (883911, 0, 0),
  (884700, 2, 2),
  (886077, 2, 1),
  (886454, 3, 1),
  (887628, 0, 0),
  (887905, 1, 1),
  (888125, 0, 2),
  (889908, 3, 1),
  (890813, 2, 1),
  (891144, 2, 2),
  (893795, 2, 1),
  (898599, 0, 0),
  (904830, 0, 2),
  (910866, 3, 1),
  (912531, 3, 2),
  (915232, 1, 2),
  (915500, 3, 0),
  (918200, 3, 0),
  (918833, 3, 1),
  (919141, 1, 0),
  (922170, 0, 0),
  (923869, 1, 1),
  (925740, 0, 1),
  (926993, 3, 0),
  (929914, 2, 2),
  (934829, 0, 1),
  (939070, 2, 2),
  (940178, 1, 2),
  (944193, 0, 1),
  (944669, 2, 2),
  (948578, 2, 2),
  (949283, 0, 2),
  (950926, 3, 1),
  (951525, 0, 2),
  (954455, 2, 2),
  (956672, 3, 0),
  (959333, 3, 2),
  (961026, 3, 2),
  (966950, 0, 2),
  (970657, 3, 2),
  (976356, 3, 0),
  (977291, 1, 2),
  (979787, 1, 2),
  (980607, 0, 0),
  (981473, 2, 1),
  (982227, 1, 1),
  (985154, 1, 1),
  (986156, 3, 1),
  (988652, 0, 1),
  (993196, 2, 0),
  (996562, 0, 1),
  (998470, 3, 0),
  (1002990, 1, 2),
  (1004152, 3, 1),
  (1004691, 2, 0),
  (1004811, 3, 0),
  (1007838, 3, 0),
  (1008877, 2, 2),
  (1010906, 3, 2),
  (1011120, 1, 0),
  (1011452, 2, 1),
  (1012610, 0, 0),
  (1015000, 1, 2),
  (1017718, 0, 2),
  (1018642, 3, 0),
  (1020775, 3, 1),
  (1022539, 2, 0),
  (1026037, 0, 1),
  (1027919, 1, 1),
  (1031346, 2, 2),
  (1031543, 0, 1),
  (1032112, 0, 2),
  (1036659, 0, 2),
  (1036720, 2, 1),
  (1041514, 1, 2),
  (1041966, 2, 2),
  (1050007, 1, 2),
  (1051318, 3, 0),
  (1051555, 3, 2),
  (1052126, 1, 2),
  (1052981, 1, 1),
  (1054811, 2, 2),
  (1058434, 2, 1),
  (1062193, 1, 2),
  (1064111, 0, 1),
  (1064723, 0, 1),
  (1065053, 3, 2),
  (1066512, 1, 0),
  (1066543, 1, 2),
  (1067216, 3, 2),
  (1067480, 0, 0),
  (1067731, 3, 0),
  (1070417, 0, 1),
  (1071434, 1, 1),
  (1071503, 0, 2),
  (1074034, 1, 1),
  (1079011, 1, 2),
  (1079310, 2, 1),
  (1080178, 1, 0),
  (1082719, 0, 1),
  (1084899, 2, 0),
  (1085397, 3, 2),
  (1089297, 0, 0),
  (1089336, 1, 1),
  (1090448, 3, 1),
  (1090805, 0, 1),
  (1093835, 2, 2),
  (1094214, 1, 0),
  (1095587, 0, 0),
  (1100585, 1, 2),
  (1103791, 2, 0),
  (1104704, 0, 0),
  (1106516, 0, 1),
  (1106793, 1, 0),
  (1108963, 1, 2),
  (1111554, 1, 2),
  (1111928, 0, 1),
  (1114525, 1, 2),
  (1114888, 3, 2),
  (1115982, 0, 0),
  (1116438, 0, 0),
  (1120424, 3, 1),
  (1124239, 2, 2),
  (1124392, 3, 1),
  (1125030, 3, 1),
  (1125834, 1, 0),
  (1127839, 1, 1),
  (1132227, 0, 2),
  (1132267, 0, 2),
  (1138343, 0, 1),
  (1139114, 1, 2),
  (1146552, 0, 0),
  (1148015, 0, 1),
  (1148878, 2, 2),
  (1149814, 2, 1),
  (1150767, 2, 0),
  (1150954, 0, 0),
  (1151090, 2, 1),
  (1151488, 2, 0),
  (1153308, 3, 0),
  (1153667, 3, 1),
  (1154117, 3, 2),
  (1154544, 0, 1),
  (1154632, 3, 2),
  (1155382, 3, 0),
  (1155601, 0, 0),
  (1157178, 0, 0),
  (1160715, 1, 0),
  (1162455, 2, 1),
  (1163071, 3, 0),
  (1165144, 2, 1),
  (1165727, 2, 0),
  (1166564, 2, 0),
  (1170699, 1, 2),
  (1171734, 2, 0),
  (1172506, 2, 2),
  (1173361, 3, 1),
  (1173425, 2, 2),
  (1173881, 3, 1),
  (1177588, 0, 1),
  (1178218, 3, 1),
  (1180238, 2, 0),
  (1185648, 2, 1),
  (1187634, 2, 2),
  (1192744, 1, 0),
  (1194859, 3, 2),
  (1195449, 1, 0),
  (1197478, 0, 0),
  (1197654, 1, 2),
  (1200464, 3, 0),
  (1201565, 3, 2),
  (1208614, 0, 2),
  (1213616, 3, 1),
  (1214340, 2, 2),
  (1218868, 2, 1),
  (1221822, 1, 1),
  (1223581, 1, 0),
  (1223871, 3, 1),
  (1224286, 3, 1),
  (1224751, 1, 1),
  (1226345, 0, 0),
  (1227191, 2, 0),
  (1228712, 0, 1),
  (1229079, 0, 0),
  (1229984, 3, 0),
  (1230234, 1, 0),
  (1235025, 3, 1),
  (1237575, 0, 0),
  (1242771, 3, 2),
  (1242832, 0, 2),
  (1243811, 1, 2),
  (1246027, 3, 2),
  (1247094, 2, 2),
  (1247302, 2, 1),
  (1248402, 0, 0),
  (1250603, 2, 1),
  (1252125, 0, 2),
  (1253658, 3, 2),
  (1256941, 3, 0),
  (1261121, 0, 2),
  (1262280, 3, 2),
  (1265886, 2, 0),
  (1271214, 3, 2),
  (1278911, 3, 2),
  (1280314, 0, 1),
  (1281533, 2, 1),
  (1283215, 2, 2),
  (1284972, 2, 2),
  (1285215, 0, 1),
  (1287799, 1, 0),
  (1289091, 0, 1),
  (1294474, 0, 1),
  (1294842, 0, 1),
  (1295836, 2, 0),
  (1300777, 0, 1),
  (1302982, 0, 1),
  (1304424, 2, 1),
  (1306395, 2, 0),
  (1308637, 3, 2),
  (1309178, 1, 0),
  (1309214, 0, 1),
  (1310689, 0, 1),
  (1311346, 2, 1),
  (1313027, 2, 1),
  (1318184, 0, 2),
  (1324736, 2, 0),
  (1324987, 3, 2),
  (1326151, 0, 1),
  (1330977, 0, 2),
  (1332894, 3, 1),
  (1332973, 2, 2),
  (1334096, 2, 2),
  (1334550, 1, 2),
  (1337837, 2, 2),
  (1339450, 2, 0),
  (1339953, 1, 1),
  (1340706, 2, 1),
  (1341815, 1, 0),
  (1342156, 3, 0),
  (1343303, 2, 0),
  (1344658, 2, 0),
  (1344744, 2, 1),
  (1346529, 3, 1),
  (1349223, 1, 1),
  (1349488, 1, 0),
  (1350817, 0, 1),
  (1352788, 2, 2),
  (1353269, 2, 0),
  (1354951, 3, 1),
  (1355166, 2, 0),
  (1355470, 3, 2),
  (1355747, 1, 1),
  (1356917, 1, 1),
  (1357108, 3, 2),
  (1370112, 3, 0),
  (1370909, 2, 1),
  (1374276, 0, 1),
  (1374390, 0, 2),
  (1374584, 2, 0),
  (1377283, 0, 2),
  (1379582, 0, 2),
  (1381324, 0, 0),
  (1388706, 0, 2),
  (1389983, 3, 2),
  (1393606, 3, 1),
  (1395467, 1, 1),
  (1397019, 1, 0),
  (1400562, 2, 2),
  (1407211, 0, 2),
  (1408972, 1, 2),
  (1411840, 0, 2),
  (1414105, 3, 1),
  (1414210, 2, 0),
  (1415781, 2, 2),
  (1416347, 1, 2),
  (1416429, 3, 1),
  (1417915, 1, 0),
  (1418233, 1, 1),
  (1420039, 3, 1),
  (1421157, 1, 0),
  (1423745, 2, 2),
  (1428149, 2, 2),
  (1431884, 2, 1),
  (1432875, 1, 1),
  (1433278, 3, 0),
  (1435497, 1, 2),
  (1437815, 3, 0),
  (1438193, 0, 2),
  (1438556, 1, 1),
  (1439436, 2, 0),
  (1440149, 1, 2),
  (1441287, 0, 2),
  (1443344, 3, 2),
  (1443937, 1, 1),
  (1445010, 1, 0),
  (1445733, 0, 1),
  (1448127, 1, 1),
  (1448524, 1, 0),
  (1448771, 2, 1),
  (1449803, 3, 2),
  (1451974, 0, 2),
  (1454498, 1, 2),
  (1459008, 2, 0),
  (1463586, 2, 2),
  (1466322, 1, 1),
  (1466794, 2, 0),
  (1468726, 2, 0),
  (1473128, 3, 0),
  (1473371, 0, 2),
  (1473716, 1, 0),
  (1474330, 0, 1),
  (1477008, 0, 1),
  (1477290, 1, 0),
  (1478435, 0, 2),
  (1481886, 2, 0),
  (1483701, 0, 0),
  (1489069, 3, 0),
  (1489108, 2, 0),
  (1490327, 2, 2),
  (1491514, 1, 1),
  (1494526, 3, 0),
  (1500764, 0, 2),
  (1500924, 1, 0),
  (1501775, 0, 2),
  (1504743, 2, 0),
  (1505867, 1, 2),
  (1506991, 3, 1),
  (1510944, 2, 1),
  (1511194, 0, 2),
  (1512932, 0, 0),
  (1516406, 1, 2),
  (1519426, 1, 2),
  (1520342, 3, 1),
  (1521655, 2, 1),
  (1524357, 2, 1),
  (1527717, 2, 2),
  (1528344, 2, 0),
  (1532192, 0, 2),
  (1535962, 1, 2),
  (1537468, 2, 1),
  (1539410, 0, 2),
  (1544711, 1, 2),
  (1546166, 0, 1),
  (1546252, 0, 1),
  (1546725, 0, 2),
  (1550673, 1, 0),
  (1553589, 0, 1),
  (1553820, 2, 1),
  (1555540, 2, 1),
  (1555943, 0, 1),
  (1557098, 1, 1),
  (1557177, 1, 1),
  (1558135, 0, 0),
  (1562274, 3, 2),
  (1564730, 0, 1),
  (1565634, 0, 1),
  (1570502, 3, 0),
  (1570622, 2, 1),
  (1573062, 2, 1),
  (1574014, 0, 2),
  (1579347, 2, 0),
  (1586265, 1, 1),
  (1590808, 0, 1),
  (1591900, 2, 2),
  (1592597, 0, 2),
  (1593439, 0, 2),
  (1593540, 2, 0),
  (1594923, 3, 2),
  (1595001, 3, 1),
  (1596059, 1, 0),
  (1601682, 3, 1),
  (1602514, 2, 1),
  (1603474, 3, 0),
  (1606123, 1, 2),
  (1608764, 0, 1),
  (1611392, 2, 0),
  (1611730, 2, 0),
  (1614005, 2, 0),
  (1616047, 3, 0),
  (1616717, 1, 1),
  (1619493, 2, 0),
  (1620347, 0, 2),
  (1621648, 1, 2),
  (1628768, 0, 2),
  (1629062, 2, 2),
  (1629731, 2, 2),
  (1631434, 1, 1),
  (1631579, 0, 0),
  (1633579, 0, 0),
  (1634082, 3, 1),
  (1639609, 3, 2),
  (1641300, 0, 2),
  (1647547, 2, 1),
  (1648925, 3, 2),
  (1658584, 2, 2),
  (1659977, 1, 1),
  (1660102, 3, 2),
  (1660603, 1, 1),
  (1661211, 0, 1),
  (1662456, 1, 1),
  (1666771, 0, 2),
  (1668542, 2, 1),
  (1668770, 0, 1),
  (1672341, 0, 2),
  (1676667, 3, 1),
  (1677343, 0, 0),
  (1678024, 0, 2),
  (1678244, 0, 2),
  (1679349, 0, 2),
  (1681384, 1, 0),
  (1683004, 1, 0),
  (1684452, 3, 2),
  (1684866, 3, 0),
  (1684922, 2, 1),
  (1686600, 2, 1),
  (1689563, 2, 2),
  (1692065, 1, 1),
  (1693410, 0, 2),
  (1695013, 1, 2),
  (1696703, 0, 0),
  (1697420, 2, 2),
  (1697939, 2, 1),
  (1699910, 1, 1),
  (1700844, 2, 1),
  (1704589, 3, 2),
  (1708958, 1, 2),
  (1709329, 0, 0),
  (1710083, 0, 0),
  (1712519, 0, 0),
  (1713174, 2, 1),
  (1716340, 2, 0),
  (1717596, 3, 2),
  (1718535, 3, 2),
  (1719607, 2, 1),
  (1720885, 0, 2),
  (1723186, 0, 2),
  (1725938, 0, 2),
  (1727244, 2, 2),
  (1729074, 0, 1),
  (1730900, 3, 2),
  (1736242, 0, 0),
  (1736364, 3, 0),
  (1737596, 0, 2),
  (1741751, 0, 2),
  (1743423, 1, 1),
  (1745251, 3, 2),
  (1745929, 1, 2),
  (1746978, 0, 2),
  (1747164, 3, 1),
  (1748395, 1, 2),
  (1748419, 1, 0),
  (1748430, 2, 1),
  (1749719, 0, 0),
  (1755067, 1, 1),
  (1756878, 2, 2),
  (1759138, 0, 1),
  (1760418, 2, 2),
  (1765433, 2, 1),
  (1768013, 1, 2),
  (1771021, 2, 1),
  (1773526, 1, 2),
  (1773886, 1, 1),
  (1779216, 3, 1),
  (1779389, 3, 0),
  (1780603, 2, 0),
  (1780611, 3, 1),
  (1781452, 3, 0),
  (1786426, 2, 2),
  (1790745, 2, 0),
  (1791969, 1, 0),
  (1793847, 0, 2),
  (1797970, 3, 0),
  (1800767, 0, 1),
  (1808084, 2, 0),
  (1812145, 2, 1),
  (1813282, 0, 1),
  (1815435, 1, 1),
  (1817599, 2, 1),
  (1820975, 2, 2),
  (1821405, 3, 1),
  (1823299, 2, 0),
  (1823867, 3, 0),
  (1825366, 2, 2),
  (1825445, 1, 0),
  (1828642, 0, 0),
  (1830333, 1, 0),
  (1830558, 3, 2),
  (1839343, 2, 1),
  (1842989, 3, 2),
  (1843583, 1, 1),
  (1845617, 0, 1),
  (1849740, 1, 0),
  (1852040, 1, 1),
  (1852042, 2, 2),
  (1852410, 3, 2),
  (1855618, 3, 1),
  (1855720, 1, 1),
  (1856084, 2, 2),
  (1858128, 1, 0),
  (1858836, 3, 2),
  (1864021, 3, 2),
  (1864557, 2, 0),
  (1864587, 0, 1),
  (1865115, 3, 2),
  (1868132, 1, 0),
  (1868657, 2, 2),
  (1868976, 3, 1),
  (1872880, 2, 0),
  (1874509, 3, 2),
  (1875296, 3, 2),
  (1876875, 1, 0),
  (1879426, 1, 0),
  (1881050, 3, 1),
  (1885394, 1, 0),
  (1890178, 0, 2),
  (1890733, 2, 1),
  (1893049, 2, 2),
  (1893247, 3, 1),
  (1894005, 2, 1),
  (1894571, 1, 0),
  (1897837, 2, 0),
  (1898996, 3, 1),
  (1899873, 2, 1),
  (1900574, 0, 1),
  (1901561, 3, 2),
  (1901696, 0, 2),
  (1905973, 2, 2),
  (1907581, 3, 1),
  (1910709, 1, 1),
  (1910980, 1, 2),
  (1913173, 2, 1),
  (1913408, 0, 1),
  (1914084, 1, 2),
  (1914153, 3, 1),
  (1914663, 3, 2),
  (1916488, 3, 1),
  (1925684, 2, 1),
  (1928293, 0, 0),
  (1929549, 1, 2),
  (1931413, 1, 1),
  (1932713, 2, 2),
  (1933782, 1, 2),
  (1940853, 1, 2),
  (1941559, 3, 1),
  (1942652, 1, 1),
  (1943045, 0, 0),
  (1945914, 1, 1),
  (1946068, 1, 0),
  (1947191, 3, 1),
  (1949768, 1, 1),
  (1950485, 2, 1),
  (1953970, 2, 0),
  (1958289, 1, 0),
  (1959938, 1, 1),
  (1961707, 0, 0),
  (1964448, 0, 1),
  (1966215, 2, 2),
  (1966394, 1, 2),
  (1968851, 2, 0),
  (1970331, 3, 0),
  (1971087, 0, 1),
  (1972522, 2, 0),
  (1972619, 3, 2),
  (1972728, 2, 2),
  (1974665, 1, 2),
  (1975852, 0, 0),
  (1976195, 0, 1),
  (1977409, 3, 0),
  (1979903, 0, 1),
  (1980131, 2, 0),
  (1982038, 3, 2),
  (1983960, 2, 1),
  (1984438, 1, 2),
  (1990861, 3, 0),
  (1992773, 3, 2),
  (1997693, 1, 2),
  (1998222, 0, 2),
  (1998771, 2, 0),
  (2004349, 2, 1),
  (2004518, 2, 1),
  (2009545, 0, 1),
  (2010909, 2, 1),
  (2011589, 3, 1),
  (2012473, 3, 0),
  (2012626, 0, 0),
  (2012983, 2, 2),
  (2019984, 0, 2),
  (2020999, 3, 2),
  (2021403, 1, 2),
  (2028546, 1, 1),
  (2028709, 2, 0),
  (2029797, 0, 1),
  (2030383, 1, 0),
  (2039469, 2, 0),
  (2042401, 0, 2),
  (2042415, 0, 2),
  (2051098, 3, 0),
  (2054704, 1, 1),
  (2056090, 0, 0),
  (2059490, 1, 2),
  (2060900, 3, 2),
  (2060905, 1, 1),
  (2061074, 2, 1),
  (2063033, 2, 2),
  (2063263, 1, 0),
  (2063482, 0, 1),
  (2063796, 1, 1),
  (2064262, 1, 1),
  (2064272, 3, 0),
  (2064812, 1, 2),
  (2067168, 0, 0),
  (2069772, 0, 2),
  (2071372, 1, 1),
  (2074008, 2, 0),
  (2077178, 2, 0),
  (2078051, 3, 0),
  (2078056, 0, 0),
  (2078230, 1, 0),
  (2078817, 3, 0),
  (2078827, 3, 1),
  (2081238, 1, 2),
  (2082858, 2, 2),
  (2083149, 0, 1),
  (2084317, 0, 0),
  (2089766, 3, 0),
  (2091913, 3, 1),
  (2093729, 1, 2),
  (2096205, 3, 0),
  (2096559, 3, 2),
  (2097061, 1, 2),
  (2098476, 1, 2),
  (2099117, 0, 1),
  (2099336, 1, 2),
  (2100733, 0, 2),
  (2101634, 0, 1),
  (2103798, 3, 0),
  (2104386, 3, 1),
  (2105379, 2, 0),
  (2108636, 2, 0),
  (2111304, 2, 2),
  (2114686, 1, 2),
  (2116813, 3, 2),
  (2117316, 2, 1),
  (2118124, 2, 0),
  (2124426, 0, 1),
  (2126492, 0, 1),
  (2126704, 3, 1),
  (2132862, 2, 2),
  (2132890, 1, 1),
  (2133009, 3, 1),
  (2134365, 3, 1),
  (2136039, 0, 2),
  (2136955, 1, 0),
  (2138897, 1, 0),
  (2138945, 0, 0),
  (2140200, 2, 2),
  (2141827, 3, 2),
  (2142241, 0, 2),
  (2143169, 3, 0),
  (2144733, 2, 1),
  (2147714, 1, 1),
  (2152139, 2, 0),
  (2154307, 1, 2),
  (2154605, 3, 0),
  (2156628, 2, 0),
  (2160581, 1, 1),
  (2161081, 0, 1),
  (2165082, 1, 0),
  (2166927, 3, 1),
  (2167714, 0, 2),
  (2169567, 3, 2),
  (2170897, 0, 1),
  (2171659, 1, 2),
  (2171841, 1, 2),
  (2174981, 2, 2),
  (2175377, 2, 0),
  (2177226, 1, 1),
  (2179751, 3, 1),
  (2181650, 1, 2),
  (2182871, 3, 0),
  (2184562, 3, 2),
  (2185947, 3, 0),
  (2188105, 3, 0),
  (2188204, 1, 0),
  (2188487, 1, 0),
  (2188981, 1, 0),
  (2190692, 0, 1),
  (2199709, 0, 0),
  (2206834, 3, 2),
  (2210570, 3, 0),
  (2216982, 0, 2),
  (2218869, 2, 0),
  (2221192, 3, 0),
  (2222973, 3, 2),
  (2223656, 1, 2),
  (2225558, 1, 2),
  (2227994, 0, 2),
  (2231366, 3, 0),
  (2238698, 0, 2),
  (2239798, 3, 1),
  (2244058, 2, 1),
  (2246630, 2, 2),
  (2247521, 1, 1),
  (2248032, 2, 1),
  (2251126, 2, 2),
  (2251277, 0, 0),
  (2255659, 0, 1),
  (2257775, 1, 2),
  (2259444, 3, 1),
  (2261955, 2, 1),
  (2265392, 1, 2),
  (2265813, 1, 2),
  (2267407, 0, 2),
  (2271534, 3, 1),
  (2271946, 2, 1),
  (2273579, 3, 2),
  (2274540, 0, 1),
  (2276106, 3, 2),
  (2276657, 2, 0),
  (2279848, 3, 1),
  (2280513, 3, 0),
  (2281246, 3, 2),
  (2286367, 3, 2),
  (2286622, 3, 1),
  (2287029, 3, 0),
  (2287701, 2, 1),
  (2288678, 2, 0),
  (2291000, 0, 2),
  (2291479, 0, 2),
  (2293503, 0, 0),
  (2293874, 2, 2),
  (2297866, 2, 0),
  (2301700, 1, 1),
  (2303148, 2, 2),
  (2304926, 2, 1),
  (2310636, 3, 1),
  (2313617, 2, 2),
  (2314197, 0, 1),
  (2314897, 0, 0),
  (2317221, 2, 0),
  (2319968, 0, 1),
  (2326298, 1, 2),
  (2327969, 0, 1),
  (2328872, 1, 1),
  (2333424, 3, 0),
  (2335196, 0, 2),
  (2339605, 2, 1),
  (2340326, 2, 0),
  (2342826, 1, 2),
  (2346026, 1, 0),
  (2346499, 2, 1),
  (2348562, 3, 1),
  (2350395, 2, 1),
  (2357428, 3, 0),
  (2357890, 3, 0),
  (2359014, 1, 1),
  (2359271, 3, 1),
  (2361398, 1, 2),
  (2362336, 2, 1),
  (2362702, 3, 0),
  (2363599, 3, 1),
  (2365574, 3, 2),
  (2369447, 0, 2),
  (2376365, 2, 2),
  (2377040, 0, 0),
  (2378144, 3, 2),
  (2387951, 2, 0),
  (2389042, 0, 0),
  (2389398, 3, 2),
  (2390296, 1, 1),
  (2393665, 2, 2),
  (2396118, 1, 2),
  (2397389, 0, 0),
  (2399247, 3, 0),
  (2404270, 2, 2),
  (2404490, 2, 1),
  (2404522, 2, 1),
  (2405716, 0, 2),
  (2412853, 2, 1),
  (2413259, 0, 2),
  (2413486, 0, 2),
  (2415293, 2, 1),
  (2418432, 0, 2),
  (2418735, 0, 1),
  (2422788, 0, 0),
  (2425915, 2, 0),
  (2427995, 0, 2),
  (2428827, 1, 2),
  (2429068, 2, 1),
  (2432197, 2, 1),
  (2432340, 1, 1),
  (2434442, 3, 1),
  (2436188, 2, 0),
  (2438675, 3, 2),
  (2439558, 2, 1),
  (2441566, 2, 1),
  (2442186, 0, 1),
  (2442569, 1, 1),
  (2448563, 3, 0),
  (2450177, 0, 2),
  (2454987, 0, 0),
  (2455082, 2, 0),
  (2456329, 2, 2),
  (2457045, 2, 2),
  (2457127, 1, 1),
  (2458437, 3, 0),
  (2459772, 1, 0),
  (2463723, 0, 1),
  (2464921, 3, 1),
  (2465924, 1, 1),
  (2467144, 3, 0),
  (2467758, 2, 0),
  (2468957, 0, 1),
  (2470303, 0, 0),
  (2473494, 2, 1),
  (2476456, 3, 2),
  (2477685, 3, 2),
  (2478005, 0, 2),
  (2481145, 0, 1),
  (2486573, 1, 0),
  (2490265, 0, 1),
  (2494971, 1, 0),
  (2496507, 2, 2),
  (2496896, 1, 1),
  (2496906, 1, 2),
  (2500070, 0, 2),
  (2508536, 1, 2),
  (2509715, 3, 2),
  (2510741, 3, 2),
  (2516230, 1, 1),
  (2516330, 3, 0),
  (2517533, 0, 0),
  (2519922, 0, 2),
  (2521676, 0, 0),
  (2523931, 3, 1),
  (2525143, 2, 1),
  (2525221, 1, 2),
  (2527790, 0, 1),
  (2530548, 3, 1),
  (2530968, 1, 2),
  (2532669, 2, 0),
  (2536456, 2, 2),
  (2536697, 1, 0),
  (2536978, 0, 2),
  (2537359, 1, 1),
  (2537656, 0, 1),
  (2537827, 3, 0),
  (2538396, 1, 1),
  (2541108, 2, 1),
  (2542416, 1, 1),
  (2542712, 2, 2),
  (2542782, 1, 1),
  (2543728, 1, 2),
  (2544204, 1, 2),
  (2546278, 1, 1),
  (2550609, 3, 0),
  (2552557, 3, 1),
  (2553041, 1, 1),
  (2554396, 2, 0),
  (2556280, 0, 1),
  (2559107, 2, 2),
  (2560344, 0, 0),
  (2561599, 1, 2),
  (2561714, 3, 1),
  (2566154, 3, 1),
  (2567547, 0, 0),
  (2570516, 2, 2),
  (2572106, 1, 0),
  (2572138, 1, 2),
  (2572949, 2, 1),
  (2578074, 1, 1),
  (2579952, 2, 2),
  (2580747, 1, 1),
  (2581679, 1, 0),
  (2581705, 3, 0),
  (2582723, 0, 2),
  (2585464, 1, 2),
  (2585624, 2, 0),
  (2585651, 1, 0),
  (2585897, 0, 2),
  (2586750, 1, 1),
  (2586947, 3, 2),
  (2587530, 1, 2),
  (2589074, 0, 2),
  (2591594, 3, 1),
  (2593127, 2, 0),
  (2593286, 2, 1),
  (2594552, 2, 1),
  (2594953, 1, 0),
  (2596139, 3, 2),
  (2597513, 1, 0),
  (2599459, 1, 2),
  (2602633, 1, 1),
  (2605425, 3, 2),
  (2607876, 0, 1),
  (2609790, 1, 2),
  (2611394, 3, 1),
  (2613748, 2, 1),
  (2616579, 2, 0),
  (2616893, 1, 2),
  (2618159, 3, 1),
  (2621409, 1, 1),
  (2622469, 1, 1),
  (2625140, 1, 0),
  (2626241, 3, 0),
  (2630912, 2, 0),
  (2632832, 0, 1),
  (2632896, 2, 2),
  (2637421, 2, 1),
  (2645698, 1, 1),
  (2646551, 1, 2),
  (2647606, 1, 1),
  (2651018, 2, 2),
  (2651338, 0, 0),
  (2653057, 1, 0),
  (2654550, 1, 1),
  (2657190, 1, 1),
  (2657227, 2, 1),
  (2658861, 2, 2),
  (2660801, 1, 0),
  (2660826, 3, 1),
  (2662716, 3, 0),
  (2664982, 3, 2),
  (2667124, 3, 0),
  (2667966, 3, 2),
  (2668179, 0, 2),
  (2668964, 1, 1),
  (2670438, 2, 1),
  (2670836, 0, 0),
  (2671788, 3, 1),
  (2672323, 1, 1),
  (2673535, 2, 1),
  (2675890, 2, 1),
  (2681308, 1, 0),
  (2681397, 3, 1),
  (2682396, 0, 2),
  (2683055, 2, 2),
  (2689627, 0, 0),
  (2691678, 0, 0),
  (2692825, 1, 1),
  (2699537, 3, 2),
  (2699853, 0, 0),
  (2702577, 1, 2),
  (2708321, 1, 1),
  (2709522, 2, 2),
  (2709585, 0, 0),
  (2715041, 1, 2),
  (2718902, 2, 1),
  (2725049, 2, 2),
  (2725471, 1, 2),
  (2729022, 0, 0),
  (2732838, 3, 2),
  (2733382, 0, 2),
  (2739582, 1, 0),
  (2740079, 0, 0),
  (2749916, 3, 0),
  (2758054, 3, 2),
  (2758326, 0, 0),
  (2763757, 0, 0),
  (2765483, 3, 0),
  (2767960, 2, 0),
  (2768750, 2, 2),
  (2776795, 3, 1),
  (2778527, 1, 1),
  (2781377, 2, 2),
  (2781490, 3, 2),
  (2782260, 3, 0),
  (2782378, 3, 2),
  (2784649, 3, 0),
  (2786304, 1, 2),
  (2788959, 1, 1),
  (2789367, 2, 2),
  (2789555, 2, 1),
  (2793467, 2, 0),
  (2793506, 2, 0),
  (2795069, 0, 2),
  (2797426, 3, 2),
  (2800652, 3, 1),
  (2801808, 1, 2),
  (2804755, 1, 0),
  (2809912, 1, 2),
  (2813447, 0, 0),
  (2814052, 3, 1),
  (2814079, 1, 2),
  (2814266, 3, 0),
  (2815507, 1, 1),
  (2816063, 0, 1),
  (2822099, 3, 2),
  (2824164, 1, 1),
  (2824599, 1, 0),
  (2824796, 2, 2),
  (2832126, 0, 1),
  (2832653, 2, 2),
  (2833755, 2, 0),
  (2836459, 2, 1),
  (2836696, 0, 0),
  (2839123, 0, 1),
  (2840371, 2, 2),
  (2842239, 2, 2),
  (2844743, 2, 1),
  (2849864, 2, 2),
  (2851447, 3, 2),
  (2851986, 2, 2),
  (2853862, 1, 0),
  (2854519, 0, 2),
  (2856523, 0, 1),
  (2858330, 2, 0),
  (2860834, 3, 1),
  (2862009, 3, 1),
  (2862692, 2, 1),
  (2863425, 1, 0),
  (2864364, 3, 0),
  (2864909, 3, 2),
  (2865185, 0, 1),
  (2866629, 2, 2),
  (2872054, 1, 2),
  (2879269, 0, 1),
  (2880311, 2, 1),
  (2881782, 2, 1),
  (2883648, 2, 2),
  (2884489, 2, 0),
  (2885957, 2, 2),
  (2890443, 1, 0),
  (2890706, 1, 2),
  (2895743, 2, 1),
  (2898571, 1, 0),
  (2905462, 0, 2),
  (2906300, 3, 2),
  (2910516, 2, 0),
  (2914965, 0, 2),
  (2916075, 2, 1),
  (2917804, 1, 2),
  (2920177, 3, 0),
  (2924295, 0, 1),
  (2925350, 1, 2),
  (2925612, 1, 0),
  (2927044, 3, 2),
  (2929502, 2, 2),
  (2931771, 0, 0),
  (2932248, 1, 1),
  (2936325, 0, 0),
  (2936860, 1, 1),
  (2937543, 3, 1),
  (2939423, 0, 1),
  (2941279, 1, 0),
  (2944744, 1, 1),
  (2945166, 3, 1),
  (2947027, 0, 2),
  (2948176, 1, 1),
  (2948264, 0, 0),
  (2950283, 1, 1),
  (2950430, 2, 2),
  (2953473, 0, 2),
  (2954304, 0, 2),
  (2954580, 1, 0),
  (2957347, 1, 1),
  (2959506, 1, 2),
  (2959592, 2, 0),
  (2962994, 2, 0),
  (2965178, 0, 1),
  (2965841, 1, 2),
  (2965900, 3, 0),
  (2971760, 2, 2),
  (2972203, 1, 1),
  (2972356, 0, 2),
  (2982676, 3, 0),
  (2984249, 0, 1),
  (2984410, 1, 0),
  (2986828, 1, 0),
  (2990822, 0, 1),
  (2995141, 0, 2),
  (2996679, 2, 1),
  (2997937, 3, 0),
  (3008629, 3, 2),
  (3008667, 0, 2),
  (3009551, 3, 0),
  (3012014, 0, 1),
  (3014287, 2, 1),
  (3014732, 0, 0),
  (3015896, 2, 2),
  (3020453, 0, 1),
  (3020600, 1, 0),
  (3020886, 3, 2),
  (3021571, 2, 1),
  (3021661, 0, 2),
  (3021950, 2, 2),
  (3022760, 3, 1),
  (3024002, 1, 0),
  (3025106, 3, 1),
  (3031203, 2, 1),
  (3034736, 0, 1),
  (3038041, 1, 2),
  (3043178, 3, 1),
  (3045604, 2, 2),
  (3046421, 3, 0),
  (3048825, 1, 1),
  (3053726, 0, 0),
  (3054672, 2, 2),
  (3058174, 0, 1),
  (3059968, 3, 2),
  (3064561, 3, 0),
  (3064735, 0, 2),
  (3067632, 1, 0),
  (3069553, 3, 1),
  (3070216, 2, 1),
  (3072218, 3, 2),
  (3080532, 3, 1),
  (3081827, 0, 0),
  (3082310, 3, 0),
  (3082969, 0, 1),
  (3084626, 1, 2),
  (3084711, 1, 1),
  (3088608, 3, 0),
  (3091221, 2, 0),
  (3092114, 1, 0),
  (3096558, 0, 0),
  (3098445, 1, 2),
  (3098674, 3, 2),
  (3099114, 2, 2),
  (3100018, 1, 2),
  (3105338, 0, 1),
  (3108942, 2, 2),
  (3112936, 2, 1),
  (3113428, 2, 0),
  (3113964, 0, 2),
  (3116672, 2, 2),
  (3117455, 1, 2),
  (3119713, 0, 1),
  (3123138, 0, 1),
  (3124608, 0, 0),
  (3126585, 2, 2),
  (3126967, 3, 0),
  (3127192, 1, 2),
  (3128524, 3, 1),
  (3132688, 1, 2),
  (3136665, 0, 2),
  (3143761, 1, 2),
  (3144072, 0, 2),
  (3145117, 2, 2),
  (3148189, 0, 0),
  (3156779, 0, 0),
  (3157631, 1, 0),
  (3159408, 1, 1),
  (3162037, 0, 2),
  (3162581, 0, 1),
  (3163895, 3, 1),
  (3166491, 2, 2),
  (3167966, 2, 0),
  (3168370, 2, 0),
  (3170011, 2, 2),
  (3171873, 2, 1),
  (3173081, 2, 0),
  (3173390, 2, 0),
  (3174989, 0, 2),
  (3175479, 1, 1),
  (3176331, 1, 0),
  (3176483, 3, 1),
  (3183343, 1, 2),
  (3183668, 2, 1),
  (3184284, 3, 0),
  (3189057, 3, 1),
  (3193991, 0, 0),
  (3195975, 1, 2),
  (3196367, 2, 2),
  (3197334, 1, 2),
  (3200010, 0, 1),
  (3211152, 0, 2),
  (3212119, 0, 2),
  (3213312, 2, 0),
  (3214837, 3, 2),
  (3221742, 3, 1),
  (3221854, 1, 1),
  (3223589, 1, 0),
  (3224405, 1, 0),
  (3224738, 3, 0),
  (3225140, 3, 1),
  (3225360, 0, 1),
  (3234767, 2, 1),
  (3238876, 3, 2),
  (3239796, 1, 2),
  (3245700, 3, 0),
  (3247393, 2, 0),
  (3251227, 1, 0),
  (3253333, 0, 1),
  (3256003, 2, 1),
  (3256375, 2, 2),
  (3258656, 0, 2),
  (3260291, 1, 1),
  (3260514, 2, 1),
  (3263581, 0, 2),
  (3266391, 3, 2),
  (3267449, 2, 2),
  (3270626, 1, 1),
  (3272198, 3, 2),
  (3274223, 2, 2),
  (3274967, 2, 2),
  (3278325, 0, 1),
  (3279745, 2, 0),
  (3280341, 1, 0),
  (3282927, 3, 1),
  (3285971, 1, 0),
  (3286798, 2, 1),
  (3288852, 3, 1),
  (3290254, 2, 0),
  (3293349, 2, 1),
  (3295092, 1, 0),
  (3295232, 3, 2),
  (3295474, 2, 0),
  (3298245, 3, 0),
  (3299498, 1, 2),
  (3299923, 0, 0),
  (3300738, 1, 1),
  (3300935, 3, 2),
  (3301623, 0, 0),
  (3303714, 0, 2),
  (3304276, 2, 2),
  (3306594, 3, 2),
  (3306844, 3, 1),
  (3307894, 1, 1),
  (3308063, 1, 2),
  (3310441, 0, 0),
  (3319177, 3, 0),
  (3321772, 1, 2),
  (3322859, 3, 2),
  (3323018, 1, 0),
  (3324484, 1, 1),
  (3326481, 1, 2),
  (3329469, 1, 2),
  (3335201, 0, 1),
  (3335684, 2, 1),
  (3338090, 0, 0),
  (3338680, 0, 2),
  (3339639, 1, 2),
  (3341098, 2, 2),
  (3342001, 2, 1),
  (3344559, 3, 2),
  (3345398, 0, 1),
  (3346030, 3, 2),
  (3346559, 2, 0),
  (3346589, 0, 1),
  (3348107, 2, 1),
  (3353304, 1, 0),
  (3354512, 2, 1),
  (3356995, 2, 1),
  (3361616, 3, 2),
  (3363477, 2, 0),
  (3365763, 2, 2),
  (3367293, 3, 2),
  (3368522, 2, 1),
  (3370279, 3, 1),
  (3374633, 3, 1),
  (3377284, 3, 2),
  (3385838, 3, 1),
  (3386996, 0, 0),
  (3387642, 2, 2),
  (3388510, 0, 0),
  (3391170, 1, 0),
  (3391432, 2, 2),
  (3392771, 0, 0),
  (3392774, 2, 1),
  (3393549, 1, 2),
  (3395464, 3, 2),
  (3396963, 1, 1),
  (3398664, 0, 0),
  (3407177, 3, 0),
  (3408666, 1, 2),
  (3409057, 3, 0),
  (3409071, 2, 1),
  (3411535, 0, 2),
  (3412759, 0, 2),
  (3418000, 2, 2),
  (3419215, 1, 0),
  (3419277, 0, 0),
  (3420717, 1, 0),
  (3423148, 2, 0),
  (3423238, 3, 1),
  (3428826, 0, 2),
  (3431738, 1, 1),
  (3432794, 1, 2),
  (3433977, 0, 2),
  (3436362, 3, 0),
  (3438576, 1, 1),
  (3439195, 1, 2),
  (3439455, 2, 1),
  (3442398, 0, 1),
  (3444037, 1, 0),
  (3445579, 3, 1),
  (3446634, 1, 1),
  (3448933, 2, 1),
  (3451575, 1, 0),
  (3456108, 3, 0),
  (3456563, 1, 2),
  (3456637, 0, 2),
  (3462143, 1, 2),
  (3464366, 0, 2),
  (3464583, 3, 1),
  (3464915, 0, 1),
  (3465962, 3, 1),
  (3467436, 3, 0),
  (3468123, 1, 0),
  (3471800, 0, 2),
  (3473451, 1, 1),
  (3473689, 1, 2),
  (3475057, 2, 2),
  (3479147, 2, 0),
  (3482365, 0, 1),
  (3483331, 3, 2),
  (3495820, 1, 2),
  (3495855, 2, 1),
  (3498662, 0, 2),
  (3500289, 2, 0),
  (3500837, 0, 1),
  (3501534, 0, 1),
  (3502309, 0, 1),
  (3504964, 2, 2),
  (3505487, 0, 0),
  (3508988, 2, 1),
  (3512081, 2, 0),
  (3512834, 2, 1),
  (3521607, 1, 2),
  (3529342, 3, 1),
  (3531872, 1, 2),
  (3534025, 0, 1),
  (3534496, 2, 0),
  (3534686, 0, 2),
  (3534932, 2, 2),
  (3535533, 3, 1),
  (3536077, 3, 1),
  (3536952, 1, 2),
  (3540323, 0, 0),
  (3542842, 3, 1),
  (3543847, 3, 1),
  (3546161, 2, 2),
  (3547352, 2, 0),
  (3553003, 1, 0),
  (3554292, 2, 2),
  (3555010, 1, 1),
  (3556949, 3, 0),
  (3557252, 0, 1),
  (3557301, 1, 1),
  (3557972, 1, 2),
  (3558324, 0, 1),
  (3558496, 2, 1),
  (3560531, 1, 0),
  (3563110, 3, 0),
  (3563228, 0, 0),
  (3563962, 3, 2),
  (3564375, 0, 0),
  (3564989, 1, 0),
  (3565426, 0, 0),
  (3566654, 1, 2),
  (3567937, 0, 0),
  (3569550, 0, 2),
  (3571099, 3, 0),
  (3571433, 2, 1),
  (3573088, 2, 0),
  (3573768, 0, 2),
  (3574551, 2, 1),
  (3574867, 1, 2),
  (3574895, 1, 1),
  (3575122, 3, 0),
  (3580548, 2, 0),
  (3581567, 2, 0),
  (3583002, 0, 0),
  (3584186, 0, 2),
  (3584681, 2, 0),
  (3587162, 0, 2),
  (3593775, 2, 1),
  (3597004, 0, 1),
  (3597385, 1, 2),
  (3598750, 3, 1),
  (3599767, 2, 1),
])
