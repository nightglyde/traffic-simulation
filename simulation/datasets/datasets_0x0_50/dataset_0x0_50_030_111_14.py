from src.util import *
schedule = deque([
  (244, 3, 2),
  (3419, 2, 0),
  (7482, 1, 1),
  (9125, 1, 2),
  (10872, 2, 0),
  (14966, 1, 1),
  (15016, 0, 0),
  (15018, 3, 2),
  (17775, 2, 0),
  (19613, 2, 1),
  (22996, 2, 1),
  (23950, 1, 2),
  (24858, 3, 1),
  (32407, 1, 1),
  (34436, 2, 0),
  (35472, 0, 1),
  (36098, 1, 1),
  (37118, 0, 2),
  (39657, 3, 2),
  (42494, 2, 1),
  (44173, 0, 2),
  (48206, 2, 2),
  (50141, 0, 2),
  (54320, 2, 1),
  (56363, 1, 0),
  (60438, 0, 0),
  (65550, 1, 1),
  (76093, 0, 0),
  (77359, 1, 0),
  (80425, 0, 1),
  (82439, 3, 1),
  (82444, 3, 1),
  (83313, 0, 0),
  (83565, 0, 2),
  (86128, 3, 2),
  (86879, 1, 0),
  (91128, 1, 1),
  (95443, 1, 2),
  (98290, 0, 2),
  (101366, 2, 1),
  (102771, 3, 0),
  (104403, 3, 1),
  (105487, 2, 2),
  (112544, 2, 1),
  (112676, 3, 2),
  (112742, 0, 2),
  (117187, 1, 1),
  (118721, 3, 2),
  (120906, 2, 2),
  (130209, 2, 0),
  (130726, 1, 0),
  (133682, 1, 1),
  (135139, 1, 1),
  (139120, 2, 1),
  (139317, 0, 2),
  (142242, 2, 0),
  (143451, 3, 2),
  (147091, 1, 2),
  (149446, 3, 0),
  (150679, 2, 0),
  (151399, 1, 1),
  (151468, 1, 0),
  (151566, 3, 0),
  (152550, 1, 1),
  (152809, 1, 1),
  (155042, 2, 1),
  (155165, 1, 0),
  (155842, 0, 2),
  (158519, 0, 1),
  (159587, 2, 2),
  (162005, 2, 0),
  (166391, 2, 0),
  (167365, 3, 1),
  (168350, 3, 0),
  (169264, 3, 1),
  (170969, 0, 2),
  (172032, 2, 1),
  (172735, 3, 2),
  (173838, 1, 1),
  (173905, 0, 2),
  (174163, 3, 0),
  (174518, 2, 0),
  (179553, 0, 2),
  (180027, 2, 1),
  (181908, 2, 2),
  (183183, 0, 2),
  (186845, 2, 1),
  (191107, 3, 0),
  (191427, 2, 0),
  (191534, 2, 1),
  (192342, 0, 2),
  (194091, 3, 0),
  (195491, 2, 1),
  (197423, 3, 1),
  (199571, 0, 1),
  (202157, 1, 2),
  (202728, 2, 0),
  (204274, 0, 2),
  (204777, 2, 0),
  (206633, 2, 1),
  (207369, 3, 2),
  (211439, 2, 2),
  (216728, 1, 1),
  (219536, 0, 0),
  (223228, 1, 2),
  (228410, 3, 2),
  (230667, 1, 2),
  (231680, 3, 1),
  (232041, 1, 1),
  (232401, 0, 0),
  (233736, 2, 2),
  (239680, 1, 0),
  (241079, 0, 1),
  (244030, 1, 1),
  (244394, 2, 1),
  (249846, 0, 1),
  (255831, 3, 0),
  (256028, 3, 2),
  (256928, 2, 1),
  (257830, 1, 0),
  (257941, 1, 1),
  (259483, 3, 2),
  (259507, 2, 1),
  (261002, 3, 2),
  (271398, 3, 1),
  (272433, 0, 2),
  (273181, 1, 0),
  (274984, 0, 0),
  (275315, 0, 1),
  (276714, 2, 2),
  (277959, 2, 2),
  (279242, 3, 0),
  (283219, 3, 0),
  (284185, 3, 0),
  (287800, 2, 0),
  (289157, 0, 1),
  (297531, 1, 0),
  (300313, 3, 2),
  (300805, 3, 0),
  (308984, 0, 2),
  (309250, 1, 1),
  (311063, 3, 0),
  (311667, 2, 0),
  (312382, 3, 1),
  (312390, 0, 0),
  (312615, 3, 0),
  (316623, 1, 1),
  (319846, 0, 2),
  (324439, 1, 1),
  (326611, 3, 1),
  (328053, 1, 1),
  (328057, 0, 2),
  (332605, 0, 1),
  (333179, 0, 2),
  (334836, 2, 0),
  (336149, 3, 1),
  (336423, 3, 1),
  (339387, 3, 1),
  (343152, 1, 2),
  (353132, 0, 0),
  (354792, 2, 2),
  (361843, 3, 1),
  (364181, 2, 2),
  (365476, 0, 1),
  (366261, 1, 1),
  (371659, 1, 1),
  (373094, 2, 1),
  (373457, 0, 1),
  (373726, 3, 0),
  (375247, 3, 1),
  (376026, 1, 1),
  (380082, 2, 1),
  (384060, 2, 1),
  (385190, 0, 1),
  (390010, 3, 2),
  (390598, 0, 1),
  (390602, 3, 1),
  (391398, 1, 0),
  (392325, 1, 0),
  (393748, 0, 1),
  (395658, 0, 2),
  (398777, 1, 0),
  (400568, 1, 2),
  (401735, 1, 2),
  (403046, 3, 1),
  (403173, 1, 1),
  (403652, 1, 0),
  (404411, 2, 1),
  (406142, 3, 1),
  (407267, 3, 0),
  (409618, 0, 2),
  (410373, 1, 0),
  (412533, 1, 2),
  (413347, 3, 0),
  (417331, 3, 2),
  (418510, 2, 0),
  (421266, 3, 0),
  (422799, 2, 0),
  (424912, 0, 1),
  (427268, 3, 1),
  (428658, 2, 2),
  (429482, 1, 1),
  (430673, 1, 1),
  (432384, 0, 0),
  (439188, 2, 0),
  (442349, 3, 2),
  (449924, 0, 2),
  (450175, 3, 1),
  (450229, 0, 0),
  (454559, 2, 1),
  (455207, 2, 0),
  (458910, 1, 1),
  (459398, 0, 2),
  (461544, 0, 1),
  (462015, 0, 2),
  (462600, 1, 1),
  (465465, 2, 0),
  (466353, 0, 2),
  (467244, 1, 0),
  (467411, 3, 1),
  (467563, 1, 2),
  (467583, 0, 2),
  (473904, 2, 2),
  (474933, 0, 0),
  (478432, 3, 2),
  (484280, 1, 2),
  (485352, 2, 1),
  (486752, 3, 2),
  (487033, 1, 0),
  (492200, 3, 1),
  (492969, 3, 1),
  (493742, 3, 1),
  (495091, 2, 2),
  (498750, 1, 0),
  (499850, 0, 2),
  (502509, 1, 1),
  (503277, 0, 0),
  (506381, 0, 0),
  (508116, 2, 0),
  (508866, 3, 2),
  (512209, 2, 2),
  (518206, 2, 1),
  (521223, 1, 0),
  (521829, 2, 2),
  (521918, 0, 2),
  (522010, 3, 1),
  (525392, 3, 0),
  (526445, 1, 1),
  (526621, 0, 2),
  (527106, 0, 2),
  (528587, 3, 1),
  (529051, 2, 0),
  (532578, 3, 1),
  (534222, 2, 0),
  (537039, 3, 1),
  (537852, 1, 0),
  (538626, 0, 1),
  (538723, 2, 2),
  (540212, 2, 1),
  (543489, 3, 0),
  (544575, 1, 0),
  (549247, 3, 0),
  (551893, 1, 1),
  (552491, 2, 2),
  (559982, 0, 0),
  (561036, 0, 0),
  (564195, 1, 2),
  (568753, 2, 1),
  (573278, 3, 1),
  (575594, 3, 1),
  (576066, 0, 1),
  (577674, 2, 2),
  (585558, 1, 1),
  (587164, 3, 0),
  (588313, 2, 2),
  (589866, 2, 2),
  (590204, 2, 2),
  (590848, 2, 1),
  (591132, 0, 1),
  (593772, 0, 1),
  (596590, 1, 1),
  (596826, 3, 1),
  (596853, 3, 0),
  (599623, 0, 1),
  (603614, 1, 2),
  (606994, 0, 0),
  (613667, 3, 0),
  (614459, 3, 0),
  (615157, 1, 2),
  (616673, 2, 1),
  (619230, 3, 1),
  (620914, 1, 0),
  (625000, 1, 1),
  (625260, 3, 2),
  (627786, 2, 1),
  (627985, 1, 0),
  (633815, 0, 0),
  (637884, 0, 1),
  (639322, 0, 1),
  (640339, 1, 0),
  (644395, 2, 1),
  (644676, 0, 0),
  (647570, 0, 2),
  (648031, 3, 2),
  (652367, 3, 2),
  (653172, 2, 0),
  (654208, 3, 2),
  (656096, 3, 0),
  (658146, 3, 2),
  (659807, 1, 2),
  (661931, 1, 2),
  (663227, 1, 1),
  (663555, 1, 2),
  (667267, 0, 2),
  (674161, 0, 1),
  (676861, 1, 0),
  (677882, 0, 1),
  (678175, 1, 0),
  (681172, 0, 0),
  (682935, 3, 0),
  (684778, 1, 1),
  (691126, 1, 0),
  (694223, 0, 0),
  (694232, 3, 0),
  (696238, 2, 1),
  (701982, 2, 0),
  (702429, 1, 0),
  (706125, 2, 0),
  (708618, 2, 1),
  (713154, 0, 1),
  (715064, 1, 0),
  (716547, 2, 1),
  (716702, 3, 2),
  (717429, 0, 0),
  (717833, 1, 1),
  (717995, 2, 2),
  (721210, 1, 0),
  (721464, 2, 0),
  (722448, 1, 0),
  (724661, 3, 2),
  (724884, 2, 1),
  (725144, 0, 2),
  (725398, 3, 0),
  (727571, 1, 2),
  (727973, 2, 2),
  (728949, 2, 0),
  (729687, 3, 1),
  (733373, 0, 2),
  (736132, 3, 0),
  (736617, 3, 0),
  (738033, 1, 1),
  (738218, 3, 1),
  (741491, 0, 2),
  (742209, 2, 1),
  (742951, 1, 2),
  (743028, 1, 2),
  (744015, 1, 1),
  (744393, 0, 0),
  (744697, 2, 0),
  (745594, 1, 1),
  (747164, 1, 2),
  (747417, 1, 0),
  (751892, 1, 2),
  (753831, 2, 1),
  (754337, 3, 0),
  (756279, 2, 2),
  (756790, 2, 2),
  (756866, 1, 0),
  (757863, 3, 0),
  (758669, 1, 1),
  (760682, 2, 1),
  (763995, 3, 2),
  (765700, 3, 1),
  (767969, 1, 1),
  (770115, 2, 0),
  (773647, 2, 2),
  (774406, 0, 0),
  (781032, 0, 2),
  (781926, 0, 0),
  (784313, 3, 1),
  (784949, 3, 1),
  (788079, 3, 1),
  (788524, 0, 1),
  (789141, 3, 0),
  (797108, 0, 0),
  (797432, 3, 1),
  (799151, 3, 1),
  (804856, 1, 0),
  (807082, 2, 0),
  (811043, 2, 0),
  (819425, 1, 2),
  (820983, 0, 1),
  (821217, 2, 1),
  (829603, 1, 1),
  (831558, 2, 0),
  (833325, 1, 1),
  (836250, 0, 2),
  (838207, 1, 2),
  (838867, 1, 1),
  (839564, 3, 2),
  (840837, 1, 2),
  (846328, 3, 0),
  (846567, 0, 0),
  (848594, 3, 0),
  (848775, 0, 2),
  (848837, 1, 0),
  (849182, 2, 0),
  (849293, 3, 0),
  (852507, 1, 1),
  (860479, 0, 2),
  (862863, 2, 0),
  (864513, 2, 0),
  (865064, 1, 0),
  (869853, 0, 0),
  (870532, 0, 2),
  (874807, 2, 2),
  (875319, 1, 0),
  (875434, 0, 0),
  (878075, 0, 0),
  (878315, 2, 1),
  (878493, 2, 2),
  (879394, 3, 2),
  (880857, 0, 2),
  (883901, 3, 0),
  (884538, 2, 1),
  (887145, 2, 2),
  (887790, 0, 2),
  (888518, 1, 0),
  (896509, 3, 2),
  (899650, 0, 0),
  (904530, 0, 0),
  (904738, 1, 1),
  (906584, 2, 2),
  (910074, 3, 2),
  (911518, 3, 2),
  (913099, 2, 0),
  (913177, 2, 1),
  (913763, 0, 2),
  (914443, 3, 2),
  (915452, 2, 0),
  (919289, 3, 2),
  (919671, 3, 2),
  (920312, 2, 2),
  (923166, 0, 0),
  (926608, 3, 2),
  (926661, 3, 2),
  (926769, 3, 1),
  (928533, 0, 2),
  (932803, 2, 0),
  (937445, 0, 0),
  (938362, 0, 0),
  (939714, 1, 1),
  (942854, 1, 2),
  (947750, 2, 0),
  (947884, 2, 0),
  (951021, 1, 0),
  (951372, 3, 0),
  (955388, 1, 2),
  (961606, 3, 2),
  (961620, 3, 0),
  (965794, 2, 2),
  (965878, 2, 0),
  (967878, 1, 0),
  (969606, 2, 1),
  (971187, 1, 1),
  (975349, 2, 2),
  (975509, 1, 1),
  (976250, 2, 0),
  (982002, 0, 1),
  (987968, 3, 2),
  (989511, 3, 1),
  (996271, 1, 0),
  (999055, 2, 0),
  (999383, 0, 0),
  (1000240, 0, 0),
  (1001397, 1, 2),
  (1001857, 3, 2),
  (1002373, 2, 1),
  (1004339, 1, 1),
  (1005319, 2, 2),
  (1007444, 3, 0),
  (1010460, 2, 0),
  (1013848, 0, 2),
  (1015185, 0, 1),
  (1015932, 1, 2),
  (1020699, 1, 1),
  (1020802, 1, 2),
  (1022243, 0, 2),
  (1023369, 0, 1),
  (1027365, 1, 2),
  (1027792, 1, 2),
  (1028149, 2, 1),
  (1028912, 2, 0),
  (1033185, 2, 1),
  (1033310, 2, 1),
  (1038969, 2, 0),
  (1041092, 2, 1),
  (1042929, 1, 0),
  (1048515, 2, 0),
  (1057688, 0, 1),
  (1059070, 3, 1),
  (1059751, 0, 1),
  (1059773, 1, 1),
  (1060558, 3, 2),
  (1061071, 2, 0),
  (1065808, 3, 1),
  (1066389, 3, 0),
  (1068245, 3, 1),
  (1068467, 2, 2),
  (1068659, 0, 0),
  (1071590, 3, 2),
  (1072897, 0, 2),
  (1074484, 3, 0),
  (1075755, 0, 2),
  (1077646, 3, 0),
  (1080816, 1, 0),
  (1081842, 2, 2),
  (1082151, 0, 0),
  (1087649, 0, 2),
  (1087988, 2, 2),
  (1091698, 1, 1),
  (1096507, 2, 1),
  (1097578, 0, 0),
  (1098359, 1, 0),
  (1100349, 3, 2),
  (1100421, 3, 0),
  (1103736, 3, 1),
  (1104301, 2, 0),
  (1104395, 1, 0),
  (1108771, 2, 0),
  (1109277, 3, 0),
  (1111800, 1, 1),
  (1111936, 2, 0),
  (1118089, 3, 2),
  (1119850, 1, 0),
  (1121787, 1, 0),
  (1122502, 3, 1),
  (1127345, 2, 1),
  (1127459, 2, 0),
  (1129576, 3, 0),
  (1130516, 2, 1),
  (1130988, 1, 2),
  (1135805, 2, 0),
  (1138803, 3, 0),
  (1142366, 2, 2),
  (1148415, 1, 0),
  (1150659, 3, 2),
  (1152346, 1, 0),
  (1153340, 3, 2),
  (1155386, 3, 2),
  (1157000, 0, 2),
  (1159230, 0, 2),
  (1163145, 1, 2),
  (1165865, 2, 2),
  (1166061, 2, 0),
  (1166770, 0, 1),
  (1169734, 0, 2),
  (1175699, 0, 2),
  (1177409, 1, 1),
  (1178559, 0, 0),
  (1181061, 1, 2),
  (1182381, 1, 1),
  (1184817, 0, 2),
  (1185233, 3, 1),
  (1186976, 0, 2),
  (1187430, 3, 1),
  (1193410, 1, 1),
  (1199854, 2, 2),
  (1201006, 1, 1),
  (1204472, 3, 2),
  (1204677, 2, 0),
  (1207887, 3, 1),
  (1208718, 0, 0),
  (1209214, 3, 2),
  (1209973, 2, 2),
  (1213272, 0, 0),
  (1213365, 0, 1),
  (1213374, 0, 2),
  (1217980, 3, 0),
  (1218771, 2, 2),
  (1220368, 2, 1),
  (1221283, 0, 0),
  (1225349, 1, 1),
  (1231782, 2, 1),
  (1232004, 2, 2),
  (1232690, 0, 1),
  (1233506, 1, 0),
  (1234868, 2, 2),
  (1236105, 0, 1),
  (1237586, 3, 0),
  (1238179, 3, 0),
  (1239544, 3, 1),
  (1242091, 3, 1),
  (1242222, 2, 1),
  (1243528, 3, 2),
  (1243679, 1, 1),
  (1244102, 0, 1),
  (1247501, 1, 2),
  (1248381, 0, 2),
  (1249603, 3, 2),
  (1250254, 0, 2),
  (1252089, 1, 2),
  (1253645, 2, 1),
  (1258746, 0, 1),
  (1261928, 2, 1),
  (1266020, 0, 1),
  (1270068, 2, 2),
  (1273116, 3, 0),
  (1275016, 1, 0),
  (1277799, 2, 0),
  (1279631, 1, 0),
  (1283215, 2, 1),
  (1283777, 3, 2),
  (1283827, 2, 2),
  (1285358, 1, 2),
  (1288279, 0, 0),
  (1289055, 2, 1),
  (1289267, 2, 2),
  (1290412, 0, 2),
  (1293388, 0, 1),
  (1294155, 0, 2),
  (1295168, 1, 2),
  (1295219, 3, 2),
  (1296548, 3, 1),
  (1297526, 0, 1),
  (1298399, 3, 2),
  (1298852, 1, 2),
  (1304408, 1, 0),
  (1305394, 2, 1),
  (1308024, 0, 1),
  (1309429, 2, 0),
  (1314576, 3, 1),
  (1316177, 3, 0),
  (1317779, 3, 1),
  (1318087, 2, 0),
  (1318530, 2, 1),
  (1320592, 1, 2),
  (1321622, 1, 0),
  (1322999, 0, 1),
  (1324547, 0, 1),
  (1324838, 3, 2),
  (1327635, 0, 0),
  (1329957, 2, 1),
  (1331192, 1, 2),
  (1338699, 1, 1),
  (1347918, 1, 1),
  (1351323, 3, 0),
  (1351373, 2, 2),
  (1354563, 1, 2),
  (1357600, 2, 2),
  (1358489, 1, 1),
  (1358583, 3, 0),
  (1361211, 0, 0),
  (1367227, 1, 0),
  (1367638, 2, 0),
  (1369645, 0, 0),
  (1370879, 0, 2),
  (1372944, 0, 0),
  (1374031, 0, 2),
  (1374684, 2, 0),
  (1376767, 1, 1),
  (1377848, 0, 1),
  (1378359, 2, 0),
  (1378638, 1, 2),
  (1380906, 3, 2),
  (1382319, 0, 0),
  (1384844, 3, 0),
  (1387144, 0, 1),
  (1391590, 3, 0),
  (1393885, 2, 1),
  (1394494, 1, 2),
  (1399797, 0, 1),
  (1401786, 1, 1),
  (1405954, 2, 1),
  (1406549, 1, 1),
  (1406997, 0, 1),
  (1408682, 0, 1),
  (1409540, 2, 2),
  (1410121, 1, 2),
  (1412418, 1, 1),
  (1415652, 3, 1),
  (1419820, 3, 0),
  (1420532, 1, 1),
  (1426289, 0, 1),
  (1427543, 0, 2),
  (1428604, 0, 2),
  (1428849, 1, 1),
  (1429323, 0, 1),
  (1433743, 1, 1),
  (1436013, 2, 1),
  (1436264, 2, 2),
  (1438151, 0, 1),
  (1438994, 2, 2),
  (1439145, 3, 2),
  (1443042, 1, 0),
  (1443853, 2, 0),
  (1444867, 1, 2),
  (1445076, 2, 0),
  (1449026, 3, 0),
  (1449472, 2, 1),
  (1450189, 0, 0),
  (1451991, 3, 2),
  (1453967, 1, 0),
  (1454856, 1, 1),
  (1456372, 1, 1),
  (1464913, 2, 0),
  (1465032, 1, 2),
  (1467534, 2, 2),
  (1468980, 0, 0),
  (1471881, 0, 2),
  (1476935, 0, 0),
  (1477471, 2, 2),
  (1477717, 2, 0),
  (1479354, 0, 2),
  (1481450, 0, 2),
  (1482379, 3, 1),
  (1484173, 2, 2),
  (1486279, 3, 2),
  (1486687, 3, 0),
  (1487126, 1, 1),
  (1495352, 1, 2),
  (1498003, 3, 0),
  (1498257, 3, 2),
  (1502719, 1, 1),
  (1510058, 1, 1),
  (1510346, 1, 2),
  (1511576, 1, 1),
  (1512575, 1, 0),
  (1513507, 0, 1),
  (1514503, 1, 2),
  (1515455, 0, 2),
  (1520112, 3, 1),
  (1523229, 1, 0),
  (1527557, 1, 0),
  (1531235, 0, 1),
  (1531978, 2, 2),
  (1536910, 2, 2),
  (1537578, 3, 0),
  (1538222, 0, 0),
  (1538476, 1, 2),
  (1539737, 0, 2),
  (1541799, 1, 0),
  (1544362, 3, 0),
  (1546284, 2, 1),
  (1548168, 1, 0),
  (1548228, 3, 2),
  (1551637, 1, 2),
  (1551987, 0, 1),
  (1552596, 1, 0),
  (1557150, 0, 1),
  (1557290, 0, 1),
  (1562639, 2, 0),
  (1566928, 1, 2),
  (1568406, 3, 1),
  (1569343, 1, 0),
  (1570063, 1, 0),
  (1572521, 0, 2),
  (1573735, 2, 0),
  (1574819, 1, 2),
  (1578398, 0, 2),
  (1579720, 0, 2),
  (1581100, 2, 1),
  (1581317, 3, 2),
  (1581685, 2, 1),
  (1582918, 3, 1),
  (1583217, 2, 0),
  (1584102, 3, 1),
  (1585808, 0, 2),
  (1590698, 3, 2),
  (1593133, 3, 0),
  (1593914, 2, 1),
  (1596507, 0, 2),
  (1600015, 1, 0),
  (1600722, 1, 0),
  (1601225, 1, 1),
  (1601302, 0, 1),
  (1601488, 0, 0),
  (1603392, 0, 2),
  (1604966, 2, 2),
  (1606562, 1, 2),
  (1610506, 2, 2),
  (1610800, 1, 2),
  (1611748, 0, 1),
  (1613154, 0, 1),
  (1615010, 0, 1),
  (1615665, 3, 2),
  (1616802, 1, 0),
  (1617381, 2, 0),
  (1621442, 2, 0),
  (1622550, 3, 2),
  (1623243, 2, 1),
  (1628011, 0, 0),
  (1629808, 2, 0),
  (1630669, 0, 2),
  (1633483, 0, 1),
  (1633683, 3, 2),
  (1634276, 3, 1),
  (1636539, 2, 0),
  (1638431, 0, 0),
  (1639248, 1, 0),
  (1640293, 1, 1),
  (1640518, 1, 2),
  (1641052, 0, 1),
  (1643067, 1, 0),
  (1646360, 0, 0),
  (1648224, 2, 0),
  (1649820, 1, 0),
  (1650850, 2, 1),
  (1653107, 1, 1),
  (1654420, 2, 0),
  (1656101, 0, 0),
  (1657866, 0, 2),
  (1664236, 3, 0),
  (1664609, 1, 2),
  (1673189, 2, 2),
  (1678048, 3, 1),
  (1678421, 3, 1),
  (1678655, 0, 1),
  (1683802, 2, 0),
  (1685705, 3, 1),
  (1686414, 2, 1),
  (1687044, 3, 0),
  (1687217, 0, 2),
  (1688495, 0, 1),
  (1688526, 0, 1),
  (1689265, 3, 2),
  (1693182, 3, 2),
  (1693430, 0, 2),
  (1695583, 0, 1),
  (1695968, 1, 1),
  (1696216, 3, 1),
  (1696921, 1, 1),
  (1699861, 0, 0),
  (1699866, 0, 2),
  (1700236, 2, 2),
  (1701811, 1, 0),
  (1701910, 3, 1),
  (1703456, 1, 1),
  (1704949, 3, 2),
  (1705035, 3, 0),
  (1706861, 3, 2),
  (1708776, 1, 0),
  (1708794, 0, 2),
  (1710162, 3, 1),
  (1712135, 0, 2),
  (1714633, 2, 2),
  (1716645, 3, 0),
  (1717108, 3, 0),
  (1719521, 1, 1),
  (1724925, 0, 2),
  (1726024, 2, 0),
  (1727733, 1, 2),
  (1728508, 2, 1),
  (1728938, 3, 2),
  (1730230, 1, 1),
  (1730970, 0, 0),
  (1732015, 0, 0),
  (1733388, 2, 0),
  (1736379, 2, 0),
  (1737054, 3, 0),
  (1739529, 0, 1),
  (1741647, 3, 0),
  (1747648, 0, 1),
  (1747752, 1, 1),
  (1748046, 2, 1),
  (1750773, 3, 2),
  (1752085, 2, 2),
  (1752830, 3, 1),
  (1755255, 0, 0),
  (1755575, 2, 1),
  (1756076, 3, 2),
  (1756887, 1, 0),
  (1762438, 2, 2),
  (1764063, 0, 1),
  (1765594, 2, 2),
  (1766778, 1, 2),
  (1773385, 0, 0),
  (1773865, 2, 0),
  (1776640, 1, 0),
  (1777657, 0, 2),
  (1782382, 3, 0),
  (1788104, 0, 0),
  (1792770, 0, 0),
  (1792920, 3, 0),
  (1796954, 0, 2),
  (1797819, 1, 0),
  (1798369, 1, 1),
  (1800292, 1, 2),
  (1800303, 3, 2),
  (1800647, 0, 1),
  (1803306, 2, 1),
  (1803817, 3, 1),
  (1804135, 0, 0),
  (1806907, 3, 0),
  (1806926, 0, 2),
  (1808880, 1, 1),
  (1809877, 2, 1),
  (1810881, 0, 1),
  (1813259, 0, 1),
  (1814837, 1, 0),
  (1817585, 0, 0),
  (1818307, 2, 0),
  (1818547, 1, 0),
  (1825449, 3, 0),
  (1827716, 3, 2),
  (1829949, 2, 2),
  (1830961, 0, 0),
  (1834206, 1, 1),
  (1835025, 3, 1),
  (1836385, 1, 2),
  (1846125, 2, 0),
  (1846176, 0, 2),
  (1850401, 3, 0),
  (1850758, 1, 0),
  (1852144, 2, 0),
  (1853773, 2, 0),
  (1855450, 3, 2),
  (1858917, 1, 1),
  (1861490, 0, 2),
  (1863856, 2, 2),
  (1863911, 0, 0),
  (1870652, 3, 0),
  (1871555, 0, 1),
  (1871741, 0, 1),
  (1873493, 0, 2),
  (1875385, 0, 0),
  (1876843, 3, 0),
  (1878318, 1, 2),
  (1879256, 1, 2),
  (1880468, 2, 1),
  (1887673, 1, 1),
  (1891358, 2, 1),
  (1892431, 0, 1),
  (1894026, 2, 1),
  (1899102, 3, 0),
  (1899358, 1, 1),
  (1900319, 1, 1),
  (1900733, 2, 1),
  (1902826, 3, 1),
  (1903768, 3, 1),
  (1907930, 3, 1),
  (1910330, 1, 2),
  (1910552, 0, 0),
  (1910557, 3, 1),
  (1917136, 3, 2),
  (1917181, 3, 0),
  (1920352, 0, 0),
  (1922164, 0, 0),
  (1925505, 3, 2),
  (1927370, 2, 1),
  (1928628, 0, 0),
  (1930949, 1, 0),
  (1931502, 3, 0),
  (1934411, 2, 0),
  (1936011, 0, 2),
  (1942916, 1, 2),
  (1946100, 3, 1),
  (1951928, 0, 1),
  (1952633, 1, 0),
  (1953735, 1, 0),
  (1954682, 0, 1),
  (1959388, 3, 2),
  (1960088, 3, 2),
  (1961408, 1, 0),
  (1963841, 2, 0),
  (1968950, 1, 0),
  (1969722, 3, 0),
  (1972087, 1, 0),
  (1974641, 1, 1),
  (1978429, 1, 1),
  (1978738, 3, 0),
  (1982410, 1, 1),
  (1983898, 3, 2),
  (1984307, 1, 2),
  (1986491, 0, 2),
  (1987452, 1, 1),
  (1987480, 2, 1),
  (1987840, 2, 0),
  (1991419, 3, 1),
  (1991540, 2, 1),
  (1992182, 0, 2),
  (1993737, 1, 1),
  (1993999, 3, 2),
  (1996110, 1, 0),
  (1999605, 0, 2),
  (2002038, 3, 1),
  (2002858, 0, 2),
  (2007882, 2, 2),
  (2008004, 3, 1),
  (2009088, 2, 2),
  (2009974, 0, 1),
  (2012626, 3, 1),
  (2013434, 2, 1),
  (2014400, 2, 0),
  (2014922, 3, 1),
  (2020502, 3, 2),
  (2021765, 2, 0),
  (2025897, 0, 0),
  (2027028, 0, 1),
  (2030436, 2, 1),
  (2031286, 1, 0),
  (2031877, 0, 2),
  (2036318, 0, 1),
  (2037500, 3, 1),
  (2038981, 1, 0),
  (2043124, 2, 1),
  (2044168, 2, 2),
  (2045829, 0, 2),
  (2045924, 2, 1),
  (2046502, 2, 0),
  (2048254, 1, 2),
  (2050099, 1, 1),
  (2053449, 0, 0),
  (2056373, 1, 0),
  (2059675, 3, 2),
  (2060745, 1, 2),
  (2061570, 2, 1),
  (2062547, 0, 0),
  (2064932, 0, 2),
  (2066630, 3, 0),
  (2066720, 3, 0),
  (2071068, 0, 0),
  (2071380, 1, 2),
  (2072268, 1, 2),
  (2075317, 1, 0),
  (2075754, 3, 2),
  (2076005, 2, 2),
  (2079070, 1, 2),
  (2080077, 1, 1),
  (2080756, 1, 0),
  (2083454, 0, 0),
  (2085140, 2, 2),
  (2085734, 3, 0),
  (2086656, 2, 0),
  (2087159, 1, 0),
  (2091848, 3, 2),
  (2092043, 2, 1),
  (2092693, 1, 2),
  (2093635, 2, 0),
  (2094247, 3, 0),
  (2095567, 0, 2),
  (2097430, 2, 1),
  (2098009, 2, 0),
  (2102845, 3, 2),
  (2103734, 3, 1),
  (2104232, 2, 2),
  (2105100, 3, 0),
  (2105518, 3, 0),
  (2107947, 0, 2),
  (2110103, 1, 2),
  (2111987, 3, 2),
  (2112188, 3, 0),
  (2113730, 3, 1),
  (2115324, 3, 1),
  (2118112, 3, 0),
  (2119781, 2, 2),
  (2122432, 1, 1),
  (2124090, 0, 1),
  (2125091, 1, 2),
  (2125254, 2, 1),
  (2125789, 2, 2),
  (2126268, 3, 0),
  (2130331, 0, 0),
  (2130405, 0, 1),
  (2133732, 1, 2),
  (2134642, 0, 0),
  (2138171, 0, 1),
  (2138406, 3, 0),
  (2139221, 3, 0),
  (2139230, 1, 1),
  (2141890, 0, 2),
  (2145173, 3, 2),
  (2145239, 0, 2),
  (2145486, 3, 0),
  (2145697, 2, 2),
  (2147574, 3, 0),
  (2148572, 3, 0),
  (2149294, 3, 1),
  (2150927, 1, 2),
  (2152192, 1, 0),
  (2152479, 1, 2),
  (2154889, 3, 1),
  (2155749, 0, 1),
  (2155919, 0, 1),
  (2156293, 1, 2),
  (2160908, 0, 0),
  (2161314, 3, 0),
  (2165816, 1, 1),
  (2166154, 1, 1),
  (2167042, 3, 1),
  (2168957, 2, 2),
  (2177530, 1, 2),
  (2178332, 3, 0),
  (2178492, 0, 1),
  (2187060, 3, 1),
  (2187927, 0, 1),
  (2192220, 3, 1),
  (2193707, 3, 1),
  (2194104, 2, 1),
  (2194125, 0, 0),
  (2196122, 0, 1),
  (2197372, 1, 0),
  (2198305, 0, 1),
  (2201232, 3, 1),
  (2206955, 1, 1),
  (2210265, 2, 2),
  (2213134, 2, 0),
  (2213186, 2, 1),
  (2214656, 0, 0),
  (2218455, 3, 1),
  (2218872, 1, 2),
  (2219477, 2, 2),
  (2221077, 3, 0),
  (2221846, 2, 0),
  (2222887, 0, 0),
  (2225176, 3, 0),
  (2226009, 3, 0),
  (2232593, 1, 2),
  (2233897, 3, 2),
  (2235894, 3, 1),
  (2236432, 1, 1),
  (2238739, 1, 0),
  (2240891, 0, 1),
  (2244316, 3, 1),
  (2245636, 3, 0),
  (2246083, 2, 2),
  (2247666, 0, 0),
  (2250754, 3, 1),
  (2252324, 1, 2),
  (2252734, 1, 1),
  (2255806, 3, 1),
  (2260160, 0, 1),
  (2260949, 3, 0),
  (2262029, 3, 1),
  (2262751, 2, 0),
  (2263773, 2, 2),
  (2263832, 1, 0),
  (2264962, 3, 2),
  (2269834, 2, 1),
  (2272252, 1, 1),
  (2273221, 0, 1),
  (2274208, 0, 1),
  (2274924, 0, 1),
  (2275655, 0, 0),
  (2277531, 0, 2),
  (2281441, 3, 1),
  (2282400, 0, 2),
  (2283136, 0, 0),
  (2285827, 2, 2),
  (2290797, 3, 2),
  (2293378, 1, 2),
  (2295238, 1, 2),
  (2299528, 3, 1),
  (2299935, 1, 1),
  (2302104, 1, 0),
  (2304263, 0, 0),
  (2307422, 2, 0),
  (2308727, 1, 1),
  (2308738, 1, 1),
  (2311681, 3, 0),
  (2313713, 0, 0),
  (2315102, 1, 1),
  (2315296, 2, 1),
  (2319721, 3, 1),
  (2322591, 1, 0),
  (2323286, 1, 1),
  (2323744, 3, 1),
  (2325869, 2, 2),
  (2328745, 0, 1),
  (2330875, 3, 1),
  (2334544, 0, 0),
  (2334548, 2, 1),
  (2339185, 1, 2),
  (2344130, 0, 0),
  (2349406, 1, 2),
  (2350561, 1, 1),
  (2351635, 2, 0),
  (2352184, 3, 0),
  (2352685, 2, 1),
  (2361497, 3, 0),
  (2363729, 3, 2),
  (2365610, 2, 2),
  (2366326, 1, 1),
  (2366729, 3, 2),
  (2369048, 2, 2),
  (2377201, 3, 1),
  (2377427, 3, 2),
  (2380462, 1, 2),
  (2380727, 1, 1),
  (2380874, 1, 0),
  (2380996, 1, 1),
  (2381061, 1, 2),
  (2382503, 0, 0),
  (2382988, 2, 2),
  (2386224, 0, 1),
  (2391013, 1, 0),
  (2391886, 1, 0),
  (2395303, 3, 1),
  (2395572, 3, 2),
  (2397798, 2, 0),
  (2398406, 1, 2),
  (2401080, 1, 0),
  (2403042, 0, 0),
  (2403338, 1, 1),
  (2404754, 0, 0),
  (2404837, 0, 2),
  (2406065, 3, 2),
  (2407526, 0, 1),
  (2407628, 3, 0),
  (2408912, 2, 2),
  (2413252, 0, 1),
  (2415179, 3, 2),
  (2415237, 2, 2),
  (2419678, 1, 1),
  (2424735, 1, 0),
  (2425470, 0, 0),
  (2429091, 1, 1),
  (2431142, 1, 2),
  (2432782, 2, 2),
  (2438541, 0, 2),
  (2439110, 3, 2),
  (2440688, 0, 0),
  (2444912, 0, 1),
  (2444962, 1, 2),
  (2450537, 0, 1),
  (2452017, 1, 1),
  (2454977, 1, 1),
  (2456655, 1, 2),
  (2456801, 1, 0),
  (2458450, 1, 1),
  (2458561, 1, 0),
  (2459174, 1, 2),
  (2460222, 2, 1),
  (2461945, 1, 2),
  (2465018, 3, 0),
  (2468464, 2, 2),
  (2468964, 3, 1),
  (2470008, 3, 0),
  (2470200, 0, 1),
  (2470610, 3, 0),
  (2471510, 2, 1),
  (2474004, 3, 2),
  (2476388, 3, 1),
  (2477632, 2, 0),
  (2479528, 1, 2),
  (2484971, 0, 0),
  (2490137, 2, 1),
  (2491988, 3, 0),
  (2497027, 2, 0),
  (2501558, 1, 0),
  (2502516, 2, 2),
  (2504163, 0, 2),
  (2507549, 2, 0),
  (2511724, 2, 2),
  (2513479, 2, 2),
  (2513606, 0, 1),
  (2516509, 1, 1),
  (2516727, 2, 1),
  (2521865, 3, 2),
  (2526787, 1, 1),
  (2534743, 0, 0),
  (2536110, 0, 2),
  (2536126, 1, 0),
  (2536302, 3, 2),
  (2537259, 1, 1),
  (2546484, 2, 2),
  (2547942, 0, 0),
  (2549134, 0, 2),
  (2550241, 0, 2),
  (2550688, 0, 1),
  (2550819, 0, 0),
  (2553532, 2, 2),
  (2553563, 1, 1),
  (2554298, 1, 0),
  (2558815, 2, 2),
  (2564241, 1, 2),
  (2565138, 1, 1),
  (2571980, 0, 1),
  (2576008, 3, 0),
  (2582245, 2, 2),
  (2584193, 2, 0),
  (2592413, 3, 1),
  (2599095, 2, 2),
  (2601413, 1, 1),
  (2605496, 0, 0),
  (2606088, 0, 2),
  (2608931, 0, 2),
  (2609883, 2, 2),
  (2609938, 2, 1),
  (2609943, 3, 0),
  (2610564, 2, 0),
  (2612417, 1, 2),
  (2617243, 1, 0),
  (2621354, 2, 0),
  (2627333, 2, 0),
  (2627517, 3, 2),
  (2628099, 2, 0),
  (2628535, 0, 2),
  (2630381, 0, 2),
  (2631669, 2, 2),
  (2632058, 3, 1),
  (2632644, 3, 1),
  (2637320, 3, 2),
  (2637582, 3, 0),
  (2640461, 2, 1),
  (2640575, 1, 2),
  (2641964, 0, 1),
  (2643954, 2, 0),
  (2644548, 0, 2),
  (2645335, 3, 0),
  (2646012, 3, 0),
  (2646088, 2, 1),
  (2646853, 3, 1),
  (2652448, 3, 0),
  (2657244, 2, 2),
  (2657328, 2, 0),
  (2657498, 3, 0),
  (2659666, 3, 0),
  (2661508, 3, 0),
  (2665626, 2, 2),
  (2667848, 0, 2),
  (2669481, 0, 0),
  (2669826, 0, 0),
  (2670500, 3, 0),
  (2671454, 3, 0),
  (2671651, 0, 2),
  (2677938, 2, 2),
  (2680401, 3, 1),
  (2681207, 2, 2),
  (2682203, 3, 1),
  (2685333, 2, 2),
  (2695129, 1, 1),
  (2695883, 2, 1),
  (2696868, 0, 0),
  (2698390, 2, 2),
  (2698978, 0, 2),
  (2702344, 3, 1),
  (2702786, 0, 1),
  (2703503, 1, 2),
  (2703697, 3, 2),
  (2703743, 1, 1),
  (2704271, 0, 2),
  (2704687, 1, 1),
  (2705720, 2, 1),
  (2706330, 1, 0),
  (2708054, 3, 2),
  (2708325, 3, 0),
  (2710153, 3, 1),
  (2713143, 0, 2),
  (2714417, 2, 1),
  (2723406, 3, 1),
  (2724344, 2, 0),
  (2725891, 1, 2),
  (2726090, 1, 0),
  (2728735, 3, 1),
  (2729457, 0, 2),
  (2731422, 0, 0),
  (2733709, 1, 2),
  (2733819, 1, 0),
  (2735079, 3, 1),
  (2736847, 0, 1),
  (2738242, 3, 0),
  (2739494, 0, 1),
  (2741314, 1, 2),
  (2742599, 2, 1),
  (2744621, 3, 1),
  (2744635, 2, 0),
  (2745030, 0, 1),
  (2745452, 1, 1),
  (2752779, 2, 1),
  (2753521, 1, 1),
  (2754236, 0, 0),
  (2756090, 3, 1),
  (2759727, 2, 1),
  (2760120, 3, 2),
  (2760567, 1, 2),
  (2761306, 1, 2),
  (2761516, 3, 1),
  (2762254, 0, 0),
  (2764697, 3, 1),
  (2765379, 3, 1),
  (2767123, 0, 0),
  (2767517, 3, 0),
  (2770702, 3, 1),
  (2774446, 0, 2),
  (2774925, 2, 1),
  (2774931, 2, 2),
  (2778659, 0, 1),
  (2780187, 0, 1),
  (2781070, 3, 1),
  (2782623, 1, 1),
  (2791285, 0, 1),
  (2796302, 0, 2),
  (2802079, 0, 0),
  (2804236, 0, 0),
  (2807832, 1, 2),
  (2808478, 1, 2),
  (2808871, 3, 1),
  (2808984, 3, 2),
  (2810608, 3, 2),
  (2810831, 2, 2),
  (2812056, 2, 0),
  (2812909, 3, 2),
  (2813979, 0, 1),
  (2814209, 0, 1),
  (2816707, 1, 0),
  (2816841, 1, 2),
  (2822494, 0, 2),
  (2826466, 3, 0),
  (2827137, 2, 2),
  (2829518, 0, 0),
  (2830783, 3, 0),
  (2831743, 1, 2),
  (2832216, 1, 2),
  (2832752, 1, 2),
  (2834883, 2, 1),
  (2836217, 1, 0),
  (2841790, 2, 0),
  (2841815, 0, 2),
  (2843865, 0, 2),
  (2847337, 2, 2),
  (2847953, 3, 2),
  (2848457, 1, 2),
  (2849473, 1, 0),
  (2853718, 0, 0),
  (2855861, 3, 1),
  (2857803, 3, 0),
  (2863611, 2, 1),
  (2865785, 1, 0),
  (2866328, 0, 1),
  (2867073, 3, 0),
  (2869494, 0, 2),
  (2870771, 3, 1),
  (2872142, 0, 0),
  (2873840, 1, 2),
  (2875589, 0, 1),
  (2877957, 2, 1),
  (2881001, 2, 0),
  (2881219, 0, 1),
  (2883115, 3, 0),
  (2888834, 0, 2),
  (2890054, 2, 0),
  (2891007, 0, 0),
  (2893224, 0, 1),
  (2894704, 3, 2),
  (2896388, 0, 2),
  (2896517, 3, 1),
  (2896673, 2, 0),
  (2898101, 0, 2),
  (2898230, 0, 0),
  (2900695, 2, 2),
  (2901275, 2, 1),
  (2903734, 0, 0),
  (2905661, 1, 0),
  (2906399, 2, 1),
  (2909443, 1, 1),
  (2911450, 3, 1),
  (2917110, 0, 1),
  (2917302, 0, 2),
  (2921066, 3, 2),
  (2921510, 0, 1),
  (2930738, 2, 0),
  (2932188, 1, 2),
  (2935177, 1, 2),
  (2936377, 0, 2),
  (2936449, 3, 1),
  (2939261, 0, 2),
  (2939509, 3, 2),
  (2944090, 2, 0),
  (2944635, 3, 1),
  (2952397, 3, 1),
  (2952543, 1, 1),
  (2954757, 0, 1),
  (2956204, 0, 2),
  (2957664, 0, 2),
  (2959730, 2, 0),
  (2961693, 0, 1),
  (2965760, 1, 0),
  (2966072, 3, 0),
  (2969982, 3, 2),
  (2970708, 2, 1),
  (2970880, 3, 2),
  (2970999, 3, 2),
  (2972880, 3, 2),
  (2975354, 1, 1),
  (2977758, 0, 0),
  (2978703, 2, 2),
  (2984592, 2, 0),
  (2985190, 0, 0),
  (2985598, 1, 2),
  (2987415, 1, 1),
  (2988431, 2, 2),
  (2994622, 3, 2),
  (2994960, 2, 2),
  (2996697, 0, 2),
  (2997489, 1, 1),
  (3000962, 3, 0),
  (3002441, 2, 2),
  (3002994, 3, 2),
  (3004125, 2, 1),
  (3005277, 0, 2),
  (3011262, 3, 0),
  (3017392, 3, 2),
  (3020207, 0, 0),
  (3021477, 0, 0),
  (3023012, 0, 0),
  (3023123, 2, 1),
  (3026196, 3, 1),
  (3031548, 2, 2),
  (3032326, 3, 1),
  (3036820, 2, 1),
  (3040094, 3, 1),
  (3040291, 2, 1),
  (3042742, 0, 2),
  (3046985, 3, 1),
  (3047748, 1, 1),
  (3049393, 1, 2),
  (3051345, 0, 0),
  (3057011, 2, 0),
  (3064094, 2, 1),
  (3065708, 1, 2),
  (3068347, 3, 0),
  (3069318, 2, 2),
  (3079473, 3, 0),
  (3081722, 1, 2),
  (3086072, 3, 2),
  (3086578, 1, 1),
  (3087226, 3, 1),
  (3090484, 1, 2),
  (3090514, 3, 2),
  (3090599, 3, 1),
  (3091053, 3, 0),
  (3091210, 0, 2),
  (3092014, 0, 1),
  (3092041, 3, 0),
  (3095713, 3, 1),
  (3098154, 0, 2),
  (3098297, 0, 0),
  (3100647, 3, 0),
  (3101019, 3, 0),
  (3101167, 1, 0),
  (3101495, 2, 0),
  (3105626, 1, 2),
  (3111569, 0, 0),
  (3114237, 1, 2),
  (3115679, 1, 0),
  (3116849, 1, 2),
  (3124246, 1, 1),
  (3125664, 1, 2),
  (3126923, 2, 2),
  (3127714, 2, 2),
  (3133676, 2, 1),
  (3135231, 1, 1),
  (3135822, 0, 2),
  (3146569, 2, 1),
  (3149706, 2, 2),
  (3150149, 3, 1),
  (3150953, 0, 2),
  (3151271, 2, 2),
  (3152090, 3, 0),
  (3152758, 1, 2),
  (3155826, 3, 2),
  (3156405, 3, 2),
  (3157317, 0, 0),
  (3157401, 1, 0),
  (3158246, 1, 0),
  (3159286, 3, 1),
  (3160238, 1, 1),
  (3163183, 3, 2),
  (3164375, 0, 1),
  (3166410, 3, 0),
  (3167195, 0, 0),
  (3170329, 1, 2),
  (3171349, 0, 2),
  (3173800, 2, 2),
  (3174744, 1, 1),
  (3176976, 2, 2),
  (3180238, 3, 2),
  (3181358, 3, 0),
  (3183389, 3, 1),
  (3184015, 2, 0),
  (3184341, 3, 2),
  (3184643, 0, 0),
  (3185762, 2, 0),
  (3186164, 1, 2),
  (3186847, 1, 1),
  (3192072, 0, 1),
  (3194151, 3, 2),
  (3195681, 0, 0),
  (3197628, 2, 2),
  (3202023, 0, 0),
  (3205396, 2, 0),
  (3208830, 3, 2),
  (3208967, 3, 0),
  (3209046, 0, 1),
  (3213622, 1, 1),
  (3213673, 1, 1),
  (3213838, 0, 0),
  (3216466, 1, 0),
  (3218796, 3, 1),
  (3219824, 3, 2),
  (3220075, 0, 0),
  (3221792, 3, 1),
  (3222694, 1, 2),
  (3222863, 2, 2),
  (3224228, 2, 1),
  (3226040, 1, 2),
  (3226163, 2, 2),
  (3229846, 1, 2),
  (3230749, 1, 2),
  (3237222, 0, 1),
  (3239049, 3, 1),
  (3239382, 3, 0),
  (3240490, 3, 2),
  (3240822, 2, 0),
  (3243959, 1, 1),
  (3253619, 0, 2),
  (3253953, 3, 0),
  (3256914, 0, 2),
  (3264128, 0, 1),
  (3264967, 1, 1),
  (3265668, 2, 0),
  (3266138, 1, 0),
  (3268272, 2, 2),
  (3269930, 1, 2),
  (3271510, 1, 0),
  (3276939, 0, 1),
  (3278892, 0, 2),
  (3279631, 1, 0),
  (3284385, 3, 2),
  (3293355, 1, 2),
  (3295507, 0, 2),
  (3296023, 1, 0),
  (3299257, 0, 2),
  (3299889, 3, 2),
  (3300743, 3, 2),
  (3302582, 3, 2),
  (3303582, 1, 0),
  (3303643, 2, 2),
  (3305886, 0, 0),
  (3306627, 2, 0),
  (3306898, 3, 2),
  (3309460, 1, 2),
  (3309716, 2, 1),
  (3312035, 2, 2),
  (3314663, 0, 2),
  (3320057, 3, 0),
  (3321232, 0, 1),
  (3322670, 1, 0),
  (3324273, 0, 1),
  (3328498, 1, 0),
  (3329642, 3, 1),
  (3329677, 1, 0),
  (3330395, 2, 2),
  (3331313, 1, 1),
  (3333739, 3, 2),
  (3333891, 3, 2),
  (3334365, 0, 1),
  (3334621, 0, 2),
  (3334973, 3, 0),
  (3340135, 0, 1),
  (3342383, 1, 2),
  (3342826, 3, 2),
  (3342862, 1, 2),
  (3343419, 0, 0),
  (3344270, 0, 2),
  (3347075, 3, 0),
  (3348603, 0, 0),
  (3355834, 1, 0),
  (3362089, 0, 2),
  (3363680, 3, 2),
  (3364111, 3, 1),
  (3364225, 0, 1),
  (3368458, 1, 0),
  (3368865, 2, 0),
  (3371482, 1, 0),
  (3371671, 0, 1),
  (3374963, 2, 1),
  (3375416, 1, 2),
  (3376020, 1, 2),
  (3378847, 3, 0),
  (3380286, 2, 2),
  (3380865, 0, 0),
  (3382223, 0, 2),
  (3382261, 0, 2),
  (3382394, 2, 0),
  (3383428, 0, 1),
  (3385705, 2, 2),
  (3387569, 1, 1),
  (3389803, 2, 0),
  (3390436, 0, 0),
  (3394495, 0, 1),
  (3403749, 2, 2),
  (3408096, 2, 1),
  (3408613, 3, 2),
  (3408899, 0, 1),
  (3409721, 3, 0),
  (3411046, 2, 0),
  (3412198, 1, 0),
  (3413236, 2, 1),
  (3416433, 0, 2),
  (3416626, 0, 2),
  (3417585, 3, 1),
  (3418444, 1, 1),
  (3419244, 3, 2),
  (3419752, 0, 0),
  (3421988, 0, 0),
  (3423795, 2, 1),
  (3424188, 3, 1),
  (3425414, 3, 2),
  (3432550, 2, 2),
  (3436172, 2, 2),
  (3436735, 3, 0),
  (3438258, 3, 2),
  (3441372, 2, 0),
  (3443195, 0, 1),
  (3445788, 1, 2),
  (3448323, 2, 0),
  (3452561, 3, 1),
  (3452797, 2, 2),
  (3453573, 0, 0),
  (3456866, 2, 1),
  (3457480, 0, 1),
  (3457669, 0, 0),
  (3458218, 0, 0),
  (3458699, 3, 2),
  (3459048, 3, 1),
  (3466206, 0, 1),
  (3466335, 3, 1),
  (3468586, 2, 1),
  (3469525, 3, 0),
  (3470729, 1, 0),
  (3472288, 1, 2),
  (3475233, 0, 1),
  (3475373, 3, 2),
  (3478682, 2, 2),
  (3479031, 3, 1),
  (3480528, 1, 0),
  (3480915, 0, 0),
  (3483273, 3, 0),
  (3488263, 1, 1),
  (3490556, 1, 1),
  (3490859, 3, 0),
  (3495437, 3, 2),
  (3497385, 1, 2),
  (3498384, 3, 2),
  (3508363, 2, 1),
  (3510574, 2, 2),
  (3512074, 0, 0),
  (3514940, 1, 1),
  (3523121, 3, 1),
  (3525114, 1, 0),
  (3529311, 3, 1),
  (3531023, 0, 1),
  (3531853, 0, 2),
  (3532321, 1, 1),
  (3533780, 1, 1),
  (3534647, 0, 1),
  (3535027, 0, 0),
  (3535556, 2, 2),
  (3540933, 1, 1),
  (3541464, 2, 0),
  (3541678, 1, 1),
  (3541913, 2, 0),
  (3542799, 1, 2),
  (3544885, 0, 0),
  (3545302, 2, 1),
  (3546536, 3, 0),
  (3547303, 1, 2),
  (3548612, 2, 1),
  (3548956, 2, 0),
  (3550129, 3, 2),
  (3557189, 3, 2),
  (3557747, 1, 1),
  (3563492, 2, 0),
  (3565379, 0, 1),
  (3568175, 0, 2),
  (3568551, 2, 0),
  (3568582, 1, 2),
  (3570193, 0, 2),
  (3570360, 1, 2),
  (3571145, 1, 1),
  (3572353, 3, 2),
  (3572683, 3, 1),
  (3579219, 0, 1),
  (3579647, 2, 2),
  (3580776, 3, 0),
  (3584860, 1, 2),
  (3585830, 0, 1),
  (3587017, 3, 2),
  (3587773, 3, 0),
  (3591129, 3, 0),
  (3591219, 3, 1),
  (3591299, 1, 1),
  (3593160, 3, 2),
  (3593428, 3, 1),
  (3594548, 3, 2),
  (3596432, 3, 0),
  (3596639, 3, 2),
  (3599074, 3, 2),
])
