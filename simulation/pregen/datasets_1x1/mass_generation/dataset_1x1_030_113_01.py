from util import *
schedule = deque([
  (343, 3, 4),
  (391, 0, 0),
  (1676, 2, 7),
  (2594, 1, 7),
  (3211, 6, 0),
  (4339, 0, 7),
  (4938, 0, 3),
  (7142, 0, 3),
  (8133, 2, 2),
  (11818, 3, 2),
  (12229, 7, 2),
  (13538, 4, 2),
  (14842, 3, 7),
  (20365, 0, 4),
  (21498, 3, 2),
  (23408, 3, 3),
  (27531, 0, 4),
  (28420, 3, 6),
  (31053, 3, 6),
  (33743, 6, 7),
  (39054, 0, 7),
  (39770, 1, 0),
  (40510, 1, 6),
  (42866, 4, 6),
  (45450, 5, 7),
  (50895, 3, 2),
  (54486, 6, 7),
  (55439, 0, 5),
  (58505, 7, 7),
  (59099, 5, 3),
  (60692, 0, 0),
  (64407, 1, 3),
  (64705, 1, 7),
  (65869, 3, 7),
  (72536, 0, 0),
  (72842, 6, 4),
  (75098, 4, 6),
  (78518, 7, 0),
  (79396, 0, 7),
  (86127, 1, 0),
  (87600, 2, 3),
  (94388, 3, 6),
  (97929, 2, 5),
  (98470, 5, 3),
  (100097, 3, 7),
  (101084, 7, 6),
  (103411, 4, 2),
  (108371, 6, 7),
  (110605, 1, 4),
  (116749, 6, 7),
  (117731, 2, 5),
  (121013, 4, 4),
  (121516, 3, 5),
  (124440, 0, 7),
  (124573, 0, 7),
  (126091, 0, 7),
  (131566, 1, 0),
  (134416, 1, 2),
  (134480, 1, 4),
  (134613, 4, 2),
  (134690, 0, 7),
  (136448, 3, 2),
  (138056, 0, 0),
  (138346, 7, 0),
  (138537, 1, 7),
  (140493, 4, 6),
  (140893, 4, 7),
  (142505, 1, 0),
  (143617, 2, 1),
  (144677, 5, 3),
  (146920, 4, 7),
  (149887, 4, 6),
  (150850, 6, 7),
  (150951, 4, 7),
  (152021, 1, 7),
  (154487, 7, 5),
  (156134, 6, 6),
  (157697, 5, 3),
  (158598, 6, 7),
  (158750, 4, 2),
  (161545, 1, 4),
  (162492, 1, 7),
  (170040, 0, 0),
  (171539, 4, 3),
  (171716, 7, 7),
  (173187, 7, 4),
  (178238, 7, 0),
  (180452, 2, 3),
  (184569, 4, 5),
  (187801, 7, 7),
  (190147, 0, 7),
  (193314, 0, 0),
  (195809, 1, 4),
  (195995, 3, 5),
  (198928, 5, 7),
  (202474, 3, 4),
  (202830, 4, 5),
  (203020, 1, 7),
  (204568, 0, 7),
  (205089, 1, 3),
  (206928, 4, 7),
  (211864, 2, 7),
  (212068, 5, 3),
  (215763, 7, 7),
  (215917, 5, 6),
  (217602, 7, 0),
  (217885, 3, 2),
  (224056, 2, 3),
  (224720, 7, 4),
  (228816, 3, 4),
  (230311, 0, 0),
  (231332, 3, 3),
  (231440, 0, 4),
  (232614, 3, 7),
  (233863, 4, 2),
  (236609, 7, 7),
  (236811, 7, 7),
  (237996, 0, 7),
  (238727, 4, 3),
  (238805, 7, 7),
  (239727, 2, 2),
  (240584, 1, 3),
  (243980, 6, 3),
  (248238, 1, 3),
  (248316, 5, 7),
  (251031, 0, 7),
  (252373, 3, 6),
  (256739, 3, 7),
  (257252, 7, 7),
  (262166, 2, 6),
  (264084, 5, 3),
  (265461, 4, 7),
  (267155, 5, 3),
  (270230, 5, 6),
  (274448, 0, 7),
  (274491, 4, 7),
  (277029, 2, 2),
  (281085, 0, 7),
  (284284, 3, 5),
  (293069, 6, 0),
  (295908, 6, 7),
  (296149, 5, 7),
  (297956, 3, 6),
  (299720, 6, 7),
  (300006, 5, 7),
  (301786, 6, 0),
  (302831, 0, 7),
  (304235, 6, 7),
  (308337, 2, 7),
  (311335, 7, 2),
  (311903, 1, 0),
  (313598, 5, 7),
  (314435, 6, 3),
  (317404, 0, 4),
  (318442, 3, 7),
  (319506, 1, 4),
  (329428, 0, 0),
  (329444, 0, 3),
  (333036, 0, 6),
  (338279, 5, 7),
  (339000, 3, 7),
  (339607, 5, 3),
  (341813, 5, 3),
  (343435, 1, 0),
  (343713, 2, 7),
  (347155, 1, 5),
  (347691, 3, 7),
  (348955, 5, 3),
  (354591, 4, 7),
  (354966, 1, 7),
  (356476, 4, 3),
  (356538, 4, 7),
  (358458, 2, 2),
  (360123, 6, 7),
  (360283, 4, 6),
  (360748, 5, 3),
  (362371, 2, 7),
  (365829, 5, 7),
  (366359, 4, 7),
  (366571, 4, 4),
  (368714, 6, 3),
  (369576, 1, 7),
  (371311, 4, 5),
  (371689, 2, 3),
  (375512, 0, 3),
  (383054, 7, 5),
  (385476, 6, 6),
  (385708, 3, 4),
  (387552, 7, 0),
  (387771, 5, 7),
  (390228, 1, 7),
  (390436, 7, 4),
  (391116, 3, 5),
  (391128, 7, 3),
  (394579, 5, 3),
  (397806, 2, 5),
  (398090, 3, 6),
  (399510, 7, 3),
  (399717, 1, 7),
  (409157, 5, 7),
  (415760, 6, 0),
  (416498, 5, 3),
  (417390, 2, 7),
  (418076, 6, 7),
  (426891, 3, 3),
  (429881, 7, 0),
  (431860, 0, 7),
  (433457, 3, 6),
  (434817, 7, 4),
  (449356, 2, 7),
  (449926, 5, 3),
  (451046, 4, 0),
  (456251, 7, 0),
  (459699, 0, 6),
  (461107, 3, 7),
  (462717, 3, 3),
  (465795, 6, 4),
  (466083, 6, 1),
  (466174, 2, 3),
  (466430, 4, 7),
  (467686, 7, 0),
  (473072, 7, 7),
  (473113, 5, 7),
  (478205, 7, 7),
  (478269, 2, 3),
  (479860, 7, 3),
  (480290, 5, 7),
  (480577, 7, 6),
  (485575, 2, 7),
  (486295, 1, 7),
  (488625, 2, 6),
  (489056, 5, 7),
  (491476, 7, 7),
  (492478, 3, 3),
  (492783, 0, 5),
  (493180, 5, 2),
  (498367, 7, 4),
  (499412, 2, 2),
  (502969, 3, 3),
  (504169, 7, 7),
  (504291, 6, 6),
  (506112, 0, 3),
  (506231, 6, 6),
  (512875, 1, 7),
  (513268, 1, 6),
  (515273, 6, 0),
  (517008, 4, 6),
  (518736, 6, 6),
  (519818, 6, 4),
  (521670, 1, 0),
  (523370, 5, 7),
  (526962, 2, 3),
  (527978, 1, 0),
  (529513, 1, 7),
  (530660, 1, 7),
  (533487, 2, 2),
  (537041, 1, 6),
  (538619, 3, 6),
  (538923, 1, 7),
  (544831, 6, 3),
  (548671, 7, 4),
  (550651, 6, 3),
  (552202, 7, 3),
  (553160, 7, 5),
  (553272, 4, 2),
  (554143, 5, 7),
  (554162, 1, 4),
  (557371, 3, 6),
  (557451, 4, 3),
  (564402, 0, 0),
  (565702, 1, 0),
  (568012, 0, 7),
  (571094, 5, 3),
  (571951, 6, 7),
  (574512, 0, 7),
  (575047, 7, 7),
  (578653, 2, 7),
  (580263, 2, 7),
  (581188, 6, 7),
  (581439, 4, 2),
  (581829, 6, 7),
  (586498, 2, 3),
  (588574, 7, 7),
  (588806, 1, 6),
  (590514, 4, 7),
  (593541, 0, 0),
  (593838, 1, 0),
  (595796, 0, 0),
  (598134, 0, 2),
  (601032, 4, 3),
  (602502, 1, 7),
  (604686, 0, 7),
  (606589, 0, 7),
  (606704, 6, 0),
  (609431, 6, 4),
  (610503, 3, 7),
  (618897, 4, 7),
  (621949, 3, 2),
  (624461, 3, 3),
  (628939, 1, 6),
  (629325, 0, 7),
  (629669, 2, 7),
  (631812, 6, 4),
  (635437, 0, 0),
  (640661, 7, 5),
  (641370, 5, 7),
  (642916, 5, 6),
  (650080, 0, 0),
  (650905, 7, 7),
  (651274, 2, 3),
  (651582, 5, 7),
  (652651, 3, 7),
  (653152, 1, 7),
  (654297, 0, 6),
  (655746, 6, 7),
  (656091, 5, 7),
  (657472, 7, 7),
  (657477, 1, 4),
  (658180, 4, 2),
  (659273, 7, 0),
  (659465, 0, 7),
  (660041, 0, 0),
  (661566, 0, 7),
  (663698, 1, 7),
  (670007, 6, 0),
  (672380, 5, 1),
  (672717, 4, 3),
  (674093, 0, 7),
  (674161, 7, 4),
  (678194, 2, 3),
  (681789, 6, 2),
  (684629, 0, 7),
  (687100, 3, 2),
  (692188, 0, 0),
  (693257, 5, 3),
  (694340, 7, 7),
  (698042, 7, 7),
  (698144, 4, 3),
  (700407, 1, 3),
  (701637, 0, 4),
  (702183, 5, 7),
  (705441, 6, 4),
  (710748, 7, 7),
  (712777, 5, 5),
  (712807, 0, 3),
  (717727, 5, 7),
  (718082, 5, 7),
  (719448, 3, 7),
  (720421, 7, 0),
  (721275, 6, 4),
  (721308, 6, 3),
  (721913, 6, 6),
  (724189, 5, 5),
  (724434, 3, 6),
  (724833, 7, 7),
  (724916, 3, 7),
  (727068, 4, 6),
  (728547, 7, 4),
  (728799, 3, 7),
  (729384, 6, 4),
  (730150, 2, 3),
  (730726, 1, 7),
  (732784, 6, 0),
  (732846, 6, 2),
  (737819, 0, 6),
  (743409, 4, 7),
  (743903, 1, 0),
  (749789, 5, 6),
  (752527, 5, 7),
  (755762, 4, 3),
  (760192, 7, 6),
  (760922, 1, 6),
  (761731, 0, 4),
  (764003, 2, 7),
  (765286, 4, 7),
  (766125, 7, 7),
  (771109, 0, 0),
  (771566, 7, 0),
  (773349, 3, 3),
  (776178, 3, 6),
  (776600, 3, 7),
  (777434, 2, 7),
  (781440, 6, 4),
  (781760, 1, 3),
  (782765, 4, 7),
  (783993, 6, 4),
  (786872, 5, 6),
  (787256, 5, 7),
  (791655, 3, 5),
  (793134, 1, 0),
  (794132, 4, 3),
  (794483, 5, 7),
  (798131, 2, 7),
  (799287, 1, 5),
  (801731, 5, 5),
  (802880, 2, 3),
  (805551, 7, 4),
  (805748, 4, 5),
  (806565, 5, 6),
  (807310, 7, 2),
  (808380, 4, 3),
  (809766, 2, 7),
  (811214, 6, 0),
  (812054, 7, 7),
  (814922, 1, 6),
  (815363, 4, 2),
  (817662, 1, 7),
  (821374, 1, 7),
  (821521, 4, 4),
  (821800, 7, 0),
  (822086, 6, 4),
  (822278, 5, 3),
  (825899, 4, 7),
  (826197, 6, 0),
  (827311, 7, 0),
  (828717, 4, 7),
  (830096, 1, 0),
  (833209, 5, 2),
  (835767, 4, 3),
  (835834, 3, 3),
  (837299, 1, 2),
  (838567, 2, 3),
  (839582, 2, 3),
  (840119, 0, 7),
  (840343, 7, 7),
  (841412, 2, 7),
  (842145, 2, 2),
  (843182, 6, 7),
  (843256, 2, 3),
  (844502, 4, 7),
  (844646, 0, 0),
  (845549, 1, 3),
  (847308, 4, 7),
  (855258, 3, 3),
  (855608, 3, 5),
  (858816, 5, 2),
  (860042, 4, 5),
  (860750, 0, 3),
  (868096, 4, 3),
  (871738, 0, 7),
  (874806, 7, 0),
  (875071, 4, 3),
  (878320, 5, 4),
  (879151, 3, 7),
  (882788, 5, 7),
  (883506, 6, 0),
  (883552, 4, 3),
  (884044, 5, 3),
  (886421, 0, 4),
  (887085, 6, 7),
  (887760, 4, 7),
  (888071, 3, 5),
  (890211, 7, 0),
  (895105, 2, 1),
  (899739, 7, 4),
  (901299, 0, 4),
  (906006, 3, 7),
  (907124, 5, 3),
  (908191, 7, 1),
  (910714, 3, 3),
  (910960, 5, 7),
  (913346, 4, 5),
  (916203, 1, 0),
  (918219, 4, 2),
  (919233, 0, 7),
  (925401, 7, 0),
  (928415, 5, 3),
  (929832, 7, 4),
  (932148, 3, 7),
  (936625, 2, 7),
  (936740, 5, 3),
  (938757, 7, 7),
  (941315, 1, 7),
  (943420, 0, 0),
  (944092, 7, 4),
  (945097, 5, 3),
  (945419, 1, 4),
  (945492, 0, 6),
  (947123, 7, 7),
  (950660, 7, 7),
  (952078, 6, 3),
  (953884, 7, 5),
  (958277, 6, 7),
  (959145, 0, 7),
  (959804, 2, 7),
  (960481, 3, 3),
  (960901, 7, 7),
  (965112, 7, 7),
  (965986, 3, 5),
  (970605, 0, 7),
  (974658, 3, 3),
  (976299, 1, 0),
  (978607, 4, 7),
  (979401, 4, 7),
  (980812, 7, 0),
  (981364, 3, 2),
  (981776, 3, 6),
  (984884, 3, 2),
  (988944, 1, 5),
  (989165, 5, 7),
  (989863, 3, 5),
  (992197, 1, 7),
  (992246, 5, 5),
  (995064, 7, 7),
  (995634, 1, 3),
  (998264, 7, 4),
  (998915, 5, 2),
  (999705, 1, 0),
  (1000767, 2, 3),
  (1003455, 2, 7),
  (1005321, 5, 3),
  (1007605, 5, 6),
  (1012829, 0, 3),
  (1013957, 4, 1),
  (1017716, 6, 3),
  (1017983, 3, 2),
  (1020567, 2, 5),
  (1020991, 4, 7),
  (1021956, 0, 7),
  (1026336, 5, 3),
  (1028909, 4, 6),
  (1033130, 5, 7),
  (1034595, 6, 3),
  (1035589, 3, 7),
  (1036904, 3, 7),
  (1037159, 3, 3),
  (1039354, 5, 7),
  (1040089, 0, 6),
  (1042180, 0, 0),
  (1046481, 2, 3),
  (1052105, 2, 6),
  (1052692, 1, 7),
  (1052793, 3, 7),
  (1056333, 4, 6),
  (1056934, 4, 7),
  (1060153, 5, 5),
  (1060353, 2, 3),
  (1060363, 7, 6),
  (1071704, 4, 7),
  (1072439, 2, 2),
  (1072514, 2, 7),
  (1075499, 5, 7),
  (1075747, 0, 0),
  (1079534, 0, 7),
  (1080677, 6, 6),
  (1080877, 2, 7),
  (1085030, 0, 2),
  (1088050, 1, 7),
  (1088317, 4, 3),
  (1094564, 6, 7),
  (1100597, 7, 7),
  (1104344, 5, 6),
  (1105482, 7, 6),
  (1107858, 4, 3),
  (1113274, 3, 2),
  (1117685, 2, 2),
  (1119691, 2, 5),
  (1120071, 2, 7),
  (1125507, 6, 7),
  (1128668, 5, 4),
  (1130069, 5, 0),
  (1130854, 7, 3),
  (1131755, 2, 7),
  (1132806, 1, 3),
  (1134844, 6, 0),
  (1135397, 3, 5),
  (1135751, 5, 7),
  (1137066, 6, 3),
  (1138167, 6, 7),
  (1140049, 7, 7),
  (1140800, 5, 7),
  (1140880, 1, 7),
  (1147956, 0, 0),
  (1148709, 2, 3),
  (1149846, 1, 7),
  (1155734, 0, 4),
  (1163820, 2, 7),
  (1165222, 4, 2),
  (1165297, 7, 7),
  (1167279, 3, 3),
  (1169514, 4, 7),
  (1172066, 6, 3),
  (1172373, 7, 6),
  (1174322, 6, 7),
  (1177655, 2, 6),
  (1179981, 4, 7),
  (1183209, 4, 6),
  (1184007, 2, 7),
  (1184069, 7, 4),
  (1184858, 0, 7),
  (1185133, 7, 7),
  (1187104, 4, 7),
  (1190170, 7, 3),
  (1190192, 1, 7),
  (1192346, 1, 7),
  (1194519, 4, 3),
  (1195877, 3, 1),
  (1195983, 0, 3),
  (1198420, 1, 5),
  (1198789, 3, 6),
  (1198933, 1, 3),
  (1200254, 7, 7),
  (1203860, 6, 7),
  (1205416, 0, 0),
  (1206234, 3, 6),
  (1208536, 7, 6),
  (1210731, 0, 7),
  (1213486, 0, 7),
  (1217490, 3, 7),
  (1217498, 6, 0),
  (1218426, 1, 4),
  (1218897, 7, 0),
  (1221658, 1, 4),
  (1222120, 0, 4),
  (1223107, 4, 3),
  (1225056, 1, 7),
  (1228418, 2, 7),
  (1238927, 2, 5),
  (1240808, 1, 7),
  (1242348, 2, 6),
  (1243807, 5, 7),
  (1245272, 0, 3),
  (1247622, 3, 3),
  (1249179, 4, 7),
  (1254987, 7, 7),
  (1256848, 5, 7),
  (1257689, 6, 3),
  (1258163, 5, 2),
  (1259400, 0, 3),
  (1260134, 1, 4),
  (1261577, 5, 6),
  (1266449, 6, 7),
  (1266781, 5, 2),
  (1272787, 6, 3),
  (1275120, 3, 3),
  (1277449, 3, 5),
  (1278212, 1, 7),
  (1278637, 6, 4),
  (1281647, 3, 7),
  (1283048, 4, 3),
  (1284790, 2, 3),
  (1292760, 2, 3),
  (1292775, 2, 2),
  (1294576, 4, 7),
  (1294699, 7, 7),
  (1296240, 5, 7),
  (1297783, 6, 6),
  (1301279, 3, 7),
  (1301426, 4, 7),
  (1304663, 2, 7),
  (1304749, 4, 7),
  (1305117, 4, 2),
  (1308311, 2, 3),
  (1308864, 4, 6),
  (1311795, 2, 5),
  (1320446, 6, 0),
  (1322796, 1, 0),
  (1322936, 3, 7),
  (1323179, 3, 0),
  (1324624, 5, 7),
  (1328582, 7, 6),
  (1328667, 2, 7),
  (1329109, 4, 2),
  (1330276, 4, 2),
  (1330956, 6, 0),
  (1331516, 3, 7),
  (1332322, 5, 2),
  (1337046, 5, 1),
  (1337600, 0, 7),
  (1341928, 6, 0),
  (1342218, 3, 1),
  (1342467, 6, 3),
  (1343509, 5, 3),
  (1346262, 6, 7),
  (1347506, 4, 7),
  (1348914, 3, 1),
  (1349238, 2, 5),
  (1353604, 0, 6),
  (1355182, 5, 3),
  (1355495, 4, 6),
  (1358055, 7, 0),
  (1360507, 5, 7),
  (1363266, 7, 7),
  (1363587, 6, 7),
  (1366398, 0, 3),
  (1368839, 2, 7),
  (1369176, 0, 0),
  (1372717, 2, 7),
  (1373497, 0, 7),
  (1373669, 3, 2),
  (1377254, 0, 0),
  (1378162, 4, 5),
  (1378459, 4, 7),
  (1378872, 6, 7),
  (1382241, 1, 0),
  (1382712, 1, 2),
  (1383045, 2, 7),
  (1383580, 7, 6),
  (1384765, 4, 3),
  (1387254, 3, 3),
  (1389985, 0, 7),
  (1391067, 3, 3),
  (1394137, 1, 6),
  (1394791, 2, 7),
  (1397343, 6, 3),
  (1398899, 6, 0),
  (1402297, 4, 3),
  (1402620, 4, 7),
  (1404832, 7, 0),
  (1409762, 2, 7),
  (1409810, 3, 3),
  (1409963, 1, 3),
  (1409979, 1, 7),
  (1412443, 6, 0),
  (1412463, 5, 7),
  (1412923, 2, 7),
  (1414542, 7, 0),
  (1417000, 1, 4),
  (1417560, 0, 3),
  (1423379, 4, 2),
  (1426631, 0, 5),
  (1427622, 6, 7),
  (1429624, 0, 7),
  (1441423, 5, 3),
  (1443869, 7, 7),
  (1444299, 7, 7),
  (1445242, 5, 2),
  (1446777, 4, 1),
  (1447491, 0, 6),
  (1447854, 4, 6),
  (1449938, 4, 7),
  (1454282, 7, 0),
  (1455074, 2, 3),
  (1455347, 1, 4),
  (1456851, 7, 0),
  (1457864, 3, 6),
  (1459226, 0, 0),
  (1459244, 5, 5),
  (1467284, 3, 6),
  (1471023, 7, 0),
  (1474285, 5, 2),
  (1477567, 3, 6),
  (1481469, 3, 7),
  (1482898, 0, 7),
  (1482989, 0, 3),
  (1486042, 3, 7),
  (1487682, 0, 7),
  (1489311, 2, 6),
  (1489567, 3, 7),
  (1490850, 5, 6),
  (1493607, 0, 3),
  (1494004, 4, 6),
  (1494636, 1, 7),
  (1502169, 3, 3),
  (1503173, 7, 7),
  (1504400, 3, 3),
  (1506162, 2, 7),
  (1506563, 7, 7),
  (1508126, 3, 3),
  (1508839, 5, 2),
  (1512929, 4, 7),
  (1514512, 7, 4),
  (1515549, 0, 7),
  (1517629, 7, 0),
  (1518679, 2, 7),
  (1520407, 4, 3),
  (1521584, 4, 7),
  (1526659, 5, 2),
  (1529121, 6, 7),
  (1530453, 0, 0),
  (1533978, 4, 7),
  (1534533, 6, 7),
  (1535659, 6, 0),
  (1536292, 7, 7),
  (1536709, 0, 0),
  (1537009, 4, 3),
  (1537197, 4, 3),
  (1537951, 7, 7),
  (1538322, 5, 6),
  (1538998, 1, 4),
  (1539734, 7, 7),
  (1539999, 7, 6),
  (1540454, 1, 7),
  (1541562, 5, 3),
  (1541881, 6, 6),
  (1542876, 7, 4),
  (1543021, 6, 3),
  (1545793, 0, 3),
  (1546183, 3, 7),
  (1552589, 6, 0),
  (1556630, 0, 7),
  (1560929, 3, 3),
  (1561103, 1, 4),
  (1561398, 0, 0),
  (1562237, 0, 7),
  (1562736, 0, 7),
  (1564165, 6, 7),
  (1567266, 5, 3),
  (1567354, 6, 4),
  (1568120, 1, 7),
  (1570099, 3, 3),
  (1573015, 2, 2),
  (1574322, 4, 5),
  (1574679, 6, 0),
  (1575178, 2, 3),
  (1575770, 4, 7),
  (1577397, 6, 0),
  (1578494, 6, 7),
  (1579503, 0, 4),
  (1583240, 7, 7),
  (1583767, 7, 0),
  (1586465, 4, 5),
  (1588905, 2, 5),
  (1588981, 7, 7),
  (1590720, 7, 4),
  (1591079, 1, 7),
  (1592319, 2, 2),
  (1596494, 5, 3),
  (1598058, 5, 3),
  (1599153, 4, 7),
  (1599980, 3, 5),
  (1600686, 3, 7),
  (1601192, 0, 4),
  (1602363, 7, 0),
  (1602801, 7, 7),
  (1602867, 6, 4),
  (1603220, 3, 3),
  (1610922, 4, 7),
  (1615171, 6, 7),
  (1619909, 4, 1),
  (1620610, 4, 7),
  (1622708, 5, 5),
  (1622825, 0, 3),
  (1623043, 1, 2),
  (1623190, 2, 0),
  (1625155, 7, 7),
  (1628083, 2, 5),
  (1630446, 7, 5),
  (1635342, 5, 7),
  (1635831, 4, 7),
  (1638996, 3, 7),
  (1640415, 2, 6),
  (1643365, 3, 7),
  (1644962, 3, 7),
  (1645975, 1, 4),
  (1646500, 6, 0),
  (1648815, 3, 7),
  (1649739, 7, 0),
  (1650114, 1, 0),
  (1654205, 6, 7),
  (1659289, 5, 7),
  (1659305, 3, 7),
  (1663079, 4, 2),
  (1663190, 0, 0),
  (1665229, 6, 0),
  (1665304, 5, 7),
  (1665493, 2, 7),
  (1669627, 0, 6),
  (1670775, 1, 3),
  (1679083, 0, 6),
  (1679288, 6, 3),
  (1679395, 7, 7),
  (1680250, 2, 6),
  (1680936, 2, 2),
  (1681303, 6, 0),
  (1683083, 2, 6),
  (1684950, 4, 3),
  (1687294, 2, 7),
  (1688553, 0, 0),
  (1691910, 4, 2),
  (1703338, 6, 3),
  (1704189, 2, 1),
  (1706590, 3, 1),
  (1708690, 1, 3),
  (1710159, 2, 7),
  (1711865, 4, 6),
  (1721970, 3, 3),
  (1722258, 1, 7),
  (1723289, 3, 3),
  (1725574, 3, 3),
  (1727310, 0, 3),
  (1732268, 6, 3),
  (1735087, 7, 7),
  (1735543, 4, 7),
  (1736637, 0, 4),
  (1738775, 7, 4),
  (1741376, 2, 6),
  (1742923, 3, 7),
  (1743071, 4, 2),
  (1743297, 1, 6),
  (1743801, 6, 0),
  (1746343, 2, 5),
  (1747962, 0, 7),
  (1750787, 0, 0),
  (1753657, 5, 6),
  (1753689, 4, 7),
  (1761764, 5, 7),
  (1762923, 1, 0),
  (1763970, 3, 7),
  (1768053, 1, 6),
  (1768552, 7, 4),
  (1770519, 7, 7),
  (1772768, 7, 7),
  (1774693, 4, 7),
  (1775386, 5, 2),
  (1776728, 1, 3),
  (1778014, 7, 0),
  (1779020, 4, 2),
  (1785900, 2, 7),
  (1786918, 3, 6),
  (1789382, 7, 3),
  (1789696, 2, 2),
  (1790871, 2, 2),
  (1792644, 4, 6),
  (1802060, 4, 7),
  (1802940, 0, 7),
  (1803189, 7, 7),
  (1804618, 4, 2),
  (1804806, 6, 0),
  (1808061, 4, 6),
  (1813273, 7, 7),
  (1814738, 7, 3),
  (1815618, 4, 5),
  (1820291, 1, 0),
  (1821787, 6, 0),
  (1823373, 5, 7),
  (1823398, 3, 5),
  (1826445, 3, 7),
  (1826949, 4, 2),
  (1828620, 0, 7),
  (1829246, 4, 7),
  (1833680, 5, 7),
  (1834607, 5, 3),
  (1840196, 0, 3),
  (1840901, 7, 0),
  (1842047, 0, 5),
  (1845367, 4, 7),
  (1847038, 7, 4),
  (1849429, 7, 3),
  (1849436, 7, 7),
  (1851902, 5, 7),
  (1853387, 3, 5),
  (1855343, 0, 5),
  (1858610, 5, 7),
  (1861471, 0, 7),
  (1863470, 6, 3),
  (1864934, 5, 5),
  (1865602, 6, 6),
  (1868390, 7, 7),
  (1868906, 4, 2),
  (1871810, 1, 7),
  (1874969, 7, 7),
  (1876039, 3, 7),
  (1878626, 7, 3),
  (1879187, 1, 5),
  (1879435, 0, 7),
  (1879663, 6, 4),
  (1881199, 6, 3),
  (1884058, 1, 7),
  (1884498, 3, 1),
  (1884505, 7, 0),
  (1885064, 2, 7),
  (1885576, 0, 0),
  (1886743, 6, 4),
  (1887943, 6, 7),
  (1891152, 4, 2),
  (1892162, 7, 7),
  (1892489, 4, 7),
  (1892581, 2, 5),
  (1895678, 0, 7),
  (1895982, 1, 0),
  (1896783, 2, 6),
  (1896808, 2, 3),
  (1896995, 5, 1),
  (1904812, 7, 7),
  (1907642, 2, 7),
  (1910841, 6, 4),
  (1911230, 4, 3),
  (1912752, 4, 7),
  (1915006, 0, 7),
  (1918786, 3, 2),
  (1922363, 6, 7),
  (1922805, 3, 6),
  (1928138, 0, 4),
  (1928727, 3, 2),
  (1929734, 5, 2),
  (1929813, 3, 4),
  (1929905, 1, 3),
  (1934528, 4, 6),
  (1935260, 6, 0),
  (1936993, 4, 7),
  (1937058, 7, 7),
  (1937964, 1, 0),
  (1939544, 7, 7),
  (1941542, 5, 7),
  (1946638, 6, 7),
  (1946831, 4, 7),
  (1953273, 1, 7),
  (1954645, 4, 7),
  (1961769, 2, 1),
  (1964569, 1, 0),
  (1966126, 0, 7),
  (1967878, 7, 0),
  (1968362, 1, 0),
  (1968376, 5, 6),
  (1969238, 6, 7),
  (1971633, 2, 5),
  (1972170, 7, 3),
  (1974521, 4, 7),
  (1977250, 0, 7),
  (1979415, 7, 6),
  (1980763, 3, 7),
  (1983124, 7, 7),
  (1984364, 6, 5),
  (1985404, 7, 3),
  (1985783, 4, 7),
  (1986027, 0, 4),
  (1988823, 0, 0),
  (1989600, 5, 7),
  (1990246, 4, 7),
  (1990911, 7, 7),
  (1991287, 4, 7),
  (2002143, 0, 3),
  (2004942, 3, 2),
  (2005166, 3, 2),
  (2005833, 5, 3),
  (2008279, 1, 7),
  (2011114, 6, 0),
  (2016505, 7, 0),
  (2017014, 4, 3),
  (2019996, 1, 4),
  (2020350, 1, 0),
  (2022136, 7, 7),
  (2022719, 1, 4),
  (2023391, 7, 4),
  (2030277, 4, 2),
  (2034787, 2, 7),
  (2037699, 7, 7),
  (2038474, 6, 0),
  (2039338, 1, 7),
  (2043139, 7, 7),
  (2044034, 4, 2),
  (2046365, 0, 7),
  (2046742, 6, 4),
  (2047816, 1, 7),
  (2049452, 7, 7),
  (2052049, 4, 2),
  (2057607, 3, 5),
  (2058100, 2, 6),
  (2061255, 5, 2),
  (2064012, 1, 0),
  (2064190, 2, 3),
  (2070546, 1, 5),
  (2071671, 6, 0),
  (2072819, 1, 3),
  (2073053, 2, 7),
  (2076118, 1, 7),
  (2076878, 7, 7),
  (2078598, 3, 6),
  (2079870, 0, 7),
  (2084469, 2, 6),
  (2085826, 1, 7),
  (2087603, 4, 7),
  (2087880, 4, 7),
  (2090386, 0, 6),
  (2090477, 5, 2),
  (2092427, 4, 7),
  (2093068, 5, 2),
  (2093332, 7, 0),
  (2093698, 5, 6),
  (2097259, 6, 6),
  (2098753, 0, 4),
  (2099965, 1, 3),
  (2101625, 6, 0),
  (2101853, 4, 7),
  (2103138, 5, 7),
  (2105705, 0, 7),
  (2110622, 0, 7),
  (2111948, 2, 7),
  (2112001, 4, 7),
  (2113155, 3, 5),
  (2114271, 7, 7),
  (2116008, 4, 3),
  (2116160, 0, 3),
  (2120202, 7, 5),
  (2120275, 2, 3),
  (2120857, 1, 7),
  (2125111, 6, 7),
  (2126635, 2, 7),
  (2127878, 4, 3),
  (2128529, 6, 7),
  (2131423, 3, 6),
  (2133499, 4, 7),
  (2134392, 7, 0),
  (2138801, 3, 6),
  (2140871, 2, 7),
  (2141561, 4, 7),
  (2143154, 6, 7),
  (2145655, 4, 7),
  (2148154, 2, 6),
  (2148678, 7, 7),
  (2149064, 2, 2),
  (2151581, 7, 7),
  (2153642, 7, 7),
  (2153897, 4, 7),
  (2155748, 2, 3),
  (2157562, 5, 3),
  (2161632, 5, 3),
  (2164386, 6, 3),
  (2164754, 1, 0),
  (2164947, 5, 3),
  (2165518, 0, 4),
  (2167036, 2, 3),
  (2168805, 1, 0),
  (2169257, 0, 4),
  (2179596, 7, 3),
  (2183872, 2, 7),
  (2189075, 7, 0),
  (2189683, 7, 5),
  (2191157, 1, 7),
  (2194524, 3, 7),
  (2201594, 2, 3),
  (2202563, 0, 7),
  (2203251, 1, 7),
  (2203729, 1, 7),
  (2208855, 5, 7),
  (2209855, 0, 7),
  (2210132, 2, 3),
  (2211534, 3, 3),
  (2211597, 1, 0),
  (2213076, 1, 7),
  (2213079, 2, 3),
  (2216563, 0, 7),
  (2216722, 6, 7),
  (2217425, 1, 4),
  (2219192, 4, 3),
  (2223752, 2, 6),
  (2224187, 3, 2),
  (2229118, 0, 2),
  (2234398, 2, 7),
  (2236116, 1, 7),
  (2239612, 4, 6),
  (2241026, 5, 6),
  (2243839, 6, 4),
  (2251990, 7, 4),
  (2260366, 7, 4),
  (2263375, 0, 7),
  (2263510, 5, 7),
  (2266679, 3, 7),
  (2279732, 7, 6),
  (2280566, 6, 4),
  (2281588, 2, 5),
  (2281608, 5, 7),
  (2282521, 4, 3),
  (2282826, 3, 3),
  (2284731, 3, 3),
  (2285243, 3, 7),
  (2288296, 1, 7),
  (2288359, 7, 4),
  (2291031, 0, 3),
  (2292993, 0, 7),
  (2293276, 0, 3),
  (2301634, 2, 2),
  (2302019, 5, 7),
  (2305073, 1, 3),
  (2308597, 2, 6),
  (2309003, 0, 7),
  (2309703, 0, 0),
  (2309976, 3, 2),
  (2312219, 2, 7),
  (2313461, 7, 7),
  (2318882, 4, 6),
  (2319862, 3, 7),
  (2320751, 2, 5),
  (2321784, 3, 7),
  (2322086, 0, 0),
  (2325775, 7, 6),
  (2326510, 4, 2),
  (2326977, 2, 5),
  (2328680, 1, 6),
  (2330322, 0, 0),
  (2330568, 7, 3),
  (2336855, 1, 3),
  (2338507, 5, 7),
  (2343051, 2, 7),
  (2343847, 0, 7),
  (2345890, 4, 3),
  (2347036, 6, 3),
  (2352366, 3, 7),
  (2355650, 0, 7),
  (2357251, 3, 3),
  (2362139, 5, 6),
  (2366535, 7, 7),
  (2366761, 1, 7),
  (2367867, 5, 7),
  (2369131, 4, 7),
  (2369704, 2, 6),
  (2369719, 0, 7),
  (2377247, 1, 7),
  (2379040, 5, 6),
  (2379373, 1, 3),
  (2381153, 4, 7),
  (2381502, 0, 0),
  (2383980, 3, 3),
  (2389173, 4, 7),
  (2392039, 1, 6),
  (2393041, 2, 3),
  (2394586, 6, 4),
  (2398658, 6, 7),
  (2398881, 4, 7),
  (2401030, 1, 0),
  (2401034, 7, 7),
  (2401841, 3, 3),
  (2409164, 6, 1),
  (2409731, 0, 7),
  (2412210, 5, 2),
  (2413588, 2, 6),
  (2415294, 2, 5),
  (2416725, 4, 6),
  (2416987, 0, 3),
  (2419234, 4, 5),
  (2430444, 4, 2),
  (2432591, 1, 6),
  (2440380, 2, 3),
  (2440885, 1, 0),
  (2440987, 3, 6),
  (2443205, 6, 5),
  (2443270, 7, 7),
  (2444024, 6, 3),
  (2444053, 0, 3),
  (2446281, 2, 7),
  (2448012, 3, 7),
  (2449491, 1, 7),
  (2450953, 2, 7),
  (2453318, 1, 7),
  (2454445, 0, 3),
  (2456118, 2, 6),
  (2459118, 0, 3),
  (2459210, 4, 6),
  (2468819, 3, 7),
  (2469604, 2, 7),
  (2472108, 6, 6),
  (2484311, 4, 3),
  (2484947, 3, 7),
  (2487196, 1, 3),
  (2490816, 6, 7),
  (2491359, 3, 7),
  (2503830, 4, 6),
  (2506135, 6, 7),
  (2507448, 7, 3),
  (2511365, 4, 7),
  (2517975, 3, 6),
  (2518270, 1, 3),
  (2519426, 6, 3),
  (2520407, 0, 1),
  (2523701, 1, 0),
  (2523956, 4, 7),
  (2525622, 3, 3),
  (2528036, 3, 6),
  (2529606, 6, 7),
  (2531362, 5, 3),
  (2531503, 0, 7),
  (2532792, 5, 3),
  (2533513, 7, 0),
  (2537578, 5, 7),
  (2537622, 6, 3),
  (2540558, 4, 4),
  (2543185, 7, 7),
  (2545702, 1, 7),
  (2546072, 7, 6),
  (2549099, 6, 3),
  (2554349, 1, 7),
  (2554614, 7, 7),
  (2555594, 1, 2),
  (2558157, 1, 7),
  (2558958, 1, 7),
  (2563702, 3, 7),
  (2568347, 3, 5),
  (2568766, 1, 7),
  (2570274, 3, 5),
  (2573362, 0, 0),
  (2573469, 2, 7),
  (2573756, 7, 0),
  (2576148, 2, 6),
  (2579335, 3, 1),
  (2581433, 2, 7),
  (2587660, 7, 7),
  (2588159, 2, 2),
  (2590406, 0, 7),
  (2592220, 3, 3),
  (2596288, 6, 0),
  (2597559, 2, 2),
  (2599683, 1, 3),
  (2600244, 7, 7),
  (2603964, 4, 7),
  (2605422, 7, 4),
  (2606128, 1, 0),
  (2607539, 5, 1),
  (2609861, 7, 7),
  (2612275, 2, 6),
  (2614227, 2, 7),
  (2624241, 0, 4),
  (2624248, 0, 4),
  (2625875, 0, 6),
  (2627449, 4, 7),
  (2627816, 4, 7),
  (2628726, 4, 6),
  (2631197, 2, 3),
  (2632389, 3, 7),
  (2634262, 3, 2),
  (2634891, 1, 7),
  (2635560, 4, 5),
  (2636240, 0, 7),
  (2640622, 6, 7),
  (2641124, 3, 7),
  (2647313, 5, 7),
  (2648452, 1, 6),
  (2648476, 2, 7),
  (2649055, 3, 7),
  (2650743, 0, 4),
  (2651536, 6, 4),
  (2655579, 2, 5),
  (2658527, 1, 7),
  (2666832, 0, 7),
  (2668277, 5, 7),
  (2668343, 1, 7),
  (2668861, 2, 6),
  (2673127, 2, 7),
  (2675051, 0, 4),
  (2679152, 6, 7),
  (2681747, 1, 7),
  (2685503, 3, 7),
  (2686361, 7, 7),
  (2686458, 1, 7),
  (2687824, 3, 3),
  (2688214, 4, 5),
  (2689976, 0, 4),
  (2690106, 4, 2),
  (2701090, 6, 7),
  (2701352, 0, 4),
  (2702973, 3, 2),
  (2704692, 1, 7),
  (2706934, 2, 4),
  (2707153, 7, 3),
  (2709789, 1, 7),
  (2715119, 0, 3),
  (2716947, 7, 7),
  (2717873, 7, 6),
  (2718146, 0, 0),
  (2718423, 0, 7),
  (2719158, 0, 0),
  (2720453, 2, 3),
  (2721429, 7, 3),
  (2726126, 3, 7),
  (2727283, 3, 2),
  (2727697, 2, 7),
  (2727932, 2, 7),
  (2728139, 4, 7),
  (2728996, 0, 7),
  (2733015, 6, 0),
  (2737067, 7, 0),
  (2741533, 4, 3),
  (2747164, 5, 3),
  (2753639, 1, 4),
  (2754044, 2, 7),
  (2756115, 3, 7),
  (2763473, 4, 7),
  (2766022, 2, 3),
  (2766372, 2, 6),
  (2766829, 3, 7),
  (2766920, 4, 7),
  (2767664, 0, 6),
  (2770324, 2, 6),
  (2773653, 7, 7),
  (2773807, 7, 7),
  (2776108, 5, 7),
  (2779014, 1, 4),
  (2779134, 7, 3),
  (2780288, 5, 3),
  (2788710, 4, 6),
  (2790145, 0, 0),
  (2794793, 7, 4),
  (2797531, 2, 7),
  (2798025, 2, 2),
  (2798288, 5, 7),
  (2799029, 7, 5),
  (2799852, 6, 7),
  (2799980, 1, 7),
  (2801566, 7, 0),
  (2804650, 1, 4),
  (2805056, 6, 7),
  (2805974, 7, 6),
  (2806160, 0, 0),
  (2806215, 7, 4),
  (2806791, 0, 7),
  (2808851, 5, 2),
  (2814503, 7, 7),
  (2821317, 3, 3),
  (2823299, 2, 3),
  (2823745, 5, 7),
  (2825702, 2, 3),
  (2830881, 5, 2),
  (2832839, 6, 7),
  (2833257, 7, 4),
  (2833585, 2, 2),
  (2834379, 3, 6),
  (2834787, 5, 5),
  (2837493, 0, 1),
  (2840938, 0, 7),
  (2842795, 4, 6),
  (2844702, 1, 7),
  (2848011, 0, 7),
  (2848997, 0, 0),
  (2859588, 7, 7),
  (2861583, 1, 7),
  (2865822, 7, 3),
  (2870764, 1, 7),
  (2871742, 2, 5),
  (2874986, 4, 7),
  (2875515, 3, 3),
  (2875617, 0, 7),
  (2877729, 2, 7),
  (2880070, 1, 0),
  (2880646, 2, 4),
  (2881856, 0, 3),
  (2881889, 0, 0),
  (2882990, 5, 6),
  (2886854, 2, 5),
  (2894255, 2, 7),
  (2895071, 5, 1),
  (2895116, 5, 7),
  (2898810, 0, 0),
  (2901206, 7, 6),
  (2902993, 6, 0),
  (2906736, 6, 0),
  (2907468, 1, 3),
  (2909039, 7, 7),
  (2912684, 0, 7),
  (2916371, 4, 7),
  (2917141, 7, 6),
  (2919386, 1, 7),
  (2919568, 6, 7),
  (2920686, 2, 7),
  (2924059, 2, 5),
  (2925951, 4, 5),
  (2926527, 0, 0),
  (2930145, 6, 0),
  (2936364, 1, 4),
  (2940094, 1, 7),
  (2940120, 2, 3),
  (2940393, 2, 2),
  (2940565, 6, 7),
  (2943127, 6, 4),
  (2943162, 7, 6),
  (2943952, 5, 2),
  (2947860, 7, 3),
  (2947961, 6, 0),
  (2951707, 7, 0),
  (2952277, 1, 6),
  (2952760, 6, 2),
  (2956240, 7, 0),
  (2959140, 7, 7),
  (2960609, 0, 7),
  (2962029, 2, 7),
  (2963168, 0, 4),
  (2963506, 2, 3),
  (2963798, 7, 3),
  (2966894, 3, 5),
  (2967051, 2, 7),
  (2971618, 0, 4),
  (2978609, 2, 2),
  (2978640, 1, 4),
  (2981750, 0, 3),
  (2981784, 3, 1),
  (2983016, 2, 5),
  (2983090, 4, 3),
  (2985113, 0, 4),
  (2988509, 5, 5),
  (2989774, 1, 7),
  (2990751, 4, 7),
  (2993465, 0, 7),
  (2995280, 7, 3),
  (2998594, 4, 6),
  (3001139, 7, 0),
  (3004413, 2, 7),
  (3004953, 3, 3),
  (3007226, 4, 3),
  (3007813, 7, 0),
  (3008832, 7, 7),
  (3009421, 1, 0),
  (3010197, 1, 4),
  (3010821, 2, 2),
  (3012183, 1, 7),
  (3019388, 7, 4),
  (3019644, 4, 6),
  (3023051, 2, 7),
  (3031415, 5, 6),
  (3034991, 4, 3),
  (3035370, 4, 3),
  (3035427, 4, 7),
  (3039098, 0, 7),
  (3040542, 3, 7),
  (3041234, 2, 7),
  (3047479, 7, 0),
  (3048301, 2, 6),
  (3052010, 0, 4),
  (3052105, 7, 7),
  (3052697, 7, 7),
  (3055366, 3, 5),
  (3058284, 1, 0),
  (3060235, 7, 0),
  (3060962, 5, 7),
  (3063163, 7, 7),
  (3063840, 7, 1),
  (3065105, 0, 3),
  (3065633, 3, 3),
  (3067136, 7, 7),
  (3068507, 7, 7),
  (3071598, 0, 1),
  (3072109, 0, 7),
  (3076782, 7, 6),
  (3076899, 0, 4),
  (3078941, 5, 3),
  (3079754, 4, 6),
  (3079888, 0, 4),
  (3082003, 7, 3),
  (3091174, 6, 2),
  (3091861, 7, 6),
  (3093765, 2, 6),
  (3093771, 5, 7),
  (3094718, 2, 2),
  (3095035, 4, 2),
  (3095731, 2, 4),
  (3099327, 5, 7),
  (3101522, 7, 7),
  (3102128, 6, 7),
  (3105424, 7, 4),
  (3108894, 3, 3),
  (3109426, 6, 4),
  (3110453, 6, 0),
  (3111172, 7, 7),
  (3112093, 3, 2),
  (3114057, 3, 7),
  (3115017, 5, 7),
  (3117568, 6, 7),
  (3117840, 5, 0),
  (3124131, 1, 3),
  (3125420, 7, 0),
  (3126383, 0, 4),
  (3127545, 6, 3),
  (3128221, 5, 7),
  (3130193, 0, 6),
  (3130441, 7, 7),
  (3132395, 2, 7),
  (3133509, 4, 7),
  (3139037, 4, 6),
  (3146738, 1, 0),
  (3146787, 2, 3),
  (3149360, 6, 6),
  (3150668, 4, 2),
  (3150950, 5, 3),
  (3153594, 0, 4),
  (3155219, 2, 3),
  (3164927, 6, 0),
  (3167028, 1, 4),
  (3167782, 1, 7),
  (3169049, 0, 7),
  (3169796, 4, 7),
  (3170725, 3, 6),
  (3171642, 7, 0),
  (3175140, 6, 4),
  (3176133, 5, 6),
  (3184120, 7, 4),
  (3184627, 6, 7),
  (3184735, 5, 7),
  (3185817, 0, 7),
  (3186846, 2, 4),
  (3186968, 2, 7),
  (3191412, 7, 3),
  (3191460, 5, 7),
  (3193196, 1, 0),
  (3193219, 5, 7),
  (3195512, 3, 7),
  (3196025, 7, 4),
  (3196930, 7, 0),
  (3199277, 5, 2),
  (3201355, 4, 7),
  (3202434, 0, 3),
  (3202472, 6, 6),
  (3203457, 7, 3),
  (3204690, 7, 3),
  (3205493, 7, 7),
  (3208511, 1, 7),
  (3210686, 4, 7),
  (3214077, 0, 7),
  (3218149, 2, 6),
  (3218547, 1, 0),
  (3222349, 5, 2),
  (3222861, 1, 7),
  (3225129, 6, 4),
  (3226869, 3, 7),
  (3228612, 4, 5),
  (3229667, 4, 7),
  (3230055, 1, 3),
  (3230565, 5, 7),
  (3230569, 3, 7),
  (3233102, 3, 7),
  (3233485, 2, 6),
  (3237594, 1, 6),
  (3238315, 6, 7),
  (3238523, 2, 7),
  (3238668, 2, 6),
  (3239308, 6, 0),
  (3244395, 3, 5),
  (3244994, 6, 0),
  (3246696, 6, 7),
  (3248550, 0, 3),
  (3254576, 5, 2),
  (3254977, 0, 3),
  (3255997, 7, 7),
  (3258210, 5, 2),
  (3259622, 7, 0),
  (3262406, 4, 2),
  (3264141, 1, 7),
  (3267593, 7, 7),
  (3267694, 5, 3),
  (3269905, 5, 3),
  (3272945, 3, 3),
  (3278203, 3, 7),
  (3280808, 5, 2),
  (3281035, 0, 3),
  (3282543, 7, 7),
  (3284861, 6, 0),
  (3284925, 6, 7),
  (3285971, 7, 0),
  (3291257, 0, 0),
  (3291366, 7, 0),
  (3292514, 7, 3),
  (3293970, 0, 0),
  (3295352, 7, 7),
  (3299952, 2, 2),
  (3301683, 5, 3),
  (3302151, 6, 4),
  (3302750, 6, 0),
  (3302812, 2, 4),
  (3305766, 0, 2),
  (3308513, 6, 5),
  (3311518, 6, 7),
  (3312558, 7, 0),
  (3314411, 6, 7),
  (3317154, 1, 0),
  (3319632, 4, 3),
  (3321367, 4, 7),
  (3322772, 6, 2),
  (3325257, 4, 7),
  (3328696, 3, 7),
  (3331508, 7, 0),
  (3333964, 1, 3),
  (3334183, 5, 3),
  (3336480, 6, 2),
  (3340373, 2, 6),
  (3340553, 6, 2),
  (3341295, 2, 7),
  (3341786, 6, 0),
  (3342809, 6, 6),
  (3343462, 6, 7),
  (3343944, 6, 5),
  (3347937, 6, 3),
  (3348797, 7, 0),
  (3351654, 7, 4),
  (3354675, 6, 7),
  (3354840, 2, 7),
  (3355295, 2, 2),
  (3358946, 0, 7),
  (3359407, 3, 2),
  (3359609, 7, 6),
  (3361210, 0, 7),
  (3361771, 1, 7),
  (3362621, 5, 6),
  (3363115, 2, 5),
  (3363217, 0, 7),
  (3366746, 2, 3),
  (3366902, 6, 3),
  (3371081, 4, 3),
  (3373014, 3, 7),
  (3374150, 5, 7),
  (3375218, 0, 0),
  (3375405, 3, 2),
  (3377407, 7, 3),
  (3380332, 7, 0),
  (3381975, 3, 6),
  (3387023, 6, 3),
  (3388692, 3, 7),
  (3391048, 0, 3),
  (3391124, 1, 0),
  (3391134, 7, 7),
  (3391269, 5, 7),
  (3395370, 0, 2),
  (3396022, 7, 3),
  (3396241, 0, 4),
  (3398332, 0, 3),
  (3399428, 7, 7),
  (3401479, 4, 2),
  (3403512, 5, 6),
  (3404126, 1, 0),
  (3406371, 2, 2),
  (3407731, 4, 7),
  (3409721, 7, 3),
  (3410600, 6, 4),
  (3411437, 5, 3),
  (3412629, 1, 7),
  (3419823, 0, 2),
  (3423146, 2, 7),
  (3423670, 1, 5),
  (3425355, 3, 3),
  (3426436, 1, 2),
  (3427411, 3, 2),
  (3427558, 5, 2),
  (3432582, 0, 7),
  (3433476, 6, 3),
  (3436494, 5, 2),
  (3437784, 7, 0),
  (3439019, 1, 7),
  (3439296, 1, 7),
  (3445116, 1, 7),
  (3445484, 1, 7),
  (3446952, 6, 4),
  (3447300, 0, 7),
  (3451050, 2, 3),
  (3455116, 3, 7),
  (3456199, 7, 3),
  (3457035, 2, 3),
  (3459283, 3, 7),
  (3460759, 0, 0),
  (3462047, 2, 7),
  (3462770, 3, 4),
  (3462800, 1, 7),
  (3464439, 2, 6),
  (3468300, 1, 7),
  (3471933, 7, 0),
  (3472675, 1, 7),
  (3473667, 4, 7),
  (3473759, 2, 2),
  (3474854, 2, 3),
  (3476640, 1, 0),
  (3477117, 0, 4),
  (3477693, 5, 6),
  (3479331, 4, 7),
  (3482467, 3, 7),
  (3482586, 2, 7),
  (3482761, 4, 7),
  (3484124, 2, 7),
  (3485110, 4, 6),
  (3485159, 7, 0),
  (3489354, 0, 7),
  (3490957, 4, 7),
  (3491924, 7, 7),
  (3503285, 3, 3),
  (3505587, 6, 7),
  (3508794, 1, 0),
  (3511382, 7, 0),
  (3512661, 1, 3),
  (3513591, 3, 7),
  (3516071, 3, 2),
  (3525877, 6, 7),
  (3527498, 0, 5),
  (3529792, 6, 0),
  (3529970, 0, 3),
  (3531981, 4, 3),
  (3532593, 1, 0),
  (3534195, 2, 3),
  (3537648, 0, 7),
  (3537685, 7, 6),
  (3543376, 7, 7),
  (3543893, 1, 0),
  (3547350, 0, 3),
  (3552383, 0, 0),
  (3552827, 4, 7),
  (3554097, 7, 0),
  (3554623, 1, 3),
  (3557063, 6, 3),
  (3557131, 3, 7),
  (3560682, 2, 3),
  (3563058, 7, 7),
  (3563828, 5, 3),
  (3568341, 3, 2),
  (3570437, 0, 0),
  (3571816, 4, 7),
  (3572764, 6, 5),
  (3575617, 2, 7),
  (3584800, 6, 0),
  (3584955, 7, 0),
  (3587184, 3, 3),
  (3588423, 1, 4),
  (3589434, 5, 3),
  (3591415, 7, 4),
  (3595110, 3, 2),
  (3595511, 2, 6),
  (3595687, 6, 7),
  (3599879, 7, 7),
])
