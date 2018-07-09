from util import *
schedule = deque([
  (984, 2, 6),
  (1772, 1, 4),
  (2002, 7, 3),
  (2857, 5, 5),
  (5152, 6, 0),
  (7787, 1, 6),
  (10584, 5, 3),
  (12217, 3, 3),
  (12323, 5, 3),
  (13826, 7, 4),
  (15743, 6, 0),
  (17210, 1, 0),
  (22433, 3, 7),
  (24031, 7, 3),
  (24998, 5, 6),
  (29334, 2, 7),
  (31885, 7, 7),
  (36414, 0, 7),
  (38823, 3, 3),
  (48715, 2, 3),
  (49441, 7, 0),
  (53872, 2, 3),
  (54784, 7, 6),
  (55864, 2, 7),
  (59243, 4, 3),
  (61427, 4, 7),
  (64286, 0, 7),
  (64938, 2, 2),
  (68829, 0, 4),
  (70779, 2, 2),
  (71298, 6, 3),
  (72011, 7, 7),
  (75255, 5, 3),
  (75867, 6, 0),
  (77176, 7, 4),
  (81392, 2, 7),
  (81759, 0, 3),
  (82949, 0, 0),
  (83638, 0, 4),
  (88282, 6, 2),
  (90573, 6, 0),
  (90670, 3, 7),
  (91114, 0, 4),
  (94176, 5, 7),
  (94394, 7, 4),
  (97238, 3, 3),
  (101186, 5, 5),
  (103989, 4, 3),
  (105970, 0, 5),
  (107159, 3, 3),
  (108550, 5, 7),
  (108685, 4, 2),
  (109142, 6, 7),
  (109219, 7, 0),
  (109535, 5, 6),
  (109908, 1, 7),
  (111568, 4, 2),
  (116452, 5, 2),
  (121113, 4, 3),
  (124235, 1, 4),
  (124815, 3, 1),
  (126938, 2, 2),
  (127626, 4, 2),
  (128350, 3, 7),
  (128998, 3, 0),
  (134373, 7, 4),
  (137611, 3, 5),
  (138850, 0, 0),
  (143629, 3, 3),
  (144768, 2, 7),
  (145153, 1, 4),
  (146404, 0, 0),
  (147081, 5, 2),
  (148336, 2, 2),
  (153092, 4, 3),
  (153439, 3, 3),
  (156664, 4, 3),
  (158346, 4, 3),
  (158627, 2, 3),
  (161186, 0, 0),
  (161721, 4, 2),
  (163639, 0, 0),
  (164399, 3, 7),
  (166852, 7, 5),
  (167330, 2, 6),
  (172106, 0, 5),
  (180010, 7, 0),
  (180257, 7, 7),
  (183177, 7, 0),
  (183837, 3, 7),
  (185974, 0, 4),
  (190424, 2, 3),
  (190616, 1, 2),
  (192704, 0, 4),
  (194715, 7, 4),
  (197800, 4, 5),
  (197971, 5, 2),
  (203866, 5, 5),
  (205210, 1, 0),
  (205368, 4, 2),
  (205473, 0, 0),
  (206440, 0, 0),
  (207168, 3, 6),
  (211450, 0, 7),
  (214524, 4, 5),
  (214831, 5, 7),
  (219826, 5, 7),
  (229393, 1, 0),
  (232447, 7, 3),
  (232777, 1, 4),
  (233580, 5, 7),
  (236737, 2, 7),
  (238514, 3, 7),
  (239513, 4, 6),
  (242224, 0, 4),
  (245336, 6, 0),
  (245939, 2, 6),
  (246534, 7, 3),
  (249263, 0, 7),
  (258110, 6, 0),
  (259124, 7, 7),
  (263178, 0, 4),
  (266288, 5, 3),
  (267752, 7, 7),
  (270371, 2, 2),
  (271483, 2, 3),
  (272637, 2, 6),
  (273710, 7, 0),
  (276894, 5, 3),
  (277508, 6, 4),
  (278053, 4, 7),
  (283776, 0, 4),
  (284045, 7, 4),
  (284437, 5, 7),
  (285073, 6, 4),
  (285142, 4, 3),
  (285530, 1, 5),
  (287533, 3, 2),
  (288087, 0, 0),
  (288618, 3, 0),
  (292423, 4, 6),
  (292929, 7, 2),
  (295115, 0, 0),
  (296274, 5, 6),
  (296381, 3, 0),
  (297324, 7, 4),
  (300847, 7, 7),
  (300876, 7, 0),
  (301685, 6, 7),
  (304986, 6, 0),
  (305219, 1, 3),
  (306193, 3, 7),
  (307477, 6, 0),
  (312417, 5, 7),
  (312987, 7, 6),
  (315385, 3, 3),
  (317546, 1, 4),
  (318562, 4, 3),
  (320141, 0, 0),
  (323465, 0, 3),
  (326402, 5, 7),
  (327007, 1, 2),
  (330056, 1, 6),
  (335210, 3, 3),
  (336505, 1, 4),
  (337310, 1, 0),
  (337788, 4, 3),
  (339607, 0, 3),
  (341721, 4, 3),
  (342011, 7, 3),
  (343891, 3, 7),
  (344049, 7, 7),
  (348713, 5, 7),
  (349738, 3, 3),
  (352038, 2, 4),
  (352593, 0, 1),
  (356135, 0, 0),
  (358264, 7, 4),
  (358706, 7, 4),
  (362013, 5, 6),
  (364341, 0, 3),
  (366192, 5, 3),
  (370768, 2, 6),
  (371043, 6, 3),
  (372676, 7, 7),
  (375306, 3, 3),
  (377650, 5, 2),
  (380209, 1, 0),
  (381394, 7, 4),
  (381539, 1, 0),
  (384196, 3, 1),
  (384707, 1, 3),
  (389081, 5, 0),
  (390167, 2, 0),
  (395025, 7, 7),
  (395506, 6, 3),
  (405069, 4, 5),
  (405764, 3, 2),
  (409068, 6, 0),
  (410153, 5, 6),
  (410642, 7, 4),
  (413546, 1, 2),
  (414144, 0, 0),
  (415209, 2, 6),
  (424916, 7, 3),
  (429079, 7, 3),
  (429722, 2, 6),
  (429977, 0, 0),
  (431279, 7, 7),
  (432793, 2, 5),
  (434645, 7, 7),
  (437199, 1, 3),
  (437398, 0, 0),
  (439577, 7, 7),
  (440707, 6, 7),
  (441869, 2, 7),
  (443060, 1, 6),
  (450545, 2, 7),
  (450752, 5, 7),
  (453883, 1, 2),
  (455158, 1, 4),
  (456257, 4, 3),
  (456261, 0, 3),
  (458297, 5, 5),
  (458418, 5, 5),
  (459666, 6, 6),
  (460320, 0, 3),
  (461399, 4, 5),
  (461637, 4, 3),
  (462723, 4, 7),
  (462866, 0, 4),
  (465235, 0, 3),
  (466324, 2, 3),
  (467340, 7, 7),
  (468905, 5, 7),
  (470187, 2, 5),
  (471888, 7, 7),
  (473718, 3, 6),
  (473754, 0, 0),
  (478217, 1, 6),
  (478906, 0, 7),
  (479753, 5, 6),
  (481754, 3, 4),
  (486240, 1, 4),
  (489433, 2, 3),
  (489695, 7, 2),
  (496142, 0, 7),
  (496199, 1, 0),
  (497718, 7, 7),
  (498506, 3, 3),
  (499781, 7, 0),
  (500237, 7, 0),
  (503801, 4, 3),
  (506684, 3, 5),
  (507353, 0, 7),
  (509280, 7, 0),
  (509969, 4, 7),
  (512761, 0, 6),
  (515558, 0, 5),
  (517650, 6, 7),
  (517818, 3, 3),
  (518485, 3, 2),
  (520720, 4, 3),
  (526346, 3, 7),
  (526820, 5, 6),
  (527962, 6, 6),
  (529510, 7, 7),
  (531057, 3, 3),
  (531229, 2, 6),
  (535304, 4, 6),
  (538652, 4, 3),
  (539197, 3, 3),
  (539496, 6, 6),
  (541859, 1, 4),
  (542781, 3, 2),
  (543126, 0, 7),
  (544175, 2, 7),
  (548997, 7, 0),
  (549366, 7, 0),
  (555737, 2, 6),
  (556456, 2, 7),
  (558501, 4, 3),
  (559315, 0, 5),
  (560053, 5, 7),
  (560558, 0, 5),
  (561293, 6, 3),
  (561457, 6, 7),
  (561744, 4, 1),
  (565834, 7, 0),
  (569200, 7, 1),
  (570302, 2, 3),
  (570536, 7, 3),
  (573108, 5, 3),
  (576452, 3, 2),
  (576472, 0, 4),
  (577078, 1, 0),
  (589539, 6, 7),
  (592285, 3, 0),
  (596695, 3, 3),
  (599630, 7, 3),
  (600781, 3, 7),
  (601200, 2, 6),
  (602531, 7, 4),
  (605803, 1, 7),
  (607653, 7, 3),
  (608203, 2, 7),
  (610891, 3, 3),
  (611318, 4, 3),
  (611894, 1, 4),
  (612235, 1, 5),
  (612416, 3, 7),
  (613534, 2, 3),
  (614462, 0, 7),
  (616572, 3, 5),
  (618663, 0, 7),
  (627855, 4, 3),
  (628265, 2, 3),
  (631819, 4, 7),
  (632776, 5, 5),
  (635671, 0, 0),
  (639214, 1, 7),
  (647579, 1, 7),
  (649335, 7, 4),
  (650086, 2, 3),
  (650231, 2, 3),
  (650476, 6, 0),
  (651710, 2, 5),
  (653082, 6, 4),
  (654795, 4, 6),
  (655064, 3, 5),
  (656904, 5, 6),
  (660233, 6, 0),
  (662802, 2, 7),
  (664091, 3, 3),
  (667263, 2, 2),
  (671781, 7, 4),
  (677518, 3, 6),
  (680795, 2, 7),
  (681132, 4, 3),
  (683361, 0, 3),
  (687080, 4, 3),
  (691868, 2, 7),
  (694948, 5, 2),
  (695985, 1, 0),
  (700235, 1, 0),
  (702003, 5, 2),
  (707314, 4, 3),
  (712247, 6, 4),
  (714356, 4, 7),
  (716825, 4, 7),
  (717848, 0, 3),
  (718213, 0, 7),
  (718677, 6, 7),
  (720085, 7, 2),
  (720940, 5, 2),
  (722798, 7, 7),
  (723225, 6, 7),
  (727310, 4, 3),
  (728513, 4, 3),
  (729021, 2, 3),
  (729840, 5, 3),
  (731565, 7, 7),
  (732383, 4, 3),
  (733586, 0, 1),
  (737690, 4, 7),
  (739059, 7, 5),
  (741601, 6, 7),
  (743213, 4, 6),
  (744836, 0, 3),
  (749436, 3, 2),
  (750147, 2, 3),
  (750839, 3, 7),
  (754037, 6, 5),
  (757509, 6, 6),
  (759396, 6, 7),
  (760970, 7, 7),
  (763623, 7, 0),
  (764216, 6, 0),
  (770079, 2, 6),
  (771367, 2, 3),
  (772818, 6, 0),
  (774256, 7, 3),
  (774489, 1, 0),
  (776779, 6, 0),
  (776919, 5, 7),
  (777198, 6, 7),
  (777922, 4, 7),
  (782754, 0, 7),
  (784098, 3, 6),
  (786385, 4, 1),
  (787996, 0, 7),
  (788186, 5, 0),
  (790404, 2, 7),
  (792003, 6, 7),
  (792110, 3, 6),
  (792224, 7, 7),
  (795409, 0, 2),
  (795923, 2, 2),
  (802169, 5, 7),
  (803038, 0, 0),
  (803181, 7, 7),
  (804298, 2, 3),
  (808673, 4, 5),
  (808821, 6, 6),
  (809775, 1, 0),
  (813018, 2, 7),
  (813107, 0, 4),
  (822771, 1, 3),
  (823289, 4, 2),
  (826995, 5, 2),
  (827462, 7, 5),
  (829705, 2, 0),
  (831333, 1, 6),
  (831826, 6, 0),
  (834119, 3, 7),
  (835808, 4, 3),
  (837079, 5, 2),
  (837803, 6, 6),
  (838169, 6, 6),
  (839328, 0, 3),
  (842082, 6, 4),
  (842633, 1, 0),
  (845470, 3, 7),
  (853455, 2, 7),
  (855697, 0, 6),
  (858009, 3, 5),
  (858058, 7, 4),
  (861921, 7, 0),
  (862452, 5, 7),
  (862569, 7, 0),
  (863468, 3, 7),
  (875630, 3, 3),
  (876311, 6, 0),
  (876549, 0, 0),
  (877426, 3, 7),
  (878877, 0, 7),
  (879467, 0, 0),
  (880218, 6, 4),
  (880350, 0, 6),
  (883368, 1, 3),
  (886121, 6, 3),
  (890015, 7, 7),
  (891367, 5, 6),
  (895665, 6, 4),
  (898301, 6, 7),
  (901857, 0, 3),
  (909521, 6, 7),
  (910796, 2, 7),
  (911678, 7, 7),
  (912525, 3, 3),
  (914754, 1, 7),
  (914922, 1, 7),
  (915645, 0, 5),
  (916182, 6, 4),
  (916460, 7, 0),
  (916510, 1, 3),
  (922010, 3, 2),
  (923423, 3, 6),
  (924007, 7, 0),
  (924570, 6, 3),
  (926616, 2, 3),
  (929533, 5, 6),
  (931552, 4, 7),
  (935341, 0, 4),
  (940204, 1, 7),
  (940839, 5, 2),
  (941332, 3, 7),
  (945023, 7, 0),
  (947561, 6, 7),
  (950682, 7, 0),
  (950840, 1, 0),
  (952882, 7, 7),
  (953573, 2, 7),
  (955024, 6, 0),
  (955464, 7, 0),
  (955944, 6, 3),
  (956883, 3, 2),
  (957681, 1, 0),
  (959216, 1, 7),
  (961860, 7, 3),
  (963952, 4, 7),
  (965994, 0, 4),
  (967837, 4, 3),
  (970422, 7, 0),
  (971352, 7, 3),
  (971399, 4, 7),
  (973356, 3, 6),
  (978278, 5, 2),
  (978602, 2, 7),
  (981616, 0, 2),
  (984823, 4, 7),
  (985703, 2, 6),
  (987233, 2, 7),
  (987719, 3, 4),
  (991356, 2, 7),
  (991623, 3, 7),
  (992353, 1, 0),
  (992682, 4, 6),
  (994214, 5, 3),
  (996376, 4, 3),
  (996509, 3, 6),
  (996578, 3, 7),
  (997435, 4, 6),
  (999253, 1, 6),
  (1000530, 5, 2),
  (1002833, 4, 3),
  (1002947, 2, 3),
  (1004870, 7, 7),
  (1005884, 0, 2),
  (1006215, 3, 7),
  (1007080, 0, 0),
  (1008200, 4, 2),
  (1011688, 7, 7),
  (1015914, 3, 6),
  (1016935, 6, 0),
  (1020109, 0, 0),
  (1022464, 1, 0),
  (1023446, 2, 3),
  (1023867, 0, 4),
  (1024159, 5, 3),
  (1024807, 3, 7),
  (1028518, 0, 3),
  (1030483, 3, 2),
  (1031207, 7, 0),
  (1031990, 1, 7),
  (1034642, 6, 4),
  (1035235, 1, 1),
  (1040452, 0, 4),
  (1040546, 6, 4),
  (1042195, 6, 7),
  (1042921, 6, 7),
  (1046704, 5, 6),
  (1054577, 0, 7),
  (1057742, 2, 3),
  (1059140, 2, 7),
  (1059364, 3, 5),
  (1061955, 6, 3),
  (1064369, 2, 3),
  (1066192, 1, 7),
  (1068086, 5, 7),
  (1068901, 1, 7),
  (1071256, 1, 4),
  (1079281, 6, 3),
  (1082811, 1, 6),
  (1084724, 5, 6),
  (1086239, 1, 4),
  (1086578, 1, 4),
  (1087002, 7, 7),
  (1087166, 6, 3),
  (1087569, 6, 4),
  (1089443, 0, 5),
  (1091559, 6, 3),
  (1092600, 6, 1),
  (1095501, 2, 7),
  (1095794, 6, 7),
  (1097211, 5, 7),
  (1098926, 7, 5),
  (1098991, 2, 3),
  (1100022, 4, 6),
  (1100982, 5, 2),
  (1101415, 0, 7),
  (1103883, 5, 3),
  (1104472, 7, 0),
  (1105323, 1, 3),
  (1105927, 0, 7),
  (1108135, 4, 3),
  (1110859, 3, 7),
  (1113723, 3, 5),
  (1122966, 7, 7),
  (1126261, 7, 7),
  (1128020, 3, 3),
  (1130636, 1, 7),
  (1131598, 1, 7),
  (1132378, 3, 2),
  (1134402, 4, 6),
  (1134630, 2, 0),
  (1137211, 2, 6),
  (1137835, 5, 3),
  (1139123, 0, 7),
  (1139905, 7, 4),
  (1142388, 4, 3),
  (1142519, 2, 7),
  (1146972, 0, 3),
  (1147421, 6, 6),
  (1148103, 7, 3),
  (1148294, 2, 7),
  (1148876, 3, 7),
  (1153979, 4, 7),
  (1154236, 1, 4),
  (1158660, 7, 7),
  (1163616, 2, 3),
  (1166349, 7, 0),
  (1167200, 3, 6),
  (1168761, 3, 7),
  (1169233, 6, 3),
  (1170390, 7, 3),
  (1171181, 5, 7),
  (1173471, 7, 7),
  (1177018, 4, 2),
  (1178511, 2, 7),
  (1179977, 3, 5),
  (1182188, 7, 6),
  (1183793, 5, 7),
  (1184683, 5, 6),
  (1185459, 0, 0),
  (1185593, 0, 7),
  (1187513, 4, 3),
  (1189201, 0, 4),
  (1190112, 4, 3),
  (1192353, 0, 3),
  (1193794, 2, 7),
  (1195642, 5, 7),
  (1195802, 4, 6),
  (1199712, 0, 0),
  (1203752, 6, 5),
  (1204163, 5, 7),
  (1208985, 2, 7),
  (1211424, 3, 6),
  (1214479, 2, 2),
  (1215488, 1, 4),
  (1218404, 5, 4),
  (1222087, 5, 3),
  (1222116, 0, 0),
  (1222678, 6, 3),
  (1223317, 1, 0),
  (1230700, 3, 7),
  (1230951, 1, 0),
  (1232406, 7, 0),
  (1235211, 5, 5),
  (1235831, 0, 4),
  (1240326, 5, 7),
  (1241421, 7, 4),
  (1245958, 6, 0),
  (1246039, 2, 3),
  (1249101, 6, 2),
  (1249228, 3, 3),
  (1252316, 7, 7),
  (1252348, 2, 7),
  (1252622, 3, 1),
  (1252807, 2, 6),
  (1252965, 3, 7),
  (1255506, 5, 6),
  (1258852, 4, 6),
  (1261503, 6, 7),
  (1264921, 4, 4),
  (1265698, 2, 5),
  (1266384, 3, 1),
  (1268109, 6, 4),
  (1268221, 3, 7),
  (1269685, 0, 6),
  (1269727, 4, 7),
  (1270926, 3, 6),
  (1272653, 2, 2),
  (1272700, 0, 4),
  (1275621, 4, 7),
  (1280643, 2, 3),
  (1281779, 3, 2),
  (1281880, 7, 7),
  (1282432, 7, 6),
  (1288636, 6, 0),
  (1289631, 6, 0),
  (1290997, 4, 0),
  (1292804, 3, 3),
  (1294419, 0, 6),
  (1305117, 5, 2),
  (1307126, 4, 4),
  (1308600, 7, 7),
  (1311658, 3, 7),
  (1314339, 0, 0),
  (1316720, 1, 0),
  (1316970, 7, 0),
  (1318805, 5, 2),
  (1322720, 5, 2),
  (1323878, 0, 0),
  (1325708, 6, 7),
  (1325929, 6, 7),
  (1327254, 3, 7),
  (1332221, 4, 7),
  (1333989, 6, 4),
  (1338183, 7, 0),
  (1341039, 1, 0),
  (1347852, 5, 7),
  (1348587, 5, 6),
  (1348930, 5, 3),
  (1351474, 1, 4),
  (1352245, 5, 3),
  (1352312, 2, 3),
  (1355245, 6, 4),
  (1357556, 7, 7),
  (1360786, 5, 3),
  (1362465, 6, 3),
  (1362515, 6, 0),
  (1364834, 0, 7),
  (1365891, 0, 7),
  (1367917, 2, 7),
  (1368665, 5, 3),
  (1372540, 1, 7),
  (1373397, 1, 7),
  (1374687, 4, 3),
  (1376028, 3, 2),
  (1376518, 6, 0),
  (1377543, 7, 5),
  (1378523, 2, 4),
  (1379980, 7, 6),
  (1381642, 0, 0),
  (1385596, 3, 6),
  (1386437, 4, 3),
  (1387670, 4, 3),
  (1389290, 7, 6),
  (1390769, 2, 7),
  (1394224, 7, 5),
  (1398212, 2, 3),
  (1399019, 1, 3),
  (1401033, 5, 2),
  (1405539, 1, 7),
  (1410056, 5, 6),
  (1411464, 4, 7),
  (1413262, 4, 7),
  (1413600, 6, 7),
  (1415720, 3, 6),
  (1417639, 5, 5),
  (1421437, 4, 2),
  (1422680, 5, 6),
  (1425111, 1, 4),
  (1427782, 2, 7),
  (1427802, 6, 4),
  (1428685, 2, 3),
  (1428876, 7, 7),
  (1429503, 5, 3),
  (1434072, 7, 4),
  (1434640, 3, 4),
  (1437248, 0, 0),
  (1437553, 2, 3),
  (1437940, 4, 3),
  (1441231, 2, 7),
  (1447301, 3, 2),
  (1456345, 5, 7),
  (1456378, 7, 7),
  (1456698, 3, 7),
  (1456998, 3, 4),
  (1459266, 0, 6),
  (1466534, 0, 7),
  (1466898, 7, 3),
  (1468398, 7, 7),
  (1468713, 1, 0),
  (1474823, 3, 5),
  (1475873, 2, 2),
  (1476343, 3, 3),
  (1477026, 4, 2),
  (1478334, 2, 0),
  (1480013, 6, 0),
  (1480177, 4, 3),
  (1483937, 0, 7),
  (1485975, 4, 2),
  (1487925, 6, 0),
  (1489246, 0, 0),
  (1489512, 0, 0),
  (1490789, 7, 7),
  (1494986, 1, 4),
  (1500242, 7, 3),
  (1502130, 0, 7),
  (1506546, 6, 5),
  (1507435, 3, 6),
  (1513322, 1, 6),
  (1513548, 0, 0),
  (1515272, 3, 7),
  (1515833, 1, 0),
  (1518183, 5, 2),
  (1523170, 1, 4),
  (1524529, 3, 5),
  (1530590, 0, 7),
  (1538544, 6, 0),
  (1540535, 5, 3),
  (1543534, 0, 3),
  (1544583, 3, 7),
  (1547062, 6, 7),
  (1547819, 4, 2),
  (1548421, 3, 2),
  (1549289, 2, 7),
  (1550500, 6, 4),
  (1551704, 6, 7),
  (1552307, 4, 7),
  (1552804, 0, 4),
  (1559082, 7, 7),
  (1559413, 1, 7),
  (1559536, 7, 1),
  (1559771, 1, 6),
  (1561663, 4, 6),
  (1562331, 5, 6),
  (1563166, 6, 3),
  (1563406, 3, 3),
  (1563726, 1, 4),
  (1565106, 4, 7),
  (1566765, 0, 4),
  (1567986, 6, 3),
  (1572675, 1, 7),
  (1572854, 3, 7),
  (1573400, 0, 3),
  (1574369, 5, 3),
  (1577605, 3, 2),
  (1577615, 6, 7),
  (1578150, 2, 7),
  (1585487, 1, 7),
  (1587510, 7, 6),
  (1593272, 7, 2),
  (1595565, 3, 3),
  (1596357, 5, 6),
  (1596709, 4, 0),
  (1599625, 6, 6),
  (1601281, 3, 3),
  (1602864, 6, 7),
  (1603584, 2, 3),
  (1604687, 5, 7),
  (1605479, 3, 3),
  (1608565, 4, 7),
  (1609751, 0, 4),
  (1610449, 0, 0),
  (1617837, 2, 7),
  (1619562, 7, 2),
  (1619584, 0, 7),
  (1619753, 2, 6),
  (1624678, 7, 0),
  (1625116, 7, 4),
  (1629344, 3, 3),
  (1636217, 5, 2),
  (1640108, 1, 6),
  (1646837, 6, 4),
  (1648577, 5, 3),
  (1655686, 1, 0),
  (1656787, 2, 7),
  (1657084, 5, 3),
  (1660028, 7, 2),
  (1661921, 1, 4),
  (1663839, 0, 0),
  (1664041, 7, 0),
  (1671425, 6, 5),
  (1674728, 5, 2),
  (1677387, 5, 0),
  (1677801, 0, 4),
  (1678355, 7, 6),
  (1680107, 4, 6),
  (1683755, 0, 0),
  (1687958, 0, 7),
  (1688592, 4, 2),
  (1689964, 0, 5),
  (1690467, 3, 7),
  (1691096, 3, 7),
  (1691352, 5, 3),
  (1691756, 6, 2),
  (1692806, 2, 3),
  (1693743, 5, 6),
  (1695119, 6, 0),
  (1701722, 6, 7),
  (1704526, 1, 0),
  (1705540, 1, 0),
  (1706358, 5, 7),
  (1712010, 2, 4),
  (1714682, 3, 7),
  (1716710, 5, 7),
  (1717812, 4, 2),
  (1718211, 0, 4),
  (1718968, 4, 7),
  (1719069, 4, 6),
  (1721121, 7, 3),
  (1722282, 1, 7),
  (1724240, 3, 7),
  (1727221, 7, 4),
  (1727356, 4, 3),
  (1727517, 2, 3),
  (1727963, 7, 4),
  (1728105, 0, 6),
  (1728135, 5, 7),
  (1728886, 2, 3),
  (1729270, 5, 5),
  (1730151, 1, 4),
  (1731149, 4, 6),
  (1732607, 1, 4),
  (1733649, 2, 5),
  (1733777, 3, 7),
  (1742607, 7, 0),
  (1743747, 2, 5),
  (1744223, 3, 1),
  (1749158, 1, 4),
  (1750666, 3, 7),
  (1752607, 2, 3),
  (1752711, 4, 4),
  (1761578, 0, 0),
  (1764423, 2, 2),
  (1766135, 3, 0),
  (1767488, 3, 3),
  (1767530, 6, 7),
  (1768070, 4, 4),
  (1769858, 1, 0),
  (1770464, 0, 7),
  (1771437, 5, 7),
  (1773297, 2, 7),
  (1775638, 2, 7),
  (1778197, 4, 5),
  (1781133, 0, 7),
  (1781502, 7, 6),
  (1784262, 2, 7),
  (1785004, 0, 3),
  (1786875, 5, 7),
  (1788256, 4, 2),
  (1789279, 3, 7),
  (1793140, 1, 6),
  (1793271, 5, 6),
  (1794852, 7, 0),
  (1796893, 1, 4),
  (1797486, 3, 2),
  (1800904, 3, 7),
  (1801389, 2, 3),
  (1803854, 0, 4),
  (1809394, 4, 7),
  (1813268, 5, 1),
  (1813654, 3, 7),
  (1817066, 2, 6),
  (1818260, 3, 3),
  (1818946, 0, 7),
  (1819367, 2, 2),
  (1819600, 3, 3),
  (1819613, 0, 7),
  (1822617, 5, 2),
  (1824425, 2, 3),
  (1826747, 3, 3),
  (1828751, 4, 7),
  (1832514, 2, 7),
  (1833072, 6, 5),
  (1833749, 4, 6),
  (1834100, 3, 2),
  (1834606, 0, 3),
  (1834840, 0, 4),
  (1836634, 3, 6),
  (1841091, 1, 0),
  (1842475, 4, 3),
  (1844432, 5, 3),
  (1845403, 5, 3),
  (1846397, 7, 3),
  (1847320, 6, 7),
  (1847535, 3, 7),
  (1849662, 5, 3),
  (1851393, 7, 7),
  (1854806, 2, 2),
  (1860337, 4, 7),
  (1862909, 1, 0),
  (1863337, 2, 4),
  (1868747, 0, 0),
  (1870179, 3, 1),
  (1870771, 1, 3),
  (1873508, 5, 3),
  (1881571, 4, 3),
  (1882880, 7, 5),
  (1884601, 3, 7),
  (1886504, 6, 7),
  (1887133, 1, 2),
  (1898729, 2, 7),
  (1901115, 1, 7),
  (1902579, 0, 4),
  (1902713, 2, 3),
  (1904196, 1, 7),
  (1907145, 5, 3),
  (1913797, 5, 2),
  (1914832, 7, 7),
  (1915277, 4, 3),
  (1915467, 4, 3),
  (1919869, 5, 6),
  (1919870, 1, 4),
  (1920956, 3, 7),
  (1923575, 1, 7),
  (1926124, 4, 6),
  (1928454, 1, 6),
  (1930393, 1, 7),
  (1930409, 4, 3),
  (1933252, 6, 0),
  (1933754, 1, 4),
  (1937119, 6, 7),
  (1946694, 7, 2),
  (1951867, 7, 7),
  (1952464, 4, 4),
  (1952654, 7, 0),
  (1955729, 5, 7),
  (1956934, 0, 6),
  (1961616, 7, 6),
  (1962912, 4, 6),
  (1964413, 6, 7),
  (1966196, 2, 2),
  (1966707, 0, 0),
  (1967948, 7, 7),
  (1971563, 1, 0),
  (1972104, 7, 0),
  (1975604, 0, 0),
  (1976090, 7, 1),
  (1976521, 2, 3),
  (1977420, 4, 2),
  (1977822, 3, 3),
  (1977937, 7, 0),
  (1986058, 0, 0),
  (1987675, 4, 3),
  (1990020, 0, 3),
  (1991091, 4, 0),
  (1991822, 6, 4),
  (1993460, 6, 0),
  (1993490, 3, 3),
  (1994041, 2, 7),
  (1996939, 1, 7),
  (1998822, 1, 0),
  (1999627, 3, 6),
  (2001110, 5, 7),
  (2004107, 5, 3),
  (2004628, 1, 0),
  (2004745, 5, 2),
  (2007158, 1, 0),
  (2008258, 3, 7),
  (2010498, 6, 7),
  (2013342, 6, 0),
  (2014474, 7, 3),
  (2016478, 3, 6),
  (2018091, 0, 2),
  (2018900, 7, 7),
  (2019218, 6, 7),
  (2020218, 0, 7),
  (2023239, 1, 7),
  (2024240, 0, 7),
  (2024571, 1, 3),
  (2027296, 5, 2),
  (2029828, 3, 6),
  (2030713, 4, 2),
  (2031550, 1, 0),
  (2033056, 4, 5),
  (2035571, 5, 3),
  (2035914, 4, 7),
  (2035950, 2, 3),
  (2039435, 1, 7),
  (2043234, 4, 5),
  (2043299, 7, 4),
  (2043479, 5, 7),
  (2045219, 3, 3),
  (2046358, 2, 3),
  (2047159, 6, 5),
  (2047813, 5, 7),
  (2047966, 1, 6),
  (2048381, 7, 7),
  (2050335, 1, 0),
  (2051066, 1, 0),
  (2054688, 5, 3),
  (2055588, 3, 3),
  (2056133, 2, 3),
  (2057555, 2, 6),
  (2057769, 3, 4),
  (2058419, 1, 0),
  (2062027, 2, 0),
  (2062273, 3, 7),
  (2062619, 0, 7),
  (2065964, 0, 7),
  (2066681, 1, 3),
  (2067193, 5, 7),
  (2071346, 5, 0),
  (2073062, 6, 3),
  (2076142, 4, 7),
  (2079482, 7, 0),
  (2085255, 0, 0),
  (2086896, 4, 3),
  (2087524, 4, 3),
  (2092321, 1, 0),
  (2093792, 5, 3),
  (2094481, 0, 2),
  (2094788, 6, 7),
  (2095403, 5, 3),
  (2095438, 1, 3),
  (2095445, 1, 7),
  (2104206, 1, 3),
  (2106702, 0, 7),
  (2108080, 4, 1),
  (2111251, 0, 3),
  (2117792, 2, 6),
  (2117897, 7, 7),
  (2122779, 3, 0),
  (2125335, 6, 0),
  (2127249, 1, 0),
  (2130632, 0, 7),
  (2131999, 2, 1),
  (2134496, 2, 2),
  (2144170, 5, 3),
  (2144909, 0, 3),
  (2149084, 6, 7),
  (2152808, 3, 7),
  (2154712, 2, 1),
  (2155108, 0, 0),
  (2157448, 0, 3),
  (2159369, 0, 4),
  (2159434, 2, 7),
  (2161568, 1, 7),
  (2161823, 3, 3),
  (2166500, 7, 5),
  (2172147, 7, 0),
  (2173047, 5, 1),
  (2179269, 5, 3),
  (2180719, 1, 3),
  (2185024, 4, 3),
  (2185975, 0, 7),
  (2186008, 2, 7),
  (2186780, 3, 1),
  (2187549, 2, 7),
  (2188325, 1, 0),
  (2188448, 6, 2),
  (2189315, 7, 4),
  (2193210, 3, 5),
  (2199576, 4, 3),
  (2201760, 5, 7),
  (2202310, 4, 7),
  (2205001, 1, 7),
  (2206137, 1, 7),
  (2210294, 5, 7),
  (2211101, 4, 3),
  (2214158, 2, 3),
  (2214777, 4, 1),
  (2215306, 5, 7),
  (2221026, 1, 2),
  (2222758, 7, 0),
  (2223279, 3, 3),
  (2224727, 2, 3),
  (2225872, 7, 7),
  (2227994, 7, 7),
  (2230578, 2, 7),
  (2231257, 4, 7),
  (2232206, 0, 3),
  (2241419, 0, 3),
  (2246896, 7, 0),
  (2247620, 2, 7),
  (2248714, 0, 7),
  (2248832, 5, 3),
  (2250220, 5, 1),
  (2250560, 5, 7),
  (2257073, 6, 0),
  (2257735, 0, 3),
  (2259777, 3, 3),
  (2261079, 5, 4),
  (2261350, 1, 7),
  (2264193, 1, 5),
  (2268631, 6, 0),
  (2269588, 6, 3),
  (2269786, 1, 7),
  (2270435, 7, 6),
  (2276660, 3, 3),
  (2281240, 1, 0),
  (2282848, 2, 5),
  (2283616, 3, 7),
  (2284131, 4, 2),
  (2284346, 3, 5),
  (2287650, 2, 3),
  (2288500, 3, 6),
  (2288726, 6, 0),
  (2289304, 5, 2),
  (2298163, 3, 2),
  (2298478, 3, 3),
  (2300580, 0, 3),
  (2301426, 2, 3),
  (2301840, 2, 2),
  (2307974, 1, 7),
  (2311571, 7, 6),
  (2312330, 1, 4),
  (2313213, 1, 7),
  (2317995, 5, 6),
  (2320994, 6, 7),
  (2321365, 2, 2),
  (2322199, 5, 4),
  (2325088, 1, 7),
  (2332051, 7, 0),
  (2341621, 3, 3),
  (2344792, 7, 4),
  (2347045, 4, 7),
  (2350012, 7, 7),
  (2354689, 0, 0),
  (2355453, 5, 3),
  (2357445, 6, 6),
  (2361230, 2, 0),
  (2362403, 4, 7),
  (2366114, 1, 7),
  (2366171, 6, 7),
  (2367437, 5, 3),
  (2372160, 0, 0),
  (2373390, 6, 6),
  (2373485, 5, 3),
  (2375014, 0, 0),
  (2376561, 5, 2),
  (2376709, 4, 2),
  (2379210, 5, 6),
  (2379918, 7, 7),
  (2384136, 6, 7),
  (2385430, 3, 3),
  (2389476, 0, 7),
  (2389558, 7, 0),
  (2392016, 7, 3),
  (2395136, 6, 7),
  (2396297, 7, 3),
  (2397137, 3, 6),
  (2397443, 6, 0),
  (2400230, 0, 7),
  (2402342, 7, 0),
  (2403265, 4, 6),
  (2404075, 2, 7),
  (2407402, 2, 6),
  (2407721, 0, 4),
  (2408858, 1, 7),
  (2414212, 3, 7),
  (2418614, 3, 3),
  (2422137, 4, 7),
  (2431100, 2, 7),
  (2442918, 5, 7),
  (2447436, 2, 2),
  (2448676, 1, 1),
  (2449982, 3, 2),
  (2452909, 4, 1),
  (2453395, 4, 5),
  (2457125, 6, 4),
  (2458648, 6, 0),
  (2459841, 2, 3),
  (2461083, 5, 2),
  (2461348, 2, 3),
  (2462713, 4, 6),
  (2465214, 6, 6),
  (2466791, 5, 3),
  (2467560, 0, 0),
  (2467883, 5, 3),
  (2472585, 2, 6),
  (2473716, 3, 2),
  (2475437, 5, 5),
  (2477066, 1, 0),
  (2478179, 5, 7),
  (2481360, 6, 3),
  (2481937, 4, 4),
  (2483062, 7, 3),
  (2484149, 6, 0),
  (2487994, 5, 2),
  (2490211, 5, 3),
  (2491985, 0, 4),
  (2493093, 7, 4),
  (2495469, 3, 7),
  (2497426, 7, 4),
  (2498318, 4, 7),
  (2499113, 5, 2),
  (2502741, 4, 6),
  (2504960, 7, 7),
  (2508298, 4, 7),
  (2509187, 4, 7),
  (2509875, 6, 7),
  (2511530, 3, 5),
  (2511692, 6, 0),
  (2514651, 7, 4),
  (2515103, 0, 7),
  (2515267, 3, 3),
  (2517496, 0, 0),
  (2518887, 6, 5),
  (2519534, 5, 3),
  (2519798, 6, 7),
  (2519875, 4, 3),
  (2521062, 4, 2),
  (2522777, 7, 0),
  (2523003, 3, 7),
  (2527688, 0, 7),
  (2528442, 7, 7),
  (2528537, 1, 3),
  (2529061, 4, 6),
  (2532692, 6, 0),
  (2534569, 2, 5),
  (2536579, 0, 3),
  (2537261, 7, 0),
  (2542185, 4, 3),
  (2543685, 0, 7),
  (2544653, 2, 5),
  (2547756, 1, 5),
  (2549082, 3, 5),
  (2550240, 3, 3),
  (2550462, 6, 0),
  (2552544, 7, 7),
  (2554009, 2, 6),
  (2554468, 7, 0),
  (2557117, 2, 7),
  (2557330, 4, 3),
  (2561315, 7, 0),
  (2562071, 0, 4),
  (2562083, 1, 3),
  (2567032, 3, 3),
  (2570172, 6, 3),
  (2570917, 0, 3),
  (2571896, 0, 7),
  (2572198, 3, 3),
  (2572419, 1, 7),
  (2573376, 1, 6),
  (2575270, 4, 3),
  (2578973, 2, 3),
  (2580874, 4, 7),
  (2586868, 0, 4),
  (2589627, 2, 7),
  (2590226, 6, 6),
  (2594189, 3, 5),
  (2596297, 6, 4),
  (2597617, 1, 7),
  (2601126, 0, 1),
  (2604597, 4, 2),
  (2605631, 4, 2),
  (2605643, 5, 6),
  (2606685, 3, 0),
  (2608991, 5, 5),
  (2612403, 0, 7),
  (2613683, 4, 7),
  (2616013, 2, 5),
  (2623296, 1, 3),
  (2624702, 4, 3),
  (2625330, 0, 0),
  (2639952, 3, 7),
  (2642791, 3, 3),
  (2643155, 7, 0),
  (2643529, 1, 3),
  (2644841, 0, 3),
  (2648451, 2, 7),
  (2651112, 2, 3),
  (2655114, 1, 3),
  (2657570, 5, 3),
  (2660808, 5, 6),
  (2662459, 1, 0),
  (2663645, 4, 3),
  (2664591, 4, 2),
  (2665174, 1, 7),
  (2665870, 1, 0),
  (2666754, 6, 4),
  (2671575, 3, 5),
  (2675279, 7, 0),
  (2676449, 6, 7),
  (2676555, 4, 3),
  (2677445, 1, 7),
  (2677629, 5, 3),
  (2678587, 6, 0),
  (2680740, 3, 5),
  (2682354, 3, 1),
  (2685405, 4, 5),
  (2685431, 0, 3),
  (2687414, 7, 0),
  (2689949, 5, 6),
  (2691431, 1, 0),
  (2692391, 5, 5),
  (2693201, 0, 6),
  (2694757, 6, 6),
  (2697550, 7, 4),
  (2697801, 1, 7),
  (2697940, 4, 7),
  (2698677, 0, 0),
  (2699917, 6, 0),
  (2705386, 1, 2),
  (2706413, 5, 3),
  (2707119, 2, 2),
  (2707451, 4, 7),
  (2708288, 2, 3),
  (2709293, 2, 3),
  (2713470, 1, 0),
  (2718004, 4, 7),
  (2718957, 1, 7),
  (2720269, 3, 6),
  (2721040, 3, 6),
  (2724894, 2, 4),
  (2725602, 7, 2),
  (2727138, 1, 6),
  (2727566, 2, 6),
  (2729358, 1, 5),
  (2729949, 5, 7),
  (2730513, 0, 4),
  (2731241, 7, 4),
  (2731422, 2, 4),
  (2736194, 6, 7),
  (2737894, 2, 3),
  (2740582, 7, 7),
  (2742323, 3, 3),
  (2743497, 6, 4),
  (2744147, 2, 2),
  (2747716, 6, 0),
  (2748700, 2, 6),
  (2749347, 6, 7),
  (2750736, 3, 6),
  (2753807, 5, 7),
  (2754281, 5, 4),
  (2754402, 7, 7),
  (2757676, 6, 4),
  (2758145, 3, 7),
  (2764720, 6, 7),
  (2765589, 0, 0),
  (2769273, 0, 6),
  (2769807, 6, 0),
  (2771595, 0, 4),
  (2773210, 0, 3),
  (2776350, 4, 3),
  (2777789, 3, 1),
  (2782418, 3, 0),
  (2785334, 3, 3),
  (2788305, 7, 0),
  (2788316, 4, 7),
  (2788423, 6, 7),
  (2797487, 3, 3),
  (2798233, 6, 0),
  (2800326, 2, 3),
  (2800624, 2, 7),
  (2800776, 7, 0),
  (2805020, 3, 3),
  (2806421, 7, 0),
  (2807198, 3, 3),
  (2807906, 6, 7),
  (2809986, 5, 3),
  (2810477, 2, 7),
  (2811149, 0, 0),
  (2811202, 3, 3),
  (2811231, 0, 3),
  (2813655, 0, 0),
  (2814936, 0, 6),
  (2815641, 2, 2),
  (2816089, 3, 2),
  (2819036, 5, 2),
  (2819689, 3, 3),
  (2820765, 0, 0),
  (2824081, 4, 3),
  (2825420, 0, 0),
  (2826832, 7, 7),
  (2829283, 5, 4),
  (2830012, 6, 4),
  (2830961, 5, 3),
  (2831716, 0, 0),
  (2837923, 7, 3),
  (2837946, 0, 0),
  (2840519, 3, 3),
  (2841407, 0, 3),
  (2843882, 0, 3),
  (2847581, 0, 4),
  (2849977, 1, 5),
  (2853383, 4, 4),
  (2854572, 1, 0),
  (2857169, 4, 7),
  (2868860, 6, 0),
  (2870529, 6, 0),
  (2872501, 7, 3),
  (2874176, 1, 4),
  (2876920, 7, 0),
  (2878876, 7, 3),
  (2881877, 7, 0),
  (2887820, 5, 3),
  (2890326, 3, 7),
  (2890443, 6, 4),
  (2895157, 7, 6),
  (2899921, 0, 3),
  (2900072, 2, 3),
  (2900579, 1, 7),
  (2901875, 0, 0),
  (2902064, 3, 4),
  (2902799, 5, 2),
  (2908103, 7, 7),
  (2908557, 0, 3),
  (2908927, 6, 3),
  (2909476, 4, 5),
  (2911125, 3, 2),
  (2913115, 1, 7),
  (2914306, 3, 7),
  (2916864, 4, 6),
  (2917829, 1, 3),
  (2917897, 6, 7),
  (2918486, 0, 1),
  (2919417, 5, 6),
  (2920034, 3, 2),
  (2920485, 7, 5),
  (2921187, 5, 3),
  (2922980, 2, 4),
  (2927980, 6, 6),
  (2929879, 1, 4),
  (2930874, 6, 3),
  (2932101, 4, 6),
  (2932828, 2, 7),
  (2936563, 3, 3),
  (2936988, 3, 2),
  (2943185, 2, 7),
  (2943227, 7, 4),
  (2943867, 7, 4),
  (2943907, 2, 7),
  (2944606, 4, 2),
  (2946528, 5, 7),
  (2948039, 0, 4),
  (2949681, 7, 0),
  (2949921, 4, 0),
  (2950294, 6, 0),
  (2954069, 4, 6),
  (2956835, 1, 7),
  (2958038, 4, 2),
  (2960573, 6, 7),
  (2962250, 7, 7),
  (2962712, 3, 3),
  (2962981, 6, 7),
  (2963283, 4, 2),
  (2964525, 5, 1),
  (2969521, 3, 5),
  (2971487, 2, 6),
  (2971723, 6, 4),
  (2972216, 1, 0),
  (2972259, 3, 5),
  (2974493, 1, 4),
  (2974777, 7, 4),
  (2979345, 3, 3),
  (2983625, 3, 7),
  (2983951, 6, 0),
  (2984862, 7, 7),
  (2989406, 3, 7),
  (2992706, 3, 6),
  (2996044, 4, 7),
  (2996969, 7, 0),
  (2997005, 4, 7),
  (3000365, 7, 0),
  (3002056, 4, 6),
  (3002071, 1, 1),
  (3002374, 1, 0),
  (3011477, 0, 7),
  (3012287, 4, 7),
  (3016226, 6, 7),
  (3023536, 6, 1),
  (3024106, 5, 6),
  (3025532, 7, 0),
  (3025677, 5, 7),
  (3032229, 5, 4),
  (3032269, 7, 0),
  (3037269, 4, 3),
  (3037343, 3, 7),
  (3038641, 2, 4),
  (3040846, 3, 7),
  (3041613, 5, 7),
  (3042386, 0, 6),
  (3049846, 3, 6),
  (3050815, 0, 2),
  (3051755, 2, 3),
  (3052451, 3, 2),
  (3053891, 1, 3),
  (3055825, 0, 3),
  (3055963, 2, 7),
  (3056061, 6, 7),
  (3060822, 0, 1),
  (3066932, 0, 4),
  (3067807, 6, 7),
  (3072082, 0, 6),
  (3072749, 1, 7),
  (3074024, 0, 0),
  (3074261, 4, 3),
  (3080348, 4, 1),
  (3083548, 4, 3),
  (3084060, 0, 6),
  (3087710, 7, 0),
  (3088681, 6, 3),
  (3090753, 5, 3),
  (3093670, 3, 3),
  (3096217, 0, 0),
  (3098980, 1, 7),
  (3103781, 4, 4),
  (3107365, 6, 7),
  (3110929, 3, 6),
  (3112992, 7, 7),
  (3115300, 1, 3),
  (3115543, 3, 6),
  (3116729, 1, 0),
  (3119462, 1, 4),
  (3121247, 6, 3),
  (3122325, 0, 7),
  (3127718, 7, 7),
  (3127907, 5, 3),
  (3128521, 4, 7),
  (3138721, 0, 6),
  (3139020, 3, 6),
  (3140172, 7, 0),
  (3140236, 3, 2),
  (3141846, 4, 2),
  (3146523, 3, 7),
  (3150346, 4, 3),
  (3152602, 3, 7),
  (3154705, 5, 6),
  (3157234, 0, 0),
  (3158479, 2, 6),
  (3159309, 2, 3),
  (3160734, 4, 3),
  (3162203, 0, 4),
  (3165419, 5, 7),
  (3167259, 0, 7),
  (3172665, 4, 2),
  (3175238, 7, 0),
  (3175736, 1, 0),
  (3177118, 2, 3),
  (3177441, 6, 7),
  (3180266, 2, 3),
  (3181773, 1, 4),
  (3182496, 7, 3),
  (3185703, 7, 7),
  (3186382, 2, 2),
  (3190399, 2, 7),
  (3193709, 4, 7),
  (3195585, 7, 1),
  (3195838, 7, 5),
  (3197558, 5, 6),
  (3197969, 3, 3),
  (3201659, 6, 7),
  (3207627, 4, 0),
  (3207761, 6, 0),
  (3210144, 3, 3),
  (3212124, 2, 4),
  (3216672, 2, 7),
  (3218422, 7, 4),
  (3218592, 1, 3),
  (3226710, 3, 7),
  (3227443, 7, 7),
  (3230791, 3, 3),
  (3234176, 0, 3),
  (3239810, 4, 7),
  (3241889, 7, 4),
  (3245350, 4, 7),
  (3246001, 7, 7),
  (3246553, 0, 0),
  (3246679, 2, 6),
  (3249235, 4, 5),
  (3249911, 3, 3),
  (3250871, 4, 3),
  (3251046, 0, 7),
  (3252310, 6, 0),
  (3252709, 3, 3),
  (3255074, 2, 7),
  (3256658, 1, 7),
  (3257838, 6, 7),
  (3261160, 2, 3),
  (3261738, 7, 7),
  (3263786, 0, 7),
  (3264612, 7, 3),
  (3268178, 1, 7),
  (3268610, 2, 6),
  (3269919, 3, 7),
  (3272582, 2, 7),
  (3277619, 3, 2),
  (3280858, 2, 6),
  (3282880, 7, 7),
  (3285012, 3, 7),
  (3286611, 2, 7),
  (3288137, 7, 2),
  (3289482, 7, 4),
  (3291250, 0, 7),
  (3291905, 7, 3),
  (3292583, 2, 7),
  (3292923, 7, 7),
  (3294645, 6, 0),
  (3298747, 0, 4),
  (3300739, 6, 3),
  (3302770, 7, 7),
  (3306300, 0, 6),
  (3306356, 4, 2),
  (3309397, 5, 7),
  (3312258, 6, 4),
  (3319162, 2, 7),
  (3321584, 6, 7),
  (3322028, 5, 6),
  (3325041, 3, 6),
  (3325828, 1, 0),
  (3326433, 4, 7),
  (3326522, 5, 7),
  (3327577, 2, 7),
  (3328528, 3, 2),
  (3329611, 3, 7),
  (3330565, 1, 7),
  (3333582, 2, 6),
  (3334098, 0, 0),
  (3338639, 0, 4),
  (3339127, 1, 0),
  (3339665, 1, 7),
  (3341698, 4, 6),
  (3342330, 3, 3),
  (3342394, 7, 4),
  (3342566, 5, 7),
  (3343131, 5, 4),
  (3343987, 5, 3),
  (3345110, 4, 2),
  (3347655, 7, 5),
  (3348273, 5, 3),
  (3354640, 4, 4),
  (3357516, 1, 4),
  (3359795, 2, 0),
  (3360800, 7, 4),
  (3363558, 4, 5),
  (3368155, 0, 4),
  (3369045, 2, 6),
  (3369917, 4, 7),
  (3370543, 2, 2),
  (3378017, 4, 3),
  (3379517, 0, 4),
  (3380931, 1, 7),
  (3384860, 3, 2),
  (3385289, 2, 3),
  (3390884, 1, 0),
  (3392252, 6, 4),
  (3394091, 0, 3),
  (3398563, 3, 7),
  (3400509, 4, 6),
  (3401666, 0, 0),
  (3404016, 7, 6),
  (3405817, 4, 7),
  (3411215, 0, 7),
  (3414960, 7, 0),
  (3417262, 0, 4),
  (3418214, 0, 0),
  (3424917, 6, 0),
  (3425563, 5, 3),
  (3425796, 1, 3),
  (3426912, 1, 0),
  (3432076, 3, 7),
  (3432378, 6, 7),
  (3433578, 6, 7),
  (3434898, 4, 7),
  (3436500, 7, 7),
  (3437424, 7, 7),
  (3441344, 4, 6),
  (3442345, 2, 7),
  (3443119, 2, 6),
  (3446085, 3, 7),
  (3448141, 3, 3),
  (3448369, 2, 7),
  (3449013, 2, 3),
  (3449690, 4, 3),
  (3461442, 0, 0),
  (3461525, 0, 0),
  (3461872, 3, 3),
  (3462618, 1, 3),
  (3463377, 1, 7),
  (3463447, 2, 5),
  (3464692, 3, 3),
  (3467704, 3, 7),
  (3469883, 7, 0),
  (3472151, 2, 7),
  (3472246, 2, 5),
  (3473252, 7, 4),
  (3473982, 3, 3),
  (3474368, 2, 6),
  (3478690, 1, 7),
  (3480669, 3, 3),
  (3483300, 6, 0),
  (3486863, 3, 7),
  (3489153, 1, 7),
  (3491067, 1, 0),
  (3493237, 5, 3),
  (3495358, 5, 4),
  (3495780, 3, 6),
  (3496077, 0, 3),
  (3500734, 6, 4),
  (3501349, 2, 6),
  (3503234, 1, 3),
  (3503632, 5, 6),
  (3503696, 0, 2),
  (3506787, 3, 2),
  (3507523, 3, 7),
  (3509440, 0, 0),
  (3509454, 2, 7),
  (3512336, 6, 0),
  (3513468, 5, 4),
  (3513836, 6, 4),
  (3514341, 7, 1),
  (3514674, 2, 3),
  (3515825, 5, 7),
  (3516167, 5, 3),
  (3520097, 2, 2),
  (3521103, 0, 0),
  (3521633, 2, 3),
  (3521915, 4, 7),
  (3523476, 2, 3),
  (3523677, 0, 6),
  (3529623, 0, 3),
  (3529637, 0, 0),
  (3530743, 2, 0),
  (3532087, 6, 3),
  (3533341, 0, 3),
  (3536838, 4, 7),
  (3537891, 4, 6),
  (3538417, 1, 6),
  (3539310, 6, 0),
  (3540187, 6, 6),
  (3544166, 1, 6),
  (3544337, 7, 7),
  (3548741, 4, 6),
  (3550867, 0, 4),
  (3553386, 5, 7),
  (3554094, 4, 2),
  (3554258, 5, 3),
  (3554937, 7, 0),
  (3559522, 2, 7),
  (3560795, 7, 7),
  (3561556, 2, 0),
  (3562581, 7, 6),
  (3564228, 0, 3),
  (3565053, 7, 4),
  (3569410, 1, 7),
  (3569839, 0, 7),
  (3572300, 6, 7),
  (3574702, 3, 6),
  (3575498, 3, 5),
  (3576451, 0, 0),
  (3581986, 4, 7),
  (3587754, 5, 5),
  (3594752, 4, 3),
  (3598615, 7, 7),
])