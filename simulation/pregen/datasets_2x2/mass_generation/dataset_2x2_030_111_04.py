from util import *
schedule = deque([
  (1187, 7, 10),
  (2520, 8, 13),
  (2999, 0, 6),
  (3785, 8, 5),
  (11336, 5, 10),
  (16362, 3, 18),
  (17648, 0, 18),
  (18511, 0, 11),
  (19247, 7, 10),
  (19630, 6, 0),
  (19834, 2, 16),
  (21101, 6, 17),
  (23589, 4, 10),
  (24193, 5, 17),
  (28600, 4, 10),
  (29569, 2, 2),
  (31160, 4, 9),
  (31348, 3, 0),
  (31734, 1, 11),
  (37239, 3, 10),
  (38650, 5, 18),
  (41068, 10, 18),
  (42349, 9, 13),
  (47067, 3, 7),
  (54804, 3, 7),
  (56244, 10, 0),
  (57402, 2, 7),
  (57842, 7, 3),
  (57919, 0, 18),
  (58076, 7, 11),
  (60514, 2, 7),
  (61516, 4, 9),
  (62871, 5, 21),
  (64714, 6, 5),
  (66873, 6, 21),
  (67346, 7, 10),
  (70492, 2, 3),
  (71725, 0, 3),
  (73659, 6, 10),
  (75468, 6, 21),
  (77609, 2, 18),
  (78136, 2, 15),
  (80112, 11, 0),
  (86629, 10, 10),
  (88157, 3, 7),
  (89239, 5, 10),
  (90176, 3, 18),
  (90433, 5, 10),
  (90452, 7, 13),
  (90489, 3, 18),
  (91850, 3, 15),
  (95275, 4, 22),
  (95952, 4, 2),
  (97770, 2, 4),
  (98940, 8, 5),
  (100207, 8, 4),
  (101508, 11, 22),
  (102891, 7, 10),
  (103678, 7, 0),
  (104173, 7, 10),
  (105150, 5, 10),
  (105719, 11, 0),
  (106151, 0, 0),
  (106654, 4, 10),
  (106755, 9, 13),
  (107053, 3, 10),
  (107469, 3, 7),
  (107714, 1, 0),
  (111830, 0, 0),
  (112410, 7, 11),
  (118625, 4, 17),
  (121190, 5, 21),
  (121968, 8, 3),
  (123701, 9, 17),
  (123855, 0, 10),
  (133685, 9, 2),
  (133865, 5, 22),
  (135727, 3, 18),
  (136400, 4, 10),
  (136565, 3, 16),
  (142117, 6, 10),
  (142270, 9, 16),
  (143605, 9, 7),
  (144843, 6, 17),
  (152446, 4, 9),
  (154221, 5, 17),
  (155112, 10, 11),
  (157093, 9, 18),
  (163287, 10, 20),
  (165913, 4, 9),
  (167307, 2, 7),
  (167898, 4, 17),
  (171657, 10, 18),
  (172200, 9, 0),
  (172546, 3, 7),
  (175150, 11, 11),
  (175191, 11, 6),
  (176357, 2, 2),
  (176411, 6, 10),
  (177136, 4, 9),
  (178722, 4, 10),
  (181087, 1, 18),
  (181542, 3, 3),
  (182456, 0, 0),
  (183479, 0, 6),
  (184206, 6, 17),
  (187799, 5, 10),
  (193056, 10, 0),
  (193275, 4, 10),
  (197403, 11, 0),
  (200892, 5, 10),
  (206387, 3, 12),
  (209402, 5, 5),
  (210285, 5, 10),
  (216767, 5, 10),
  (219928, 10, 0),
  (222573, 2, 15),
  (223653, 1, 0),
  (224606, 5, 10),
  (225084, 9, 7),
  (227471, 9, 3),
  (231551, 4, 16),
  (233067, 3, 3),
  (235565, 6, 17),
  (236235, 6, 10),
  (237237, 4, 10),
  (237958, 3, 7),
  (239509, 5, 9),
  (241469, 8, 2),
  (247501, 0, 0),
  (247805, 7, 10),
  (248516, 6, 17),
  (250306, 7, 10),
  (254965, 2, 3),
  (259096, 5, 10),
  (259191, 3, 5),
  (259499, 10, 11),
  (263729, 0, 0),
  (266297, 10, 22),
  (270821, 10, 0),
  (271149, 9, 4),
  (275682, 0, 11),
  (281625, 2, 3),
  (283786, 4, 10),
  (284181, 11, 0),
  (284612, 11, 11),
  (284613, 4, 10),
  (286946, 3, 7),
  (302760, 9, 0),
  (303850, 11, 0),
  (309377, 11, 18),
  (312334, 2, 3),
  (313556, 10, 0),
  (314416, 1, 3),
  (316599, 5, 17),
  (317385, 8, 11),
  (319944, 5, 7),
  (323069, 11, 22),
  (323433, 0, 11),
  (323527, 2, 3),
  (323645, 9, 7),
  (324818, 2, 3),
  (327112, 8, 8),
  (327646, 5, 10),
  (333266, 5, 9),
  (334316, 7, 16),
  (336548, 3, 7),
  (338669, 0, 16),
  (339725, 3, 17),
  (345250, 11, 0),
  (346714, 5, 17),
  (347275, 11, 0),
  (349326, 10, 11),
  (350964, 10, 0),
  (351191, 9, 0),
  (351405, 3, 7),
  (352872, 5, 22),
  (353246, 4, 10),
  (353270, 5, 10),
  (353444, 8, 6),
  (353918, 6, 10),
  (354086, 2, 0),
  (356515, 10, 9),
  (356904, 9, 7),
  (357518, 7, 22),
  (358649, 0, 22),
  (365839, 8, 16),
  (368455, 7, 10),
  (371251, 0, 10),
  (376219, 0, 0),
  (379483, 3, 8),
  (385501, 5, 9),
  (387604, 6, 17),
  (388603, 8, 0),
  (395616, 11, 22),
  (395986, 6, 21),
  (397432, 5, 17),
  (397837, 11, 11),
  (399758, 7, 10),
  (407705, 11, 7),
  (410124, 10, 17),
  (411278, 6, 10),
  (411342, 10, 10),
  (411343, 5, 10),
  (411434, 0, 0),
  (418873, 10, 0),
  (420708, 11, 0),
  (423016, 8, 7),
  (423855, 11, 22),
  (424628, 3, 3),
  (425258, 9, 10),
  (430462, 11, 11),
  (438125, 1, 22),
  (440117, 9, 14),
  (440411, 5, 2),
  (440786, 7, 22),
  (442341, 8, 13),
  (444414, 9, 3),
  (445667, 4, 10),
  (447253, 10, 11),
  (450262, 7, 10),
  (456113, 8, 4),
  (458957, 4, 10),
  (459659, 5, 10),
  (459945, 11, 11),
  (461323, 2, 1),
  (465898, 6, 21),
  (467059, 1, 13),
  (469641, 2, 8),
  (470589, 10, 0),
  (471134, 6, 10),
  (481473, 11, 11),
  (481627, 3, 13),
  (482374, 3, 0),
  (484799, 8, 7),
  (487616, 5, 9),
  (491110, 8, 14),
  (493759, 0, 0),
  (496249, 2, 13),
  (497750, 10, 11),
  (497841, 9, 13),
  (500516, 4, 14),
  (506677, 6, 4),
  (507943, 2, 3),
  (508438, 3, 4),
  (508810, 7, 10),
  (509194, 10, 0),
  (514406, 0, 0),
  (519707, 1, 14),
  (520542, 11, 0),
  (530662, 7, 15),
  (531603, 10, 0),
  (533967, 10, 22),
  (534155, 11, 2),
  (535561, 9, 7),
  (540057, 11, 0),
  (542162, 5, 17),
  (545696, 2, 3),
  (547025, 9, 3),
  (548796, 3, 17),
  (551342, 0, 0),
  (553495, 0, 0),
  (555162, 3, 3),
  (556257, 4, 1),
  (556683, 1, 0),
  (558741, 11, 0),
  (562651, 4, 13),
  (565300, 4, 17),
  (565300, 10, 0),
  (567631, 0, 0),
  (571097, 5, 10),
  (578442, 1, 0),
  (580814, 5, 21),
  (582309, 2, 9),
  (592485, 2, 13),
  (593173, 6, 10),
  (594376, 7, 10),
  (597849, 4, 20),
  (611721, 4, 17),
  (612288, 11, 10),
  (616162, 3, 0),
  (619978, 6, 17),
  (620667, 1, 0),
  (623152, 0, 0),
  (624048, 0, 11),
  (626058, 8, 11),
  (627429, 1, 15),
  (628964, 6, 10),
  (630169, 7, 13),
  (630231, 0, 0),
  (631946, 1, 0),
  (635711, 1, 11),
  (639634, 11, 11),
  (642600, 5, 10),
  (644864, 5, 10),
  (645926, 10, 0),
  (649266, 11, 0),
  (652358, 6, 6),
  (655646, 1, 0),
  (659334, 5, 10),
  (660358, 3, 3),
  (662819, 7, 10),
  (663191, 4, 9),
  (664396, 6, 10),
  (666232, 1, 0),
  (667190, 0, 0),
  (667222, 0, 11),
  (667609, 8, 7),
  (669431, 8, 4),
  (669808, 3, 8),
  (671246, 1, 18),
  (672255, 10, 0),
  (673094, 9, 7),
  (675127, 8, 3),
  (677160, 11, 0),
  (680321, 7, 3),
  (681218, 8, 7),
  (683071, 8, 0),
  (683612, 8, 0),
  (684088, 11, 0),
  (689319, 11, 3),
  (690203, 3, 13),
  (690960, 8, 2),
  (691250, 11, 0),
  (694604, 3, 7),
  (695099, 4, 18),
  (695192, 11, 6),
  (695422, 7, 16),
  (696692, 9, 3),
  (697889, 11, 0),
  (700362, 6, 10),
  (700957, 1, 0),
  (702041, 9, 3),
  (702788, 1, 0),
  (704829, 1, 0),
  (709782, 10, 10),
  (711438, 3, 7),
  (718799, 10, 0),
  (719117, 11, 0),
  (720308, 5, 5),
  (720339, 8, 10),
  (722750, 8, 3),
  (727890, 8, 7),
  (728305, 8, 7),
  (728495, 7, 10),
  (729786, 8, 13),
  (730734, 7, 10),
  (732697, 0, 0),
  (733179, 4, 10),
  (733650, 2, 13),
  (735098, 1, 11),
  (735947, 7, 18),
  (741717, 2, 7),
  (742671, 1, 7),
  (753698, 9, 15),
  (754841, 7, 17),
  (756239, 8, 8),
  (756388, 7, 10),
  (757592, 0, 0),
  (757885, 5, 10),
  (759332, 3, 8),
  (760823, 11, 0),
  (763425, 11, 14),
  (764528, 7, 10),
  (768757, 4, 17),
  (770086, 6, 10),
  (771733, 8, 10),
  (772257, 2, 3),
  (774517, 10, 11),
  (775517, 3, 3),
  (778207, 2, 4),
  (779974, 1, 11),
  (784116, 2, 7),
  (786257, 7, 17),
  (786266, 0, 0),
  (786430, 5, 10),
  (788131, 7, 17),
  (788607, 5, 10),
  (790485, 9, 15),
  (791480, 0, 0),
  (793375, 10, 0),
  (793513, 5, 21),
  (793772, 0, 0),
  (794616, 10, 0),
  (800077, 7, 10),
  (803929, 6, 10),
  (804727, 6, 17),
  (806882, 6, 10),
  (808416, 6, 17),
  (810142, 2, 8),
  (810726, 0, 2),
  (812808, 0, 22),
  (818120, 10, 11),
  (821154, 6, 16),
  (826203, 10, 14),
  (826776, 8, 1),
  (834114, 5, 17),
  (834266, 10, 0),
  (835545, 5, 10),
  (836869, 7, 10),
  (839611, 9, 14),
  (839715, 1, 18),
  (841425, 1, 0),
  (841510, 3, 3),
  (844904, 8, 4),
  (848480, 11, 14),
  (848612, 9, 2),
  (849964, 3, 3),
  (850463, 9, 5),
  (856978, 5, 10),
  (857832, 11, 11),
  (860814, 8, 7),
  (867843, 4, 10),
  (871129, 1, 0),
  (880626, 8, 3),
  (882211, 8, 18),
  (882373, 1, 0),
  (883901, 0, 0),
  (884355, 8, 7),
  (892270, 8, 4),
  (893671, 10, 22),
  (894317, 1, 0),
  (894421, 10, 18),
  (895948, 4, 10),
  (900898, 0, 11),
  (906227, 11, 0),
  (906305, 11, 0),
  (908094, 6, 10),
  (914769, 9, 4),
  (919070, 5, 10),
  (920101, 3, 4),
  (921973, 2, 3),
  (923388, 3, 6),
  (923607, 2, 6),
  (931017, 0, 12),
  (937128, 8, 3),
  (938410, 7, 21),
  (939214, 0, 19),
  (944574, 7, 10),
  (945611, 0, 6),
  (946042, 2, 4),
  (949462, 2, 14),
  (951751, 1, 0),
  (953700, 6, 17),
  (956893, 3, 2),
  (961012, 1, 11),
  (962073, 4, 15),
  (963187, 7, 17),
  (963251, 0, 0),
  (967053, 6, 9),
  (969216, 0, 0),
  (969338, 6, 22),
  (972015, 2, 0),
  (972429, 9, 3),
  (973186, 0, 0),
  (973234, 3, 10),
  (973807, 9, 3),
  (973842, 6, 1),
  (977147, 5, 22),
  (979257, 1, 0),
  (979565, 2, 3),
  (982378, 6, 17),
  (984450, 5, 13),
  (988018, 9, 13),
  (991049, 6, 19),
  (991348, 1, 22),
  (994823, 1, 0),
  (995650, 10, 18),
  (996150, 8, 1),
  (998823, 9, 14),
  (999546, 9, 3),
  (1000467, 9, 3),
  (1002770, 1, 18),
  (1003228, 1, 18),
  (1004726, 9, 1),
  (1007253, 7, 10),
  (1013337, 5, 13),
  (1018374, 4, 17),
  (1018570, 0, 22),
  (1021551, 7, 17),
  (1021659, 2, 7),
  (1021702, 4, 10),
  (1022138, 10, 0),
  (1022198, 4, 17),
  (1024127, 9, 1),
  (1024602, 11, 0),
  (1029775, 7, 22),
  (1035441, 3, 13),
  (1040238, 1, 0),
  (1040399, 5, 6),
  (1041071, 11, 6),
  (1042512, 11, 14),
  (1047407, 9, 3),
  (1050259, 0, 5),
  (1052073, 11, 0),
  (1055094, 1, 0),
  (1055493, 8, 11),
  (1055703, 9, 7),
  (1057382, 1, 0),
  (1057605, 11, 0),
  (1057956, 3, 2),
  (1061982, 8, 16),
  (1062279, 5, 21),
  (1062561, 9, 0),
  (1063494, 3, 10),
  (1064926, 8, 3),
  (1066569, 1, 0),
  (1067062, 9, 7),
  (1071035, 1, 11),
  (1071188, 2, 3),
  (1074317, 3, 7),
  (1074432, 0, 0),
  (1076385, 1, 11),
  (1079216, 0, 3),
  (1081238, 9, 13),
  (1081602, 11, 3),
  (1084448, 9, 12),
  (1084458, 5, 10),
  (1085080, 11, 19),
  (1086263, 1, 0),
  (1088638, 8, 3),
  (1090413, 9, 7),
  (1095037, 9, 16),
  (1096240, 7, 17),
  (1097747, 6, 10),
  (1099967, 10, 7),
  (1101123, 4, 17),
  (1101583, 11, 11),
  (1101620, 9, 18),
  (1102664, 4, 21),
  (1103853, 1, 0),
  (1107545, 11, 0),
  (1109616, 4, 5),
  (1113595, 5, 10),
  (1113597, 8, 10),
  (1114262, 6, 10),
  (1116816, 4, 14),
  (1123262, 5, 10),
  (1125469, 5, 9),
  (1133968, 10, 11),
  (1134197, 4, 17),
  (1134200, 11, 11),
  (1134230, 11, 0),
  (1136985, 11, 17),
  (1137113, 5, 6),
  (1142639, 7, 10),
  (1142994, 0, 11),
  (1143747, 1, 18),
  (1144083, 0, 0),
  (1145568, 5, 22),
  (1146301, 0, 22),
  (1148118, 5, 10),
  (1150876, 1, 0),
  (1158270, 10, 3),
  (1158332, 3, 7),
  (1160335, 7, 18),
  (1163477, 7, 6),
  (1164264, 11, 11),
  (1164290, 2, 18),
  (1165753, 6, 10),
  (1166776, 9, 1),
  (1168518, 7, 21),
  (1168767, 5, 10),
  (1171007, 10, 0),
  (1174485, 1, 18),
  (1177393, 1, 9),
  (1178687, 6, 17),
  (1179971, 10, 0),
  (1180783, 3, 18),
  (1186121, 1, 22),
  (1188109, 1, 0),
  (1189956, 7, 10),
  (1195884, 10, 0),
  (1196388, 4, 21),
  (1198174, 10, 0),
  (1199521, 8, 8),
  (1204375, 7, 10),
  (1206352, 5, 10),
  (1207351, 0, 0),
  (1215336, 3, 7),
  (1226655, 5, 17),
  (1230626, 10, 16),
  (1231315, 10, 15),
  (1233209, 9, 3),
  (1236298, 11, 0),
  (1236484, 0, 18),
  (1239310, 8, 3),
  (1239906, 6, 17),
  (1242965, 8, 1),
  (1243557, 0, 3),
  (1246923, 4, 10),
  (1247895, 0, 10),
  (1250065, 11, 0),
  (1254772, 7, 10),
  (1255823, 6, 13),
  (1257684, 8, 5),
  (1259535, 11, 0),
  (1260557, 5, 22),
  (1261412, 1, 0),
  (1264105, 11, 22),
  (1264323, 5, 3),
  (1268954, 5, 19),
  (1269657, 4, 10),
  (1270233, 7, 10),
  (1270702, 4, 10),
  (1271132, 0, 10),
  (1275736, 0, 0),
  (1276360, 2, 7),
  (1277052, 1, 17),
  (1279489, 5, 10),
  (1280924, 4, 10),
  (1281054, 10, 10),
  (1281206, 5, 2),
  (1281365, 5, 22),
  (1283228, 9, 1),
  (1293952, 7, 6),
  (1296296, 11, 0),
  (1298028, 2, 7),
  (1298388, 0, 11),
  (1298860, 6, 13),
  (1301485, 6, 22),
  (1301596, 0, 0),
  (1301998, 9, 18),
  (1302098, 7, 17),
  (1302863, 6, 8),
  (1304326, 11, 0),
  (1306432, 7, 5),
  (1307879, 5, 10),
  (1309943, 11, 0),
  (1311885, 1, 0),
  (1312766, 0, 2),
  (1318054, 8, 4),
  (1319892, 3, 10),
  (1321503, 0, 0),
  (1325875, 7, 17),
  (1327634, 10, 0),
  (1337755, 2, 10),
  (1338952, 1, 0),
  (1340023, 5, 1),
  (1340209, 0, 14),
  (1340854, 11, 11),
  (1340977, 5, 10),
  (1342563, 4, 10),
  (1342706, 3, 10),
  (1343999, 10, 0),
  (1344398, 0, 11),
  (1348000, 7, 10),
  (1351220, 7, 10),
  (1353549, 10, 7),
  (1360707, 7, 10),
  (1360728, 11, 10),
  (1362519, 5, 13),
  (1363648, 8, 10),
  (1365703, 10, 21),
  (1367946, 10, 0),
  (1369166, 0, 0),
  (1373430, 3, 3),
  (1375412, 5, 17),
  (1375722, 6, 5),
  (1376810, 9, 7),
  (1376871, 3, 13),
  (1379246, 6, 13),
  (1383221, 9, 3),
  (1384293, 3, 3),
  (1386725, 11, 0),
  (1387434, 4, 17),
  (1388517, 8, 18),
  (1388715, 0, 0),
  (1392522, 4, 10),
  (1397220, 10, 15),
  (1398062, 2, 16),
  (1400366, 4, 10),
  (1401787, 5, 17),
  (1404567, 5, 22),
  (1406309, 3, 10),
  (1406447, 7, 10),
  (1414013, 10, 0),
  (1415055, 2, 7),
  (1417560, 4, 5),
  (1417579, 2, 10),
  (1419168, 3, 3),
  (1424273, 8, 3),
  (1426236, 1, 0),
  (1432425, 2, 3),
  (1432822, 2, 3),
  (1434497, 1, 0),
  (1437920, 8, 4),
  (1440162, 5, 10),
  (1440509, 10, 0),
  (1440864, 6, 10),
  (1445046, 1, 11),
  (1445917, 4, 10),
  (1449080, 11, 2),
  (1450116, 6, 16),
  (1450729, 5, 10),
  (1452417, 8, 0),
  (1454891, 2, 10),
  (1456000, 1, 18),
  (1458823, 10, 0),
  (1459533, 1, 0),
  (1461746, 1, 6),
  (1462055, 9, 3),
  (1466123, 7, 10),
  (1466941, 7, 18),
  (1470220, 0, 0),
  (1470541, 9, 7),
  (1471307, 7, 10),
  (1471742, 8, 7),
  (1472035, 4, 10),
  (1472831, 4, 10),
  (1477932, 2, 12),
  (1479686, 3, 6),
  (1479889, 10, 3),
  (1480829, 5, 17),
  (1483166, 7, 10),
  (1487888, 1, 0),
  (1489506, 11, 0),
  (1489994, 5, 17),
  (1491094, 4, 10),
  (1500349, 8, 3),
  (1501358, 0, 22),
  (1504940, 1, 0),
  (1510979, 7, 10),
  (1512322, 5, 10),
  (1513982, 0, 22),
  (1517284, 2, 8),
  (1518064, 3, 1),
  (1518970, 6, 21),
  (1518973, 11, 1),
  (1519246, 6, 10),
  (1519471, 4, 10),
  (1520047, 6, 21),
  (1522299, 3, 7),
  (1522556, 1, 0),
  (1525586, 1, 14),
  (1526690, 11, 13),
  (1527225, 0, 0),
  (1528828, 2, 4),
  (1529449, 5, 17),
  (1529489, 8, 11),
  (1530500, 6, 16),
  (1530985, 0, 18),
  (1531885, 8, 9),
  (1534029, 3, 0),
  (1534083, 6, 22),
  (1534936, 1, 0),
  (1535797, 3, 15),
  (1539858, 6, 12),
  (1543568, 7, 10),
  (1543804, 0, 11),
  (1544203, 0, 11),
  (1544637, 0, 0),
  (1546590, 1, 0),
  (1548502, 1, 11),
  (1550847, 7, 10),
  (1555642, 1, 15),
  (1556333, 11, 10),
  (1557756, 0, 0),
  (1557792, 7, 10),
  (1557862, 8, 3),
  (1558347, 8, 3),
  (1560634, 4, 10),
  (1563345, 6, 17),
  (1566295, 2, 0),
  (1566743, 11, 11),
  (1567599, 10, 0),
  (1568834, 6, 10),
  (1570598, 1, 18),
  (1573544, 3, 4),
  (1573960, 2, 10),
  (1578514, 11, 0),
  (1581435, 0, 22),
  (1582556, 8, 18),
  (1583758, 1, 0),
  (1583930, 4, 10),
  (1587644, 7, 17),
  (1589246, 1, 0),
  (1590111, 2, 16),
  (1590554, 11, 0),
  (1591476, 4, 12),
  (1594704, 5, 10),
  (1596643, 3, 6),
  (1597089, 9, 18),
  (1598806, 10, 17),
  (1601452, 7, 21),
  (1603726, 0, 11),
  (1610373, 5, 10),
  (1610952, 11, 0),
  (1611875, 0, 0),
  (1611954, 4, 17),
  (1612377, 3, 10),
  (1612734, 0, 14),
  (1614827, 4, 9),
  (1617725, 6, 10),
  (1618619, 3, 10),
  (1621123, 0, 22),
  (1623747, 3, 10),
  (1624122, 8, 0),
  (1624885, 9, 18),
  (1626230, 1, 11),
  (1628585, 7, 22),
  (1629496, 7, 10),
  (1629775, 1, 0),
  (1634305, 3, 17),
  (1634661, 1, 0),
  (1635556, 0, 6),
  (1636023, 10, 0),
  (1637430, 8, 7),
  (1644752, 1, 11),
  (1646001, 6, 10),
  (1646942, 6, 17),
  (1646963, 0, 7),
  (1647529, 3, 13),
  (1648189, 5, 10),
  (1650321, 5, 10),
  (1651986, 8, 10),
  (1653666, 9, 0),
  (1656687, 3, 3),
  (1657839, 1, 0),
  (1659443, 6, 10),
  (1659699, 1, 0),
  (1665963, 6, 18),
  (1666267, 11, 0),
  (1671828, 6, 17),
  (1673236, 5, 17),
  (1674128, 5, 10),
  (1678459, 5, 10),
  (1687574, 1, 0),
  (1688136, 2, 18),
  (1689605, 9, 8),
  (1691145, 8, 4),
  (1691272, 7, 17),
  (1691894, 11, 0),
  (1692904, 7, 10),
  (1692933, 11, 0),
  (1693436, 10, 0),
  (1698479, 1, 0),
  (1704875, 6, 10),
  (1705555, 3, 10),
  (1705613, 7, 10),
  (1706643, 7, 17),
  (1708590, 7, 10),
  (1708947, 3, 6),
  (1710369, 3, 14),
  (1713888, 8, 7),
  (1714170, 2, 5),
  (1714421, 6, 17),
  (1717271, 1, 0),
  (1720390, 0, 18),
  (1723560, 1, 11),
  (1725099, 2, 8),
  (1726306, 6, 17),
  (1733506, 11, 11),
  (1734119, 6, 10),
  (1734211, 10, 11),
  (1737268, 6, 21),
  (1739131, 10, 0),
  (1740720, 9, 4),
  (1741429, 7, 22),
  (1742646, 4, 17),
  (1746435, 3, 10),
  (1748335, 5, 21),
  (1750695, 6, 17),
  (1754685, 9, 10),
  (1755764, 1, 11),
  (1757860, 4, 10),
  (1759157, 6, 16),
  (1760429, 11, 11),
  (1760643, 0, 14),
  (1761379, 9, 3),
  (1761611, 5, 17),
  (1764531, 9, 6),
  (1766078, 4, 10),
  (1766542, 1, 11),
  (1766707, 2, 4),
  (1768248, 4, 16),
  (1769906, 7, 10),
  (1774326, 1, 11),
  (1775170, 4, 10),
  (1781093, 10, 0),
  (1781192, 10, 10),
  (1787595, 2, 7),
  (1788525, 0, 0),
  (1790338, 6, 17),
  (1792321, 7, 10),
  (1794851, 1, 0),
  (1795013, 1, 3),
  (1797182, 6, 10),
  (1798164, 7, 17),
  (1799489, 6, 10),
  (1799601, 0, 0),
  (1801179, 8, 6),
  (1802297, 2, 18),
  (1804113, 3, 7),
  (1804592, 0, 0),
  (1808738, 5, 9),
  (1812974, 8, 18),
  (1814877, 5, 10),
  (1815041, 2, 7),
  (1817727, 0, 0),
  (1819493, 8, 5),
  (1820952, 9, 1),
  (1823320, 3, 0),
  (1824972, 10, 11),
  (1826244, 10, 22),
  (1829696, 3, 18),
  (1829889, 2, 3),
  (1833977, 11, 0),
  (1835366, 11, 0),
  (1837923, 6, 22),
  (1839372, 6, 17),
  (1840844, 8, 7),
  (1841621, 8, 10),
  (1842287, 0, 22),
  (1842979, 8, 7),
  (1844063, 11, 7),
  (1844506, 4, 10),
  (1850027, 0, 0),
  (1852916, 5, 22),
  (1854773, 1, 0),
  (1854952, 6, 17),
  (1858752, 7, 9),
  (1864301, 10, 7),
  (1864971, 5, 10),
  (1865022, 1, 0),
  (1865545, 0, 6),
  (1866134, 11, 7),
  (1867489, 7, 19),
  (1870475, 8, 3),
  (1871921, 0, 11),
  (1872866, 5, 9),
  (1874647, 6, 18),
  (1880911, 1, 1),
  (1882777, 5, 10),
  (1885012, 3, 7),
  (1886915, 11, 0),
  (1887337, 7, 10),
  (1888954, 7, 10),
  (1895528, 2, 7),
  (1895622, 4, 17),
  (1898126, 7, 10),
  (1899392, 11, 0),
  (1899917, 11, 22),
  (1901133, 5, 10),
  (1901721, 4, 17),
  (1902440, 5, 10),
  (1902656, 8, 15),
  (1903893, 1, 0),
  (1906974, 6, 10),
  (1908957, 0, 10),
  (1910708, 0, 3),
  (1910751, 7, 9),
  (1911452, 3, 17),
  (1912408, 0, 0),
  (1913538, 8, 11),
  (1915043, 4, 10),
  (1916358, 1, 11),
  (1919899, 3, 3),
  (1922490, 9, 13),
  (1924301, 6, 22),
  (1926362, 6, 21),
  (1931004, 9, 0),
  (1932940, 8, 3),
  (1934140, 0, 18),
  (1943774, 1, 0),
  (1947935, 10, 11),
  (1948407, 5, 10),
  (1948774, 0, 18),
  (1949468, 4, 17),
  (1949576, 6, 10),
  (1950763, 10, 7),
  (1951227, 9, 13),
  (1954648, 3, 13),
  (1955364, 2, 7),
  (1956233, 8, 14),
  (1957890, 0, 22),
  (1958071, 8, 7),
  (1958259, 6, 10),
  (1959849, 6, 10),
  (1960584, 2, 7),
  (1962877, 7, 2),
  (1964022, 11, 3),
  (1967066, 8, 9),
  (1972847, 4, 21),
  (1973147, 5, 17),
  (1973722, 10, 19),
  (1975109, 5, 10),
  (1975594, 7, 17),
  (1976352, 2, 4),
  (1980230, 1, 16),
  (1980385, 6, 10),
  (1981270, 7, 21),
  (1983650, 1, 7),
  (1984626, 0, 0),
  (1992224, 0, 3),
  (1993618, 3, 3),
  (1997342, 6, 10),
  (1998957, 2, 18),
  (1999048, 0, 11),
  (2000241, 1, 7),
  (2002190, 5, 10),
  (2002387, 9, 18),
  (2004252, 6, 10),
  (2004426, 7, 13),
  (2006112, 10, 3),
  (2007112, 8, 17),
  (2008270, 10, 10),
  (2009593, 11, 0),
  (2010174, 0, 10),
  (2010683, 8, 7),
  (2010972, 3, 17),
  (2011042, 7, 3),
  (2014710, 2, 13),
  (2017977, 4, 19),
  (2019341, 0, 10),
  (2023616, 3, 3),
  (2025823, 2, 3),
  (2029600, 11, 0),
  (2030454, 5, 17),
  (2031142, 5, 10),
  (2031656, 0, 0),
  (2032748, 7, 17),
  (2036366, 0, 11),
  (2037784, 5, 10),
  (2038109, 4, 10),
  (2038532, 6, 13),
  (2038536, 6, 7),
  (2040679, 2, 15),
  (2040755, 0, 10),
  (2042439, 11, 0),
  (2043068, 0, 10),
  (2045977, 10, 0),
  (2046419, 10, 18),
  (2047947, 3, 0),
  (2049930, 4, 18),
  (2052383, 7, 10),
  (2055085, 8, 9),
  (2055172, 11, 0),
  (2057632, 10, 0),
  (2059176, 8, 3),
  (2060585, 9, 7),
  (2061256, 4, 10),
  (2061481, 4, 11),
  (2064166, 3, 3),
  (2067508, 9, 4),
  (2069420, 8, 3),
  (2075464, 8, 7),
  (2076802, 10, 0),
  (2078934, 8, 4),
  (2080629, 8, 18),
  (2081016, 9, 3),
  (2082586, 4, 17),
  (2085394, 3, 18),
  (2085656, 5, 9),
  (2086018, 10, 14),
  (2087215, 3, 3),
  (2091445, 3, 10),
  (2092795, 1, 0),
  (2093479, 9, 3),
  (2098245, 1, 0),
  (2099304, 3, 13),
  (2100563, 8, 18),
  (2101470, 10, 0),
  (2101494, 6, 21),
  (2103839, 2, 18),
  (2104455, 11, 0),
  (2106212, 7, 17),
  (2109124, 8, 15),
  (2117848, 5, 10),
  (2118160, 6, 10),
  (2119888, 2, 7),
  (2122330, 6, 10),
  (2126105, 4, 17),
  (2126274, 3, 18),
  (2131579, 3, 3),
  (2131806, 8, 3),
  (2132694, 0, 0),
  (2133521, 4, 10),
  (2135277, 11, 11),
  (2140711, 7, 10),
  (2141076, 6, 10),
  (2141915, 7, 17),
  (2142776, 0, 11),
  (2144146, 2, 13),
  (2146751, 6, 3),
  (2146892, 10, 11),
  (2151291, 10, 0),
  (2151797, 10, 0),
  (2157036, 4, 10),
  (2157518, 3, 7),
  (2158201, 3, 0),
  (2158779, 7, 10),
  (2163425, 3, 3),
  (2164429, 8, 7),
  (2168604, 3, 18),
  (2173710, 1, 18),
  (2175876, 6, 21),
  (2176591, 9, 14),
  (2176699, 5, 10),
  (2177049, 2, 3),
  (2178672, 6, 17),
  (2181344, 10, 0),
  (2182961, 7, 22),
  (2183883, 6, 10),
  (2192517, 5, 17),
  (2192909, 4, 3),
  (2198956, 5, 10),
  (2201317, 0, 22),
  (2207359, 0, 0),
  (2207460, 3, 3),
  (2208175, 4, 10),
  (2212657, 10, 22),
  (2212746, 9, 11),
  (2219605, 11, 12),
  (2221035, 6, 18),
  (2222955, 6, 10),
  (2223925, 0, 6),
  (2228919, 9, 14),
  (2230952, 7, 17),
  (2231876, 7, 6),
  (2236071, 4, 21),
  (2237657, 6, 9),
  (2239833, 7, 10),
  (2241092, 5, 22),
  (2241792, 11, 0),
  (2241946, 2, 3),
  (2242814, 11, 0),
  (2246950, 4, 3),
  (2249568, 11, 0),
  (2253297, 7, 10),
  (2254418, 7, 3),
  (2255356, 6, 10),
  (2255573, 11, 0),
  (2256575, 9, 3),
  (2256840, 4, 10),
  (2260897, 6, 13),
  (2261555, 5, 17),
  (2262195, 2, 10),
  (2264976, 1, 0),
  (2266450, 1, 0),
  (2269948, 0, 0),
  (2273630, 2, 2),
  (2276721, 11, 8),
  (2279681, 8, 11),
  (2283387, 5, 10),
  (2286983, 5, 18),
  (2286996, 6, 17),
  (2287833, 8, 17),
  (2287951, 8, 4),
  (2292454, 9, 2),
  (2297327, 11, 0),
  (2297798, 3, 3),
  (2299365, 3, 12),
  (2299795, 2, 13),
  (2300367, 5, 10),
  (2301136, 2, 7),
  (2301331, 11, 0),
  (2303577, 1, 0),
  (2304353, 9, 13),
  (2304650, 10, 18),
  (2305836, 8, 1),
  (2310830, 8, 7),
  (2314717, 4, 10),
  (2315795, 0, 0),
  (2316352, 10, 10),
  (2316606, 2, 7),
  (2317504, 1, 11),
  (2318934, 0, 11),
  (2320240, 1, 19),
  (2324893, 2, 3),
  (2328442, 1, 10),
  (2328724, 8, 4),
  (2330216, 10, 0),
  (2330908, 1, 11),
  (2333357, 11, 6),
  (2334146, 2, 12),
  (2337989, 7, 20),
  (2338011, 7, 10),
  (2342382, 9, 7),
  (2344268, 9, 12),
  (2344906, 9, 13),
  (2346124, 8, 3),
  (2348069, 0, 0),
  (2350091, 1, 5),
  (2350367, 8, 7),
  (2353037, 9, 8),
  (2353089, 11, 11),
  (2354932, 11, 0),
  (2361818, 6, 9),
  (2364248, 2, 0),
  (2367388, 10, 0),
  (2368416, 1, 0),
  (2371235, 6, 10),
  (2371685, 8, 3),
  (2371972, 10, 0),
  (2379999, 5, 17),
  (2380160, 4, 10),
  (2380816, 6, 17),
  (2383009, 1, 11),
  (2384528, 2, 3),
  (2384952, 10, 13),
  (2389310, 4, 17),
  (2389599, 4, 17),
  (2391596, 3, 7),
  (2394247, 5, 9),
  (2395908, 0, 2),
  (2396389, 6, 17),
  (2398115, 1, 0),
  (2402967, 5, 17),
  (2403092, 8, 7),
  (2404147, 4, 2),
  (2404307, 7, 9),
  (2405185, 11, 11),
  (2405998, 11, 0),
  (2406821, 8, 3),
  (2407299, 0, 18),
  (2410015, 7, 22),
  (2415465, 0, 18),
  (2423806, 5, 10),
  (2424180, 0, 0),
  (2424954, 11, 11),
  (2425635, 10, 7),
  (2428311, 0, 11),
  (2433213, 10, 17),
  (2436040, 10, 22),
  (2442229, 6, 10),
  (2443167, 11, 0),
  (2444198, 10, 0),
  (2446617, 6, 21),
  (2446805, 4, 21),
  (2449123, 4, 13),
  (2449539, 1, 21),
  (2451751, 5, 11),
  (2453090, 8, 0),
  (2453782, 8, 16),
  (2454904, 7, 9),
  (2462412, 8, 3),
  (2471069, 4, 10),
  (2472885, 6, 17),
  (2477497, 2, 7),
  (2478584, 8, 10),
  (2480576, 7, 10),
  (2481648, 7, 10),
  (2481693, 6, 10),
  (2482066, 1, 17),
  (2484038, 2, 13),
  (2484328, 2, 4),
  (2485874, 2, 13),
  (2487141, 10, 0),
  (2487309, 2, 16),
  (2488335, 4, 10),
  (2493048, 5, 17),
  (2495506, 7, 10),
  (2495851, 4, 22),
  (2496203, 1, 11),
  (2497331, 10, 0),
  (2499195, 2, 3),
  (2499841, 2, 14),
  (2500157, 6, 10),
  (2501700, 11, 18),
  (2507187, 4, 3),
  (2511825, 8, 12),
  (2513225, 7, 10),
  (2514539, 4, 10),
  (2517390, 0, 0),
  (2517607, 1, 0),
  (2519519, 9, 7),
  (2522829, 11, 10),
  (2523699, 3, 3),
  (2525890, 11, 0),
  (2527463, 10, 0),
  (2531027, 0, 0),
  (2533123, 10, 0),
  (2534087, 10, 0),
  (2541876, 9, 3),
  (2542011, 5, 10),
  (2543737, 1, 0),
  (2550602, 7, 18),
  (2553107, 2, 7),
  (2553879, 5, 10),
  (2554278, 5, 10),
  (2554282, 9, 4),
  (2554567, 6, 5),
  (2556666, 0, 0),
  (2557352, 7, 22),
  (2557441, 7, 10),
  (2557787, 4, 16),
  (2560067, 6, 22),
  (2562387, 11, 11),
  (2572599, 0, 11),
  (2572922, 9, 7),
  (2573374, 4, 21),
  (2573940, 6, 10),
  (2576767, 8, 10),
  (2577606, 0, 0),
  (2578089, 11, 20),
  (2583329, 6, 17),
  (2585881, 4, 10),
  (2588923, 0, 6),
  (2589382, 9, 0),
  (2590021, 9, 3),
  (2593889, 7, 17),
  (2594027, 11, 0),
  (2594430, 6, 16),
  (2594591, 7, 10),
  (2594769, 8, 12),
  (2594961, 6, 4),
  (2595311, 11, 0),
  (2597400, 7, 10),
  (2598836, 9, 10),
  (2601471, 9, 1),
  (2606263, 4, 22),
  (2606605, 6, 10),
  (2610433, 9, 13),
  (2612117, 8, 7),
  (2612663, 9, 3),
  (2614580, 9, 3),
  (2616769, 8, 3),
  (2621294, 5, 17),
  (2624924, 5, 16),
  (2625979, 11, 22),
  (2628713, 1, 10),
  (2631080, 1, 0),
  (2632322, 9, 7),
  (2632587, 7, 22),
  (2633942, 8, 10),
  (2634167, 8, 0),
  (2635739, 1, 0),
  (2636297, 5, 17),
  (2637630, 9, 3),
  (2638075, 1, 3),
  (2638520, 0, 0),
  (2638609, 6, 17),
  (2639246, 8, 10),
  (2640684, 2, 18),
  (2641957, 11, 0),
  (2644111, 1, 0),
  (2647604, 11, 10),
  (2648900, 10, 10),
  (2652733, 8, 14),
  (2655387, 8, 11),
  (2659175, 2, 16),
  (2663855, 11, 10),
  (2665782, 7, 17),
  (2667534, 5, 10),
  (2667634, 7, 21),
  (2670137, 1, 15),
  (2670186, 8, 3),
  (2671272, 8, 3),
  (2674081, 1, 10),
  (2675331, 5, 10),
  (2675563, 8, 3),
  (2678831, 8, 18),
  (2679827, 6, 17),
  (2680862, 1, 0),
  (2683109, 6, 17),
  (2683532, 11, 0),
  (2684781, 3, 3),
  (2686084, 4, 10),
  (2687330, 9, 13),
  (2691164, 8, 17),
  (2693375, 11, 11),
  (2695345, 6, 10),
  (2696117, 6, 10),
  (2696422, 8, 0),
  (2696967, 5, 9),
  (2702531, 4, 10),
  (2705710, 6, 17),
  (2708956, 4, 10),
  (2712382, 3, 12),
  (2713545, 6, 10),
  (2713911, 3, 0),
  (2714612, 1, 0),
  (2719453, 8, 18),
  (2725466, 0, 5),
  (2725855, 0, 11),
  (2727452, 2, 4),
  (2730972, 5, 10),
  (2732693, 10, 20),
  (2740474, 7, 6),
  (2743831, 11, 0),
  (2744101, 3, 2),
  (2744626, 9, 7),
  (2745534, 9, 7),
  (2748965, 3, 6),
  (2750457, 3, 3),
  (2756318, 4, 8),
  (2757694, 1, 0),
  (2763126, 1, 0),
  (2765873, 2, 3),
  (2768766, 5, 16),
  (2771157, 4, 17),
  (2775581, 1, 14),
  (2778753, 11, 11),
  (2779300, 0, 0),
  (2780301, 1, 10),
  (2783992, 9, 3),
  (2784640, 1, 0),
  (2785122, 11, 0),
  (2789798, 5, 10),
  (2789886, 2, 7),
  (2792196, 7, 10),
  (2795519, 9, 3),
  (2795725, 1, 11),
  (2799568, 7, 10),
  (2803459, 10, 10),
  (2803829, 9, 17),
  (2809948, 0, 0),
  (2810728, 3, 3),
  (2811723, 0, 1),
  (2813819, 5, 2),
  (2814263, 5, 17),
  (2818720, 1, 22),
  (2820778, 4, 19),
  (2820958, 1, 0),
  (2823589, 3, 16),
  (2827200, 10, 18),
  (2829104, 4, 9),
  (2829330, 3, 0),
  (2829535, 5, 10),
  (2833945, 10, 0),
  (2833953, 2, 5),
  (2835119, 9, 3),
  (2838224, 9, 3),
  (2839099, 0, 16),
  (2839238, 9, 1),
  (2844120, 4, 10),
  (2846236, 11, 0),
  (2846906, 1, 0),
  (2849429, 6, 21),
  (2854815, 0, 13),
  (2855922, 2, 7),
  (2858493, 11, 0),
  (2858852, 9, 7),
  (2859396, 4, 10),
  (2864050, 7, 10),
  (2864550, 2, 7),
  (2864609, 8, 13),
  (2867435, 8, 3),
  (2869608, 4, 16),
  (2870849, 2, 18),
  (2871129, 0, 4),
  (2872458, 8, 10),
  (2874109, 6, 17),
  (2875947, 2, 16),
  (2877419, 2, 7),
  (2880171, 8, 10),
  (2885612, 4, 10),
  (2888770, 4, 9),
  (2891076, 2, 7),
  (2894597, 4, 22),
  (2897047, 3, 3),
  (2899090, 8, 10),
  (2901512, 2, 13),
  (2905046, 11, 11),
  (2905269, 0, 10),
  (2907733, 6, 10),
  (2909127, 1, 0),
  (2912433, 10, 0),
  (2913493, 10, 11),
  (2914399, 3, 3),
  (2914452, 7, 8),
  (2917296, 10, 0),
  (2919269, 9, 3),
  (2919571, 7, 9),
  (2921550, 0, 0),
  (2924500, 2, 18),
  (2925394, 7, 22),
  (2928285, 7, 10),
  (2930508, 1, 0),
  (2931408, 11, 0),
  (2932839, 6, 9),
  (2938694, 0, 0),
  (2941625, 1, 0),
  (2946191, 4, 10),
  (2946750, 2, 3),
  (2949228, 11, 0),
  (2950956, 5, 17),
  (2952430, 8, 7),
  (2954637, 0, 0),
  (2961728, 2, 0),
  (2962599, 3, 7),
  (2966512, 4, 10),
  (2967909, 9, 7),
  (2968250, 3, 7),
  (2970903, 10, 17),
  (2971093, 9, 18),
  (2974370, 6, 17),
  (2977073, 10, 0),
  (2977381, 0, 0),
  (2977900, 7, 10),
  (2978012, 3, 5),
  (2978438, 2, 18),
  (2983546, 3, 4),
  (2993644, 3, 7),
  (2994011, 2, 4),
  (2994441, 5, 16),
  (2995331, 11, 0),
  (2997251, 1, 10),
  (2998325, 4, 17),
  (3007284, 3, 11),
  (3007345, 9, 7),
  (3010719, 10, 14),
  (3011493, 5, 5),
  (3013207, 2, 0),
  (3018671, 11, 19),
  (3022628, 6, 10),
  (3023831, 1, 22),
  (3024386, 8, 9),
  (3024553, 0, 10),
  (3026795, 9, 16),
  (3028301, 2, 0),
  (3028509, 9, 3),
  (3029299, 4, 15),
  (3030400, 11, 18),
  (3030493, 5, 0),
  (3031772, 9, 10),
  (3033469, 3, 7),
  (3034572, 0, 11),
  (3037519, 4, 10),
  (3037555, 1, 0),
  (3038067, 11, 11),
  (3040675, 0, 0),
  (3040764, 10, 17),
  (3043504, 5, 17),
  (3043982, 11, 20),
  (3046734, 7, 10),
  (3050779, 2, 11),
  (3053534, 1, 10),
  (3054147, 11, 0),
  (3060673, 0, 0),
  (3061497, 6, 17),
  (3062530, 10, 22),
  (3063660, 8, 3),
  (3070952, 5, 10),
  (3071745, 3, 7),
  (3075349, 3, 6),
  (3078478, 11, 0),
  (3079550, 5, 9),
  (3080026, 11, 7),
  (3081379, 9, 7),
  (3082526, 1, 0),
  (3083469, 2, 6),
  (3085933, 8, 10),
  (3085959, 4, 10),
  (3088072, 9, 13),
  (3093038, 7, 5),
  (3093357, 8, 7),
  (3094020, 2, 13),
  (3095772, 8, 6),
  (3097809, 2, 1),
  (3101430, 2, 3),
  (3101673, 8, 7),
  (3101968, 7, 22),
  (3102465, 7, 10),
  (3105642, 10, 0),
  (3109756, 6, 10),
  (3114260, 10, 3),
  (3114576, 8, 3),
  (3122818, 9, 4),
  (3125675, 7, 17),
  (3131863, 0, 11),
  (3136189, 0, 0),
  (3136448, 4, 13),
  (3136911, 2, 3),
  (3136989, 1, 0),
  (3137088, 10, 0),
  (3137296, 1, 0),
  (3141105, 9, 13),
  (3141222, 2, 7),
  (3142994, 6, 6),
  (3146266, 2, 16),
  (3147714, 11, 1),
  (3150037, 11, 19),
  (3153554, 3, 7),
  (3153693, 1, 9),
  (3155131, 7, 10),
  (3155793, 10, 0),
  (3156489, 6, 9),
  (3158262, 6, 10),
  (3160781, 7, 18),
  (3161027, 11, 18),
  (3164689, 2, 4),
  (3165893, 7, 10),
  (3166827, 6, 10),
  (3167893, 5, 13),
  (3171975, 10, 22),
  (3172744, 5, 10),
  (3175672, 3, 7),
  (3176229, 8, 7),
  (3177341, 10, 7),
  (3177975, 1, 0),
  (3180974, 1, 0),
  (3185307, 2, 3),
  (3186113, 9, 3),
  (3191845, 5, 10),
  (3194707, 5, 17),
  (3197608, 6, 10),
  (3198153, 9, 0),
  (3199086, 6, 21),
  (3200291, 0, 15),
  (3202088, 1, 0),
  (3214654, 11, 0),
  (3214912, 11, 7),
  (3215559, 3, 3),
  (3216137, 10, 0),
  (3217120, 0, 11),
  (3218623, 6, 5),
  (3219616, 4, 12),
  (3219665, 11, 4),
  (3221199, 2, 2),
  (3224801, 6, 17),
  (3225304, 7, 17),
  (3227003, 11, 0),
  (3230306, 7, 10),
  (3231073, 0, 14),
  (3231787, 11, 11),
  (3235260, 4, 10),
  (3236597, 5, 10),
  (3238459, 10, 8),
  (3240853, 3, 13),
  (3244555, 10, 9),
  (3244567, 3, 2),
  (3245094, 7, 10),
  (3249456, 1, 7),
  (3252914, 1, 11),
  (3257341, 11, 10),
  (3260268, 5, 13),
  (3260932, 2, 3),
  (3261053, 1, 0),
  (3262351, 6, 10),
  (3266179, 4, 21),
  (3268074, 1, 0),
  (3268612, 6, 16),
  (3280225, 4, 9),
  (3281194, 9, 3),
  (3281775, 8, 0),
  (3286982, 2, 7),
  (3292572, 6, 17),
  (3295739, 4, 17),
  (3296119, 6, 10),
  (3298396, 5, 10),
  (3300141, 9, 3),
  (3301079, 10, 0),
  (3301444, 10, 18),
  (3303496, 11, 11),
  (3309979, 9, 6),
  (3310402, 1, 0),
  (3310995, 5, 10),
  (3312350, 11, 0),
  (3312545, 7, 10),
  (3313079, 3, 10),
  (3313318, 5, 10),
  (3315009, 0, 22),
  (3315238, 2, 3),
  (3316098, 5, 10),
  (3319470, 11, 0),
  (3320089, 10, 10),
  (3321220, 1, 0),
  (3322177, 11, 11),
  (3322835, 4, 10),
  (3323522, 6, 22),
  (3325277, 7, 16),
  (3331940, 3, 7),
  (3331991, 4, 10),
  (3334279, 0, 0),
  (3335112, 3, 16),
  (3340697, 9, 13),
  (3341829, 3, 16),
  (3344402, 10, 0),
  (3345179, 6, 10),
  (3345492, 5, 9),
  (3347765, 2, 7),
  (3351969, 11, 0),
  (3353900, 4, 6),
  (3356768, 5, 10),
  (3356871, 3, 2),
  (3356911, 11, 11),
  (3357458, 4, 13),
  (3362319, 10, 9),
  (3362681, 3, 7),
  (3362795, 2, 0),
  (3369091, 7, 17),
  (3370260, 7, 17),
  (3372354, 11, 11),
  (3372894, 8, 3),
  (3376950, 2, 3),
  (3380838, 10, 0),
  (3386012, 5, 17),
  (3386918, 9, 14),
  (3388469, 0, 0),
  (3395537, 10, 18),
  (3400647, 9, 7),
  (3401421, 0, 22),
  (3401531, 2, 1),
  (3404507, 2, 6),
  (3405834, 2, 15),
  (3406247, 7, 17),
  (3407038, 9, 7),
  (3414959, 10, 10),
  (3417288, 11, 1),
  (3419214, 3, 1),
  (3420688, 4, 10),
  (3423180, 4, 18),
  (3423631, 9, 13),
  (3423825, 7, 17),
  (3429984, 3, 4),
  (3430123, 3, 16),
  (3435646, 11, 10),
  (3435872, 11, 6),
  (3436495, 8, 7),
  (3440209, 11, 10),
  (3440662, 8, 10),
  (3444718, 2, 7),
  (3446400, 11, 0),
  (3447339, 7, 21),
  (3448825, 9, 0),
  (3449602, 0, 0),
  (3449609, 1, 0),
  (3452340, 6, 10),
  (3454723, 3, 15),
  (3456636, 10, 0),
  (3460457, 2, 18),
  (3461851, 0, 0),
  (3462990, 10, 10),
  (3464828, 6, 10),
  (3465597, 4, 10),
  (3467005, 3, 7),
  (3467670, 9, 9),
  (3467982, 1, 6),
  (3468841, 7, 9),
  (3470118, 11, 0),
  (3472587, 0, 0),
  (3473363, 9, 11),
  (3476380, 5, 9),
  (3479016, 4, 10),
  (3480144, 9, 15),
  (3481779, 2, 2),
  (3482064, 3, 7),
  (3483405, 7, 10),
  (3483779, 9, 7),
  (3488504, 2, 18),
  (3490252, 4, 4),
  (3491274, 9, 10),
  (3491576, 7, 10),
  (3492828, 7, 16),
  (3496734, 9, 9),
  (3496763, 0, 0),
  (3496774, 5, 2),
  (3497898, 0, 0),
  (3499755, 4, 10),
  (3500777, 11, 0),
  (3501985, 0, 0),
  (3505484, 2, 13),
  (3507624, 7, 14),
  (3510830, 0, 7),
  (3512756, 4, 10),
  (3517704, 6, 10),
  (3518014, 5, 10),
  (3521718, 9, 14),
  (3525722, 9, 18),
  (3528758, 8, 11),
  (3529678, 2, 6),
  (3530871, 9, 3),
  (3532253, 5, 21),
  (3534852, 3, 7),
  (3537971, 7, 7),
  (3539647, 4, 17),
  (3543258, 0, 0),
  (3544332, 2, 5),
  (3545441, 0, 0),
  (3547948, 6, 22),
  (3549039, 5, 10),
  (3552835, 5, 17),
  (3554150, 7, 10),
  (3555385, 2, 16),
  (3555791, 1, 0),
  (3557410, 10, 11),
  (3558109, 3, 17),
  (3560537, 10, 0),
  (3560788, 10, 4),
  (3562645, 3, 5),
  (3563451, 8, 10),
  (3564081, 0, 11),
  (3566586, 9, 3),
  (3569321, 9, 16),
  (3569345, 7, 10),
  (3570373, 8, 3),
  (3570966, 8, 3),
  (3571053, 9, 15),
  (3573882, 9, 0),
  (3573983, 9, 14),
  (3577770, 3, 3),
  (3585163, 7, 22),
  (3585241, 1, 10),
  (3590451, 6, 10),
  (3593332, 5, 10),
  (3594611, 0, 17),
  (3596772, 4, 17),
  (3598815, 0, 0),
])