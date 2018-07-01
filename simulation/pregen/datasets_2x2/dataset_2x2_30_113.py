from util import *
schedule = deque([
  (1736, 2, 7),
  (2976, 0, 0),
  (3998, 1, 9),
  (6321, 9, 3),
  (9509, 5, 9),
  (13184, 8, 18),
  (13319, 5, 5),
  (13625, 1, 9),
  (14914, 9, 18),
  (15573, 7, 22),
  (15582, 11, 11),
  (17453, 8, 18),
  (18871, 11, 9),
  (20383, 2, 7),
  (23813, 8, 7),
  (24126, 5, 20),
  (25842, 11, 6),
  (26047, 1, 11),
  (28118, 5, 20),
  (29983, 5, 10),
  (30560, 8, 7),
  (31258, 7, 20),
  (31827, 5, 22),
  (35965, 3, 18),
  (38178, 10, 9),
  (41500, 1, 0),
  (44250, 2, 13),
  (46147, 11, 0),
  (46422, 3, 18),
  (47328, 2, 3),
  (48631, 11, 21),
  (49876, 11, 17),
  (50288, 0, 21),
  (53110, 8, 3),
  (53376, 2, 14),
  (57335, 1, 17),
  (58814, 1, 11),
  (62145, 0, 22),
  (62599, 0, 22),
  (63670, 10, 19),
  (64132, 9, 18),
  (64948, 8, 3),
  (65551, 3, 7),
  (66067, 4, 10),
  (68169, 3, 13),
  (70589, 8, 13),
  (72942, 10, 17),
  (73013, 3, 9),
  (73769, 9, 3),
  (77998, 6, 22),
  (86938, 3, 2),
  (95558, 4, 17),
  (95875, 6, 22),
  (96835, 6, 10),
  (98931, 10, 10),
  (101079, 5, 22),
  (102887, 1, 22),
  (105462, 2, 13),
  (106405, 8, 17),
  (108964, 0, 0),
  (111879, 11, 17),
  (112932, 10, 0),
  (118476, 2, 16),
  (118931, 0, 18),
  (120317, 1, 16),
  (121951, 0, 0),
  (122214, 9, 7),
  (128740, 3, 7),
  (132296, 11, 16),
  (134289, 8, 18),
  (135807, 4, 10),
  (135880, 2, 7),
  (136411, 3, 18),
  (137095, 10, 6),
  (138963, 9, 14),
  (139665, 10, 0),
  (140704, 10, 21),
  (142795, 2, 13),
  (145165, 11, 22),
  (145990, 3, 10),
  (146928, 11, 17),
  (150839, 10, 22),
  (151600, 9, 12),
  (153364, 3, 10),
  (153668, 8, 12),
  (155564, 4, 8),
  (158168, 11, 14),
  (159619, 2, 7),
  (160091, 4, 3),
  (160902, 0, 22),
  (161477, 5, 20),
  (164851, 6, 22),
  (165509, 1, 22),
  (167226, 4, 10),
  (171479, 8, 7),
  (174136, 2, 7),
  (174974, 9, 18),
  (175471, 11, 18),
  (175532, 3, 2),
  (176858, 6, 22),
  (177107, 4, 22),
  (177400, 1, 0),
  (177918, 1, 18),
  (179627, 1, 0),
  (179905, 5, 9),
  (181297, 9, 7),
  (183459, 8, 7),
  (184985, 6, 22),
  (187531, 5, 10),
  (189158, 3, 13),
  (190154, 8, 7),
  (191808, 0, 9),
  (197203, 3, 13),
  (197884, 1, 22),
  (199496, 5, 17),
  (208363, 11, 11),
  (209385, 9, 15),
  (212526, 7, 16),
  (212623, 4, 21),
  (213884, 7, 22),
  (216634, 10, 11),
  (217542, 11, 12),
  (219318, 9, 17),
  (219953, 9, 10),
  (220608, 5, 21),
  (221272, 7, 22),
  (221711, 4, 10),
  (225734, 10, 21),
  (226365, 4, 9),
  (226784, 3, 10),
  (228228, 6, 10),
  (229110, 7, 22),
  (229221, 4, 10),
  (229553, 11, 22),
  (229607, 7, 10),
  (229686, 5, 22),
  (230411, 0, 0),
  (230915, 5, 21),
  (231825, 5, 20),
  (236991, 10, 17),
  (240444, 11, 0),
  (240622, 3, 10),
  (241336, 5, 3),
  (241352, 10, 0),
  (242855, 3, 12),
  (243821, 10, 6),
  (246738, 3, 3),
  (247268, 7, 22),
  (247500, 6, 17),
  (248395, 2, 2),
  (249635, 6, 9),
  (252721, 6, 8),
  (256339, 9, 3),
  (258080, 4, 10),
  (258958, 1, 15),
  (260126, 4, 17),
  (260159, 9, 10),
  (260932, 7, 9),
  (263276, 9, 7),
  (264578, 3, 18),
  (264949, 7, 17),
  (268012, 2, 18),
  (273991, 1, 18),
  (274635, 10, 0),
  (278854, 4, 20),
  (282111, 1, 11),
  (282451, 0, 17),
  (283301, 1, 22),
  (284861, 3, 18),
  (289981, 11, 11),
  (290930, 8, 3),
  (294409, 4, 9),
  (296292, 4, 10),
  (296447, 1, 18),
  (297776, 8, 13),
  (300363, 8, 2),
  (300986, 3, 10),
  (303700, 2, 3),
  (304340, 11, 18),
  (307787, 4, 22),
  (307997, 1, 10),
  (309808, 5, 10),
  (310993, 2, 3),
  (314942, 6, 22),
  (321286, 2, 18),
  (321675, 11, 22),
  (322086, 4, 9),
  (328969, 3, 13),
  (330206, 11, 22),
  (333280, 0, 6),
  (336080, 1, 11),
  (338422, 1, 0),
  (338518, 6, 10),
  (339712, 3, 7),
  (340963, 11, 17),
  (341899, 10, 10),
  (342086, 0, 22),
  (344509, 6, 17),
  (348894, 8, 7),
  (350674, 8, 18),
  (351750, 4, 15),
  (353016, 4, 17),
  (353177, 0, 0),
  (353705, 9, 13),
  (360223, 6, 9),
  (362344, 10, 11),
  (362878, 9, 18),
  (368885, 2, 18),
  (369135, 6, 17),
  (378338, 0, 0),
  (378535, 8, 3),
  (380969, 2, 13),
  (382936, 6, 21),
  (383371, 5, 10),
  (384634, 7, 10),
  (385840, 6, 10),
  (388528, 4, 10),
  (389029, 9, 3),
  (389163, 10, 0),
  (389366, 11, 18),
  (390556, 7, 22),
  (393102, 11, 0),
  (394149, 11, 10),
  (394183, 6, 21),
  (395817, 3, 18),
  (396013, 10, 0),
  (399367, 3, 17),
  (402672, 5, 10),
  (405888, 10, 6),
  (406654, 4, 21),
  (406682, 3, 13),
  (407169, 10, 5),
  (407678, 3, 15),
  (410668, 5, 17),
  (411400, 1, 10),
  (415826, 1, 11),
  (418228, 2, 18),
  (420032, 11, 17),
  (422425, 9, 13),
  (422453, 0, 11),
  (424238, 9, 7),
  (425043, 9, 3),
  (428603, 11, 22),
  (431511, 5, 9),
  (436763, 1, 0),
  (439841, 1, 0),
  (440869, 2, 15),
  (440999, 5, 22),
  (448629, 3, 18),
  (449418, 7, 16),
  (451583, 8, 14),
  (453325, 2, 18),
  (456770, 7, 22),
  (457818, 9, 6),
  (462144, 11, 0),
  (462369, 9, 7),
  (468519, 9, 17),
  (468721, 4, 22),
  (473593, 0, 10),
  (474170, 4, 10),
  (476961, 7, 18),
  (477482, 6, 2),
  (480194, 5, 10),
  (480250, 9, 13),
  (481763, 7, 10),
  (482379, 8, 6),
  (485139, 10, 4),
  (485664, 0, 18),
  (487723, 8, 3),
  (492748, 11, 22),
  (495248, 1, 17),
  (498894, 8, 16),
  (499660, 9, 10),
  (500825, 8, 18),
  (500874, 8, 9),
  (501610, 10, 22),
  (503132, 2, 7),
  (511289, 8, 10),
  (516680, 1, 20),
  (517323, 0, 11),
  (517870, 9, 10),
  (522408, 0, 22),
  (523808, 9, 15),
  (525975, 6, 16),
  (526238, 11, 22),
  (528328, 2, 18),
  (532224, 6, 22),
  (533344, 9, 17),
  (533634, 10, 22),
  (534066, 11, 19),
  (534519, 1, 17),
  (534523, 10, 11),
  (534718, 10, 10),
  (537184, 9, 18),
  (537230, 9, 3),
  (540763, 10, 7),
  (541748, 6, 17),
  (543785, 9, 18),
  (543907, 8, 6),
  (544816, 9, 18),
  (544927, 7, 21),
  (547774, 5, 12),
  (548379, 7, 17),
  (551709, 3, 18),
  (553853, 2, 3),
  (557065, 3, 16),
  (560267, 5, 22),
  (561590, 5, 21),
  (561956, 1, 19),
  (564475, 4, 9),
  (566973, 5, 10),
  (572778, 3, 13),
  (575910, 8, 18),
  (577062, 1, 22),
  (577363, 6, 10),
  (577516, 8, 18),
  (577696, 0, 10),
  (577940, 1, 10),
  (578915, 7, 22),
  (584502, 9, 10),
  (586876, 8, 18),
  (586971, 4, 10),
  (588417, 1, 17),
  (589362, 7, 20),
  (590512, 1, 0),
  (595180, 9, 3),
  (596494, 1, 18),
  (597686, 3, 3),
  (597944, 1, 22),
  (598881, 5, 10),
  (599159, 1, 10),
  (599892, 0, 0),
  (601838, 1, 11),
  (601854, 3, 13),
  (602308, 8, 18),
  (603866, 1, 11),
  (612573, 9, 17),
  (613803, 6, 20),
  (619389, 1, 11),
  (619988, 4, 22),
  (622569, 7, 22),
  (624072, 2, 3),
  (624322, 11, 21),
  (628642, 8, 18),
  (630033, 8, 13),
  (632369, 0, 22),
  (633970, 10, 22),
  (647387, 8, 10),
  (653762, 8, 10),
  (656376, 6, 15),
  (656767, 10, 19),
  (658654, 4, 21),
  (662615, 8, 18),
  (663441, 2, 3),
  (663893, 6, 22),
  (666256, 5, 21),
  (666323, 4, 17),
  (667133, 11, 0),
  (670639, 2, 7),
  (670648, 8, 15),
  (679835, 9, 15),
  (683053, 10, 0),
  (686447, 4, 16),
  (688150, 9, 18),
  (688797, 5, 10),
  (689031, 10, 22),
  (689851, 4, 17),
  (691654, 3, 3),
  (693974, 2, 10),
  (694227, 6, 9),
  (695796, 3, 18),
  (697773, 7, 21),
  (701718, 7, 9),
  (701978, 6, 20),
  (705368, 7, 10),
  (708656, 2, 3),
  (709325, 10, 17),
  (709473, 9, 7),
  (710918, 2, 13),
  (714934, 4, 16),
  (718344, 5, 4),
  (721051, 3, 10),
  (721900, 5, 9),
  (722726, 5, 9),
  (723089, 0, 10),
  (723113, 9, 10),
  (723113, 11, 18),
  (726944, 9, 5),
  (731144, 11, 17),
  (731170, 2, 7),
  (733707, 2, 14),
  (738254, 10, 11),
  (740828, 10, 22),
  (743465, 7, 10),
  (744548, 8, 18),
  (745828, 9, 3),
  (746520, 1, 10),
  (748211, 0, 22),
  (749165, 10, 22),
  (754970, 10, 17),
  (755188, 9, 7),
  (757081, 1, 11),
  (758377, 5, 21),
  (760447, 7, 15),
  (761651, 3, 15),
  (770900, 0, 18),
  (772215, 7, 9),
  (772600, 4, 10),
  (773390, 7, 10),
  (773426, 11, 0),
  (778072, 10, 6),
  (779042, 0, 11),
  (780751, 10, 10),
  (784638, 10, 18),
  (786856, 4, 21),
  (787028, 1, 0),
  (788271, 1, 10),
  (788729, 11, 0),
  (789633, 6, 5),
  (790678, 8, 3),
  (793094, 3, 13),
  (793147, 1, 18),
  (793580, 10, 22),
  (793977, 0, 22),
  (794718, 11, 14),
  (794979, 7, 10),
  (798384, 10, 18),
  (798591, 1, 22),
  (798669, 2, 18),
  (804560, 8, 3),
  (805773, 5, 16),
  (806214, 7, 17),
  (808153, 10, 22),
  (812115, 4, 22),
  (813445, 7, 16),
  (816594, 5, 22),
  (821025, 8, 13),
  (821338, 7, 17),
  (821437, 10, 0),
  (824108, 11, 10),
  (827594, 2, 7),
  (827787, 5, 17),
  (828482, 9, 18),
  (829614, 11, 18),
  (830468, 7, 16),
  (831560, 9, 12),
  (836326, 8, 15),
  (840809, 0, 11),
  (841837, 2, 7),
  (842218, 4, 8),
  (843345, 3, 18),
  (843503, 8, 3),
  (844197, 5, 9),
  (846190, 2, 18),
  (846516, 4, 10),
  (848824, 0, 0),
  (851763, 6, 10),
  (853767, 2, 15),
  (855579, 6, 17),
  (857173, 6, 22),
  (857347, 3, 18),
  (858597, 5, 15),
  (860861, 7, 10),
  (861983, 11, 0),
  (862377, 9, 15),
  (866545, 2, 15),
  (867361, 4, 5),
  (868895, 1, 0),
  (874580, 9, 3),
  (876463, 7, 21),
  (884738, 0, 21),
  (885630, 8, 3),
  (886906, 5, 17),
  (888526, 1, 22),
  (889826, 6, 10),
  (889869, 7, 4),
  (891151, 8, 15),
  (895378, 3, 3),
  (899864, 3, 6),
  (900606, 11, 0),
  (901047, 0, 6),
  (901628, 0, 9),
  (901917, 9, 18),
  (903458, 2, 7),
  (903569, 6, 13),
  (905073, 8, 3),
  (906232, 0, 0),
  (908894, 11, 22),
  (909326, 6, 10),
  (910753, 10, 0),
  (914966, 9, 12),
  (916203, 4, 22),
  (917881, 9, 17),
  (923381, 5, 22),
  (924385, 1, 10),
  (924430, 6, 22),
  (925562, 3, 13),
  (926719, 0, 0),
  (927323, 5, 10),
  (927618, 0, 9),
  (931500, 0, 11),
  (935358, 9, 7),
  (939565, 10, 22),
  (941154, 8, 10),
  (941462, 9, 18),
  (943913, 9, 18),
  (946093, 2, 17),
  (946908, 9, 3),
  (948149, 9, 13),
  (948405, 1, 20),
  (948843, 5, 16),
  (949444, 5, 22),
  (951893, 1, 21),
  (954669, 9, 13),
  (956895, 8, 3),
  (960133, 5, 10),
  (964095, 8, 10),
  (966588, 9, 15),
  (973432, 9, 13),
  (975469, 7, 10),
  (977500, 5, 22),
  (981235, 1, 11),
  (981315, 5, 17),
  (981681, 7, 16),
  (982361, 0, 21),
  (983948, 7, 22),
  (985339, 0, 0),
  (991321, 3, 15),
  (994332, 10, 17),
  (994448, 5, 16),
  (999875, 0, 22),
  (1000818, 2, 18),
  (1002716, 1, 0),
  (1003685, 1, 16),
  (1005359, 0, 0),
  (1010229, 1, 22),
  (1011081, 6, 22),
  (1017359, 8, 7),
  (1022971, 6, 9),
  (1027092, 6, 22),
  (1029402, 1, 0),
  (1029586, 9, 18),
  (1034687, 3, 10),
  (1035378, 10, 22),
  (1036064, 2, 15),
  (1040285, 3, 3),
  (1040457, 1, 22),
  (1042371, 7, 17),
  (1044038, 5, 9),
  (1045463, 6, 17),
  (1045652, 6, 16),
  (1049777, 11, 22),
  (1051798, 0, 22),
  (1052898, 4, 13),
  (1055969, 5, 17),
  (1056227, 10, 0),
  (1058728, 7, 16),
  (1058896, 4, 17),
  (1059745, 3, 15),
  (1060353, 10, 0),
  (1063283, 0, 22),
  (1063318, 1, 11),
  (1064681, 10, 18),
  (1067263, 6, 16),
  (1072966, 7, 14),
  (1074371, 0, 22),
  (1074549, 8, 3),
  (1074639, 2, 18),
  (1080383, 3, 17),
  (1081815, 10, 0),
  (1085489, 0, 0),
  (1085800, 4, 7),
  (1087028, 8, 3),
  (1088577, 6, 10),
  (1092013, 1, 22),
  (1093239, 8, 18),
  (1095898, 8, 15),
  (1099346, 9, 12),
  (1099784, 4, 10),
  (1100482, 8, 7),
  (1102456, 10, 10),
  (1105485, 5, 22),
  (1105918, 2, 3),
  (1107502, 5, 22),
  (1108953, 1, 0),
  (1114086, 2, 13),
  (1117607, 3, 15),
  (1122278, 7, 22),
  (1122785, 11, 10),
  (1123689, 11, 11),
  (1124781, 8, 15),
  (1125958, 0, 0),
  (1126298, 11, 10),
  (1132730, 3, 7),
  (1132909, 10, 18),
  (1135861, 3, 13),
  (1136915, 7, 22),
  (1138519, 11, 22),
  (1140991, 3, 3),
  (1142574, 9, 4),
  (1143384, 6, 9),
  (1143514, 5, 10),
  (1143931, 8, 9),
  (1149944, 11, 22),
  (1154676, 6, 22),
  (1155095, 4, 22),
  (1155448, 6, 22),
  (1155910, 4, 17),
  (1159555, 3, 17),
  (1161091, 5, 10),
  (1162632, 2, 10),
  (1171787, 11, 0),
  (1174103, 11, 22),
  (1174123, 10, 11),
  (1176177, 0, 0),
  (1177237, 4, 19),
  (1177476, 1, 19),
  (1184850, 0, 22),
  (1186814, 9, 3),
  (1187596, 10, 22),
  (1188200, 6, 9),
  (1190464, 9, 15),
  (1197274, 10, 14),
  (1197553, 9, 7),
  (1199800, 0, 18),
  (1202321, 7, 9),
  (1202328, 0, 0),
  (1202431, 0, 21),
  (1206726, 5, 8),
  (1209428, 8, 7),
  (1211683, 4, 22),
  (1213414, 0, 16),
  (1215396, 1, 22),
  (1215568, 4, 22),
  (1217034, 6, 13),
  (1218521, 7, 10),
  (1219446, 2, 18),
  (1220249, 5, 8),
  (1221501, 3, 7),
  (1226781, 8, 3),
  (1229363, 2, 7),
  (1229524, 0, 9),
  (1231379, 0, 0),
  (1232630, 5, 16),
  (1233613, 10, 0),
  (1234236, 9, 10),
  (1237037, 8, 7),
  (1238055, 4, 17),
  (1238149, 3, 18),
  (1239767, 1, 0),
  (1245447, 6, 16),
  (1245546, 6, 22),
  (1247150, 4, 19),
  (1250407, 8, 18),
  (1250812, 4, 17),
  (1253550, 11, 22),
  (1254731, 8, 3),
  (1255597, 6, 10),
  (1255989, 4, 8),
  (1258302, 1, 9),
  (1259538, 7, 21),
  (1260745, 6, 10),
  (1261568, 4, 10),
  (1264427, 5, 15),
  (1265201, 2, 17),
  (1267748, 0, 11),
  (1268066, 10, 0),
  (1268165, 2, 7),
  (1270875, 3, 3),
  (1272389, 8, 11),
  (1277941, 2, 7),
  (1278246, 10, 22),
  (1279038, 0, 10),
  (1280919, 10, 10),
  (1284228, 6, 21),
  (1286316, 1, 0),
  (1288802, 4, 21),
  (1289005, 0, 19),
  (1289069, 10, 22),
  (1292715, 7, 20),
  (1294094, 2, 10),
  (1296086, 5, 17),
  (1298743, 10, 10),
  (1305949, 3, 10),
  (1308415, 3, 13),
  (1313665, 7, 17),
  (1320388, 7, 20),
  (1322821, 8, 13),
  (1323077, 3, 13),
  (1333014, 9, 3),
  (1333520, 10, 22),
  (1338238, 5, 15),
  (1342385, 11, 17),
  (1345753, 1, 0),
  (1346674, 2, 3),
  (1348467, 1, 10),
  (1348929, 9, 12),
  (1351193, 11, 10),
  (1352200, 4, 10),
  (1353154, 8, 17),
  (1355962, 5, 21),
  (1356662, 2, 3),
  (1360546, 10, 17),
  (1364463, 2, 15),
  (1368107, 10, 0),
  (1368953, 1, 0),
  (1369685, 11, 11),
  (1370084, 0, 22),
  (1372698, 4, 10),
  (1379101, 5, 17),
  (1382943, 11, 3),
  (1385437, 7, 21),
  (1387943, 6, 22),
  (1388793, 2, 3),
  (1390817, 11, 0),
  (1392755, 4, 10),
  (1393613, 1, 17),
  (1394569, 7, 8),
  (1395788, 6, 22),
  (1395830, 10, 22),
  (1396566, 11, 6),
  (1399006, 1, 22),
  (1399047, 0, 11),
  (1399557, 5, 16),
  (1401209, 8, 10),
  (1401646, 0, 0),
  (1410282, 6, 22),
  (1411724, 3, 18),
  (1414678, 10, 10),
  (1416632, 8, 18),
  (1420695, 6, 12),
  (1421466, 5, 22),
  (1422255, 11, 0),
  (1429780, 9, 3),
  (1430615, 7, 17),
  (1432608, 8, 3),
  (1433176, 7, 17),
  (1443472, 3, 3),
  (1443724, 11, 11),
  (1446136, 8, 10),
  (1452298, 3, 17),
  (1454269, 5, 17),
  (1455147, 8, 7),
  (1458309, 5, 10),
  (1459739, 3, 13),
  (1464570, 6, 22),
  (1466122, 0, 22),
  (1466854, 11, 22),
  (1467640, 2, 18),
  (1468201, 6, 22),
  (1469438, 8, 2),
  (1472606, 8, 14),
  (1473637, 1, 6),
  (1475283, 5, 22),
  (1475941, 10, 0),
  (1476240, 7, 20),
  (1480224, 2, 17),
  (1480270, 2, 13),
  (1481538, 3, 18),
  (1485027, 4, 21),
  (1485176, 4, 22),
  (1485221, 10, 10),
  (1490587, 4, 22),
  (1494179, 4, 10),
  (1494690, 9, 14),
  (1502136, 6, 22),
  (1504808, 4, 10),
  (1505389, 9, 3),
  (1508467, 9, 3),
  (1514524, 1, 0),
  (1515080, 1, 0),
  (1515446, 4, 22),
  (1516497, 3, 13),
  (1517743, 3, 9),
  (1520399, 7, 22),
  (1520675, 9, 18),
  (1520748, 11, 22),
  (1521375, 6, 9),
  (1521500, 2, 7),
  (1522214, 3, 3),
  (1524001, 8, 3),
  (1525123, 7, 10),
  (1527381, 3, 3),
  (1529840, 11, 14),
  (1530265, 11, 22),
  (1531109, 8, 13),
  (1535717, 6, 10),
  (1536149, 9, 3),
  (1536933, 9, 10),
  (1537806, 6, 10),
  (1538515, 11, 11),
  (1539237, 6, 10),
  (1540541, 5, 22),
  (1541178, 8, 7),
  (1541647, 10, 0),
  (1545654, 5, 10),
  (1546397, 4, 22),
  (1547221, 7, 20),
  (1548306, 3, 3),
  (1548399, 2, 12),
  (1548747, 11, 22),
  (1549059, 2, 7),
  (1550778, 9, 18),
  (1550907, 10, 18),
  (1556439, 0, 10),
  (1560024, 0, 17),
  (1561263, 10, 11),
  (1562066, 10, 21),
  (1562602, 6, 10),
  (1572398, 1, 11),
  (1572583, 7, 10),
  (1574131, 3, 10),
  (1575432, 5, 22),
  (1575973, 6, 9),
  (1577736, 0, 0),
  (1579469, 2, 17),
  (1579972, 1, 11),
  (1580169, 5, 10),
  (1580355, 11, 22),
  (1582612, 6, 19),
  (1583424, 9, 3),
  (1584190, 9, 18),
  (1586450, 5, 15),
  (1586963, 3, 3),
  (1587394, 7, 17),
  (1593454, 8, 18),
  (1596068, 5, 22),
  (1596477, 1, 0),
  (1599002, 4, 17),
  (1599432, 9, 12),
  (1600296, 9, 18),
  (1600524, 3, 13),
  (1600662, 5, 9),
  (1600874, 10, 22),
  (1601729, 7, 16),
  (1603985, 3, 3),
  (1606296, 7, 22),
  (1612583, 2, 3),
  (1613399, 8, 17),
  (1614958, 3, 18),
  (1623928, 9, 18),
  (1624190, 1, 11),
  (1628842, 3, 18),
  (1630399, 4, 9),
  (1632873, 4, 13),
  (1634863, 1, 22),
  (1640396, 10, 18),
  (1641769, 4, 6),
  (1644166, 4, 21),
  (1645652, 4, 16),
  (1648841, 4, 21),
  (1651595, 3, 7),
  (1652081, 4, 22),
  (1652663, 11, 0),
  (1655076, 5, 17),
  (1658002, 4, 22),
  (1658817, 6, 19),
  (1659239, 1, 22),
  (1661702, 6, 21),
  (1662071, 7, 17),
  (1664032, 11, 0),
  (1664403, 7, 10),
  (1664437, 5, 22),
  (1665001, 9, 13),
  (1668277, 0, 22),
  (1671971, 0, 0),
  (1676485, 11, 0),
  (1676506, 7, 10),
  (1678802, 11, 6),
  (1679124, 7, 21),
  (1679540, 10, 22),
  (1680113, 9, 10),
  (1682064, 7, 17),
  (1683879, 8, 17),
  (1684123, 10, 21),
  (1685606, 11, 10),
  (1691543, 11, 0),
  (1694436, 9, 10),
  (1697104, 8, 15),
  (1697677, 5, 5),
  (1701750, 3, 13),
  (1704390, 9, 7),
  (1704904, 10, 17),
  (1706854, 2, 18),
  (1707316, 1, 0),
  (1707902, 8, 10),
  (1708027, 2, 18),
  (1715110, 1, 0),
  (1718898, 1, 0),
  (1721473, 1, 11),
  (1730897, 6, 22),
  (1735135, 11, 11),
  (1740726, 2, 18),
  (1741286, 1, 17),
  (1742393, 8, 7),
  (1744136, 3, 13),
  (1745440, 3, 13),
  (1745666, 11, 9),
  (1745794, 0, 10),
  (1746737, 2, 18),
  (1750635, 0, 22),
  (1752597, 11, 22),
  (1753820, 5, 17),
  (1754547, 5, 16),
  (1755388, 0, 22),
  (1755469, 1, 18),
  (1755563, 9, 2),
  (1756401, 10, 22),
  (1757898, 3, 7),
  (1760604, 7, 22),
  (1761940, 0, 0),
  (1762423, 9, 1),
  (1763107, 6, 9),
  (1764988, 7, 17),
  (1765843, 6, 10),
  (1765918, 1, 0),
  (1770885, 2, 7),
  (1773810, 5, 21),
  (1774064, 0, 10),
  (1775165, 8, 18),
  (1776362, 4, 11),
  (1779502, 7, 16),
  (1782955, 3, 15),
  (1786432, 9, 10),
  (1789879, 0, 17),
  (1792344, 11, 10),
  (1792359, 9, 7),
  (1793437, 2, 9),
  (1795912, 7, 2),
  (1796674, 1, 0),
  (1797939, 6, 10),
  (1800591, 9, 16),
  (1802962, 6, 8),
  (1803730, 9, 6),
  (1805359, 10, 0),
  (1807742, 6, 10),
  (1810169, 1, 18),
  (1811493, 1, 17),
  (1812704, 7, 22),
  (1813012, 0, 0),
  (1813864, 5, 22),
  (1815900, 9, 10),
  (1819110, 9, 7),
  (1819970, 1, 22),
  (1821324, 3, 7),
  (1822251, 10, 22),
  (1822640, 5, 22),
  (1823813, 0, 6),
  (1824214, 3, 2),
  (1829637, 11, 22),
  (1830230, 10, 0),
  (1831224, 0, 22),
  (1833221, 9, 6),
  (1834572, 2, 3),
  (1835587, 6, 10),
  (1840299, 3, 10),
  (1844048, 10, 6),
  (1844074, 11, 17),
  (1846649, 9, 9),
  (1849242, 3, 18),
  (1849469, 1, 22),
  (1856056, 10, 22),
  (1860620, 2, 13),
  (1865682, 6, 17),
  (1866223, 6, 10),
  (1867674, 7, 9),
  (1868215, 6, 21),
  (1871006, 11, 11),
  (1873925, 2, 10),
  (1876444, 8, 13),
  (1877607, 6, 22),
  (1877608, 1, 18),
  (1878894, 0, 18),
  (1879370, 11, 22),
  (1882983, 5, 22),
  (1887185, 1, 10),
  (1887602, 8, 18),
  (1887630, 10, 0),
  (1892082, 2, 18),
  (1892750, 7, 10),
  (1905781, 9, 15),
  (1907507, 5, 22),
  (1909020, 4, 22),
  (1909426, 9, 13),
  (1911449, 7, 22),
  (1913488, 4, 18),
  (1919469, 4, 22),
  (1920889, 6, 22),
  (1921524, 2, 13),
  (1922041, 10, 9),
  (1922576, 3, 17),
  (1924444, 4, 10),
  (1924469, 3, 9),
  (1924860, 4, 9),
  (1926107, 10, 22),
  (1926572, 9, 18),
  (1928889, 9, 14),
  (1928899, 6, 9),
  (1930870, 0, 21),
  (1935202, 8, 18),
  (1942294, 3, 18),
  (1943535, 11, 19),
  (1945064, 10, 11),
  (1946017, 2, 17),
  (1946522, 8, 10),
  (1949697, 7, 9),
  (1958782, 1, 11),
  (1964422, 9, 18),
  (1966377, 0, 10),
  (1969625, 6, 18),
  (1970074, 6, 22),
  (1972127, 10, 11),
  (1973217, 7, 10),
  (1975773, 3, 10),
  (1977597, 4, 10),
  (1980344, 7, 16),
  (1981277, 0, 22),
  (1981286, 10, 6),
  (1984447, 6, 21),
  (1987768, 8, 18),
  (1988227, 1, 22),
  (1989403, 3, 18),
  (1991599, 1, 19),
  (1994093, 10, 22),
  (1996295, 3, 4),
  (1997536, 1, 17),
  (1999991, 2, 13),
  (2001276, 2, 13),
  (2011289, 1, 0),
  (2011869, 1, 22),
  (2012613, 8, 3),
  (2017961, 10, 18),
  (2019863, 10, 22),
  (2021303, 1, 11),
  (2021467, 6, 8),
  (2023915, 4, 16),
  (2024021, 1, 17),
  (2024301, 11, 18),
  (2025038, 9, 3),
  (2029258, 5, 22),
  (2031456, 10, 22),
  (2031555, 5, 10),
  (2032222, 5, 10),
  (2034878, 4, 10),
  (2036569, 1, 21),
  (2049625, 3, 18),
  (2049869, 9, 10),
  (2051626, 3, 12),
  (2052461, 5, 19),
  (2053756, 6, 11),
  (2057873, 3, 4),
  (2062685, 10, 11),
  (2065888, 10, 22),
  (2066244, 11, 0),
  (2069436, 6, 9),
  (2071099, 3, 3),
  (2071376, 2, 7),
  (2071460, 9, 15),
  (2081345, 9, 14),
  (2082640, 11, 0),
  (2082985, 0, 22),
  (2084490, 3, 7),
  (2086489, 9, 10),
  (2086945, 2, 3),
  (2088434, 0, 0),
  (2088676, 9, 10),
  (2092100, 4, 8),
  (2099807, 1, 6),
  (2100823, 2, 15),
  (2100887, 2, 3),
  (2100987, 10, 11),
  (2102988, 5, 10),
  (2104941, 11, 10),
  (2104978, 7, 8),
  (2105144, 1, 11),
  (2105622, 0, 11),
  (2105849, 6, 10),
  (2107341, 1, 22),
  (2110949, 2, 16),
  (2112162, 4, 16),
  (2112308, 9, 6),
  (2117768, 2, 3),
  (2118820, 9, 18),
  (2122291, 8, 18),
  (2124417, 2, 7),
  (2125390, 9, 10),
  (2127134, 6, 10),
  (2129195, 8, 7),
  (2136390, 4, 15),
  (2138281, 2, 10),
  (2139695, 10, 21),
  (2140002, 3, 14),
  (2140050, 0, 18),
  (2143175, 0, 21),
  (2144185, 6, 21),
  (2144427, 11, 0),
  (2144729, 8, 3),
  (2144758, 6, 10),
  (2145308, 2, 17),
  (2145313, 4, 20),
  (2146734, 3, 16),
  (2147667, 11, 22),
  (2147883, 2, 7),
  (2149563, 0, 0),
  (2149898, 5, 20),
  (2158140, 1, 11),
  (2158627, 6, 17),
  (2160448, 10, 10),
  (2160693, 0, 11),
  (2161132, 6, 10),
  (2163052, 9, 12),
  (2163924, 8, 16),
  (2165218, 9, 7),
  (2168637, 9, 18),
  (2172079, 4, 10),
  (2175194, 9, 2),
  (2177141, 0, 11),
  (2178236, 2, 3),
  (2179330, 10, 22),
  (2181335, 5, 22),
  (2181630, 4, 9),
  (2182453, 2, 18),
  (2182623, 6, 10),
  (2182674, 7, 10),
  (2184005, 6, 10),
  (2189497, 4, 9),
  (2190089, 9, 18),
  (2191802, 11, 17),
  (2192502, 10, 22),
  (2193879, 9, 7),
  (2198137, 0, 10),
  (2198838, 11, 10),
  (2202869, 11, 22),
  (2204507, 2, 7),
  (2206414, 10, 0),
  (2206966, 2, 3),
  (2208198, 1, 17),
  (2209352, 6, 10),
  (2209380, 4, 9),
  (2210209, 3, 18),
  (2217133, 10, 0),
  (2219679, 1, 17),
  (2223530, 1, 11),
  (2223909, 3, 18),
  (2224324, 10, 17),
  (2226275, 7, 15),
  (2227378, 7, 22),
  (2230504, 3, 3),
  (2231055, 6, 20),
  (2232932, 8, 15),
  (2239033, 5, 5),
  (2241118, 10, 0),
  (2241464, 9, 3),
  (2242445, 10, 18),
  (2244000, 4, 22),
  (2245862, 0, 10),
  (2248346, 5, 17),
  (2250977, 5, 17),
  (2257531, 8, 7),
  (2262596, 3, 10),
  (2262642, 8, 18),
  (2264399, 8, 3),
  (2265555, 11, 17),
  (2265814, 0, 18),
  (2266800, 11, 0),
  (2268258, 3, 7),
  (2268812, 1, 22),
  (2269687, 6, 22),
  (2270491, 5, 9),
  (2276151, 11, 10),
  (2278556, 1, 18),
  (2280638, 2, 3),
  (2281422, 3, 3),
  (2282148, 7, 14),
  (2284472, 7, 5),
  (2287331, 2, 14),
  (2288734, 0, 18),
  (2294328, 10, 11),
  (2296731, 6, 22),
  (2299321, 4, 22),
  (2301900, 9, 3),
  (2302248, 11, 11),
  (2304694, 5, 10),
  (2309928, 3, 7),
  (2312582, 11, 0),
  (2317297, 4, 10),
  (2318484, 7, 17),
  (2318814, 1, 22),
  (2319019, 11, 10),
  (2321043, 2, 7),
  (2324841, 4, 17),
  (2325830, 7, 19),
  (2326612, 11, 16),
  (2329737, 5, 22),
  (2331928, 4, 13),
  (2332828, 5, 10),
  (2333464, 2, 3),
  (2337978, 10, 22),
  (2338008, 10, 10),
  (2344514, 6, 16),
  (2344678, 3, 8),
  (2349872, 6, 10),
  (2352637, 8, 2),
  (2353172, 4, 22),
  (2353609, 7, 17),
  (2354482, 7, 22),
  (2354540, 6, 21),
  (2355057, 0, 22),
  (2356391, 2, 14),
  (2356392, 3, 3),
  (2356420, 6, 9),
  (2358894, 1, 0),
  (2361818, 3, 7),
  (2361895, 0, 21),
  (2363463, 0, 16),
  (2365465, 10, 0),
  (2366535, 7, 9),
  (2369636, 7, 21),
  (2372348, 1, 22),
  (2376224, 10, 6),
  (2377641, 8, 18),
  (2379406, 3, 13),
  (2380735, 8, 10),
  (2386210, 2, 10),
  (2386323, 11, 17),
  (2386881, 2, 18),
  (2387551, 2, 17),
  (2389839, 7, 22),
  (2391808, 1, 21),
  (2394222, 5, 10),
  (2394833, 3, 2),
  (2401954, 10, 17),
  (2404312, 2, 10),
  (2404884, 3, 13),
  (2405309, 6, 17),
  (2409383, 2, 10),
  (2411135, 5, 20),
  (2413734, 4, 21),
  (2415586, 0, 11),
  (2419301, 1, 18),
  (2423112, 10, 22),
  (2429914, 10, 0),
  (2430465, 4, 22),
  (2433932, 9, 18),
  (2435433, 4, 17),
  (2439277, 2, 15),
  (2442828, 5, 9),
  (2445381, 2, 6),
  (2449628, 10, 17),
  (2450561, 0, 11),
  (2451467, 8, 18),
  (2453611, 11, 11),
  (2453761, 11, 0),
  (2455694, 2, 3),
  (2458935, 11, 0),
  (2464199, 4, 10),
  (2464227, 2, 13),
  (2465223, 4, 10),
  (2465879, 7, 17),
  (2466889, 4, 22),
  (2466902, 5, 9),
  (2471916, 7, 10),
  (2472044, 6, 20),
  (2474809, 1, 0),
  (2475864, 10, 11),
  (2476334, 8, 18),
  (2476461, 8, 13),
  (2477287, 5, 2),
  (2477717, 7, 19),
  (2477769, 0, 18),
  (2478084, 1, 18),
  (2486411, 11, 0),
  (2486478, 3, 7),
  (2486625, 3, 14),
  (2488237, 9, 10),
  (2490620, 7, 22),
  (2491134, 1, 6),
  (2493837, 2, 3),
  (2495419, 10, 17),
  (2497905, 1, 0),
  (2498064, 11, 22),
  (2498505, 10, 10),
  (2498954, 2, 10),
  (2499892, 2, 10),
  (2502848, 1, 11),
  (2504031, 11, 22),
  (2504941, 9, 13),
  (2508322, 11, 10),
  (2508640, 6, 9),
  (2508654, 9, 12),
  (2511483, 9, 7),
  (2512926, 4, 2),
  (2513316, 4, 17),
  (2516989, 6, 18),
  (2517381, 9, 7),
  (2518874, 9, 3),
  (2519922, 1, 22),
  (2520839, 1, 11),
  (2526759, 9, 3),
  (2529332, 7, 10),
  (2533169, 7, 20),
  (2542169, 2, 2),
  (2544599, 9, 7),
  (2544810, 5, 16),
  (2555951, 4, 10),
  (2558492, 0, 2),
  (2559245, 11, 14),
  (2561042, 0, 22),
  (2562642, 7, 22),
  (2563895, 4, 13),
  (2568977, 0, 20),
  (2570128, 4, 22),
  (2577048, 4, 20),
  (2577999, 0, 22),
  (2581236, 4, 8),
  (2583824, 1, 11),
  (2588415, 6, 22),
  (2592942, 8, 3),
  (2593749, 5, 5),
  (2595808, 0, 0),
  (2595987, 6, 17),
  (2597330, 8, 18),
  (2598333, 8, 7),
  (2603550, 6, 10),
  (2607827, 10, 6),
  (2609186, 1, 0),
  (2609416, 5, 9),
  (2618927, 5, 22),
  (2621155, 0, 0),
  (2627021, 9, 3),
  (2631561, 10, 22),
  (2631912, 9, 18),
  (2632794, 10, 11),
  (2638200, 3, 7),
  (2638524, 8, 3),
  (2640069, 3, 10),
  (2642987, 0, 0),
  (2644104, 10, 22),
  (2645516, 2, 13),
  (2649636, 7, 10),
  (2649724, 3, 5),
  (2651656, 1, 18),
  (2652674, 6, 10),
  (2658135, 7, 10),
  (2660267, 5, 17),
  (2660452, 1, 22),
  (2661319, 1, 0),
  (2666033, 0, 11),
  (2666434, 6, 15),
  (2667161, 1, 0),
  (2667549, 0, 17),
  (2668338, 7, 17),
  (2669651, 9, 18),
  (2670919, 8, 3),
  (2671609, 6, 17),
  (2674641, 8, 18),
  (2676184, 11, 0),
  (2676919, 1, 0),
  (2677691, 5, 9),
  (2678831, 3, 17),
  (2679540, 5, 9),
  (2682837, 11, 18),
  (2685385, 8, 15),
  (2686836, 3, 18),
  (2691694, 0, 9),
  (2693467, 11, 10),
  (2694998, 2, 6),
  (2695208, 11, 0),
  (2697808, 9, 7),
  (2702645, 1, 0),
  (2705991, 5, 22),
  (2707972, 0, 0),
  (2708470, 8, 18),
  (2709156, 4, 10),
  (2710291, 7, 18),
  (2710359, 0, 21),
  (2711249, 3, 3),
  (2712593, 0, 18),
  (2713866, 1, 0),
  (2719388, 5, 19),
  (2723340, 5, 10),
  (2723515, 11, 10),
  (2727084, 3, 10),
  (2727549, 0, 11),
  (2728192, 2, 10),
  (2728431, 5, 21),
  (2729298, 6, 19),
  (2729467, 11, 10),
  (2731038, 4, 21),
  (2732664, 3, 10),
  (2733789, 0, 22),
  (2735316, 3, 17),
  (2740160, 2, 7),
  (2744773, 6, 22),
  (2744979, 11, 0),
  (2746661, 6, 22),
  (2747375, 0, 0),
  (2748016, 6, 20),
  (2752960, 7, 14),
  (2755844, 9, 18),
  (2760771, 5, 17),
  (2768280, 5, 13),
  (2770702, 11, 11),
  (2776313, 4, 9),
  (2780524, 0, 22),
  (2780987, 11, 0),
  (2783062, 8, 3),
  (2785596, 1, 0),
  (2786801, 4, 16),
  (2789426, 7, 9),
  (2792615, 4, 9),
  (2794028, 5, 9),
  (2794433, 5, 10),
  (2797399, 3, 18),
  (2798488, 3, 6),
  (2798547, 1, 10),
  (2799600, 5, 15),
  (2800675, 2, 7),
  (2801420, 0, 9),
  (2801908, 11, 0),
  (2802726, 6, 22),
  (2803488, 4, 10),
  (2804332, 8, 3),
  (2805533, 10, 11),
  (2807767, 10, 0),
  (2807902, 2, 18),
  (2810763, 6, 22),
  (2814266, 1, 18),
  (2820338, 8, 7),
  (2820637, 0, 13),
  (2821880, 3, 3),
  (2822654, 3, 5),
  (2825089, 0, 22),
  (2825179, 6, 10),
  (2825482, 1, 22),
  (2830629, 8, 7),
  (2830930, 4, 21),
  (2838142, 9, 3),
  (2839901, 10, 18),
  (2841670, 0, 10),
  (2841728, 5, 9),
  (2845057, 9, 7),
  (2847471, 0, 0),
  (2847763, 6, 5),
  (2848209, 2, 15),
  (2850220, 4, 17),
  (2851503, 5, 22),
  (2852538, 10, 10),
  (2854962, 2, 13),
  (2866108, 4, 17),
  (2867203, 11, 22),
  (2870664, 10, 22),
  (2875258, 7, 5),
  (2887850, 4, 20),
  (2887903, 9, 3),
  (2888899, 2, 13),
  (2889745, 4, 22),
  (2889851, 1, 11),
  (2891548, 0, 10),
  (2899867, 4, 10),
  (2900138, 11, 6),
  (2900686, 7, 10),
  (2901539, 7, 17),
  (2905061, 2, 10),
  (2906806, 2, 13),
  (2908467, 11, 22),
  (2909449, 6, 22),
  (2909969, 1, 18),
  (2913112, 2, 3),
  (2916674, 7, 9),
  (2917105, 11, 22),
  (2924263, 0, 10),
  (2927222, 0, 19),
  (2932545, 4, 10),
  (2934350, 11, 22),
  (2935054, 11, 22),
  (2938053, 6, 22),
  (2943885, 11, 0),
  (2945477, 5, 17),
  (2945490, 8, 18),
  (2946985, 2, 7),
  (2947639, 3, 10),
  (2948131, 0, 0),
  (2952640, 6, 21),
  (2953845, 8, 18),
  (2954019, 11, 21),
  (2955535, 4, 22),
  (2955729, 0, 0),
  (2958066, 1, 2),
  (2958148, 2, 7),
  (2958630, 10, 22),
  (2962078, 3, 10),
  (2964678, 3, 3),
  (2965856, 8, 13),
  (2966167, 3, 18),
  (2966872, 5, 17),
  (2968585, 8, 12),
  (2969122, 5, 4),
  (2969330, 3, 12),
  (2971902, 1, 22),
  (2972547, 11, 10),
  (2972699, 6, 22),
  (2972746, 0, 10),
  (2972799, 0, 22),
  (2975577, 11, 19),
  (2976616, 3, 14),
  (2978759, 2, 11),
  (2983000, 10, 11),
  (2983386, 8, 6),
  (2984761, 10, 6),
  (2984886, 1, 3),
  (2984932, 5, 17),
  (2985173, 1, 14),
  (2985496, 11, 17),
  (2986373, 7, 2),
  (2987355, 9, 18),
  (2988885, 7, 22),
  (2989860, 10, 0),
  (2990210, 3, 7),
  (2991335, 3, 3),
  (2993672, 11, 22),
  (2997968, 7, 10),
  (2998148, 5, 10),
  (2998170, 8, 15),
  (2998656, 6, 10),
  (2998789, 3, 1),
  (3000670, 8, 18),
  (3003209, 4, 10),
  (3006657, 9, 10),
  (3013303, 2, 3),
  (3015517, 9, 3),
  (3016957, 3, 7),
  (3019712, 5, 13),
  (3021951, 10, 22),
  (3022158, 3, 18),
  (3023334, 0, 11),
  (3023779, 2, 6),
  (3029452, 0, 10),
  (3030189, 9, 13),
  (3033138, 1, 22),
  (3034836, 3, 16),
  (3036834, 7, 9),
  (3037623, 5, 9),
  (3038022, 7, 22),
  (3040564, 7, 17),
  (3043473, 2, 15),
  (3044434, 5, 17),
  (3047739, 10, 20),
  (3052556, 5, 22),
  (3053163, 1, 11),
  (3054125, 9, 15),
  (3055234, 7, 22),
  (3055739, 6, 22),
  (3057915, 10, 22),
  (3059164, 3, 15),
  (3062942, 0, 0),
  (3063768, 5, 21),
  (3071816, 3, 17),
  (3075162, 9, 10),
  (3075858, 5, 16),
  (3078627, 4, 16),
  (3081690, 3, 15),
  (3082187, 8, 6),
  (3085460, 11, 11),
  (3086726, 3, 3),
  (3089269, 7, 20),
  (3091889, 5, 18),
  (3092896, 5, 18),
  (3093376, 5, 13),
  (3095798, 9, 7),
  (3099610, 11, 0),
  (3101488, 4, 21),
  (3101711, 11, 11),
  (3101822, 11, 10),
  (3104585, 6, 10),
  (3104691, 8, 18),
  (3105445, 11, 22),
  (3109069, 8, 10),
  (3110869, 7, 10),
  (3113276, 2, 10),
  (3113588, 2, 18),
  (3114983, 11, 22),
  (3115438, 2, 15),
  (3116011, 1, 22),
  (3117668, 5, 22),
  (3119724, 3, 2),
  (3133497, 4, 21),
  (3134721, 11, 18),
  (3137484, 11, 13),
  (3139392, 0, 0),
  (3142905, 2, 18),
  (3143423, 9, 3),
  (3147776, 4, 22),
  (3157260, 10, 17),
  (3157306, 8, 17),
  (3159892, 5, 10),
  (3160137, 7, 22),
  (3160424, 0, 10),
  (3163464, 1, 18),
  (3165446, 2, 18),
  (3166742, 7, 17),
  (3166876, 11, 11),
  (3166957, 4, 22),
  (3168495, 3, 7),
  (3171217, 8, 3),
  (3174222, 3, 7),
  (3174904, 4, 22),
  (3175741, 9, 18),
  (3177132, 7, 21),
  (3177458, 1, 11),
  (3177814, 4, 17),
  (3179173, 1, 11),
  (3182614, 5, 17),
  (3187622, 10, 0),
  (3191416, 9, 7),
  (3191974, 3, 17),
  (3194689, 10, 0),
  (3195453, 0, 22),
  (3196649, 1, 17),
  (3197384, 2, 7),
  (3197664, 1, 22),
  (3200758, 3, 18),
  (3200940, 1, 0),
  (3202887, 4, 19),
  (3203441, 10, 17),
  (3206898, 4, 21),
  (3207335, 4, 5),
  (3217298, 10, 20),
  (3217842, 5, 10),
  (3218953, 8, 18),
  (3222229, 7, 10),
  (3225401, 5, 10),
  (3226394, 1, 0),
  (3227002, 3, 13),
  (3228014, 5, 8),
  (3228626, 8, 10),
  (3229341, 1, 17),
  (3231458, 10, 10),
  (3236703, 1, 11),
  (3239945, 2, 17),
  (3245938, 4, 22),
  (3246084, 4, 9),
  (3250658, 9, 17),
  (3252013, 6, 21),
  (3253589, 10, 17),
  (3256853, 1, 22),
  (3257652, 7, 10),
  (3259007, 5, 19),
  (3261131, 4, 22),
  (3261582, 1, 17),
  (3262292, 3, 18),
  (3263270, 1, 22),
  (3267562, 11, 10),
  (3273017, 7, 10),
  (3273268, 7, 15),
  (3273681, 5, 19),
  (3274492, 4, 16),
  (3277352, 11, 22),
  (3279278, 2, 3),
  (3280375, 10, 21),
  (3283487, 5, 13),
  (3289605, 2, 18),
  (3290541, 11, 22),
  (3294023, 2, 3),
  (3294168, 9, 10),
  (3295376, 1, 18),
  (3297260, 2, 6),
  (3298936, 6, 13),
  (3298975, 10, 21),
  (3301346, 5, 10),
  (3303276, 3, 18),
  (3303318, 6, 17),
  (3308096, 0, 11),
  (3309844, 11, 22),
  (3315161, 9, 15),
  (3316077, 5, 16),
  (3316577, 1, 16),
  (3319201, 6, 22),
  (3320179, 2, 6),
  (3323775, 5, 17),
  (3323837, 0, 22),
  (3323969, 1, 0),
  (3326236, 1, 18),
  (3326817, 3, 10),
  (3331414, 7, 10),
  (3333146, 5, 21),
  (3342663, 6, 21),
  (3344162, 0, 22),
  (3344572, 7, 22),
  (3347824, 0, 11),
  (3350952, 6, 22),
  (3354806, 8, 12),
  (3365523, 10, 22),
  (3365818, 0, 9),
  (3368965, 10, 18),
  (3373429, 2, 17),
  (3373514, 6, 22),
  (3375685, 11, 9),
  (3375750, 10, 22),
  (3375925, 9, 15),
  (3379487, 1, 10),
  (3380698, 0, 0),
  (3384753, 3, 18),
  (3385442, 7, 5),
  (3389437, 3, 18),
  (3389651, 9, 13),
  (3394100, 10, 11),
  (3394685, 8, 7),
  (3396698, 5, 22),
  (3399147, 1, 10),
  (3399847, 7, 17),
  (3400712, 0, 0),
  (3401360, 6, 8),
  (3402623, 1, 0),
  (3403189, 11, 22),
  (3403368, 7, 10),
  (3406716, 6, 17),
  (3407660, 9, 18),
  (3412295, 1, 17),
  (3415804, 2, 3),
  (3418951, 11, 0),
  (3419090, 9, 7),
  (3419944, 3, 13),
  (3420933, 0, 10),
  (3424488, 3, 7),
  (3426585, 9, 7),
  (3426946, 1, 11),
  (3430688, 8, 16),
  (3432018, 2, 3),
  (3440060, 5, 1),
  (3440270, 0, 21),
  (3443196, 7, 16),
  (3447882, 9, 18),
  (3449260, 2, 7),
  (3452174, 3, 17),
  (3455830, 9, 13),
  (3455947, 0, 10),
  (3457201, 2, 3),
  (3459892, 0, 22),
  (3468832, 2, 3),
  (3469051, 4, 17),
  (3470874, 2, 18),
  (3472606, 5, 19),
  (3475568, 8, 3),
  (3476896, 6, 10),
  (3478134, 3, 7),
  (3479303, 3, 3),
  (3479311, 8, 10),
  (3480138, 1, 18),
  (3481579, 11, 11),
  (3481965, 0, 22),
  (3483783, 3, 14),
  (3486249, 2, 3),
  (3487633, 10, 22),
  (3490908, 9, 18),
  (3491682, 2, 18),
  (3492564, 11, 22),
  (3497346, 5, 22),
  (3499278, 3, 10),
  (3502525, 8, 18),
  (3506874, 0, 10),
  (3512047, 10, 17),
  (3512697, 10, 14),
  (3518140, 4, 19),
  (3520133, 1, 22),
  (3520269, 3, 17),
  (3521236, 6, 10),
  (3521411, 6, 10),
  (3522941, 11, 22),
  (3524685, 1, 18),
  (3525216, 1, 22),
  (3537008, 4, 22),
  (3537962, 4, 17),
  (3538809, 0, 0),
  (3541487, 8, 18),
  (3542280, 4, 9),
  (3542839, 1, 17),
  (3544800, 2, 3),
  (3545631, 6, 20),
  (3548997, 11, 10),
  (3549401, 6, 17),
  (3552514, 11, 21),
  (3554913, 4, 22),
  (3555752, 2, 18),
  (3556529, 3, 18),
  (3557573, 6, 22),
  (3563947, 4, 17),
  (3566067, 7, 22),
  (3569408, 9, 15),
  (3570311, 9, 18),
  (3572999, 3, 8),
  (3573297, 10, 6),
  (3580123, 6, 10),
  (3583117, 2, 7),
  (3584748, 1, 11),
  (3586969, 2, 7),
  (3591567, 9, 3),
  (3595606, 10, 11),
  (3596709, 4, 9),
  (3599467, 8, 17),
])