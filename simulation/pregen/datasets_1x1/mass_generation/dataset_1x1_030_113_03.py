from util import *
schedule = deque([
  (1591, 0, 7),
  (2019, 4, 3),
  (3382, 1, 7),
  (4679, 1, 6),
  (9185, 0, 7),
  (10588, 0, 7),
  (11125, 1, 4),
  (12144, 3, 3),
  (16816, 5, 6),
  (17041, 5, 3),
  (20655, 2, 6),
  (21865, 6, 0),
  (22889, 0, 4),
  (23954, 7, 3),
  (24905, 0, 1),
  (27610, 7, 3),
  (28390, 6, 4),
  (28529, 5, 5),
  (31014, 3, 3),
  (35610, 5, 5),
  (35889, 5, 7),
  (41213, 7, 0),
  (41735, 1, 7),
  (44489, 4, 7),
  (46322, 2, 2),
  (48221, 7, 7),
  (50946, 1, 3),
  (57048, 4, 7),
  (57264, 3, 7),
  (57367, 7, 7),
  (57901, 1, 7),
  (58619, 3, 3),
  (60035, 0, 7),
  (60506, 3, 3),
  (62351, 6, 0),
  (63570, 4, 7),
  (68758, 7, 0),
  (70467, 1, 0),
  (71790, 5, 7),
  (77835, 5, 0),
  (78680, 2, 2),
  (80376, 1, 0),
  (90698, 5, 2),
  (90962, 1, 7),
  (93243, 4, 3),
  (95394, 2, 7),
  (99664, 3, 2),
  (106363, 6, 7),
  (106856, 3, 7),
  (109990, 3, 3),
  (115962, 0, 0),
  (117778, 0, 7),
  (118125, 5, 5),
  (119670, 5, 0),
  (120858, 1, 7),
  (122632, 5, 3),
  (123678, 2, 7),
  (124822, 0, 7),
  (127672, 7, 3),
  (130341, 7, 7),
  (131218, 4, 7),
  (131727, 0, 6),
  (132406, 4, 6),
  (132514, 7, 3),
  (134159, 5, 7),
  (137847, 4, 3),
  (139762, 3, 3),
  (141824, 3, 3),
  (143294, 2, 7),
  (144002, 7, 4),
  (146589, 7, 0),
  (157883, 4, 7),
  (159293, 4, 5),
  (160016, 5, 6),
  (161210, 2, 4),
  (165374, 4, 2),
  (167119, 6, 5),
  (170269, 5, 7),
  (171691, 0, 7),
  (176605, 7, 4),
  (179977, 3, 3),
  (181289, 6, 2),
  (182211, 1, 7),
  (186750, 1, 7),
  (188430, 1, 7),
  (190647, 1, 3),
  (190868, 3, 7),
  (193120, 6, 7),
  (194997, 7, 6),
  (195309, 5, 5),
  (195613, 4, 7),
  (203973, 6, 3),
  (205378, 5, 6),
  (206324, 7, 7),
  (209485, 0, 7),
  (210488, 5, 4),
  (212911, 4, 7),
  (213140, 1, 4),
  (218535, 5, 3),
  (221125, 5, 7),
  (221139, 4, 2),
  (222904, 6, 4),
  (223610, 2, 7),
  (227342, 0, 0),
  (227989, 1, 7),
  (229566, 2, 7),
  (230978, 1, 7),
  (233527, 5, 6),
  (236057, 4, 3),
  (236136, 0, 3),
  (236244, 1, 0),
  (238426, 2, 5),
  (242241, 6, 7),
  (242365, 6, 7),
  (249909, 2, 5),
  (250286, 3, 7),
  (253373, 3, 2),
  (258490, 5, 3),
  (259130, 1, 7),
  (259817, 0, 7),
  (260428, 5, 6),
  (260789, 7, 4),
  (262872, 0, 4),
  (266822, 7, 6),
  (270204, 6, 0),
  (270338, 5, 7),
  (273731, 5, 3),
  (276192, 0, 4),
  (276877, 4, 7),
  (277608, 7, 7),
  (279446, 6, 0),
  (283925, 3, 2),
  (284575, 5, 2),
  (289748, 6, 6),
  (293210, 3, 7),
  (295788, 1, 7),
  (296289, 7, 4),
  (301165, 0, 7),
  (302381, 3, 0),
  (304319, 6, 7),
  (307801, 4, 3),
  (312868, 1, 7),
  (313013, 2, 6),
  (313834, 4, 3),
  (314055, 5, 7),
  (314431, 0, 7),
  (314608, 2, 7),
  (318611, 3, 4),
  (323164, 1, 3),
  (323314, 6, 0),
  (329461, 1, 7),
  (330729, 3, 2),
  (331740, 1, 7),
  (335806, 7, 3),
  (338923, 2, 7),
  (340272, 0, 0),
  (342937, 2, 2),
  (342956, 6, 7),
  (346852, 7, 7),
  (347031, 6, 7),
  (347075, 4, 7),
  (348046, 3, 7),
  (348729, 3, 6),
  (348888, 5, 7),
  (356215, 3, 7),
  (357240, 6, 0),
  (359842, 1, 6),
  (360074, 3, 1),
  (360359, 3, 7),
  (360482, 4, 3),
  (360544, 5, 5),
  (365706, 6, 7),
  (366150, 4, 3),
  (366210, 1, 1),
  (369674, 2, 5),
  (372129, 4, 3),
  (372517, 2, 2),
  (378254, 2, 7),
  (379567, 6, 7),
  (382718, 0, 7),
  (383037, 3, 7),
  (384123, 2, 2),
  (384750, 4, 3),
  (387703, 0, 6),
  (388996, 1, 0),
  (394986, 4, 7),
  (395637, 6, 0),
  (396222, 3, 7),
  (397633, 7, 7),
  (398579, 0, 7),
  (401374, 2, 2),
  (401443, 5, 7),
  (405410, 5, 3),
  (407245, 2, 2),
  (408083, 0, 7),
  (409614, 2, 3),
  (417078, 2, 7),
  (417298, 7, 7),
  (418496, 6, 7),
  (419009, 4, 6),
  (420460, 5, 2),
  (420485, 5, 7),
  (421548, 2, 7),
  (421586, 6, 0),
  (422193, 5, 6),
  (431867, 0, 7),
  (434412, 4, 3),
  (435956, 1, 7),
  (436726, 0, 0),
  (437061, 2, 7),
  (440610, 0, 4),
  (441313, 2, 2),
  (441971, 2, 7),
  (442035, 6, 4),
  (442370, 1, 3),
  (445202, 0, 7),
  (445496, 6, 7),
  (447913, 6, 3),
  (448177, 6, 0),
  (454779, 5, 7),
  (454946, 0, 4),
  (455472, 4, 6),
  (456214, 2, 6),
  (462925, 2, 3),
  (465961, 3, 7),
  (466629, 7, 4),
  (467449, 0, 7),
  (468707, 0, 4),
  (469057, 0, 2),
  (469219, 3, 5),
  (472660, 7, 2),
  (477007, 5, 7),
  (478564, 5, 2),
  (481172, 7, 7),
  (484112, 5, 2),
  (484841, 4, 7),
  (485179, 3, 2),
  (490527, 0, 7),
  (496601, 0, 4),
  (498871, 7, 7),
  (502751, 6, 7),
  (504341, 1, 6),
  (508157, 0, 7),
  (514902, 0, 0),
  (515834, 0, 3),
  (516054, 2, 3),
  (521260, 3, 7),
  (523806, 4, 7),
  (523983, 1, 7),
  (525209, 5, 2),
  (527944, 2, 0),
  (528028, 1, 7),
  (528558, 5, 2),
  (529336, 1, 7),
  (530486, 3, 5),
  (535302, 5, 7),
  (536952, 5, 6),
  (537248, 2, 7),
  (540711, 5, 7),
  (541364, 3, 3),
  (544192, 6, 3),
  (544649, 2, 7),
  (545057, 6, 3),
  (545989, 4, 7),
  (553073, 3, 2),
  (555906, 5, 6),
  (557097, 7, 0),
  (558088, 6, 4),
  (559895, 0, 7),
  (560371, 6, 7),
  (561321, 2, 3),
  (563764, 5, 7),
  (564808, 3, 7),
  (577889, 5, 3),
  (578891, 7, 7),
  (579700, 6, 7),
  (582335, 1, 7),
  (583867, 4, 5),
  (583995, 0, 7),
  (586967, 7, 0),
  (588634, 5, 6),
  (590651, 5, 6),
  (592705, 1, 6),
  (594799, 7, 1),
  (595267, 7, 4),
  (596627, 7, 6),
  (600745, 1, 3),
  (601823, 6, 0),
  (605345, 6, 3),
  (605935, 1, 7),
  (607111, 6, 0),
  (608399, 4, 7),
  (610989, 2, 6),
  (611105, 5, 4),
  (611332, 1, 7),
  (612180, 0, 3),
  (615238, 2, 6),
  (615242, 4, 6),
  (615600, 6, 4),
  (620784, 7, 7),
  (622576, 2, 3),
  (626620, 4, 2),
  (627027, 7, 0),
  (629077, 1, 7),
  (630104, 7, 6),
  (630327, 6, 7),
  (630345, 7, 4),
  (630893, 0, 7),
  (631226, 7, 0),
  (631985, 5, 7),
  (632356, 1, 7),
  (634724, 1, 7),
  (636009, 5, 6),
  (636017, 5, 7),
  (639024, 3, 3),
  (643443, 2, 7),
  (644679, 7, 7),
  (652375, 3, 6),
  (654761, 5, 2),
  (655088, 0, 4),
  (657795, 1, 7),
  (660171, 7, 6),
  (665617, 2, 0),
  (667703, 0, 6),
  (668212, 4, 6),
  (670741, 5, 7),
  (671578, 6, 7),
  (675383, 5, 2),
  (676369, 1, 6),
  (677259, 7, 3),
  (678704, 6, 7),
  (681377, 5, 2),
  (682841, 0, 7),
  (683083, 2, 2),
  (686105, 3, 2),
  (688827, 5, 2),
  (689233, 7, 4),
  (689927, 3, 7),
  (693683, 4, 7),
  (694020, 5, 3),
  (696652, 5, 6),
  (696665, 2, 2),
  (698219, 4, 7),
  (699678, 3, 2),
  (700017, 7, 3),
  (703124, 2, 7),
  (716532, 6, 7),
  (717734, 6, 7),
  (721684, 6, 0),
  (722305, 7, 6),
  (722429, 4, 2),
  (726224, 1, 7),
  (726514, 4, 7),
  (728851, 6, 7),
  (728862, 0, 0),
  (731587, 1, 2),
  (733230, 0, 3),
  (735188, 0, 0),
  (735443, 6, 7),
  (741423, 4, 7),
  (742195, 3, 5),
  (747384, 4, 2),
  (747768, 6, 4),
  (747989, 0, 2),
  (750578, 3, 7),
  (751875, 7, 0),
  (759489, 6, 7),
  (760185, 4, 3),
  (760926, 7, 7),
  (760954, 7, 4),
  (761449, 7, 7),
  (762888, 4, 2),
  (773747, 2, 7),
  (774796, 6, 7),
  (775258, 3, 7),
  (781235, 1, 4),
  (785683, 1, 7),
  (788635, 1, 4),
  (792477, 7, 0),
  (793147, 2, 7),
  (793430, 3, 5),
  (795330, 6, 0),
  (798038, 1, 0),
  (801439, 0, 3),
  (803998, 5, 7),
  (805744, 2, 3),
  (806946, 0, 7),
  (809646, 0, 7),
  (813188, 4, 7),
  (814595, 1, 3),
  (815449, 4, 7),
  (816199, 4, 2),
  (816363, 6, 3),
  (820181, 1, 3),
  (821102, 3, 3),
  (821576, 2, 3),
  (822522, 4, 2),
  (826378, 3, 7),
  (826427, 1, 7),
  (827343, 2, 6),
  (828144, 6, 4),
  (833785, 5, 5),
  (834053, 0, 7),
  (834197, 6, 7),
  (835025, 3, 5),
  (837110, 1, 7),
  (838261, 6, 0),
  (840478, 2, 3),
  (849226, 6, 7),
  (850885, 5, 7),
  (852126, 5, 7),
  (853182, 1, 0),
  (854162, 2, 5),
  (854173, 3, 3),
  (855296, 1, 7),
  (855490, 6, 6),
  (855996, 1, 3),
  (860233, 3, 7),
  (863839, 0, 3),
  (864133, 6, 7),
  (865290, 0, 7),
  (868504, 3, 6),
  (873444, 3, 7),
  (873608, 6, 7),
  (882152, 5, 7),
  (883668, 5, 6),
  (883949, 6, 7),
  (884425, 4, 3),
  (887799, 5, 1),
  (890032, 4, 6),
  (890241, 6, 7),
  (891727, 5, 3),
  (896897, 1, 7),
  (897974, 3, 5),
  (899175, 1, 7),
  (901057, 3, 3),
  (908843, 3, 7),
  (910045, 4, 7),
  (911908, 0, 0),
  (913295, 6, 3),
  (916716, 6, 0),
  (917885, 7, 7),
  (918311, 3, 5),
  (919676, 0, 7),
  (920590, 5, 7),
  (921875, 2, 7),
  (923187, 2, 7),
  (925183, 1, 0),
  (926841, 2, 5),
  (927427, 2, 7),
  (929616, 0, 6),
  (932514, 1, 4),
  (933402, 2, 7),
  (934704, 5, 5),
  (937149, 7, 7),
  (937767, 3, 2),
  (942540, 4, 7),
  (944388, 2, 7),
  (945103, 6, 4),
  (946427, 1, 3),
  (946462, 2, 3),
  (946795, 7, 0),
  (947303, 1, 3),
  (947403, 2, 6),
  (948836, 2, 3),
  (961887, 4, 7),
  (964239, 4, 7),
  (964650, 1, 5),
  (966304, 5, 7),
  (968858, 4, 4),
  (970114, 2, 7),
  (970657, 1, 3),
  (971376, 0, 7),
  (972453, 6, 7),
  (973797, 3, 6),
  (975078, 0, 4),
  (976576, 5, 7),
  (979006, 2, 7),
  (980044, 1, 3),
  (982310, 7, 0),
  (985269, 6, 0),
  (985573, 7, 7),
  (987290, 5, 6),
  (990524, 0, 0),
  (991668, 0, 3),
  (992077, 4, 3),
  (993493, 2, 6),
  (995131, 3, 2),
  (998725, 3, 3),
  (1001325, 6, 0),
  (1001815, 6, 3),
  (1002750, 7, 4),
  (1009506, 7, 7),
  (1013321, 7, 6),
  (1015561, 7, 6),
  (1015831, 4, 7),
  (1020383, 2, 5),
  (1022727, 4, 7),
  (1024642, 6, 1),
  (1024695, 7, 7),
  (1028844, 0, 6),
  (1029389, 6, 5),
  (1032090, 4, 5),
  (1033239, 6, 5),
  (1033829, 6, 4),
  (1038389, 6, 7),
  (1039887, 0, 7),
  (1044340, 5, 3),
  (1045279, 5, 2),
  (1045953, 3, 2),
  (1046395, 2, 2),
  (1046965, 1, 5),
  (1048397, 1, 0),
  (1049872, 3, 2),
  (1049941, 4, 7),
  (1050734, 7, 7),
  (1051402, 1, 7),
  (1057088, 0, 7),
  (1059647, 2, 3),
  (1063478, 6, 2),
  (1063575, 1, 7),
  (1064051, 5, 7),
  (1067135, 1, 7),
  (1067167, 1, 7),
  (1071945, 3, 6),
  (1072548, 1, 7),
  (1073568, 4, 1),
  (1081171, 3, 1),
  (1085034, 3, 6),
  (1085302, 3, 7),
  (1085957, 7, 4),
  (1088723, 3, 6),
  (1090650, 2, 3),
  (1092002, 1, 4),
  (1093235, 6, 4),
  (1097830, 1, 7),
  (1097841, 2, 3),
  (1097879, 7, 4),
  (1099401, 3, 6),
  (1100844, 2, 7),
  (1103532, 0, 7),
  (1104136, 1, 2),
  (1105162, 5, 6),
  (1106982, 5, 3),
  (1111386, 1, 7),
  (1116024, 3, 4),
  (1119808, 7, 0),
  (1121252, 1, 7),
  (1128236, 2, 6),
  (1132200, 2, 3),
  (1133513, 6, 7),
  (1135505, 4, 1),
  (1137719, 2, 7),
  (1142735, 1, 3),
  (1144368, 6, 1),
  (1149971, 5, 7),
  (1160615, 0, 6),
  (1161489, 2, 3),
  (1164104, 5, 7),
  (1164208, 2, 7),
  (1165103, 6, 0),
  (1168315, 1, 0),
  (1169225, 7, 7),
  (1170703, 3, 3),
  (1171409, 6, 0),
  (1175043, 5, 2),
  (1176417, 1, 7),
  (1179085, 4, 2),
  (1180440, 1, 4),
  (1180731, 1, 0),
  (1180874, 2, 5),
  (1182437, 4, 7),
  (1190022, 0, 6),
  (1190145, 5, 7),
  (1190861, 7, 4),
  (1192837, 0, 6),
  (1194296, 5, 2),
  (1194636, 1, 7),
  (1197622, 2, 7),
  (1198455, 7, 5),
  (1203131, 7, 7),
  (1206121, 3, 3),
  (1206758, 0, 7),
  (1206876, 7, 7),
  (1208300, 0, 0),
  (1210047, 4, 7),
  (1211224, 6, 4),
  (1213643, 5, 7),
  (1219519, 6, 6),
  (1219724, 1, 7),
  (1226911, 4, 7),
  (1227621, 5, 7),
  (1229328, 5, 7),
  (1229551, 1, 3),
  (1234696, 3, 5),
  (1236250, 4, 3),
  (1238282, 1, 0),
  (1238995, 1, 7),
  (1240321, 7, 4),
  (1242013, 7, 3),
  (1242909, 1, 7),
  (1244770, 7, 7),
  (1251846, 7, 7),
  (1258843, 0, 0),
  (1260426, 4, 5),
  (1262446, 7, 0),
  (1262789, 7, 3),
  (1263086, 4, 4),
  (1267163, 3, 2),
  (1270186, 4, 7),
  (1271327, 7, 7),
  (1275759, 6, 7),
  (1276569, 3, 3),
  (1277447, 0, 3),
  (1278084, 5, 6),
  (1280163, 5, 5),
  (1281190, 7, 0),
  (1282372, 2, 4),
  (1282567, 3, 6),
  (1284046, 5, 3),
  (1287530, 1, 4),
  (1288405, 0, 7),
  (1292614, 6, 0),
  (1297182, 6, 7),
  (1297349, 6, 0),
  (1297665, 4, 3),
  (1299559, 1, 4),
  (1301956, 5, 7),
  (1304234, 7, 7),
  (1307802, 7, 1),
  (1313488, 7, 7),
  (1314571, 6, 4),
  (1314587, 2, 7),
  (1314730, 6, 7),
  (1320138, 7, 0),
  (1320486, 2, 7),
  (1322331, 1, 2),
  (1324345, 0, 0),
  (1324369, 2, 7),
  (1324577, 3, 2),
  (1326390, 6, 7),
  (1327856, 0, 7),
  (1328113, 4, 6),
  (1328267, 2, 3),
  (1330466, 7, 4),
  (1332178, 0, 4),
  (1332581, 1, 0),
  (1334061, 0, 0),
  (1335189, 0, 1),
  (1340561, 5, 7),
  (1340946, 1, 7),
  (1341251, 7, 3),
  (1343274, 0, 3),
  (1348925, 2, 4),
  (1352471, 3, 7),
  (1352675, 0, 7),
  (1354431, 4, 6),
  (1356084, 1, 3),
  (1359241, 0, 0),
  (1361481, 6, 7),
  (1362806, 0, 7),
  (1364205, 3, 7),
  (1365301, 3, 2),
  (1366232, 2, 7),
  (1368582, 6, 0),
  (1369632, 6, 7),
  (1369983, 6, 7),
  (1374834, 4, 7),
  (1377306, 4, 6),
  (1380998, 3, 3),
  (1381050, 5, 3),
  (1382969, 0, 7),
  (1383548, 4, 7),
  (1383662, 1, 6),
  (1387248, 0, 4),
  (1391099, 3, 6),
  (1392384, 4, 7),
  (1401078, 0, 0),
  (1407885, 7, 7),
  (1407947, 7, 0),
  (1408293, 1, 7),
  (1414557, 7, 7),
  (1416635, 3, 7),
  (1420927, 3, 3),
  (1421450, 5, 5),
  (1423586, 1, 0),
  (1424300, 4, 3),
  (1424657, 1, 7),
  (1425053, 7, 7),
  (1428357, 3, 3),
  (1430560, 2, 2),
  (1433449, 3, 7),
  (1441395, 0, 2),
  (1442935, 3, 5),
  (1446553, 4, 7),
  (1449335, 2, 7),
  (1454862, 5, 7),
  (1455009, 6, 7),
  (1460710, 0, 7),
  (1460730, 0, 0),
  (1461242, 5, 7),
  (1463741, 4, 3),
  (1464924, 3, 7),
  (1465611, 4, 7),
  (1466633, 4, 7),
  (1467760, 0, 7),
  (1469909, 1, 4),
  (1471355, 3, 5),
  (1474888, 7, 7),
  (1477433, 4, 7),
  (1477584, 6, 6),
  (1481537, 4, 7),
  (1482781, 3, 2),
  (1486677, 5, 2),
  (1487850, 2, 3),
  (1490401, 4, 7),
  (1493277, 4, 4),
  (1497407, 6, 0),
  (1499380, 4, 6),
  (1499598, 2, 3),
  (1501448, 5, 3),
  (1510376, 7, 7),
  (1511140, 2, 7),
  (1513417, 7, 0),
  (1515602, 5, 2),
  (1516821, 4, 7),
  (1518360, 6, 7),
  (1519150, 7, 7),
  (1519785, 3, 3),
  (1527555, 7, 7),
  (1527836, 5, 3),
  (1528617, 1, 4),
  (1528794, 7, 0),
  (1529158, 3, 7),
  (1530844, 7, 7),
  (1531469, 1, 0),
  (1532964, 3, 5),
  (1533275, 1, 7),
  (1533716, 2, 7),
  (1534557, 5, 3),
  (1536326, 2, 6),
  (1538814, 2, 7),
  (1539487, 3, 3),
  (1540064, 3, 7),
  (1540343, 6, 7),
  (1543887, 6, 0),
  (1544656, 6, 4),
  (1545166, 4, 7),
  (1545635, 3, 7),
  (1546775, 4, 7),
  (1550922, 4, 6),
  (1551630, 5, 2),
  (1551882, 5, 2),
  (1556687, 1, 3),
  (1557625, 0, 7),
  (1558112, 4, 5),
  (1559412, 7, 7),
  (1559485, 0, 6),
  (1562646, 1, 7),
  (1565350, 4, 7),
  (1567738, 0, 0),
  (1570977, 3, 7),
  (1573259, 7, 0),
  (1577363, 5, 2),
  (1577496, 2, 7),
  (1580523, 7, 4),
  (1584092, 5, 6),
  (1585181, 5, 7),
  (1586891, 3, 7),
  (1586904, 7, 6),
  (1589896, 5, 7),
  (1590903, 5, 5),
  (1592842, 7, 4),
  (1599480, 2, 2),
  (1599824, 2, 7),
  (1601552, 1, 0),
  (1602650, 2, 2),
  (1602804, 7, 3),
  (1603265, 6, 4),
  (1606665, 5, 7),
  (1609028, 2, 7),
  (1610522, 4, 7),
  (1612878, 4, 2),
  (1613190, 7, 7),
  (1618492, 4, 2),
  (1621328, 5, 1),
  (1622603, 6, 0),
  (1623895, 7, 7),
  (1624384, 1, 7),
  (1624475, 0, 5),
  (1625323, 7, 0),
  (1626660, 7, 4),
  (1628674, 3, 6),
  (1633024, 0, 7),
  (1633236, 4, 2),
  (1636632, 1, 0),
  (1637781, 5, 6),
  (1638487, 7, 7),
  (1641957, 4, 2),
  (1642519, 6, 4),
  (1645817, 0, 7),
  (1646149, 4, 7),
  (1646990, 1, 3),
  (1647924, 3, 7),
  (1648987, 5, 6),
  (1653164, 6, 0),
  (1654905, 4, 6),
  (1656281, 1, 3),
  (1659014, 5, 3),
  (1660413, 1, 3),
  (1663300, 4, 7),
  (1663336, 4, 5),
  (1664523, 6, 7),
  (1669163, 7, 7),
  (1672399, 4, 7),
  (1672922, 4, 7),
  (1673468, 6, 7),
  (1673832, 4, 7),
  (1673875, 4, 7),
  (1677651, 4, 0),
  (1678234, 3, 3),
  (1682147, 0, 0),
  (1682406, 5, 3),
  (1688953, 3, 7),
  (1692822, 7, 3),
  (1693297, 0, 2),
  (1693871, 3, 7),
  (1694271, 6, 7),
  (1695150, 0, 7),
  (1697150, 3, 3),
  (1707915, 2, 7),
  (1708472, 3, 7),
  (1710934, 7, 7),
  (1713258, 4, 5),
  (1714258, 6, 4),
  (1715359, 5, 0),
  (1716983, 7, 0),
  (1717307, 5, 7),
  (1717584, 2, 7),
  (1720047, 4, 3),
  (1724108, 4, 5),
  (1727153, 4, 7),
  (1727632, 0, 7),
  (1727783, 5, 7),
  (1735446, 1, 2),
  (1736709, 7, 3),
  (1739413, 4, 3),
  (1742985, 7, 2),
  (1745020, 3, 5),
  (1746511, 3, 7),
  (1746716, 3, 3),
  (1751045, 4, 6),
  (1751247, 3, 7),
  (1754091, 6, 4),
  (1755801, 3, 2),
  (1761324, 7, 7),
  (1762064, 1, 7),
  (1763417, 4, 3),
  (1770192, 2, 7),
  (1770966, 3, 3),
  (1774509, 1, 7),
  (1778540, 5, 2),
  (1779995, 7, 7),
  (1782502, 4, 7),
  (1783556, 1, 6),
  (1784106, 4, 5),
  (1784254, 5, 2),
  (1787219, 1, 0),
  (1787861, 2, 7),
  (1790360, 2, 2),
  (1790547, 4, 5),
  (1791468, 4, 7),
  (1792605, 6, 6),
  (1793039, 3, 3),
  (1793519, 1, 7),
  (1793580, 4, 4),
  (1798352, 1, 0),
  (1800142, 3, 7),
  (1804664, 5, 7),
  (1811584, 4, 2),
  (1813627, 5, 7),
  (1814402, 4, 2),
  (1816426, 7, 6),
  (1817881, 7, 7),
  (1820052, 5, 7),
  (1821700, 0, 3),
  (1823637, 0, 4),
  (1825070, 1, 0),
  (1829273, 2, 6),
  (1832909, 6, 7),
  (1834813, 4, 7),
  (1837156, 4, 7),
  (1837431, 4, 3),
  (1839652, 3, 2),
  (1839891, 1, 4),
  (1840768, 4, 7),
  (1841146, 4, 3),
  (1841660, 7, 7),
  (1841932, 7, 3),
  (1844089, 6, 5),
  (1844881, 3, 5),
  (1847075, 6, 0),
  (1848095, 0, 0),
  (1848470, 2, 7),
  (1849628, 2, 3),
  (1852176, 3, 7),
  (1854712, 2, 2),
  (1857507, 2, 6),
  (1857561, 3, 3),
  (1861988, 0, 7),
  (1864266, 1, 7),
  (1864982, 4, 6),
  (1865961, 5, 6),
  (1868784, 0, 7),
  (1870113, 0, 0),
  (1873221, 6, 7),
  (1874540, 7, 7),
  (1876961, 3, 7),
  (1878146, 3, 5),
  (1878291, 5, 7),
  (1879873, 5, 7),
  (1883017, 4, 7),
  (1885689, 2, 7),
  (1888313, 7, 2),
  (1889474, 7, 3),
  (1893161, 5, 7),
  (1895010, 1, 0),
  (1895336, 3, 2),
  (1896662, 7, 7),
  (1901621, 7, 7),
  (1905070, 6, 7),
  (1908091, 6, 4),
  (1908329, 4, 6),
  (1909550, 5, 6),
  (1911660, 5, 7),
  (1913372, 1, 7),
  (1913383, 1, 4),
  (1915764, 0, 0),
  (1916256, 4, 3),
  (1916572, 3, 2),
  (1920444, 5, 5),
  (1925341, 5, 6),
  (1927343, 1, 0),
  (1927844, 7, 0),
  (1929243, 7, 3),
  (1929713, 1, 3),
  (1933263, 6, 0),
  (1935025, 6, 7),
  (1940230, 2, 7),
  (1941612, 2, 7),
  (1943110, 1, 7),
  (1943158, 4, 7),
  (1945774, 6, 4),
  (1946742, 0, 7),
  (1948864, 1, 7),
  (1950328, 1, 3),
  (1950676, 4, 2),
  (1951175, 4, 6),
  (1952369, 1, 7),
  (1957994, 3, 7),
  (1958208, 5, 5),
  (1962512, 7, 4),
  (1963190, 5, 7),
  (1963293, 2, 1),
  (1967294, 3, 1),
  (1967438, 3, 7),
  (1968967, 4, 7),
  (1969121, 1, 7),
  (1970822, 1, 7),
  (1971217, 1, 3),
  (1972852, 3, 7),
  (1975306, 5, 7),
  (1976165, 3, 3),
  (1978102, 6, 0),
  (1978687, 6, 7),
  (1980851, 1, 4),
  (1982024, 1, 0),
  (1988781, 0, 3),
  (1989870, 3, 7),
  (1990013, 7, 7),
  (1991255, 4, 7),
  (1991994, 4, 7),
  (1993328, 7, 0),
  (1996464, 4, 6),
  (2000985, 4, 3),
  (2002225, 4, 7),
  (2002747, 0, 7),
  (2003122, 3, 3),
  (2006233, 1, 7),
  (2016780, 2, 3),
  (2018686, 7, 6),
  (2019149, 5, 7),
  (2019636, 7, 4),
  (2020971, 2, 2),
  (2021145, 6, 0),
  (2024966, 3, 2),
  (2025406, 6, 4),
  (2030728, 1, 7),
  (2036322, 7, 5),
  (2037224, 2, 3),
  (2041293, 0, 3),
  (2050111, 0, 7),
  (2051773, 3, 4),
  (2053709, 0, 7),
  (2053755, 5, 7),
  (2054523, 6, 4),
  (2055114, 5, 7),
  (2055255, 7, 7),
  (2058784, 5, 6),
  (2059342, 0, 7),
  (2061296, 5, 2),
  (2064914, 7, 0),
  (2065585, 4, 7),
  (2065957, 2, 5),
  (2067094, 6, 7),
  (2067283, 6, 1),
  (2070333, 3, 7),
  (2072075, 1, 3),
  (2072335, 2, 4),
  (2074379, 2, 6),
  (2074915, 0, 6),
  (2075530, 1, 7),
  (2076086, 3, 6),
  (2083735, 5, 3),
  (2085726, 5, 5),
  (2087907, 4, 7),
  (2088294, 1, 7),
  (2089870, 5, 7),
  (2092308, 3, 5),
  (2092669, 4, 3),
  (2094780, 1, 7),
  (2099356, 0, 7),
  (2100992, 7, 0),
  (2105494, 2, 3),
  (2107935, 3, 2),
  (2114683, 6, 0),
  (2115542, 6, 5),
  (2117475, 1, 2),
  (2117488, 4, 7),
  (2121398, 4, 7),
  (2122446, 0, 3),
  (2123076, 3, 6),
  (2123823, 5, 7),
  (2124485, 2, 7),
  (2126955, 1, 7),
  (2127259, 5, 7),
  (2129484, 0, 4),
  (2129625, 4, 0),
  (2131517, 4, 7),
  (2134760, 5, 7),
  (2134867, 5, 4),
  (2135887, 0, 7),
  (2136504, 5, 7),
  (2140325, 6, 0),
  (2141524, 0, 2),
  (2142936, 7, 4),
  (2144984, 2, 6),
  (2149794, 3, 7),
  (2150072, 4, 7),
  (2152853, 1, 7),
  (2157050, 4, 3),
  (2157788, 7, 7),
  (2158669, 4, 3),
  (2160048, 5, 3),
  (2161955, 2, 2),
  (2169456, 7, 7),
  (2169608, 1, 0),
  (2172424, 0, 2),
  (2174547, 0, 7),
  (2179355, 6, 7),
  (2179575, 4, 6),
  (2181238, 0, 7),
  (2190296, 7, 7),
  (2196048, 5, 7),
  (2196370, 5, 7),
  (2197297, 6, 2),
  (2200707, 7, 0),
  (2201303, 1, 4),
  (2202006, 0, 7),
  (2203586, 2, 5),
  (2206063, 4, 3),
  (2209103, 4, 5),
  (2209382, 1, 0),
  (2210877, 0, 0),
  (2214945, 5, 3),
  (2219114, 1, 4),
  (2224685, 7, 4),
  (2228978, 6, 7),
  (2229454, 0, 7),
  (2230488, 1, 7),
  (2233236, 4, 3),
  (2238494, 6, 0),
  (2240733, 4, 5),
  (2242932, 4, 6),
  (2248134, 2, 6),
  (2252533, 1, 3),
  (2254244, 3, 3),
  (2256032, 5, 2),
  (2257817, 7, 0),
  (2265995, 7, 0),
  (2268516, 4, 7),
  (2271832, 6, 3),
  (2287572, 7, 7),
  (2289343, 0, 4),
  (2291982, 5, 4),
  (2295037, 6, 3),
  (2295331, 4, 7),
  (2296385, 4, 6),
  (2297453, 1, 7),
  (2298330, 5, 5),
  (2298593, 1, 0),
  (2299296, 0, 4),
  (2300934, 1, 0),
  (2301217, 6, 7),
  (2301571, 7, 0),
  (2301646, 1, 0),
  (2302009, 0, 3),
  (2304268, 2, 2),
  (2308022, 1, 7),
  (2309490, 7, 0),
  (2310334, 5, 6),
  (2317607, 6, 3),
  (2320943, 1, 7),
  (2322823, 0, 0),
  (2326392, 0, 7),
  (2335297, 4, 3),
  (2335912, 2, 2),
  (2336389, 1, 7),
  (2336865, 3, 7),
  (2339815, 6, 7),
  (2341053, 4, 3),
  (2342005, 3, 3),
  (2348062, 2, 5),
  (2348196, 3, 3),
  (2349194, 7, 3),
  (2349851, 4, 1),
  (2352753, 5, 3),
  (2356567, 5, 3),
  (2357675, 5, 7),
  (2358112, 4, 3),
  (2359908, 1, 7),
  (2361921, 0, 7),
  (2363963, 2, 7),
  (2365947, 1, 7),
  (2367780, 2, 7),
  (2370275, 3, 2),
  (2373512, 3, 7),
  (2375808, 6, 3),
  (2377466, 1, 7),
  (2377480, 0, 0),
  (2378433, 5, 7),
  (2378892, 4, 3),
  (2380119, 4, 6),
  (2387892, 6, 7),
  (2389977, 6, 7),
  (2391559, 2, 2),
  (2401557, 4, 7),
  (2402067, 5, 3),
  (2405703, 5, 2),
  (2405789, 4, 3),
  (2407405, 0, 7),
  (2409550, 1, 0),
  (2412734, 1, 7),
  (2413339, 7, 3),
  (2414770, 6, 7),
  (2415291, 1, 7),
  (2416259, 1, 7),
  (2416298, 0, 5),
  (2416595, 3, 3),
  (2417974, 5, 7),
  (2423748, 4, 7),
  (2423869, 2, 6),
  (2423929, 5, 7),
  (2425131, 7, 4),
  (2427529, 3, 3),
  (2433560, 0, 7),
  (2435505, 7, 6),
  (2436557, 7, 4),
  (2437574, 0, 3),
  (2437608, 7, 7),
  (2439161, 3, 7),
  (2439293, 6, 3),
  (2442313, 0, 3),
  (2443556, 2, 3),
  (2444238, 2, 7),
  (2446973, 5, 3),
  (2449270, 4, 3),
  (2454449, 1, 7),
  (2458205, 6, 7),
  (2459608, 5, 6),
  (2462660, 0, 3),
  (2463014, 4, 7),
  (2463367, 4, 5),
  (2463651, 2, 7),
  (2463676, 2, 2),
  (2470610, 3, 5),
  (2473257, 3, 5),
  (2473397, 7, 0),
  (2476691, 0, 0),
  (2476949, 2, 2),
  (2479679, 0, 7),
  (2480223, 6, 3),
  (2481463, 2, 7),
  (2484558, 3, 0),
  (2486855, 4, 7),
  (2487053, 0, 0),
  (2488697, 5, 6),
  (2489392, 0, 4),
  (2494850, 4, 7),
  (2496121, 4, 2),
  (2497420, 7, 3),
  (2497522, 0, 5),
  (2498483, 1, 3),
  (2498852, 4, 3),
  (2499868, 3, 2),
  (2500585, 4, 5),
  (2501745, 5, 7),
  (2502354, 6, 0),
  (2506662, 4, 5),
  (2506690, 7, 7),
  (2507539, 2, 7),
  (2508450, 7, 0),
  (2511453, 5, 3),
  (2517385, 4, 4),
  (2517401, 2, 3),
  (2518075, 7, 0),
  (2518327, 1, 4),
  (2520195, 5, 6),
  (2522727, 2, 7),
  (2529855, 1, 3),
  (2530015, 3, 7),
  (2532572, 7, 1),
  (2534368, 4, 7),
  (2536725, 5, 7),
  (2537473, 6, 0),
  (2537505, 2, 6),
  (2539200, 7, 7),
  (2539715, 7, 3),
  (2540188, 0, 0),
  (2540591, 2, 7),
  (2542501, 0, 0),
  (2544942, 6, 0),
  (2546314, 2, 5),
  (2547695, 2, 3),
  (2550165, 4, 5),
  (2554853, 6, 7),
  (2554904, 4, 3),
  (2555846, 2, 3),
  (2557911, 3, 7),
  (2560075, 5, 7),
  (2560170, 2, 7),
  (2560887, 3, 3),
  (2563769, 1, 6),
  (2564635, 6, 2),
  (2564989, 3, 7),
  (2565299, 6, 7),
  (2573373, 6, 7),
  (2576336, 4, 2),
  (2578718, 3, 1),
  (2584236, 7, 0),
  (2585637, 7, 2),
  (2587916, 5, 2),
  (2588611, 0, 7),
  (2589117, 1, 3),
  (2592288, 7, 0),
  (2593646, 0, 7),
  (2604095, 0, 7),
  (2606593, 0, 0),
  (2608037, 1, 3),
  (2614855, 6, 0),
  (2616216, 0, 7),
  (2617837, 3, 6),
  (2619214, 1, 7),
  (2620720, 7, 7),
  (2625743, 0, 0),
  (2625894, 5, 7),
  (2628085, 0, 7),
  (2630272, 4, 3),
  (2630477, 2, 2),
  (2632376, 7, 4),
  (2634033, 0, 2),
  (2635332, 1, 4),
  (2635462, 3, 7),
  (2636921, 7, 0),
  (2638216, 4, 7),
  (2639943, 4, 7),
  (2641021, 6, 7),
  (2644714, 3, 6),
  (2645569, 5, 3),
  (2645660, 0, 7),
  (2652535, 5, 5),
  (2655306, 3, 5),
  (2656677, 0, 7),
  (2657376, 0, 7),
  (2657377, 5, 6),
  (2657617, 0, 7),
  (2658224, 2, 7),
  (2658395, 6, 1),
  (2659941, 5, 2),
  (2661549, 5, 5),
  (2664843, 6, 6),
  (2665441, 6, 7),
  (2665967, 7, 7),
  (2666035, 7, 0),
  (2667058, 0, 3),
  (2667155, 5, 3),
  (2670565, 1, 7),
  (2671889, 5, 7),
  (2674222, 4, 2),
  (2675538, 4, 6),
  (2678960, 2, 6),
  (2683101, 7, 0),
  (2683242, 1, 7),
  (2683701, 7, 4),
  (2684398, 3, 2),
  (2684902, 1, 7),
  (2686020, 5, 7),
  (2688309, 1, 6),
  (2688718, 6, 0),
  (2689834, 3, 7),
  (2690451, 0, 7),
  (2691903, 7, 7),
  (2693669, 2, 7),
  (2694025, 6, 7),
  (2696841, 1, 7),
  (2697460, 6, 6),
  (2705984, 6, 3),
  (2711413, 4, 7),
  (2713129, 4, 1),
  (2715420, 4, 5),
  (2717776, 2, 2),
  (2720369, 4, 3),
  (2722373, 5, 0),
  (2726331, 1, 4),
  (2728131, 1, 6),
  (2728442, 4, 3),
  (2730359, 3, 5),
  (2730381, 7, 4),
  (2733559, 6, 7),
  (2733811, 1, 6),
  (2734531, 0, 3),
  (2738719, 0, 0),
  (2740279, 7, 0),
  (2741498, 6, 7),
  (2743051, 6, 0),
  (2743165, 1, 7),
  (2744033, 7, 7),
  (2748242, 7, 7),
  (2749696, 3, 7),
  (2749825, 2, 7),
  (2751740, 2, 7),
  (2757238, 4, 7),
  (2757476, 0, 7),
  (2758062, 4, 6),
  (2761517, 1, 7),
  (2763501, 1, 3),
  (2763960, 7, 7),
  (2767608, 2, 6),
  (2773577, 7, 3),
  (2776577, 5, 5),
  (2778220, 1, 7),
  (2780423, 4, 7),
  (2784298, 5, 2),
  (2785569, 3, 6),
  (2788341, 7, 7),
  (2789416, 7, 0),
  (2790454, 6, 3),
  (2790617, 4, 2),
  (2792627, 6, 3),
  (2793063, 3, 3),
  (2793396, 5, 6),
  (2794188, 5, 3),
  (2795450, 7, 4),
  (2797302, 5, 6),
  (2798162, 3, 7),
  (2803402, 5, 6),
  (2809779, 3, 2),
  (2815062, 2, 6),
  (2815155, 3, 2),
  (2816375, 2, 7),
  (2818689, 3, 7),
  (2819290, 1, 4),
  (2821501, 1, 0),
  (2822416, 1, 0),
  (2823431, 2, 5),
  (2825158, 7, 7),
  (2826680, 3, 6),
  (2827624, 0, 0),
  (2828127, 0, 7),
  (2832612, 1, 3),
  (2832687, 2, 3),
  (2832975, 2, 6),
  (2833257, 6, 0),
  (2833869, 1, 4),
  (2835559, 6, 7),
  (2837898, 6, 3),
  (2839613, 6, 3),
  (2841063, 1, 4),
  (2842226, 5, 6),
  (2844457, 7, 7),
  (2845514, 0, 7),
  (2847611, 3, 3),
  (2847623, 1, 7),
  (2851748, 4, 7),
  (2852295, 0, 4),
  (2853590, 7, 4),
  (2859593, 2, 3),
  (2862365, 3, 7),
  (2866079, 0, 2),
  (2867052, 0, 6),
  (2868908, 1, 7),
  (2869637, 3, 6),
  (2869747, 1, 0),
  (2871923, 5, 7),
  (2873927, 2, 2),
  (2875189, 6, 4),
  (2878048, 5, 3),
  (2878805, 4, 7),
  (2880704, 3, 2),
  (2883361, 4, 7),
  (2883639, 1, 6),
  (2884930, 4, 3),
  (2887012, 7, 0),
  (2888292, 3, 3),
  (2891128, 2, 7),
  (2892265, 6, 7),
  (2892858, 7, 5),
  (2893536, 3, 7),
  (2895668, 1, 2),
  (2895703, 6, 4),
  (2896754, 1, 7),
  (2898580, 6, 7),
  (2902176, 5, 3),
  (2904669, 7, 7),
  (2908235, 2, 6),
  (2908985, 7, 7),
  (2913097, 1, 0),
  (2914729, 5, 6),
  (2919623, 5, 6),
  (2921186, 1, 7),
  (2922351, 5, 6),
  (2931147, 4, 4),
  (2931443, 1, 6),
  (2933008, 0, 7),
  (2936425, 5, 3),
  (2937973, 2, 7),
  (2938195, 2, 3),
  (2941476, 6, 0),
  (2941693, 3, 7),
  (2942289, 6, 4),
  (2943350, 3, 3),
  (2943780, 5, 7),
  (2943786, 4, 7),
  (2945746, 1, 0),
  (2946229, 5, 3),
  (2947206, 0, 4),
  (2947605, 1, 7),
  (2948179, 0, 3),
  (2951494, 1, 7),
  (2958208, 3, 2),
  (2958400, 3, 5),
  (2959959, 7, 7),
  (2960359, 0, 7),
  (2960540, 5, 6),
  (2961668, 7, 7),
  (2961980, 7, 0),
  (2963431, 2, 6),
  (2964737, 4, 6),
  (2969098, 3, 3),
  (2970488, 6, 1),
  (2970854, 4, 7),
  (2971406, 4, 7),
  (2972622, 0, 0),
  (2975577, 6, 7),
  (2976017, 0, 4),
  (2979650, 2, 3),
  (2981125, 7, 7),
  (2982991, 7, 7),
  (2983150, 4, 3),
  (2990739, 4, 5),
  (2993817, 2, 3),
  (2996061, 0, 7),
  (2996062, 6, 7),
  (3003852, 3, 3),
  (3006483, 1, 0),
  (3008349, 1, 0),
  (3011404, 3, 3),
  (3016097, 2, 2),
  (3018087, 6, 3),
  (3018351, 1, 4),
  (3021003, 4, 1),
  (3024081, 2, 6),
  (3026216, 6, 7),
  (3026838, 2, 3),
  (3029316, 5, 0),
  (3031610, 5, 3),
  (3031720, 3, 3),
  (3032850, 7, 7),
  (3033564, 3, 7),
  (3037988, 3, 2),
  (3038017, 7, 3),
  (3038298, 1, 7),
  (3038595, 0, 3),
  (3039853, 5, 3),
  (3040942, 5, 7),
  (3041241, 0, 3),
  (3042431, 4, 3),
  (3043058, 6, 6),
  (3044739, 0, 7),
  (3046531, 4, 5),
  (3046971, 1, 0),
  (3053507, 0, 7),
  (3055023, 7, 7),
  (3056124, 3, 3),
  (3059239, 0, 3),
  (3059866, 6, 5),
  (3063527, 7, 7),
  (3063650, 2, 7),
  (3066414, 1, 7),
  (3067998, 2, 1),
  (3070689, 1, 0),
  (3072007, 5, 3),
  (3078175, 5, 3),
  (3079668, 3, 7),
  (3079873, 0, 0),
  (3080194, 1, 7),
  (3081231, 0, 3),
  (3081428, 6, 7),
  (3081570, 2, 6),
  (3087899, 6, 4),
  (3088146, 2, 5),
  (3089106, 6, 0),
  (3092326, 6, 0),
  (3093286, 6, 1),
  (3095653, 7, 7),
  (3099844, 2, 7),
  (3101455, 6, 0),
  (3102966, 5, 6),
  (3104057, 5, 7),
  (3105171, 7, 3),
  (3107831, 0, 0),
  (3109389, 2, 4),
  (3110293, 2, 3),
  (3119294, 6, 2),
  (3120892, 5, 5),
  (3123702, 2, 7),
  (3125239, 2, 2),
  (3125489, 0, 4),
  (3126313, 6, 3),
  (3128055, 0, 4),
  (3129250, 7, 3),
  (3130096, 5, 7),
  (3131221, 3, 2),
  (3132200, 0, 7),
  (3132921, 2, 5),
  (3133110, 1, 7),
  (3133365, 5, 3),
  (3138471, 6, 7),
  (3138639, 0, 4),
  (3139086, 0, 3),
  (3144274, 2, 7),
  (3144912, 0, 0),
  (3147726, 2, 2),
  (3148160, 0, 7),
  (3150907, 2, 3),
  (3151470, 1, 0),
  (3152807, 4, 7),
  (3154670, 2, 1),
  (3155290, 4, 7),
  (3157528, 3, 3),
  (3165501, 6, 7),
  (3166464, 4, 2),
  (3172187, 2, 6),
  (3172766, 4, 2),
  (3172923, 6, 7),
  (3174193, 5, 3),
  (3176762, 5, 5),
  (3178801, 2, 7),
  (3178964, 1, 3),
  (3179361, 1, 7),
  (3180710, 2, 7),
  (3181540, 6, 0),
  (3181765, 6, 3),
  (3182926, 3, 3),
  (3183674, 2, 6),
  (3187790, 5, 7),
  (3188585, 2, 7),
  (3189111, 1, 7),
  (3190172, 2, 5),
  (3196730, 3, 5),
  (3196765, 7, 6),
  (3197384, 2, 7),
  (3200154, 7, 4),
  (3201365, 5, 3),
  (3204272, 1, 6),
  (3205755, 4, 3),
  (3207926, 6, 7),
  (3212844, 7, 7),
  (3214868, 1, 3),
  (3215695, 1, 6),
  (3216413, 5, 3),
  (3218558, 5, 2),
  (3221058, 0, 3),
  (3222501, 1, 5),
  (3223841, 6, 7),
  (3225356, 4, 7),
  (3227580, 7, 7),
  (3230323, 7, 7),
  (3231408, 4, 3),
  (3233516, 0, 4),
  (3234776, 0, 4),
  (3235614, 3, 2),
  (3235759, 7, 7),
  (3237676, 6, 7),
  (3239720, 6, 3),
  (3240749, 3, 7),
  (3245500, 4, 2),
  (3246471, 0, 0),
  (3249673, 0, 3),
  (3254337, 5, 6),
  (3255565, 5, 7),
  (3255686, 2, 2),
  (3256387, 4, 2),
  (3257440, 2, 3),
  (3257864, 7, 7),
  (3258208, 6, 7),
  (3258230, 4, 7),
  (3260581, 5, 7),
  (3266127, 0, 4),
  (3269730, 6, 0),
  (3271541, 4, 2),
  (3272553, 5, 4),
  (3274046, 1, 7),
  (3277367, 5, 4),
  (3283808, 7, 0),
  (3284405, 6, 7),
  (3285371, 2, 2),
  (3288164, 5, 3),
  (3288854, 0, 7),
  (3293797, 1, 6),
  (3296420, 6, 6),
  (3296691, 6, 3),
  (3296772, 1, 7),
  (3298492, 2, 7),
  (3301305, 1, 7),
  (3308218, 4, 3),
  (3308227, 7, 7),
  (3311608, 3, 3),
  (3312442, 6, 4),
  (3315664, 6, 7),
  (3316832, 4, 7),
  (3319757, 3, 3),
  (3323010, 6, 7),
  (3325705, 1, 6),
  (3326380, 1, 0),
  (3327476, 2, 2),
  (3329579, 1, 7),
  (3330381, 0, 0),
  (3332745, 0, 3),
  (3334445, 4, 7),
  (3338017, 1, 2),
  (3338609, 6, 0),
  (3340302, 2, 2),
  (3341608, 4, 2),
  (3343728, 0, 0),
  (3344031, 7, 0),
  (3344149, 7, 4),
  (3345780, 5, 7),
  (3346552, 3, 2),
  (3347509, 3, 7),
  (3347565, 3, 6),
  (3348934, 5, 5),
  (3349446, 0, 7),
  (3350262, 3, 3),
  (3352096, 3, 5),
  (3352504, 6, 3),
  (3354381, 1, 7),
  (3360170, 4, 7),
  (3361856, 2, 2),
  (3362979, 7, 7),
  (3362998, 5, 7),
  (3365121, 0, 3),
  (3365496, 7, 4),
  (3366473, 1, 6),
  (3369262, 1, 7),
  (3369574, 4, 7),
  (3371277, 0, 7),
  (3372512, 5, 4),
  (3375475, 3, 7),
  (3376354, 0, 6),
  (3381421, 6, 0),
  (3382795, 0, 0),
  (3383103, 1, 0),
  (3383496, 0, 7),
  (3385208, 1, 0),
  (3386527, 5, 7),
  (3386747, 0, 7),
  (3387662, 4, 2),
  (3387677, 3, 7),
  (3388790, 2, 5),
  (3392068, 6, 0),
  (3393497, 5, 3),
  (3406580, 1, 3),
  (3413100, 0, 6),
  (3414626, 7, 7),
  (3417649, 7, 2),
  (3418433, 3, 7),
  (3418644, 7, 7),
  (3419950, 7, 7),
  (3425080, 4, 7),
  (3428426, 5, 5),
  (3428558, 0, 7),
  (3431662, 1, 7),
  (3431704, 1, 7),
  (3432705, 7, 4),
  (3436302, 2, 3),
  (3437466, 6, 0),
  (3439417, 3, 2),
  (3444192, 6, 7),
  (3446687, 2, 3),
  (3448647, 3, 3),
  (3451006, 2, 2),
  (3454240, 2, 7),
  (3454537, 2, 4),
  (3456437, 0, 7),
  (3458510, 3, 5),
  (3459566, 0, 7),
  (3462218, 5, 2),
  (3463902, 2, 6),
  (3466104, 1, 6),
  (3466178, 7, 0),
  (3467263, 1, 7),
  (3467589, 0, 0),
  (3470143, 3, 3),
  (3472169, 1, 0),
  (3478056, 1, 7),
  (3481522, 2, 7),
  (3483014, 5, 7),
  (3483391, 0, 3),
  (3485321, 4, 7),
  (3485547, 7, 7),
  (3487468, 5, 3),
  (3492098, 4, 6),
  (3492589, 6, 4),
  (3493599, 1, 0),
  (3493638, 0, 6),
  (3497548, 0, 2),
  (3498026, 1, 0),
  (3502496, 3, 7),
  (3503452, 1, 0),
  (3505003, 6, 4),
  (3505451, 1, 7),
  (3506301, 7, 4),
  (3510043, 6, 7),
  (3510829, 1, 7),
  (3516668, 2, 5),
  (3523897, 1, 0),
  (3528551, 7, 7),
  (3528735, 1, 3),
  (3529102, 2, 2),
  (3529357, 7, 4),
  (3529557, 4, 7),
  (3530625, 6, 4),
  (3530712, 2, 7),
  (3532499, 0, 2),
  (3532619, 7, 3),
  (3532961, 0, 3),
  (3533574, 2, 2),
  (3536122, 4, 3),
  (3536375, 7, 0),
  (3537118, 5, 7),
  (3540078, 1, 4),
  (3540820, 0, 0),
  (3541166, 2, 7),
  (3546452, 3, 7),
  (3547304, 2, 7),
  (3548195, 2, 4),
  (3549947, 2, 3),
  (3553943, 2, 5),
  (3559684, 6, 3),
  (3561333, 6, 6),
  (3563606, 7, 3),
  (3563818, 3, 6),
  (3564977, 3, 5),
  (3565016, 2, 7),
  (3566101, 6, 4),
  (3566873, 4, 7),
  (3569498, 6, 6),
  (3573212, 5, 7),
  (3574042, 6, 6),
  (3579453, 3, 2),
  (3581248, 5, 7),
  (3582988, 1, 7),
  (3583200, 6, 7),
  (3588865, 6, 0),
  (3590751, 4, 7),
  (3591368, 0, 0),
  (3597189, 3, 3),
  (3597367, 0, 7),
  (3599522, 2, 3),
])
