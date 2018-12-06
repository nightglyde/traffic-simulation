from src.util import *
schedule = deque([
  (2235, 0, 4),
  (3665, 0, 5),
  (3691, 5, 3),
  (4267, 1, 0),
  (6037, 0, 0),
  (15399, 5, 3),
  (17933, 0, 3),
  (21427, 6, 0),
  (24198, 6, 7),
  (24424, 3, 3),
  (26325, 7, 0),
  (28338, 7, 0),
  (29846, 4, 7),
  (30889, 4, 5),
  (31635, 7, 4),
  (32394, 5, 7),
  (35261, 5, 3),
  (35671, 2, 3),
  (39912, 5, 3),
  (40650, 6, 5),
  (42096, 3, 7),
  (43573, 5, 6),
  (47308, 0, 0),
  (53048, 7, 4),
  (54390, 7, 0),
  (54864, 3, 5),
  (54878, 6, 0),
  (56028, 7, 2),
  (57338, 2, 3),
  (57659, 2, 3),
  (59931, 7, 0),
  (60887, 2, 5),
  (62641, 0, 7),
  (64943, 1, 0),
  (66268, 3, 4),
  (66556, 0, 4),
  (69853, 1, 0),
  (71847, 7, 4),
  (72377, 4, 2),
  (72680, 4, 3),
  (72699, 3, 3),
  (73553, 3, 3),
  (74584, 0, 3),
  (76606, 1, 0),
  (80007, 1, 4),
  (80385, 7, 2),
  (80586, 0, 0),
  (80694, 7, 0),
  (83378, 0, 3),
  (86108, 7, 2),
  (91080, 1, 6),
  (93400, 1, 4),
  (96185, 3, 3),
  (97187, 2, 5),
  (98207, 2, 7),
  (98377, 4, 2),
  (99439, 0, 4),
  (100664, 1, 7),
  (102251, 6, 0),
  (102746, 7, 0),
  (107441, 7, 0),
  (109003, 2, 3),
  (113520, 7, 0),
  (113814, 2, 3),
  (115045, 6, 0),
  (115466, 6, 7),
  (116415, 2, 2),
  (123572, 2, 3),
  (124149, 6, 5),
  (126009, 0, 0),
  (128043, 3, 3),
  (128870, 2, 3),
  (131002, 4, 3),
  (131828, 3, 0),
  (132935, 0, 0),
  (133592, 2, 2),
  (135861, 4, 0),
  (136162, 3, 3),
  (141398, 0, 4),
  (142872, 0, 0),
  (144844, 7, 0),
  (148557, 3, 1),
  (150587, 3, 2),
  (154385, 0, 7),
  (154464, 6, 7),
  (155468, 3, 7),
  (155714, 4, 3),
  (158153, 2, 2),
  (159116, 2, 3),
  (159213, 6, 0),
  (161886, 5, 6),
  (163796, 5, 3),
  (164748, 0, 5),
  (165044, 7, 0),
  (165790, 2, 7),
  (166956, 2, 3),
  (167100, 3, 3),
  (174145, 3, 7),
  (174938, 1, 7),
  (175705, 5, 2),
  (176666, 1, 1),
  (178701, 6, 3),
  (178845, 6, 7),
  (182067, 6, 0),
  (182735, 5, 6),
  (184476, 2, 3),
  (186596, 7, 4),
  (187573, 4, 3),
  (190672, 7, 0),
  (193531, 3, 3),
  (196521, 6, 5),
  (196956, 5, 1),
  (200498, 7, 0),
  (201127, 0, 5),
  (201901, 5, 6),
  (202625, 1, 5),
  (202877, 0, 0),
  (210373, 3, 3),
  (212033, 6, 0),
  (213248, 4, 3),
  (215685, 7, 5),
  (215801, 2, 7),
  (216314, 1, 3),
  (218354, 4, 1),
  (219037, 6, 1),
  (221729, 0, 3),
  (221801, 0, 1),
  (221838, 6, 3),
  (221911, 4, 2),
  (222314, 0, 5),
  (228065, 4, 7),
  (231471, 2, 3),
  (231787, 4, 3),
  (237892, 1, 0),
  (238569, 2, 7),
  (238928, 4, 3),
  (239423, 6, 4),
  (239852, 0, 0),
  (240227, 3, 1),
  (240961, 6, 0),
  (242693, 6, 0),
  (243854, 0, 0),
  (245740, 1, 4),
  (247276, 1, 0),
  (250666, 1, 4),
  (261717, 0, 0),
  (264029, 7, 1),
  (264300, 3, 3),
  (266695, 1, 3),
  (268927, 1, 3),
  (272913, 6, 1),
  (273789, 6, 0),
  (274062, 4, 3),
  (274648, 5, 3),
  (281964, 7, 0),
  (283021, 1, 1),
  (285468, 3, 3),
  (298223, 2, 3),
  (299364, 2, 2),
  (299656, 5, 3),
  (306488, 7, 1),
  (306727, 5, 0),
  (308213, 3, 6),
  (312659, 6, 0),
  (313507, 1, 0),
  (314357, 1, 0),
  (320046, 1, 1),
  (320221, 2, 3),
  (323191, 1, 3),
  (324114, 3, 0),
  (325562, 4, 7),
  (326822, 0, 0),
  (329487, 5, 3),
  (329815, 3, 1),
  (333063, 7, 0),
  (335746, 4, 2),
  (337749, 0, 4),
  (342771, 3, 1),
  (344247, 6, 0),
  (344863, 5, 3),
  (347026, 1, 0),
  (347766, 6, 0),
  (350969, 5, 3),
  (357428, 2, 7),
  (358672, 3, 3),
  (360316, 1, 0),
  (361708, 0, 4),
  (368813, 1, 0),
  (375351, 7, 7),
  (379561, 1, 0),
  (381559, 5, 3),
  (383118, 7, 0),
  (383691, 5, 6),
  (391477, 4, 2),
  (393485, 7, 0),
  (394223, 0, 6),
  (395155, 2, 3),
  (396150, 5, 4),
  (399870, 1, 4),
  (400129, 4, 7),
  (403806, 7, 1),
  (406986, 1, 0),
  (407435, 3, 7),
  (408853, 7, 0),
  (409975, 7, 6),
  (410015, 7, 3),
  (413399, 7, 0),
  (415622, 7, 0),
  (415830, 3, 7),
  (416520, 5, 2),
  (416934, 3, 3),
  (422389, 2, 3),
  (423159, 4, 7),
  (424757, 1, 6),
  (425814, 4, 0),
  (429296, 4, 7),
  (430005, 5, 3),
  (430976, 5, 2),
  (431124, 4, 3),
  (431343, 2, 3),
  (431471, 7, 0),
  (433236, 6, 0),
  (433528, 1, 3),
  (433969, 3, 7),
  (437901, 4, 3),
  (439837, 1, 4),
  (444751, 6, 7),
  (444819, 5, 3),
  (447102, 3, 6),
  (447665, 1, 3),
  (450006, 1, 2),
  (450996, 5, 3),
  (453686, 6, 0),
  (454854, 5, 3),
  (456846, 4, 3),
  (462312, 4, 3),
  (464803, 6, 6),
  (468116, 1, 2),
  (470930, 4, 7),
  (471199, 0, 4),
  (475513, 5, 0),
  (476104, 1, 4),
  (477033, 2, 2),
  (480699, 5, 2),
  (482793, 0, 6),
  (484661, 2, 7),
  (484779, 2, 7),
  (486131, 1, 5),
  (486162, 0, 0),
  (488344, 7, 4),
  (488776, 7, 4),
  (491372, 3, 5),
  (493768, 7, 7),
  (497416, 4, 6),
  (503964, 4, 3),
  (504477, 0, 1),
  (505980, 6, 2),
  (507415, 5, 1),
  (509217, 6, 0),
  (509525, 3, 3),
  (515846, 2, 4),
  (516759, 1, 0),
  (517861, 6, 0),
  (517910, 4, 1),
  (517992, 1, 0),
  (520362, 3, 3),
  (520710, 2, 0),
  (521621, 3, 3),
  (522602, 0, 4),
  (522818, 4, 3),
  (523205, 6, 0),
  (524288, 7, 1),
  (527916, 4, 3),
  (536035, 6, 3),
  (538700, 3, 3),
  (539642, 5, 7),
  (543131, 3, 5),
  (545259, 7, 4),
  (551249, 0, 0),
  (551281, 7, 1),
  (555741, 1, 0),
  (556649, 0, 0),
  (558862, 7, 7),
  (562873, 5, 1),
  (563267, 6, 0),
  (564965, 2, 0),
  (565824, 0, 0),
  (567265, 5, 0),
  (567435, 6, 4),
  (576125, 5, 6),
  (577582, 4, 6),
  (578037, 3, 6),
  (579678, 5, 6),
  (583008, 1, 4),
  (584086, 4, 7),
  (585618, 0, 0),
  (586983, 1, 0),
  (587130, 6, 5),
  (589655, 7, 0),
  (590418, 5, 6),
  (590812, 1, 3),
  (590927, 7, 4),
  (591429, 5, 7),
  (593913, 5, 1),
  (595761, 1, 7),
  (596325, 1, 2),
  (598555, 2, 3),
  (599241, 3, 7),
  (599817, 2, 7),
  (606896, 3, 0),
  (607049, 6, 7),
  (607516, 0, 7),
  (610741, 3, 2),
  (614681, 6, 7),
  (616304, 2, 2),
  (617422, 7, 0),
  (620387, 2, 7),
  (627433, 6, 0),
  (628082, 3, 4),
  (628180, 2, 3),
  (630435, 2, 3),
  (631100, 1, 0),
  (631230, 3, 3),
  (632272, 2, 7),
  (633076, 6, 3),
  (635168, 3, 2),
  (635424, 1, 0),
  (636258, 6, 0),
  (639726, 0, 4),
  (641427, 6, 0),
  (643931, 5, 3),
  (644118, 5, 7),
  (644265, 5, 5),
  (644742, 5, 7),
  (644947, 2, 7),
  (648045, 4, 1),
  (651017, 1, 0),
  (657496, 6, 6),
  (662571, 1, 4),
  (664638, 3, 7),
  (667578, 6, 4),
  (670559, 0, 7),
  (671108, 0, 2),
  (673411, 6, 7),
  (674703, 7, 3),
  (675317, 7, 0),
  (675465, 4, 6),
  (676697, 3, 3),
  (677005, 2, 3),
  (677091, 6, 7),
  (680761, 3, 3),
  (681565, 3, 2),
  (682030, 6, 3),
  (685118, 4, 3),
  (686197, 7, 0),
  (687200, 2, 3),
  (687919, 7, 0),
  (694398, 5, 5),
  (695816, 7, 0),
  (695850, 5, 5),
  (700509, 7, 3),
  (702684, 6, 0),
  (704260, 6, 0),
  (704758, 2, 3),
  (710877, 0, 4),
  (711130, 0, 0),
  (711514, 3, 3),
  (711993, 5, 3),
  (712393, 7, 7),
  (715243, 0, 0),
  (724422, 5, 3),
  (724690, 6, 7),
  (729539, 4, 1),
  (731037, 3, 3),
  (732598, 0, 0),
  (735695, 2, 1),
  (742378, 6, 0),
  (742714, 0, 0),
  (742749, 6, 5),
  (743147, 3, 6),
  (743224, 6, 3),
  (743722, 5, 3),
  (745993, 4, 6),
  (747782, 1, 4),
  (748933, 4, 3),
  (749948, 0, 0),
  (756149, 6, 6),
  (761504, 4, 3),
  (762331, 7, 3),
  (764392, 5, 7),
  (764589, 3, 2),
  (764899, 1, 0),
  (769099, 6, 7),
  (771610, 6, 3),
  (775501, 1, 4),
  (779931, 3, 3),
  (786130, 7, 7),
  (788210, 6, 0),
  (788245, 2, 3),
  (790036, 1, 4),
  (796356, 5, 2),
  (798005, 3, 3),
  (798532, 0, 6),
  (800309, 2, 3),
  (800787, 4, 3),
  (802327, 0, 0),
  (806535, 7, 0),
  (812520, 4, 3),
  (814700, 6, 0),
  (819414, 3, 3),
  (819856, 3, 3),
  (821880, 0, 0),
  (826648, 3, 5),
  (829567, 3, 3),
  (836774, 2, 2),
  (836801, 7, 6),
  (837299, 0, 7),
  (838502, 1, 2),
  (839960, 3, 3),
  (842954, 5, 2),
  (843380, 4, 3),
  (843926, 0, 0),
  (844989, 4, 3),
  (845926, 6, 0),
  (847869, 7, 3),
  (849896, 7, 4),
  (850891, 5, 7),
  (852124, 6, 4),
  (853258, 6, 7),
  (856664, 0, 0),
  (857391, 3, 2),
  (859360, 1, 3),
  (859582, 4, 5),
  (859920, 6, 6),
  (861867, 5, 6),
  (863057, 5, 7),
  (864560, 4, 6),
  (865608, 3, 1),
  (867673, 0, 1),
  (868455, 3, 6),
  (871111, 3, 7),
  (872101, 5, 2),
  (872270, 4, 7),
  (872439, 4, 0),
  (873293, 2, 6),
  (876365, 2, 3),
  (878546, 1, 0),
  (884333, 0, 0),
  (894261, 7, 0),
  (897346, 3, 1),
  (898399, 2, 2),
  (902658, 3, 6),
  (906484, 0, 0),
  (907750, 3, 3),
  (908283, 6, 6),
  (908457, 4, 3),
  (915047, 4, 2),
  (916421, 0, 6),
  (916539, 1, 6),
  (918508, 0, 7),
  (918583, 1, 0),
  (919901, 4, 3),
  (920863, 4, 7),
  (921120, 7, 6),
  (921539, 0, 0),
  (922382, 2, 3),
  (925074, 6, 0),
  (926023, 1, 0),
  (936012, 5, 3),
  (936914, 1, 4),
  (941170, 5, 3),
  (941289, 5, 6),
  (948749, 4, 3),
  (952222, 6, 1),
  (958124, 3, 6),
  (960116, 4, 2),
  (961424, 1, 1),
  (963556, 3, 7),
  (963987, 0, 1),
  (966638, 7, 0),
  (967985, 1, 0),
  (972383, 4, 6),
  (976151, 2, 1),
  (977681, 5, 4),
  (977984, 5, 0),
  (981887, 7, 4),
  (984064, 2, 3),
  (984686, 3, 3),
  (985626, 3, 4),
  (987177, 7, 0),
  (987822, 0, 4),
  (991546, 3, 5),
  (996795, 0, 0),
  (998508, 2, 3),
  (999804, 0, 4),
  (999843, 7, 0),
  (1001152, 2, 3),
  (1001236, 3, 0),
  (1001972, 0, 0),
  (1003112, 1, 7),
  (1008007, 7, 4),
  (1010140, 3, 0),
  (1011575, 3, 2),
  (1016373, 1, 6),
  (1017353, 3, 2),
  (1017712, 0, 0),
  (1020316, 0, 3),
  (1023412, 2, 3),
  (1025963, 5, 3),
  (1027201, 6, 7),
  (1028332, 1, 3),
  (1030368, 7, 2),
  (1030891, 0, 4),
  (1032920, 2, 3),
  (1034188, 5, 7),
  (1038569, 7, 3),
  (1039217, 0, 6),
  (1041183, 2, 7),
  (1043005, 5, 6),
  (1043615, 3, 7),
  (1048383, 2, 7),
  (1049731, 1, 1),
  (1050674, 1, 0),
  (1054805, 3, 3),
  (1057568, 7, 4),
  (1058423, 0, 0),
  (1059026, 2, 6),
  (1060265, 2, 3),
  (1062161, 0, 0),
  (1065273, 0, 3),
  (1068823, 7, 7),
  (1069162, 6, 6),
  (1070706, 5, 1),
  (1070719, 6, 6),
  (1072420, 7, 0),
  (1072545, 1, 3),
  (1074578, 6, 6),
  (1077025, 7, 7),
  (1077452, 2, 7),
  (1079425, 0, 0),
  (1083667, 1, 7),
  (1085122, 3, 1),
  (1085297, 2, 3),
  (1087445, 4, 3),
  (1087857, 6, 0),
  (1088081, 5, 7),
  (1090531, 6, 5),
  (1097154, 6, 4),
  (1097906, 3, 2),
  (1100264, 2, 3),
  (1102750, 4, 5),
  (1103307, 1, 7),
  (1104892, 0, 0),
  (1108941, 3, 3),
  (1112735, 2, 2),
  (1116621, 4, 2),
  (1121055, 5, 0),
  (1121559, 5, 3),
  (1124198, 4, 3),
  (1130414, 7, 2),
  (1130432, 2, 2),
  (1131721, 7, 0),
  (1135932, 1, 3),
  (1139357, 4, 1),
  (1140087, 3, 6),
  (1140585, 7, 2),
  (1147740, 7, 6),
  (1148321, 0, 3),
  (1152824, 2, 3),
  (1153548, 0, 0),
  (1157337, 7, 0),
  (1157676, 4, 3),
  (1159329, 4, 3),
  (1163617, 7, 0),
  (1165221, 0, 7),
  (1165477, 7, 0),
  (1165784, 7, 3),
  (1165861, 7, 0),
  (1166741, 4, 7),
  (1167756, 4, 2),
  (1177261, 4, 7),
  (1184070, 4, 3),
  (1184948, 3, 3),
  (1189333, 1, 4),
  (1191089, 1, 2),
  (1194497, 6, 0),
  (1196205, 1, 0),
  (1196667, 5, 3),
  (1199222, 7, 0),
  (1211863, 5, 3),
  (1213644, 2, 2),
  (1214367, 3, 3),
  (1216297, 0, 4),
  (1220979, 5, 4),
  (1221889, 5, 5),
  (1222045, 3, 3),
  (1229743, 7, 0),
  (1233772, 6, 2),
  (1233949, 5, 6),
  (1236117, 2, 6),
  (1237602, 1, 0),
  (1239262, 2, 3),
  (1240583, 7, 4),
  (1242650, 6, 0),
  (1243791, 3, 4),
  (1248155, 5, 3),
  (1251423, 2, 3),
  (1254418, 4, 6),
  (1254902, 6, 3),
  (1264312, 3, 5),
  (1265849, 4, 6),
  (1267157, 2, 3),
  (1269235, 1, 1),
  (1270555, 6, 0),
  (1271552, 6, 4),
  (1276621, 0, 4),
  (1278657, 6, 0),
  (1279883, 0, 6),
  (1281317, 2, 3),
  (1281489, 7, 0),
  (1282769, 5, 3),
  (1283806, 3, 6),
  (1286295, 4, 3),
  (1286947, 1, 5),
  (1287362, 7, 4),
  (1293794, 2, 2),
  (1293802, 3, 3),
  (1293805, 2, 3),
  (1295303, 2, 3),
  (1298264, 4, 7),
  (1303257, 0, 0),
  (1305862, 5, 3),
  (1310376, 7, 4),
  (1310511, 1, 7),
  (1311637, 5, 7),
  (1312256, 0, 3),
  (1318453, 2, 3),
  (1324793, 2, 2),
  (1324966, 3, 3),
  (1325546, 6, 0),
  (1326815, 6, 0),
  (1328235, 3, 4),
  (1335261, 7, 6),
  (1337098, 6, 3),
  (1339222, 0, 6),
  (1339338, 3, 2),
  (1340036, 0, 3),
  (1341059, 1, 4),
  (1341911, 1, 6),
  (1343477, 7, 3),
  (1344548, 5, 6),
  (1349746, 1, 0),
  (1353966, 6, 4),
  (1354891, 5, 3),
  (1355508, 6, 7),
  (1357239, 1, 3),
  (1357637, 6, 0),
  (1358177, 1, 1),
  (1363573, 0, 4),
  (1367262, 2, 2),
  (1368990, 7, 7),
  (1372211, 6, 6),
  (1375728, 1, 4),
  (1376920, 6, 0),
  (1377617, 4, 3),
  (1378049, 5, 7),
  (1379455, 3, 5),
  (1379513, 0, 0),
  (1381893, 0, 0),
  (1383979, 3, 3),
  (1385537, 3, 2),
  (1386108, 5, 2),
  (1387541, 5, 0),
  (1389220, 4, 3),
  (1390076, 5, 1),
  (1396790, 5, 2),
  (1402774, 5, 3),
  (1403024, 4, 6),
  (1411487, 3, 3),
  (1411876, 6, 2),
  (1415845, 4, 3),
  (1418571, 0, 0),
  (1419727, 5, 3),
  (1422895, 2, 6),
  (1423087, 2, 3),
  (1423972, 2, 4),
  (1426103, 2, 3),
  (1429157, 7, 0),
  (1432692, 3, 3),
  (1435614, 6, 4),
  (1439111, 6, 0),
  (1439152, 5, 5),
  (1441086, 1, 0),
  (1441950, 7, 0),
  (1444736, 6, 6),
  (1445546, 1, 3),
  (1445759, 1, 3),
  (1446144, 5, 3),
  (1447206, 7, 4),
  (1451539, 3, 7),
  (1452323, 1, 7),
  (1458936, 4, 3),
  (1461491, 2, 3),
  (1465365, 6, 3),
  (1465423, 6, 2),
  (1472875, 6, 7),
  (1474384, 7, 3),
  (1475482, 6, 0),
  (1475519, 2, 6),
  (1476360, 4, 3),
  (1478938, 3, 4),
  (1483454, 0, 4),
  (1484303, 4, 3),
  (1484520, 4, 6),
  (1484890, 4, 3),
  (1486112, 7, 0),
  (1486975, 4, 2),
  (1487847, 2, 6),
  (1488400, 5, 3),
  (1489914, 1, 6),
  (1492822, 5, 3),
  (1495130, 2, 6),
  (1499098, 0, 7),
  (1500651, 2, 3),
  (1500832, 4, 1),
  (1503879, 0, 0),
  (1504852, 5, 7),
  (1506750, 2, 3),
  (1507078, 2, 6),
  (1508174, 0, 0),
  (1515463, 7, 0),
  (1517596, 4, 0),
  (1520899, 3, 3),
  (1522312, 0, 3),
  (1525199, 5, 6),
  (1527187, 6, 0),
  (1527947, 3, 3),
  (1538979, 3, 7),
  (1543452, 6, 0),
  (1543464, 5, 7),
  (1544470, 2, 3),
  (1545037, 4, 2),
  (1545495, 1, 5),
  (1545682, 5, 0),
  (1547454, 2, 2),
  (1550101, 6, 0),
  (1553195, 6, 0),
  (1554259, 0, 2),
  (1557174, 2, 2),
  (1559079, 7, 4),
  (1565768, 1, 7),
  (1566140, 3, 3),
  (1567914, 7, 1),
  (1568564, 0, 3),
  (1573241, 1, 0),
  (1576918, 5, 2),
  (1580819, 4, 7),
  (1585878, 2, 5),
  (1587378, 3, 2),
  (1590699, 4, 7),
  (1591433, 5, 3),
  (1592391, 2, 3),
  (1593213, 5, 2),
  (1594174, 3, 7),
  (1595922, 3, 3),
  (1604263, 2, 3),
  (1607532, 4, 4),
  (1608014, 7, 7),
  (1608262, 3, 4),
  (1609687, 2, 6),
  (1611754, 2, 2),
  (1616178, 3, 6),
  (1618343, 3, 3),
  (1621078, 2, 6),
  (1621628, 6, 6),
  (1621926, 3, 3),
  (1622380, 4, 2),
  (1622713, 5, 4),
  (1625470, 6, 0),
  (1630136, 3, 7),
  (1630568, 3, 2),
  (1638258, 1, 0),
  (1641633, 0, 3),
  (1642526, 1, 7),
  (1642530, 1, 0),
  (1642579, 3, 3),
  (1644622, 4, 3),
  (1644970, 2, 3),
  (1645450, 0, 0),
  (1648212, 7, 0),
  (1650833, 6, 3),
  (1653444, 1, 7),
  (1654240, 0, 0),
  (1658511, 6, 5),
  (1660030, 0, 0),
  (1660709, 6, 7),
  (1662206, 1, 0),
  (1665787, 4, 2),
  (1666159, 7, 0),
  (1667168, 3, 6),
  (1667743, 1, 1),
  (1667782, 4, 7),
  (1670460, 0, 0),
  (1673452, 4, 3),
  (1673900, 2, 3),
  (1676551, 7, 7),
  (1677402, 5, 3),
  (1680991, 1, 0),
  (1681286, 7, 2),
  (1683533, 2, 2),
  (1684363, 0, 0),
  (1686302, 0, 7),
  (1686518, 1, 0),
  (1688847, 2, 3),
  (1690024, 7, 3),
  (1691315, 7, 1),
  (1694879, 4, 7),
  (1697602, 3, 3),
  (1699483, 4, 3),
  (1708332, 6, 0),
  (1710065, 2, 3),
  (1710614, 3, 1),
  (1710778, 4, 3),
  (1711333, 4, 2),
  (1714758, 2, 3),
  (1716451, 1, 2),
  (1716583, 6, 7),
  (1719369, 0, 7),
  (1720524, 5, 6),
  (1725256, 2, 1),
  (1727614, 6, 0),
  (1730808, 3, 6),
  (1731376, 6, 4),
  (1732468, 2, 7),
  (1732916, 1, 5),
  (1733023, 4, 2),
  (1734904, 0, 0),
  (1735969, 2, 6),
  (1738734, 6, 0),
  (1740551, 3, 3),
  (1741424, 7, 0),
  (1743273, 4, 6),
  (1745457, 7, 0),
  (1748937, 4, 5),
  (1752295, 4, 6),
  (1752759, 5, 7),
  (1754862, 7, 0),
  (1757151, 7, 0),
  (1758556, 5, 2),
  (1759235, 3, 3),
  (1760716, 6, 7),
  (1761525, 7, 4),
  (1764398, 2, 3),
  (1765889, 2, 2),
  (1768377, 6, 7),
  (1771988, 2, 2),
  (1777069, 6, 7),
  (1777729, 5, 7),
  (1781458, 0, 0),
  (1783701, 6, 0),
  (1785402, 0, 3),
  (1786656, 3, 6),
  (1788749, 1, 4),
  (1789771, 0, 0),
  (1790143, 7, 7),
  (1790566, 7, 7),
  (1792395, 3, 5),
  (1793010, 6, 0),
  (1794254, 4, 3),
  (1795327, 3, 6),
  (1797851, 5, 2),
  (1800940, 0, 4),
  (1800993, 1, 7),
  (1801282, 0, 3),
  (1802769, 2, 3),
  (1803539, 0, 6),
  (1804300, 6, 4),
  (1809125, 3, 2),
  (1812479, 3, 7),
  (1815849, 6, 7),
  (1816069, 5, 0),
  (1818368, 6, 0),
  (1822781, 0, 0),
  (1829095, 0, 3),
  (1829681, 6, 3),
  (1830124, 5, 7),
  (1830524, 2, 3),
  (1830604, 2, 0),
  (1832663, 5, 3),
  (1833090, 7, 6),
  (1836595, 2, 6),
  (1840418, 5, 6),
  (1841147, 5, 2),
  (1845286, 1, 0),
  (1846828, 4, 3),
  (1848766, 7, 5),
  (1849682, 2, 3),
  (1849695, 5, 3),
  (1850314, 5, 6),
  (1850864, 0, 5),
  (1851611, 0, 4),
  (1854874, 2, 3),
  (1856628, 1, 0),
  (1857498, 2, 6),
  (1859589, 6, 0),
  (1861872, 3, 3),
  (1862714, 5, 6),
  (1864394, 6, 4),
  (1866211, 1, 0),
  (1866441, 2, 3),
  (1867412, 1, 1),
  (1868183, 3, 7),
  (1870776, 3, 3),
  (1871251, 0, 0),
  (1871908, 5, 3),
  (1873145, 2, 3),
  (1874527, 3, 1),
  (1878047, 2, 3),
  (1878976, 6, 0),
  (1879206, 1, 7),
  (1885903, 1, 0),
  (1887334, 5, 0),
  (1892765, 5, 3),
  (1892902, 1, 4),
  (1893693, 4, 1),
  (1897195, 0, 0),
  (1897525, 5, 1),
  (1900888, 0, 2),
  (1902056, 1, 4),
  (1913800, 3, 3),
  (1915138, 4, 5),
  (1918811, 0, 0),
  (1922395, 7, 0),
  (1922701, 0, 3),
  (1925238, 1, 0),
  (1926845, 6, 3),
  (1927143, 5, 7),
  (1928545, 5, 6),
  (1930195, 1, 4),
  (1932421, 3, 2),
  (1934005, 2, 2),
  (1935768, 2, 6),
  (1938671, 2, 0),
  (1939621, 5, 3),
  (1940529, 7, 0),
  (1940555, 7, 7),
  (1941952, 0, 0),
  (1942611, 1, 5),
  (1942892, 2, 3),
  (1947060, 5, 3),
  (1947112, 5, 6),
  (1947182, 5, 3),
  (1947678, 1, 3),
  (1948072, 7, 6),
  (1948618, 1, 2),
  (1948789, 3, 6),
  (1949310, 4, 3),
  (1949965, 6, 3),
  (1950311, 7, 4),
  (1956938, 2, 7),
  (1957735, 3, 1),
  (1958453, 5, 3),
  (1959553, 1, 7),
  (1964825, 4, 3),
  (1964975, 3, 6),
  (1965293, 4, 7),
  (1967444, 2, 7),
  (1967519, 2, 7),
  (1969002, 3, 6),
  (1970408, 3, 2),
  (1970455, 3, 4),
  (1972146, 3, 2),
  (1972967, 0, 0),
  (1974103, 4, 3),
  (1974608, 2, 3),
  (1974816, 4, 2),
  (1975030, 2, 3),
  (1976709, 4, 3),
  (1976895, 6, 5),
  (1979982, 3, 3),
  (1981336, 7, 0),
  (1982452, 5, 2),
  (1984239, 1, 3),
  (1987178, 3, 3),
  (1988189, 2, 3),
  (1993415, 5, 3),
  (1999982, 4, 6),
  (2000903, 0, 4),
  (2001241, 5, 0),
  (2005099, 5, 6),
  (2006124, 7, 0),
  (2007609, 7, 0),
  (2009128, 3, 3),
  (2012170, 7, 4),
  (2012281, 5, 5),
  (2012596, 4, 7),
  (2014188, 0, 7),
  (2014258, 3, 3),
  (2016120, 0, 7),
  (2020229, 5, 2),
  (2020366, 5, 3),
  (2027940, 2, 3),
  (2028827, 7, 7),
  (2029131, 4, 6),
  (2030846, 7, 7),
  (2036327, 2, 2),
  (2037106, 5, 3),
  (2040188, 6, 4),
  (2040591, 2, 3),
  (2041935, 4, 7),
  (2045227, 6, 0),
  (2045769, 1, 0),
  (2049389, 3, 3),
  (2052105, 7, 4),
  (2052784, 4, 7),
  (2053017, 7, 0),
  (2055453, 0, 3),
  (2056272, 6, 5),
  (2057691, 2, 2),
  (2062566, 4, 5),
  (2063190, 4, 3),
  (2064191, 7, 1),
  (2065499, 0, 7),
  (2065769, 5, 2),
  (2066566, 7, 0),
  (2067773, 2, 3),
  (2068652, 5, 6),
  (2068828, 1, 7),
  (2070740, 3, 7),
  (2070884, 4, 3),
  (2076729, 6, 7),
  (2076913, 5, 7),
  (2077731, 2, 3),
  (2081724, 2, 6),
  (2082385, 7, 2),
  (2082643, 6, 1),
  (2084623, 6, 7),
  (2086647, 3, 7),
  (2088340, 7, 0),
  (2089983, 1, 0),
  (2091630, 7, 0),
  (2093027, 2, 4),
  (2093190, 6, 5),
  (2095357, 1, 3),
  (2099122, 0, 0),
  (2099144, 7, 7),
  (2099575, 4, 6),
  (2100783, 3, 3),
  (2108450, 5, 6),
  (2110006, 6, 7),
  (2114161, 4, 6),
  (2115878, 6, 3),
  (2121716, 6, 0),
  (2124538, 0, 4),
  (2127152, 3, 6),
  (2128633, 5, 6),
  (2132346, 0, 0),
  (2134578, 0, 0),
  (2137667, 3, 3),
  (2138141, 1, 2),
  (2141011, 5, 1),
  (2141219, 0, 0),
  (2141990, 6, 0),
  (2143657, 1, 7),
  (2146307, 7, 0),
  (2147695, 7, 0),
  (2151272, 5, 3),
  (2152742, 0, 4),
  (2154727, 4, 6),
  (2159714, 1, 7),
  (2161080, 2, 4),
  (2161422, 4, 3),
  (2166472, 3, 7),
  (2169336, 6, 4),
  (2169938, 1, 0),
  (2181542, 5, 6),
  (2182891, 3, 1),
  (2183389, 4, 3),
  (2183542, 7, 7),
  (2183677, 4, 3),
  (2185581, 3, 3),
  (2187819, 7, 4),
  (2188847, 1, 3),
  (2192089, 0, 0),
  (2194920, 1, 4),
  (2195158, 1, 0),
  (2201470, 4, 6),
  (2204519, 6, 0),
  (2205269, 4, 3),
  (2207242, 4, 6),
  (2207473, 6, 3),
  (2208031, 3, 1),
  (2210132, 4, 3),
  (2213360, 1, 0),
  (2217251, 0, 0),
  (2218687, 6, 4),
  (2220139, 1, 0),
  (2221401, 7, 3),
  (2227880, 3, 3),
  (2228384, 7, 0),
  (2228388, 2, 3),
  (2231655, 6, 6),
  (2236188, 2, 2),
  (2239095, 4, 7),
  (2240109, 4, 7),
  (2240348, 4, 4),
  (2243893, 1, 4),
  (2244049, 5, 3),
  (2245614, 3, 4),
  (2246056, 0, 4),
  (2246224, 3, 3),
  (2251878, 6, 0),
  (2254535, 3, 4),
  (2254738, 3, 3),
  (2257934, 6, 0),
  (2258782, 7, 0),
  (2259751, 1, 2),
  (2260129, 7, 0),
  (2261106, 1, 0),
  (2265179, 7, 1),
  (2265563, 7, 3),
  (2265989, 1, 1),
  (2267248, 5, 3),
  (2267526, 4, 5),
  (2270343, 7, 6),
  (2272719, 2, 1),
  (2274049, 0, 3),
  (2274645, 0, 5),
  (2276338, 6, 3),
  (2278101, 2, 3),
  (2282355, 1, 3),
  (2283026, 6, 0),
  (2283097, 1, 7),
  (2290389, 3, 2),
  (2292697, 6, 0),
  (2300214, 7, 6),
  (2302423, 4, 3),
  (2307883, 0, 0),
  (2308764, 7, 0),
  (2309187, 5, 3),
  (2310507, 0, 4),
  (2311768, 7, 0),
  (2313427, 7, 4),
  (2321719, 1, 0),
  (2322866, 5, 2),
  (2328044, 6, 0),
  (2329032, 1, 0),
  (2330035, 0, 1),
  (2332833, 6, 0),
  (2333804, 5, 1),
  (2334638, 0, 7),
  (2335690, 0, 4),
  (2335904, 1, 0),
  (2337216, 0, 0),
  (2339815, 6, 7),
  (2343686, 3, 6),
  (2344686, 3, 7),
  (2347154, 7, 4),
  (2347670, 2, 3),
  (2355275, 6, 0),
  (2356609, 5, 1),
  (2357215, 1, 1),
  (2357502, 3, 6),
  (2358278, 1, 3),
  (2360626, 3, 4),
  (2361213, 5, 6),
  (2362152, 1, 6),
  (2363043, 7, 4),
  (2364241, 5, 2),
  (2365118, 1, 2),
  (2367940, 6, 1),
  (2368557, 2, 3),
  (2369399, 4, 6),
  (2370030, 7, 5),
  (2374255, 0, 7),
  (2376340, 5, 3),
  (2377308, 1, 0),
  (2377576, 1, 7),
  (2381082, 2, 3),
  (2382073, 6, 4),
  (2386796, 0, 3),
  (2386949, 2, 3),
  (2388001, 0, 6),
  (2388294, 6, 0),
  (2389624, 1, 7),
  (2390598, 0, 2),
  (2395139, 3, 3),
  (2396452, 1, 7),
  (2401106, 0, 4),
  (2401175, 2, 5),
  (2404837, 6, 0),
  (2410961, 4, 7),
  (2412244, 0, 0),
  (2413002, 1, 0),
  (2414135, 5, 3),
  (2414225, 7, 0),
  (2414539, 7, 0),
  (2414715, 2, 3),
  (2416435, 2, 4),
  (2418546, 0, 0),
  (2418595, 3, 6),
  (2419080, 4, 3),
  (2419318, 5, 3),
  (2421523, 6, 7),
  (2423077, 4, 2),
  (2424940, 3, 3),
  (2424985, 2, 2),
  (2426028, 5, 3),
  (2426185, 7, 0),
  (2426340, 6, 4),
  (2428299, 7, 7),
  (2429129, 0, 7),
  (2430193, 2, 6),
  (2433004, 4, 6),
  (2436752, 4, 6),
  (2437794, 4, 6),
  (2438068, 1, 0),
  (2438340, 3, 3),
  (2447042, 1, 3),
  (2450167, 0, 0),
  (2452413, 4, 7),
  (2455832, 3, 6),
  (2456736, 3, 3),
  (2457611, 1, 0),
  (2457639, 2, 0),
  (2458131, 3, 3),
  (2458133, 4, 3),
  (2458549, 1, 3),
  (2460562, 3, 3),
  (2461648, 0, 0),
  (2461853, 2, 3),
  (2463759, 7, 7),
  (2465200, 6, 3),
  (2476668, 4, 2),
  (2477733, 4, 3),
  (2477792, 0, 7),
  (2478687, 2, 0),
  (2478848, 7, 0),
  (2481155, 0, 7),
  (2481514, 0, 1),
  (2482955, 2, 6),
  (2482998, 2, 3),
  (2483136, 1, 6),
  (2483147, 7, 6),
  (2485944, 0, 0),
  (2487480, 7, 3),
  (2488072, 6, 1),
  (2490036, 1, 3),
  (2495638, 3, 3),
  (2499313, 4, 6),
  (2501520, 6, 0),
  (2502645, 2, 7),
  (2504586, 0, 3),
  (2505574, 7, 3),
  (2508019, 1, 0),
  (2508269, 6, 1),
  (2510767, 0, 0),
  (2513471, 0, 4),
  (2514657, 3, 2),
  (2514691, 5, 7),
  (2516065, 1, 0),
  (2521351, 5, 3),
  (2522010, 2, 6),
  (2523120, 5, 2),
  (2531675, 5, 3),
  (2532989, 1, 7),
  (2541145, 1, 0),
  (2542092, 0, 0),
  (2544997, 2, 3),
  (2549577, 1, 4),
  (2549960, 0, 0),
  (2550753, 6, 0),
  (2551737, 2, 3),
  (2552153, 0, 7),
  (2554656, 1, 0),
  (2557188, 3, 3),
  (2561943, 4, 1),
  (2566545, 4, 2),
  (2569091, 1, 0),
  (2570556, 0, 0),
  (2571183, 0, 0),
  (2571317, 1, 7),
  (2573723, 3, 7),
  (2574119, 1, 0),
  (2577558, 6, 3),
  (2579937, 0, 0),
  (2581291, 4, 6),
  (2583798, 5, 7),
  (2583908, 1, 7),
  (2585575, 5, 3),
  (2585875, 4, 4),
  (2587791, 0, 0),
  (2590043, 5, 3),
  (2590626, 3, 7),
  (2592574, 2, 2),
  (2596723, 6, 6),
  (2599144, 3, 3),
  (2601103, 6, 0),
  (2605137, 5, 5),
  (2606157, 0, 4),
  (2606531, 1, 2),
  (2606890, 2, 2),
  (2607723, 4, 3),
  (2608513, 3, 5),
  (2608549, 3, 6),
  (2609719, 5, 1),
  (2612464, 3, 2),
  (2618011, 5, 3),
  (2619026, 3, 6),
  (2621592, 1, 0),
  (2627718, 3, 3),
  (2630075, 4, 3),
  (2630393, 4, 3),
  (2630900, 5, 3),
  (2631729, 1, 4),
  (2631924, 5, 4),
  (2639254, 2, 2),
  (2640654, 4, 3),
  (2642229, 0, 0),
  (2645389, 2, 1),
  (2647253, 7, 0),
  (2649233, 6, 6),
  (2650279, 4, 3),
  (2650427, 4, 3),
  (2651138, 3, 7),
  (2651346, 4, 3),
  (2652283, 3, 7),
  (2655103, 6, 0),
  (2655769, 2, 3),
  (2656805, 6, 3),
  (2658797, 1, 0),
  (2660455, 0, 4),
  (2661159, 4, 6),
  (2664383, 4, 3),
  (2667200, 2, 3),
  (2669032, 1, 4),
  (2680182, 2, 3),
  (2681978, 4, 3),
  (2682741, 7, 3),
  (2683783, 6, 5),
  (2685396, 1, 6),
  (2685500, 6, 7),
  (2687948, 7, 0),
  (2689211, 4, 3),
  (2689215, 1, 0),
  (2692791, 7, 0),
  (2695471, 4, 3),
  (2695818, 5, 3),
  (2697537, 0, 4),
  (2698830, 2, 7),
  (2701906, 3, 2),
  (2704459, 1, 0),
  (2706666, 4, 0),
  (2707388, 3, 2),
  (2707541, 4, 7),
  (2708750, 1, 0),
  (2710271, 5, 3),
  (2715237, 3, 3),
  (2719298, 6, 5),
  (2719309, 1, 4),
  (2726269, 1, 5),
  (2730647, 5, 3),
  (2731346, 5, 7),
  (2732865, 0, 0),
  (2732966, 0, 3),
  (2734132, 6, 3),
  (2739168, 3, 3),
  (2742951, 5, 2),
  (2743829, 0, 0),
  (2745453, 7, 3),
  (2748089, 3, 7),
  (2748673, 2, 3),
  (2749430, 6, 7),
  (2752099, 0, 0),
  (2753399, 2, 7),
  (2755093, 1, 0),
  (2756196, 4, 3),
  (2759694, 1, 7),
  (2760631, 5, 5),
  (2762918, 5, 3),
  (2765395, 0, 5),
  (2766832, 1, 3),
  (2768646, 1, 0),
  (2772863, 6, 0),
  (2774826, 1, 0),
  (2775422, 7, 5),
  (2777553, 1, 0),
  (2778894, 0, 4),
  (2780000, 3, 2),
  (2783508, 7, 6),
  (2784252, 0, 0),
  (2786797, 6, 0),
  (2787270, 2, 1),
  (2788273, 4, 3),
  (2788372, 1, 0),
  (2789291, 3, 3),
  (2789448, 1, 0),
  (2794058, 4, 3),
  (2796583, 1, 4),
  (2796838, 3, 3),
  (2797858, 6, 7),
  (2799745, 0, 0),
  (2801552, 4, 6),
  (2803716, 2, 2),
  (2804926, 1, 0),
  (2810677, 1, 3),
  (2814756, 5, 4),
  (2815588, 5, 3),
  (2823413, 5, 3),
  (2824421, 0, 5),
  (2824656, 6, 3),
  (2827375, 4, 3),
  (2839489, 2, 2),
  (2846540, 3, 4),
  (2848416, 3, 6),
  (2848500, 0, 3),
  (2850097, 1, 0),
  (2851138, 4, 6),
  (2853481, 1, 3),
  (2854629, 3, 1),
  (2856730, 5, 0),
  (2858486, 3, 3),
  (2858811, 3, 0),
  (2859576, 3, 7),
  (2861355, 2, 6),
  (2867274, 7, 4),
  (2867385, 7, 0),
  (2873552, 6, 0),
  (2873896, 3, 3),
  (2874483, 6, 0),
  (2876447, 3, 2),
  (2882959, 2, 3),
  (2883316, 4, 3),
  (2885852, 2, 5),
  (2890129, 6, 7),
  (2893784, 5, 6),
  (2894987, 5, 2),
  (2901363, 2, 3),
  (2902208, 5, 3),
  (2902377, 1, 5),
  (2906716, 4, 3),
  (2909410, 2, 2),
  (2909963, 4, 3),
  (2914768, 3, 3),
  (2919331, 7, 0),
  (2921326, 1, 3),
  (2931078, 0, 3),
  (2932524, 5, 3),
  (2933720, 3, 2),
  (2935117, 2, 0),
  (2937672, 0, 3),
  (2941462, 6, 5),
  (2944948, 2, 3),
  (2945495, 7, 4),
  (2946099, 0, 3),
  (2946977, 6, 5),
  (2947029, 3, 7),
  (2947360, 1, 4),
  (2947660, 2, 7),
  (2948486, 7, 7),
  (2953430, 3, 3),
  (2955524, 0, 0),
  (2956140, 2, 3),
  (2956400, 6, 0),
  (2957774, 7, 4),
  (2957971, 4, 2),
  (2958079, 2, 3),
  (2962264, 0, 0),
  (2964521, 5, 3),
  (2965191, 4, 6),
  (2965845, 6, 0),
  (2968082, 3, 7),
  (2970626, 3, 3),
  (2970846, 5, 3),
  (2976180, 4, 2),
  (2979363, 3, 2),
  (2979620, 2, 0),
  (2981529, 2, 3),
  (2984249, 7, 5),
  (2986280, 4, 3),
  (2988859, 6, 4),
  (2989948, 1, 7),
  (2990266, 5, 7),
  (2993811, 2, 6),
  (2994536, 5, 0),
  (2998549, 6, 0),
  (2998623, 6, 0),
  (2998820, 2, 5),
  (2999767, 2, 1),
  (3003144, 0, 3),
  (3004413, 2, 5),
  (3007050, 7, 0),
  (3007939, 3, 3),
  (3009745, 3, 2),
  (3010848, 6, 0),
  (3012364, 0, 0),
  (3014512, 0, 0),
  (3020785, 4, 7),
  (3024071, 5, 3),
  (3031839, 7, 0),
  (3032041, 3, 2),
  (3034833, 5, 3),
  (3038486, 1, 4),
  (3038700, 7, 1),
  (3039071, 2, 7),
  (3039968, 7, 0),
  (3041875, 5, 7),
  (3042252, 6, 3),
  (3044353, 7, 3),
  (3046100, 4, 6),
  (3046250, 7, 0),
  (3046669, 1, 1),
  (3047750, 2, 5),
  (3048049, 3, 3),
  (3050162, 5, 3),
  (3052630, 7, 6),
  (3053197, 5, 3),
  (3054687, 0, 4),
  (3056679, 3, 2),
  (3059418, 6, 0),
  (3061448, 1, 4),
  (3064774, 5, 7),
  (3069175, 7, 1),
  (3071460, 5, 5),
  (3075586, 7, 2),
  (3078104, 7, 1),
  (3078576, 3, 3),
  (3078937, 3, 3),
  (3080271, 3, 5),
  (3080408, 0, 3),
  (3081104, 6, 7),
  (3086489, 3, 3),
  (3090618, 0, 0),
  (3091686, 3, 5),
  (3091700, 6, 5),
  (3094576, 7, 3),
  (3094673, 5, 6),
  (3095787, 0, 4),
  (3095969, 1, 0),
  (3096847, 6, 4),
  (3097255, 1, 7),
  (3097597, 7, 0),
  (3099402, 2, 3),
  (3101358, 0, 7),
  (3101560, 3, 4),
  (3104985, 6, 0),
  (3105654, 7, 0),
  (3106375, 3, 7),
  (3108540, 4, 2),
  (3108606, 4, 1),
  (3113120, 4, 3),
  (3115890, 6, 4),
  (3117015, 2, 7),
  (3118093, 7, 7),
  (3121156, 7, 3),
  (3125100, 3, 7),
  (3125935, 7, 0),
  (3126750, 5, 3),
  (3130666, 7, 4),
  (3131214, 1, 4),
  (3131563, 2, 0),
  (3131987, 3, 3),
  (3132479, 0, 0),
  (3133535, 2, 3),
  (3134878, 0, 7),
  (3136754, 5, 7),
  (3138928, 6, 4),
  (3141672, 4, 7),
  (3142555, 6, 7),
  (3142739, 6, 0),
  (3145434, 7, 7),
  (3145588, 6, 6),
  (3145903, 7, 4),
  (3150308, 4, 3),
  (3151701, 4, 1),
  (3155824, 6, 0),
  (3156277, 2, 7),
  (3157451, 5, 7),
  (3158710, 1, 0),
  (3160350, 1, 3),
  (3161899, 0, 0),
  (3163886, 4, 3),
  (3172365, 4, 2),
  (3175764, 6, 3),
  (3177817, 7, 0),
  (3178096, 1, 0),
  (3179353, 0, 1),
  (3179663, 6, 3),
  (3181181, 6, 7),
  (3182805, 4, 3),
  (3184901, 2, 3),
  (3190275, 6, 0),
  (3191316, 5, 6),
  (3191673, 1, 5),
  (3194003, 2, 2),
  (3194777, 4, 3),
  (3200094, 2, 5),
  (3200402, 6, 7),
  (3204575, 7, 1),
  (3204874, 2, 4),
  (3206778, 4, 3),
  (3207096, 2, 3),
  (3207571, 1, 0),
  (3207940, 6, 3),
  (3209863, 2, 2),
  (3209986, 5, 3),
  (3210016, 3, 2),
  (3210161, 7, 3),
  (3216855, 7, 0),
  (3217394, 3, 3),
  (3220112, 2, 3),
  (3220903, 1, 0),
  (3223594, 3, 3),
  (3226256, 2, 3),
  (3227421, 1, 0),
  (3230108, 3, 5),
  (3230349, 1, 3),
  (3232367, 7, 4),
  (3234876, 0, 0),
  (3236995, 6, 3),
  (3242083, 5, 7),
  (3243973, 4, 2),
  (3244553, 0, 5),
  (3245857, 4, 6),
  (3247953, 3, 3),
  (3248240, 0, 4),
  (3249239, 0, 7),
  (3251596, 7, 4),
  (3252712, 3, 2),
  (3253179, 6, 7),
  (3253462, 2, 2),
  (3256409, 1, 1),
  (3256716, 2, 0),
  (3256950, 7, 3),
  (3258055, 1, 0),
  (3261306, 5, 3),
  (3262517, 7, 0),
  (3263436, 0, 0),
  (3267156, 4, 6),
  (3275416, 4, 0),
  (3276231, 3, 3),
  (3278547, 0, 5),
  (3285913, 1, 0),
  (3288073, 3, 3),
  (3289797, 2, 3),
  (3290489, 2, 3),
  (3293927, 4, 3),
  (3295997, 1, 0),
  (3296426, 0, 0),
  (3296643, 1, 0),
  (3298611, 3, 3),
  (3298700, 7, 4),
  (3300952, 1, 4),
  (3303893, 7, 5),
  (3305754, 1, 0),
  (3306634, 0, 4),
  (3307967, 2, 3),
  (3309678, 5, 3),
  (3313294, 2, 3),
  (3316719, 2, 3),
  (3319738, 5, 3),
  (3320242, 5, 6),
  (3320524, 0, 7),
  (3326039, 2, 3),
  (3326110, 2, 7),
  (3326512, 3, 3),
  (3328336, 7, 0),
  (3330090, 2, 6),
  (3331810, 1, 4),
  (3332208, 6, 0),
  (3333248, 7, 7),
  (3333629, 5, 2),
  (3335186, 4, 3),
  (3336472, 3, 3),
  (3339010, 1, 0),
  (3341058, 5, 6),
  (3342300, 1, 4),
  (3343025, 4, 3),
  (3346548, 3, 3),
  (3346746, 3, 3),
  (3352075, 1, 6),
  (3355260, 7, 1),
  (3358522, 6, 0),
  (3360612, 4, 3),
  (3360830, 7, 3),
  (3363319, 7, 7),
  (3364741, 6, 0),
  (3367472, 7, 4),
  (3367967, 7, 0),
  (3368362, 2, 1),
  (3369644, 0, 3),
  (3373330, 7, 3),
  (3373509, 0, 0),
  (3373545, 4, 7),
  (3374469, 0, 0),
  (3374477, 2, 3),
  (3383111, 3, 2),
  (3383325, 2, 3),
  (3388636, 2, 6),
  (3389497, 2, 7),
  (3392142, 6, 0),
  (3393589, 7, 7),
  (3397734, 5, 1),
  (3398414, 3, 3),
  (3402184, 6, 4),
  (3405526, 0, 6),
  (3408294, 0, 0),
  (3409804, 5, 2),
  (3410644, 4, 3),
  (3414071, 0, 0),
  (3415285, 4, 3),
  (3415512, 1, 7),
  (3416893, 7, 3),
  (3419607, 4, 4),
  (3419826, 2, 6),
  (3421575, 2, 3),
  (3422337, 7, 4),
  (3426171, 4, 7),
  (3427930, 5, 2),
  (3428223, 7, 7),
  (3430778, 4, 3),
  (3434220, 2, 4),
  (3439755, 7, 0),
  (3440636, 6, 2),
  (3443638, 2, 3),
  (3445285, 0, 3),
  (3446113, 1, 7),
  (3447101, 7, 4),
  (3449309, 4, 7),
  (3457063, 0, 0),
  (3457735, 0, 6),
  (3458467, 1, 3),
  (3460675, 7, 1),
  (3460765, 4, 6),
  (3462164, 5, 3),
  (3463009, 0, 0),
  (3463184, 4, 0),
  (3467405, 7, 4),
  (3469742, 5, 5),
  (3470900, 7, 3),
  (3477199, 7, 0),
  (3486378, 2, 3),
  (3487122, 7, 0),
  (3487562, 2, 7),
  (3488125, 1, 0),
  (3490584, 7, 7),
  (3491451, 6, 4),
  (3492612, 1, 1),
  (3496234, 5, 7),
  (3497271, 7, 3),
  (3500200, 2, 7),
  (3503365, 4, 3),
  (3504365, 0, 0),
  (3508131, 2, 3),
  (3509365, 0, 6),
  (3510060, 5, 6),
  (3510169, 7, 0),
  (3510409, 0, 0),
  (3511808, 5, 2),
  (3514073, 6, 3),
  (3514433, 6, 7),
  (3517676, 0, 1),
  (3518941, 0, 0),
  (3519421, 5, 0),
  (3520370, 2, 5),
  (3521869, 5, 2),
  (3521911, 6, 7),
  (3523509, 6, 0),
  (3530462, 4, 3),
  (3540022, 6, 0),
  (3542265, 7, 4),
  (3543953, 1, 3),
  (3545097, 5, 2),
  (3545786, 5, 1),
  (3546732, 1, 0),
  (3551222, 2, 2),
  (3551364, 7, 0),
  (3552996, 5, 3),
  (3555850, 4, 6),
  (3556281, 3, 6),
  (3560713, 6, 0),
  (3561506, 6, 0),
  (3564143, 2, 3),
  (3567172, 2, 3),
  (3568549, 6, 0),
  (3569460, 7, 0),
  (3571711, 6, 3),
  (3572486, 0, 0),
  (3572727, 4, 7),
  (3574253, 7, 0),
  (3577233, 3, 3),
  (3578738, 5, 7),
  (3579461, 2, 3),
  (3584549, 5, 2),
  (3588340, 2, 0),
  (3592726, 2, 3),
  (3593396, 5, 3),
  (3598940, 6, 4),
  (3599687, 3, 3),
  (3599747, 2, 7),
])
