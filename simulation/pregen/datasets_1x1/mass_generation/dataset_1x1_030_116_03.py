from util import *
schedule = deque([
  (1066, 7, 7),
  (4225, 6, 3),
  (4455, 0, 7),
  (8644, 6, 7),
  (8847, 2, 7),
  (9326, 0, 0),
  (10404, 3, 7),
  (10925, 4, 7),
  (12221, 5, 5),
  (16537, 4, 7),
  (20668, 4, 3),
  (21016, 5, 7),
  (21710, 6, 4),
  (22168, 6, 5),
  (23776, 5, 3),
  (25245, 6, 7),
  (26338, 2, 7),
  (26614, 7, 7),
  (26837, 1, 7),
  (27838, 1, 7),
  (28134, 5, 7),
  (29393, 0, 7),
  (29682, 3, 7),
  (29769, 4, 6),
  (29895, 5, 7),
  (33681, 1, 3),
  (34558, 7, 0),
  (35670, 2, 6),
  (37147, 6, 7),
  (40925, 7, 4),
  (41471, 1, 7),
  (43333, 7, 7),
  (47257, 1, 3),
  (48585, 4, 7),
  (50008, 7, 7),
  (53848, 5, 3),
  (57822, 0, 0),
  (59178, 2, 6),
  (60503, 4, 7),
  (63675, 2, 7),
  (65239, 7, 7),
  (65315, 0, 7),
  (66823, 3, 7),
  (69008, 6, 0),
  (71541, 0, 7),
  (79491, 3, 5),
  (81111, 6, 7),
  (81112, 2, 3),
  (82273, 5, 3),
  (84342, 0, 0),
  (85762, 0, 7),
  (88719, 7, 7),
  (88896, 0, 7),
  (90327, 3, 3),
  (90824, 0, 0),
  (91927, 3, 7),
  (98394, 7, 7),
  (101334, 0, 7),
  (102214, 5, 7),
  (103374, 2, 7),
  (108168, 3, 7),
  (111679, 4, 7),
  (112051, 5, 6),
  (114557, 2, 3),
  (116365, 1, 7),
  (116968, 0, 3),
  (121644, 3, 7),
  (125779, 0, 6),
  (128359, 5, 5),
  (129092, 4, 7),
  (133480, 3, 3),
  (134670, 2, 5),
  (136259, 4, 7),
  (137239, 5, 7),
  (138988, 3, 7),
  (141804, 1, 7),
  (145409, 5, 7),
  (147293, 4, 7),
  (150642, 0, 7),
  (150801, 3, 7),
  (157507, 0, 3),
  (157892, 0, 3),
  (158814, 3, 3),
  (161158, 5, 7),
  (164440, 5, 2),
  (164497, 7, 5),
  (165469, 6, 7),
  (165585, 0, 4),
  (167713, 1, 3),
  (169163, 3, 7),
  (172076, 4, 7),
  (177284, 2, 7),
  (179684, 7, 7),
  (181292, 2, 7),
  (181818, 3, 7),
  (185535, 0, 7),
  (189370, 1, 7),
  (190642, 3, 7),
  (192657, 7, 7),
  (194318, 4, 7),
  (198493, 6, 0),
  (203705, 5, 7),
  (205062, 5, 3),
  (205659, 6, 4),
  (205701, 6, 3),
  (205827, 6, 7),
  (208631, 2, 7),
  (209593, 7, 7),
  (220177, 4, 7),
  (221144, 4, 2),
  (222514, 5, 5),
  (222808, 4, 7),
  (222913, 3, 7),
  (226733, 5, 7),
  (229832, 5, 7),
  (230114, 0, 7),
  (230789, 4, 7),
  (231029, 7, 7),
  (231367, 6, 0),
  (235887, 0, 7),
  (236395, 0, 7),
  (236975, 6, 7),
  (237174, 3, 7),
  (237472, 0, 7),
  (242567, 5, 7),
  (244363, 7, 7),
  (245148, 7, 7),
  (246164, 1, 7),
  (250869, 7, 7),
  (255131, 0, 3),
  (258449, 4, 5),
  (261494, 7, 7),
  (262424, 3, 7),
  (263874, 0, 3),
  (265027, 4, 7),
  (266467, 0, 7),
  (266534, 6, 7),
  (268702, 5, 7),
  (269378, 5, 7),
  (269540, 6, 7),
  (272577, 0, 4),
  (275107, 5, 2),
  (278633, 1, 3),
  (290145, 2, 7),
  (291051, 1, 7),
  (291389, 7, 4),
  (293982, 1, 7),
  (296343, 7, 7),
  (296573, 7, 0),
  (297450, 6, 7),
  (298010, 0, 7),
  (299404, 1, 7),
  (299414, 6, 7),
  (302088, 3, 7),
  (307310, 5, 7),
  (308718, 3, 3),
  (308802, 4, 7),
  (309617, 3, 7),
  (318946, 3, 7),
  (321420, 3, 7),
  (325766, 3, 6),
  (326546, 1, 7),
  (327696, 5, 3),
  (328899, 4, 7),
  (328930, 2, 7),
  (331747, 7, 3),
  (332036, 7, 7),
  (332190, 5, 7),
  (334932, 0, 0),
  (337884, 2, 3),
  (340999, 3, 7),
  (341657, 1, 7),
  (342776, 2, 7),
  (346230, 1, 0),
  (350246, 6, 7),
  (351288, 5, 7),
  (353741, 7, 7),
  (354294, 0, 7),
  (355936, 2, 7),
  (356147, 0, 4),
  (356304, 5, 7),
  (360398, 1, 7),
  (361125, 5, 7),
  (361390, 5, 7),
  (362555, 7, 7),
  (363885, 5, 7),
  (365073, 1, 6),
  (365798, 2, 7),
  (366637, 1, 0),
  (366876, 2, 7),
  (367336, 5, 7),
  (368027, 1, 7),
  (368232, 1, 7),
  (369793, 5, 7),
  (374397, 6, 7),
  (375398, 2, 2),
  (375876, 0, 7),
  (376534, 4, 7),
  (385208, 3, 3),
  (385380, 2, 2),
  (387624, 0, 5),
  (390945, 7, 7),
  (401476, 4, 7),
  (401523, 4, 6),
  (403407, 0, 7),
  (405227, 2, 3),
  (410013, 3, 7),
  (410367, 4, 7),
  (418155, 7, 0),
  (425871, 2, 5),
  (429014, 1, 7),
  (437992, 4, 7),
  (440414, 1, 6),
  (444990, 0, 7),
  (448504, 2, 7),
  (449405, 5, 7),
  (454059, 2, 7),
  (456853, 1, 7),
  (457362, 4, 7),
  (462020, 4, 7),
  (468385, 0, 7),
  (468830, 7, 0),
  (468896, 0, 7),
  (469590, 0, 7),
  (471868, 2, 7),
  (473398, 3, 7),
  (473527, 0, 4),
  (475670, 0, 7),
  (476525, 5, 6),
  (477457, 1, 7),
  (477529, 5, 7),
  (482098, 0, 7),
  (486313, 1, 7),
  (486519, 4, 7),
  (492557, 0, 7),
  (496888, 3, 7),
  (503028, 2, 3),
  (504796, 1, 7),
  (506944, 0, 7),
  (507060, 3, 7),
  (508875, 7, 4),
  (509520, 7, 7),
  (509539, 0, 7),
  (510044, 2, 7),
  (513325, 6, 7),
  (513440, 6, 4),
  (514059, 2, 7),
  (517917, 6, 7),
  (519997, 2, 7),
  (520761, 0, 7),
  (521991, 2, 6),
  (524555, 7, 7),
  (526892, 3, 7),
  (527153, 5, 7),
  (528256, 3, 0),
  (528824, 7, 7),
  (529899, 7, 7),
  (531284, 6, 7),
  (532710, 3, 2),
  (535429, 4, 7),
  (535609, 0, 4),
  (536480, 7, 7),
  (541268, 4, 6),
  (546913, 1, 7),
  (552310, 4, 7),
  (555441, 7, 7),
  (559233, 7, 3),
  (561063, 1, 0),
  (562891, 3, 7),
  (563920, 3, 6),
  (566470, 1, 7),
  (566940, 6, 7),
  (567164, 5, 3),
  (571697, 1, 3),
  (572901, 2, 5),
  (574085, 2, 7),
  (575129, 4, 6),
  (576561, 3, 7),
  (580559, 2, 7),
  (582193, 7, 3),
  (583434, 0, 3),
  (589980, 2, 7),
  (593386, 0, 0),
  (597207, 2, 2),
  (599717, 5, 2),
  (602381, 6, 7),
  (602586, 3, 6),
  (605599, 1, 7),
  (606854, 3, 2),
  (607426, 7, 7),
  (611899, 6, 7),
  (612322, 2, 6),
  (613131, 4, 7),
  (615612, 6, 7),
  (615714, 4, 4),
  (616073, 0, 1),
  (616264, 6, 7),
  (620509, 2, 7),
  (623045, 6, 0),
  (623856, 0, 4),
  (629440, 1, 7),
  (631683, 3, 7),
  (631700, 0, 7),
  (632810, 0, 7),
  (633460, 0, 7),
  (633665, 6, 7),
  (634619, 5, 5),
  (637682, 0, 7),
  (641472, 4, 7),
  (641884, 7, 7),
  (642726, 6, 6),
  (644749, 0, 7),
  (647753, 4, 7),
  (648450, 2, 2),
  (649240, 2, 6),
  (649623, 6, 7),
  (650117, 7, 7),
  (650238, 6, 7),
  (651326, 7, 7),
  (652197, 1, 0),
  (653738, 5, 6),
  (657947, 2, 7),
  (662275, 4, 7),
  (662740, 2, 7),
  (664572, 4, 3),
  (665689, 4, 3),
  (668536, 5, 7),
  (670350, 7, 7),
  (675101, 0, 7),
  (678313, 3, 7),
  (678340, 5, 7),
  (681481, 7, 7),
  (684268, 2, 7),
  (684459, 1, 0),
  (686906, 5, 7),
  (686974, 4, 7),
  (689860, 4, 5),
  (690834, 6, 3),
  (693239, 3, 7),
  (694469, 3, 7),
  (708201, 1, 7),
  (710080, 2, 7),
  (710410, 1, 7),
  (711984, 0, 7),
  (712392, 6, 7),
  (713703, 5, 7),
  (716542, 1, 7),
  (717525, 4, 6),
  (719740, 6, 3),
  (722598, 7, 7),
  (725659, 6, 2),
  (725997, 1, 4),
  (729094, 6, 7),
  (729556, 6, 7),
  (729657, 5, 3),
  (729672, 1, 7),
  (729839, 4, 3),
  (735807, 5, 3),
  (743080, 7, 7),
  (743587, 3, 7),
  (745865, 5, 7),
  (746191, 5, 7),
  (748084, 0, 0),
  (749928, 1, 0),
  (750854, 7, 0),
  (752371, 4, 7),
  (752402, 7, 6),
  (757163, 1, 7),
  (759145, 7, 7),
  (762667, 1, 6),
  (763010, 7, 6),
  (768966, 7, 7),
  (769886, 2, 7),
  (771112, 2, 2),
  (773891, 7, 7),
  (774441, 7, 7),
  (775159, 4, 2),
  (775959, 5, 2),
  (776300, 5, 7),
  (777323, 1, 0),
  (779708, 5, 3),
  (779765, 2, 7),
  (780624, 4, 7),
  (784804, 1, 3),
  (785721, 1, 7),
  (789283, 2, 6),
  (789666, 7, 6),
  (790758, 5, 7),
  (793371, 5, 7),
  (794226, 2, 6),
  (794550, 5, 7),
  (796953, 6, 7),
  (797878, 0, 7),
  (798805, 0, 7),
  (799614, 7, 7),
  (801286, 1, 7),
  (802032, 3, 7),
  (806335, 0, 0),
  (811012, 2, 2),
  (814829, 1, 3),
  (816300, 1, 4),
  (816613, 6, 7),
  (818407, 7, 0),
  (818784, 0, 7),
  (820859, 2, 2),
  (822386, 2, 5),
  (822451, 3, 7),
  (829407, 6, 7),
  (843585, 6, 7),
  (849153, 1, 7),
  (850320, 2, 2),
  (851876, 4, 6),
  (853543, 1, 7),
  (855260, 0, 3),
  (862297, 3, 2),
  (864970, 4, 3),
  (866394, 0, 7),
  (866394, 5, 5),
  (868238, 2, 7),
  (873027, 4, 2),
  (875040, 7, 7),
  (877587, 1, 7),
  (877618, 7, 0),
  (878445, 6, 7),
  (881319, 0, 0),
  (883408, 0, 7),
  (889389, 6, 0),
  (890120, 1, 0),
  (890504, 7, 7),
  (892265, 7, 3),
  (897056, 1, 0),
  (897504, 2, 1),
  (898073, 1, 7),
  (898894, 7, 7),
  (898918, 3, 7),
  (899961, 4, 3),
  (900310, 4, 3),
  (903083, 2, 6),
  (914744, 7, 7),
  (917939, 7, 7),
  (918859, 4, 3),
  (919245, 1, 4),
  (923150, 2, 7),
  (923634, 3, 2),
  (929991, 0, 7),
  (932320, 1, 7),
  (933032, 5, 3),
  (933524, 4, 7),
  (934769, 7, 7),
  (936781, 3, 3),
  (937701, 5, 7),
  (943693, 2, 7),
  (944057, 0, 7),
  (948399, 0, 3),
  (948470, 7, 4),
  (949307, 6, 7),
  (950852, 7, 7),
  (955007, 6, 7),
  (956458, 1, 7),
  (958018, 1, 7),
  (958700, 3, 3),
  (958813, 0, 7),
  (964295, 1, 7),
  (964516, 4, 7),
  (964607, 1, 7),
  (965422, 1, 7),
  (967154, 7, 4),
  (969742, 7, 7),
  (974463, 4, 3),
  (978637, 2, 5),
  (981792, 1, 4),
  (982493, 3, 7),
  (983645, 2, 7),
  (983965, 7, 0),
  (986410, 4, 3),
  (990415, 2, 7),
  (992816, 7, 7),
  (993851, 7, 7),
  (1001618, 4, 7),
  (1001713, 5, 7),
  (1003997, 5, 7),
  (1006333, 4, 7),
  (1006467, 1, 7),
  (1008162, 5, 4),
  (1009918, 5, 7),
  (1012738, 4, 3),
  (1015597, 7, 7),
  (1017356, 3, 7),
  (1018218, 5, 7),
  (1023062, 3, 7),
  (1027662, 2, 7),
  (1029406, 5, 5),
  (1031011, 3, 7),
  (1032650, 4, 7),
  (1039087, 6, 3),
  (1043082, 5, 7),
  (1049835, 2, 6),
  (1049840, 0, 7),
  (1050446, 2, 7),
  (1051404, 6, 7),
  (1051711, 3, 3),
  (1054555, 1, 7),
  (1055177, 6, 0),
  (1056607, 2, 2),
  (1057246, 3, 3),
  (1057935, 5, 7),
  (1060625, 4, 7),
  (1066277, 0, 4),
  (1068181, 4, 7),
  (1069608, 7, 7),
  (1070298, 6, 6),
  (1071343, 7, 3),
  (1071412, 0, 7),
  (1073175, 6, 0),
  (1075809, 0, 3),
  (1082688, 3, 7),
  (1083523, 7, 7),
  (1083800, 5, 6),
  (1086521, 1, 2),
  (1090312, 3, 5),
  (1097343, 5, 2),
  (1098150, 0, 3),
  (1100000, 1, 7),
  (1106629, 7, 7),
  (1108082, 0, 6),
  (1108746, 6, 7),
  (1108785, 4, 7),
  (1109528, 1, 7),
  (1113023, 1, 7),
  (1114416, 6, 3),
  (1118847, 7, 7),
  (1119394, 2, 7),
  (1120001, 0, 3),
  (1120111, 5, 5),
  (1122483, 0, 7),
  (1124353, 0, 4),
  (1125311, 5, 7),
  (1127695, 6, 6),
  (1129020, 5, 7),
  (1129546, 7, 6),
  (1136049, 4, 6),
  (1136302, 7, 7),
  (1138688, 3, 7),
  (1139246, 4, 7),
  (1140536, 4, 2),
  (1140898, 3, 7),
  (1143598, 6, 7),
  (1150385, 2, 7),
  (1150932, 5, 7),
  (1151454, 6, 7),
  (1152570, 1, 7),
  (1153052, 7, 3),
  (1153383, 3, 7),
  (1156646, 7, 6),
  (1156714, 3, 6),
  (1157295, 1, 2),
  (1159397, 6, 4),
  (1161381, 4, 7),
  (1161815, 1, 7),
  (1163506, 0, 4),
  (1164854, 4, 7),
  (1168204, 2, 7),
  (1168634, 6, 7),
  (1169033, 4, 3),
  (1172143, 3, 6),
  (1172495, 3, 7),
  (1173629, 2, 7),
  (1173664, 5, 6),
  (1175088, 1, 7),
  (1176220, 5, 7),
  (1179611, 3, 7),
  (1180387, 7, 3),
  (1184558, 6, 0),
  (1187044, 3, 4),
  (1189156, 6, 7),
  (1197187, 1, 6),
  (1201194, 7, 7),
  (1202798, 2, 7),
  (1206800, 6, 6),
  (1208512, 5, 7),
  (1209159, 4, 2),
  (1211400, 5, 5),
  (1217368, 3, 2),
  (1227872, 3, 7),
  (1230137, 2, 7),
  (1233693, 0, 0),
  (1237304, 6, 7),
  (1241137, 2, 7),
  (1241164, 5, 6),
  (1246443, 1, 3),
  (1247215, 6, 4),
  (1247481, 0, 3),
  (1248616, 6, 7),
  (1252317, 7, 4),
  (1252718, 4, 2),
  (1255092, 1, 7),
  (1257377, 0, 3),
  (1257812, 7, 7),
  (1261976, 4, 3),
  (1264211, 5, 5),
  (1265404, 0, 7),
  (1267145, 6, 4),
  (1270891, 2, 6),
  (1273401, 1, 7),
  (1276588, 1, 7),
  (1277671, 7, 7),
  (1279764, 3, 7),
  (1280656, 7, 3),
  (1280968, 3, 7),
  (1286822, 1, 7),
  (1287688, 7, 4),
  (1288802, 3, 7),
  (1290480, 7, 2),
  (1291923, 0, 4),
  (1293351, 0, 4),
  (1301555, 0, 6),
  (1306723, 4, 7),
  (1307493, 4, 7),
  (1308383, 0, 4),
  (1310468, 1, 0),
  (1311309, 6, 7),
  (1311310, 0, 7),
  (1313652, 5, 5),
  (1313718, 5, 6),
  (1319126, 1, 7),
  (1320045, 2, 5),
  (1320206, 6, 7),
  (1320238, 3, 7),
  (1320353, 2, 2),
  (1321241, 7, 7),
  (1322688, 0, 7),
  (1322855, 1, 6),
  (1323997, 6, 7),
  (1324820, 3, 7),
  (1325220, 1, 4),
  (1325285, 4, 7),
  (1325987, 3, 7),
  (1327238, 4, 2),
  (1331257, 6, 7),
  (1332925, 3, 7),
  (1334162, 0, 7),
  (1338344, 7, 7),
  (1339249, 7, 4),
  (1342879, 2, 2),
  (1344126, 4, 7),
  (1344185, 6, 0),
  (1346555, 5, 7),
  (1347057, 2, 3),
  (1352221, 4, 7),
  (1352883, 4, 7),
  (1354827, 1, 7),
  (1355815, 7, 4),
  (1355826, 2, 3),
  (1358648, 7, 7),
  (1358786, 2, 4),
  (1359987, 4, 7),
  (1361602, 1, 7),
  (1362998, 6, 6),
  (1364010, 0, 2),
  (1367196, 7, 7),
  (1369377, 6, 7),
  (1370768, 2, 5),
  (1372529, 2, 3),
  (1377783, 7, 7),
  (1377973, 6, 7),
  (1382369, 3, 7),
  (1383834, 7, 7),
  (1385349, 1, 0),
  (1387094, 4, 7),
  (1388874, 1, 3),
  (1391049, 2, 2),
  (1391099, 0, 3),
  (1393894, 6, 7),
  (1394385, 7, 0),
  (1395538, 3, 2),
  (1397235, 7, 7),
  (1400892, 5, 7),
  (1401868, 0, 6),
  (1402193, 2, 6),
  (1407191, 2, 7),
  (1409884, 4, 6),
  (1409938, 1, 7),
  (1415827, 4, 7),
  (1419597, 4, 3),
  (1420514, 5, 7),
  (1429936, 0, 7),
  (1431592, 3, 7),
  (1433473, 6, 7),
  (1433648, 2, 7),
  (1435668, 4, 7),
  (1436031, 5, 2),
  (1439790, 0, 3),
  (1442431, 5, 7),
  (1442962, 4, 7),
  (1444896, 3, 7),
  (1447570, 1, 3),
  (1448317, 5, 7),
  (1448557, 5, 7),
  (1450478, 3, 3),
  (1450787, 3, 7),
  (1456353, 7, 7),
  (1457705, 3, 2),
  (1459621, 7, 7),
  (1460250, 4, 3),
  (1462436, 7, 7),
  (1463134, 7, 3),
  (1464307, 0, 0),
  (1464530, 4, 7),
  (1464544, 7, 3),
  (1468253, 5, 7),
  (1468316, 2, 3),
  (1474974, 1, 7),
  (1475593, 1, 0),
  (1475941, 5, 7),
  (1483247, 2, 3),
  (1483399, 5, 7),
  (1487810, 7, 6),
  (1490120, 6, 7),
  (1490586, 0, 7),
  (1490982, 1, 7),
  (1491758, 5, 7),
  (1496836, 3, 7),
  (1502204, 4, 7),
  (1504776, 3, 7),
  (1505168, 5, 7),
  (1506950, 7, 7),
  (1508736, 5, 7),
  (1513609, 2, 7),
  (1513779, 7, 7),
  (1514568, 2, 3),
  (1515051, 1, 3),
  (1518948, 1, 7),
  (1521322, 2, 7),
  (1525384, 2, 7),
  (1527488, 2, 3),
  (1535072, 5, 5),
  (1538024, 1, 3),
  (1540735, 4, 3),
  (1547180, 3, 7),
  (1552502, 5, 2),
  (1559021, 3, 5),
  (1563385, 0, 0),
  (1564689, 3, 6),
  (1565998, 4, 7),
  (1566391, 2, 7),
  (1567586, 3, 2),
  (1568241, 1, 7),
  (1574183, 5, 6),
  (1576039, 0, 3),
  (1578191, 1, 0),
  (1579679, 2, 3),
  (1579834, 5, 7),
  (1580114, 1, 7),
  (1580715, 2, 7),
  (1583640, 6, 0),
  (1586292, 7, 7),
  (1586549, 0, 3),
  (1592999, 3, 7),
  (1593348, 3, 3),
  (1595678, 1, 0),
  (1596594, 7, 7),
  (1597221, 1, 0),
  (1597410, 2, 3),
  (1600653, 1, 6),
  (1600898, 6, 0),
  (1601641, 1, 7),
  (1603559, 5, 7),
  (1609346, 3, 2),
  (1610526, 3, 5),
  (1613482, 5, 7),
  (1613749, 1, 7),
  (1614946, 1, 3),
  (1615152, 7, 7),
  (1616382, 2, 7),
  (1617309, 2, 2),
  (1620561, 7, 7),
  (1621931, 4, 5),
  (1622537, 7, 7),
  (1624641, 2, 7),
  (1625484, 4, 4),
  (1626589, 1, 7),
  (1632345, 1, 7),
  (1632348, 5, 7),
  (1635163, 2, 6),
  (1635208, 0, 7),
  (1638440, 2, 7),
  (1643923, 7, 7),
  (1645285, 7, 7),
  (1645513, 6, 7),
  (1647211, 5, 3),
  (1648696, 7, 7),
  (1649953, 0, 7),
  (1650348, 5, 7),
  (1652812, 6, 7),
  (1655154, 4, 7),
  (1655429, 1, 0),
  (1656902, 5, 2),
  (1656903, 6, 7),
  (1658779, 3, 7),
  (1658888, 5, 5),
  (1660532, 4, 7),
  (1661116, 1, 7),
  (1665964, 2, 7),
  (1666669, 5, 4),
  (1669164, 3, 7),
  (1670446, 4, 7),
  (1672232, 6, 7),
  (1674088, 4, 7),
  (1676679, 7, 3),
  (1677349, 5, 7),
  (1679297, 4, 2),
  (1679304, 3, 7),
  (1679353, 6, 6),
  (1680932, 7, 7),
  (1686908, 3, 6),
  (1687071, 2, 7),
  (1687093, 0, 0),
  (1687782, 1, 7),
  (1688436, 5, 5),
  (1688979, 2, 7),
  (1690958, 4, 7),
  (1692947, 6, 7),
  (1694437, 0, 6),
  (1695327, 5, 7),
  (1697997, 2, 7),
  (1701541, 2, 3),
  (1703729, 1, 7),
  (1706955, 7, 7),
  (1708548, 4, 7),
  (1717471, 5, 7),
  (1718784, 7, 7),
  (1720868, 0, 0),
  (1721139, 2, 7),
  (1723623, 6, 4),
  (1725724, 6, 7),
  (1726168, 5, 1),
  (1726778, 3, 7),
  (1729845, 5, 5),
  (1731659, 6, 7),
  (1734693, 1, 0),
  (1736678, 6, 0),
  (1738407, 6, 7),
  (1739606, 6, 7),
  (1740480, 4, 2),
  (1741294, 0, 7),
  (1741441, 2, 3),
  (1744014, 0, 0),
  (1746799, 5, 7),
  (1746881, 3, 5),
  (1749172, 1, 7),
  (1750130, 3, 7),
  (1750963, 1, 7),
  (1753402, 4, 7),
  (1753598, 3, 2),
  (1755005, 7, 7),
  (1755778, 3, 6),
  (1756297, 2, 6),
  (1757972, 1, 3),
  (1761705, 6, 7),
  (1763900, 2, 3),
  (1765450, 2, 7),
  (1765865, 7, 5),
  (1765960, 0, 4),
  (1766112, 3, 7),
  (1767195, 1, 7),
  (1767923, 1, 7),
  (1774012, 2, 7),
  (1775831, 7, 4),
  (1779311, 0, 7),
  (1779561, 6, 4),
  (1784374, 1, 7),
  (1786166, 4, 7),
  (1786857, 3, 7),
  (1789896, 3, 3),
  (1794919, 2, 7),
  (1795341, 1, 7),
  (1796365, 4, 7),
  (1799604, 5, 5),
  (1800424, 0, 2),
  (1800865, 4, 7),
  (1804071, 5, 5),
  (1807954, 1, 7),
  (1809121, 4, 6),
  (1812267, 0, 3),
  (1814875, 4, 7),
  (1819211, 0, 7),
  (1820351, 6, 6),
  (1820764, 2, 7),
  (1821573, 7, 7),
  (1822755, 7, 7),
  (1824211, 4, 6),
  (1826055, 0, 7),
  (1829793, 5, 7),
  (1831440, 3, 7),
  (1835694, 0, 7),
  (1837850, 5, 7),
  (1838075, 0, 3),
  (1839761, 5, 7),
  (1840579, 1, 7),
  (1842240, 0, 0),
  (1845002, 6, 7),
  (1854134, 6, 7),
  (1856408, 5, 7),
  (1858946, 3, 7),
  (1859560, 7, 0),
  (1859887, 6, 7),
  (1860264, 6, 7),
  (1865213, 1, 7),
  (1866822, 5, 7),
  (1874563, 2, 7),
  (1878658, 1, 0),
  (1882266, 2, 2),
  (1882565, 2, 5),
  (1884044, 4, 1),
  (1890359, 6, 7),
  (1890811, 2, 7),
  (1899191, 7, 7),
  (1904800, 2, 2),
  (1908748, 0, 3),
  (1909033, 1, 0),
  (1915238, 0, 6),
  (1915781, 0, 3),
  (1921970, 5, 7),
  (1923884, 5, 7),
  (1923957, 5, 7),
  (1924419, 0, 3),
  (1931439, 7, 0),
  (1932728, 7, 7),
  (1934153, 2, 6),
  (1934323, 6, 7),
  (1935241, 7, 7),
  (1935389, 5, 7),
  (1936909, 3, 7),
  (1938594, 1, 7),
  (1939291, 0, 0),
  (1939454, 3, 6),
  (1940497, 6, 7),
  (1942662, 4, 7),
  (1942968, 5, 7),
  (1943044, 1, 7),
  (1943789, 4, 3),
  (1943866, 2, 3),
  (1944358, 3, 7),
  (1946629, 4, 7),
  (1946878, 2, 5),
  (1951692, 1, 0),
  (1951699, 5, 2),
  (1955682, 1, 7),
  (1956055, 5, 7),
  (1957274, 7, 5),
  (1957483, 4, 7),
  (1962891, 7, 7),
  (1964050, 1, 7),
  (1966428, 3, 7),
  (1967180, 3, 7),
  (1967835, 0, 4),
  (1967974, 1, 6),
  (1970740, 5, 7),
  (1975269, 4, 7),
  (1976052, 1, 7),
  (1977181, 0, 0),
  (1977974, 6, 0),
  (1978795, 6, 7),
  (1981727, 3, 2),
  (1982244, 0, 6),
  (1983959, 7, 6),
  (1984564, 6, 6),
  (1984692, 4, 7),
  (1987151, 2, 3),
  (1987419, 7, 7),
  (1988544, 5, 3),
  (1989005, 6, 3),
  (1990332, 0, 4),
  (1994288, 0, 7),
  (1996208, 3, 7),
  (1996214, 2, 3),
  (1996325, 3, 7),
  (1996578, 5, 7),
  (2001008, 5, 7),
  (2002840, 0, 7),
  (2004171, 7, 7),
  (2004507, 7, 4),
  (2005337, 4, 7),
  (2009513, 7, 3),
  (2010174, 7, 7),
  (2014129, 4, 7),
  (2015751, 5, 7),
  (2019598, 4, 7),
  (2020530, 3, 7),
  (2021541, 6, 7),
  (2023158, 6, 7),
  (2028216, 1, 7),
  (2030938, 7, 0),
  (2035320, 6, 7),
  (2035481, 2, 7),
  (2038473, 4, 4),
  (2039458, 4, 7),
  (2046021, 6, 4),
  (2046311, 3, 6),
  (2048268, 7, 7),
  (2051470, 2, 7),
  (2052171, 5, 7),
  (2053643, 4, 7),
  (2055632, 1, 7),
  (2058949, 1, 7),
  (2064171, 0, 7),
  (2064360, 6, 0),
  (2065684, 4, 7),
  (2066541, 3, 7),
  (2067265, 7, 7),
  (2068206, 1, 7),
  (2070979, 3, 7),
  (2072774, 6, 7),
  (2074759, 4, 3),
  (2084767, 4, 7),
  (2085165, 0, 7),
  (2087025, 3, 5),
  (2087898, 2, 5),
  (2089354, 7, 3),
  (2091557, 6, 4),
  (2094017, 3, 2),
  (2094312, 2, 7),
  (2097477, 5, 7),
  (2099432, 5, 3),
  (2101210, 6, 7),
  (2103495, 6, 7),
  (2105037, 4, 2),
  (2107363, 2, 7),
  (2109488, 3, 7),
  (2110222, 3, 7),
  (2111807, 0, 7),
  (2115365, 7, 7),
  (2117564, 7, 7),
  (2119666, 5, 7),
  (2119920, 4, 6),
  (2121510, 3, 7),
  (2121700, 1, 2),
  (2129779, 3, 2),
  (2132469, 3, 6),
  (2134107, 0, 7),
  (2134772, 7, 7),
  (2135426, 3, 2),
  (2136191, 4, 6),
  (2137927, 4, 7),
  (2140330, 0, 7),
  (2145411, 1, 4),
  (2148115, 0, 7),
  (2153024, 3, 3),
  (2153598, 2, 3),
  (2157356, 3, 6),
  (2159205, 5, 7),
  (2163646, 0, 6),
  (2169028, 6, 4),
  (2169675, 1, 7),
  (2170018, 2, 7),
  (2173919, 7, 7),
  (2176385, 4, 7),
  (2176634, 0, 7),
  (2177852, 4, 7),
  (2179082, 6, 4),
  (2181187, 3, 7),
  (2184812, 4, 6),
  (2185370, 1, 7),
  (2186075, 6, 3),
  (2188093, 1, 3),
  (2193899, 7, 7),
  (2195663, 7, 7),
  (2196097, 0, 7),
  (2199881, 1, 7),
  (2200747, 1, 0),
  (2200990, 1, 4),
  (2205496, 3, 6),
  (2210125, 6, 0),
  (2210975, 7, 6),
  (2211313, 6, 7),
  (2211789, 5, 5),
  (2214625, 2, 2),
  (2218094, 5, 7),
  (2218427, 0, 7),
  (2218687, 2, 7),
  (2219441, 5, 3),
  (2223320, 6, 3),
  (2224010, 3, 7),
  (2226006, 2, 6),
  (2229336, 0, 7),
  (2238052, 5, 3),
  (2240429, 6, 0),
  (2242729, 1, 6),
  (2245520, 3, 2),
  (2248851, 3, 7),
  (2252824, 7, 4),
  (2255108, 1, 7),
  (2256095, 4, 7),
  (2256187, 2, 7),
  (2258081, 0, 7),
  (2262037, 7, 6),
  (2263226, 0, 7),
  (2265939, 4, 5),
  (2272149, 4, 7),
  (2274719, 7, 3),
  (2280549, 0, 7),
  (2284101, 7, 6),
  (2285530, 5, 7),
  (2286303, 4, 3),
  (2288298, 1, 4),
  (2294885, 1, 6),
  (2296028, 0, 4),
  (2296627, 5, 7),
  (2299814, 3, 7),
  (2300391, 1, 7),
  (2302044, 7, 7),
  (2302141, 3, 7),
  (2303955, 7, 0),
  (2305765, 0, 7),
  (2307063, 2, 7),
  (2307845, 4, 3),
  (2308319, 4, 7),
  (2311784, 4, 7),
  (2313605, 7, 7),
  (2314772, 6, 7),
  (2318767, 5, 7),
  (2319189, 5, 7),
  (2322614, 6, 4),
  (2323435, 2, 2),
  (2323528, 0, 3),
  (2324942, 6, 7),
  (2327117, 5, 7),
  (2327559, 0, 4),
  (2327812, 5, 7),
  (2331788, 3, 7),
  (2333588, 5, 2),
  (2335384, 2, 7),
  (2342723, 5, 7),
  (2343340, 7, 0),
  (2344681, 7, 7),
  (2345524, 3, 6),
  (2346845, 0, 2),
  (2347308, 7, 7),
  (2348561, 3, 5),
  (2349481, 4, 3),
  (2351456, 6, 3),
  (2353315, 2, 6),
  (2354632, 7, 0),
  (2355571, 5, 1),
  (2361521, 2, 3),
  (2364085, 3, 6),
  (2365123, 2, 6),
  (2366029, 1, 7),
  (2366120, 7, 7),
  (2367314, 3, 7),
  (2367820, 6, 7),
  (2369175, 3, 5),
  (2372384, 0, 7),
  (2372818, 6, 0),
  (2372877, 3, 7),
  (2372892, 2, 6),
  (2373216, 7, 4),
  (2375401, 6, 7),
  (2375961, 1, 3),
  (2376148, 6, 7),
  (2379107, 4, 5),
  (2386567, 7, 7),
  (2394815, 3, 7),
  (2395054, 5, 7),
  (2398013, 5, 2),
  (2399879, 5, 7),
  (2401514, 3, 7),
  (2402866, 1, 7),
  (2407368, 2, 5),
  (2407402, 5, 7),
  (2408210, 2, 7),
  (2408944, 4, 7),
  (2411192, 2, 7),
  (2411305, 3, 7),
  (2411345, 4, 3),
  (2411724, 3, 1),
  (2411795, 1, 7),
  (2413928, 1, 7),
  (2417483, 1, 0),
  (2421065, 7, 7),
  (2423345, 3, 7),
  (2426256, 5, 7),
  (2426360, 5, 2),
  (2427594, 0, 7),
  (2429191, 4, 6),
  (2430613, 4, 7),
  (2430716, 6, 0),
  (2432409, 7, 7),
  (2432506, 4, 7),
  (2432666, 4, 3),
  (2435327, 4, 6),
  (2436617, 7, 7),
  (2440839, 7, 6),
  (2440895, 7, 7),
  (2441373, 0, 3),
  (2445420, 3, 7),
  (2445454, 2, 7),
  (2450971, 3, 5),
  (2451068, 7, 0),
  (2452090, 1, 3),
  (2454447, 5, 7),
  (2454657, 6, 0),
  (2459189, 5, 2),
  (2460690, 3, 7),
  (2466902, 3, 6),
  (2467126, 6, 7),
  (2472761, 4, 7),
  (2476162, 3, 7),
  (2476624, 5, 5),
  (2479809, 7, 2),
  (2479932, 0, 7),
  (2480801, 4, 7),
  (2483867, 1, 3),
  (2484885, 6, 7),
  (2484916, 5, 2),
  (2486000, 2, 5),
  (2487744, 6, 0),
  (2488952, 3, 6),
  (2490916, 5, 7),
  (2491272, 1, 4),
  (2492401, 3, 2),
  (2493590, 2, 2),
  (2497305, 3, 3),
  (2497657, 3, 7),
  (2497750, 2, 7),
  (2499913, 0, 7),
  (2500455, 3, 7),
  (2501062, 2, 2),
  (2502700, 3, 6),
  (2506799, 6, 7),
  (2510574, 7, 7),
  (2513251, 4, 2),
  (2514284, 5, 7),
  (2514705, 4, 7),
  (2518587, 1, 0),
  (2521614, 6, 6),
  (2528892, 3, 6),
  (2534709, 6, 7),
  (2535736, 2, 7),
  (2536674, 1, 7),
  (2540686, 7, 7),
  (2543438, 0, 3),
  (2545125, 6, 3),
  (2545203, 2, 7),
  (2546111, 3, 7),
  (2546876, 6, 0),
  (2547407, 2, 6),
  (2547527, 4, 3),
  (2547849, 7, 3),
  (2548749, 0, 7),
  (2555837, 1, 0),
  (2556003, 1, 3),
  (2556458, 5, 7),
  (2556789, 4, 6),
  (2558189, 0, 7),
  (2560657, 7, 4),
  (2563244, 7, 7),
  (2563512, 5, 3),
  (2565158, 1, 7),
  (2569126, 1, 3),
  (2570872, 1, 7),
  (2571480, 4, 3),
  (2573653, 1, 7),
  (2575247, 3, 7),
  (2575672, 0, 7),
  (2576706, 5, 3),
  (2580359, 3, 3),
  (2580615, 0, 0),
  (2581330, 0, 4),
  (2583044, 4, 6),
  (2583223, 1, 6),
  (2583419, 6, 7),
  (2583826, 7, 0),
  (2584119, 5, 3),
  (2585260, 3, 7),
  (2585874, 3, 7),
  (2588049, 6, 7),
  (2589222, 6, 7),
  (2591311, 3, 7),
  (2591913, 6, 0),
  (2593563, 0, 7),
  (2597209, 7, 6),
  (2597913, 1, 6),
  (2598919, 2, 5),
  (2604816, 3, 7),
  (2608952, 3, 7),
  (2609125, 3, 7),
  (2609368, 5, 2),
  (2609629, 3, 5),
  (2609664, 5, 7),
  (2612386, 1, 3),
  (2613232, 5, 7),
  (2614596, 7, 0),
  (2615410, 4, 6),
  (2617897, 2, 3),
  (2618616, 2, 7),
  (2618976, 7, 7),
  (2620006, 3, 3),
  (2621560, 2, 3),
  (2622081, 4, 3),
  (2622208, 7, 7),
  (2624732, 7, 4),
  (2626664, 4, 3),
  (2627423, 3, 6),
  (2628584, 3, 6),
  (2630778, 2, 7),
  (2632122, 0, 4),
  (2639727, 2, 7),
  (2641176, 0, 7),
  (2641655, 2, 7),
  (2646098, 2, 3),
  (2651693, 6, 6),
  (2659657, 3, 3),
  (2660338, 5, 7),
  (2662938, 1, 0),
  (2663776, 4, 1),
  (2664015, 7, 3),
  (2664027, 6, 7),
  (2668373, 6, 7),
  (2670123, 7, 6),
  (2670654, 4, 3),
  (2672208, 2, 7),
  (2674908, 6, 7),
  (2678792, 6, 7),
  (2681113, 5, 2),
  (2685335, 5, 7),
  (2689090, 2, 2),
  (2689194, 5, 7),
  (2691664, 5, 7),
  (2695090, 6, 7),
  (2695842, 6, 7),
  (2698055, 1, 7),
  (2699355, 7, 7),
  (2700274, 0, 4),
  (2702053, 1, 7),
  (2706309, 1, 6),
  (2706356, 4, 6),
  (2708323, 7, 7),
  (2709756, 1, 7),
  (2710965, 7, 7),
  (2711570, 7, 7),
  (2714691, 1, 7),
  (2715296, 1, 0),
  (2717236, 3, 3),
  (2721094, 0, 7),
  (2722416, 3, 7),
  (2723053, 0, 7),
  (2726640, 1, 7),
  (2728044, 4, 7),
  (2728140, 0, 7),
  (2731438, 1, 0),
  (2733699, 3, 7),
  (2740139, 4, 7),
  (2741708, 0, 7),
  (2741943, 3, 7),
  (2744731, 2, 2),
  (2745842, 6, 7),
  (2747222, 4, 3),
  (2747262, 3, 7),
  (2749879, 2, 7),
  (2756303, 5, 2),
  (2756317, 5, 7),
  (2758216, 4, 7),
  (2763125, 6, 6),
  (2763780, 0, 7),
  (2767890, 3, 7),
  (2777191, 7, 7),
  (2780507, 5, 7),
  (2781281, 6, 7),
  (2783826, 1, 4),
  (2783852, 3, 5),
  (2784169, 6, 7),
  (2787820, 2, 2),
  (2788966, 6, 7),
  (2794614, 3, 7),
  (2796262, 6, 7),
  (2797160, 4, 2),
  (2800947, 4, 7),
  (2801089, 6, 4),
  (2802977, 7, 7),
  (2804984, 6, 7),
  (2805470, 5, 7),
  (2805716, 2, 7),
  (2807414, 0, 0),
  (2811811, 2, 6),
  (2811887, 3, 7),
  (2814511, 7, 7),
  (2817262, 5, 7),
  (2818344, 2, 3),
  (2818797, 2, 7),
  (2825618, 6, 7),
  (2826477, 4, 7),
  (2826518, 5, 2),
  (2826947, 2, 5),
  (2829199, 3, 7),
  (2833010, 5, 7),
  (2833097, 7, 0),
  (2838114, 0, 7),
  (2838190, 6, 0),
  (2838211, 2, 7),
  (2845727, 3, 7),
  (2846554, 1, 7),
  (2848552, 1, 6),
  (2863120, 3, 6),
  (2863282, 3, 7),
  (2865744, 5, 7),
  (2867309, 4, 7),
  (2868852, 1, 7),
  (2873107, 5, 5),
  (2875356, 3, 5),
  (2876113, 2, 3),
  (2879732, 1, 0),
  (2880012, 4, 7),
  (2880092, 7, 7),
  (2883167, 4, 7),
  (2885306, 7, 7),
  (2887147, 5, 7),
  (2888364, 6, 6),
  (2888846, 4, 7),
  (2890730, 4, 7),
  (2891073, 6, 4),
  (2893697, 7, 7),
  (2894603, 3, 7),
  (2894864, 6, 7),
  (2899679, 1, 6),
  (2900239, 7, 7),
  (2903597, 3, 7),
  (2904185, 3, 7),
  (2910034, 2, 7),
  (2911598, 5, 6),
  (2915925, 2, 3),
  (2918742, 2, 7),
  (2924501, 7, 2),
  (2927432, 1, 7),
  (2927465, 6, 7),
  (2928089, 1, 4),
  (2930153, 2, 6),
  (2934318, 0, 7),
  (2938086, 2, 7),
  (2938976, 2, 6),
  (2941828, 3, 7),
  (2943095, 3, 7),
  (2947336, 1, 0),
  (2952039, 2, 7),
  (2953026, 2, 7),
  (2955425, 5, 0),
  (2957254, 6, 0),
  (2959554, 0, 3),
  (2963062, 4, 7),
  (2964225, 4, 7),
  (2964717, 0, 7),
  (2966931, 5, 7),
  (2967383, 7, 3),
  (2967922, 4, 3),
  (2969335, 2, 7),
  (2972820, 2, 2),
  (2973202, 4, 7),
  (2973438, 6, 7),
  (2982303, 7, 7),
  (2983767, 2, 2),
  (2985132, 1, 4),
  (2992157, 7, 7),
  (2994335, 4, 7),
  (2994623, 5, 7),
  (3000516, 7, 6),
  (3003407, 0, 4),
  (3004260, 7, 7),
  (3004790, 0, 7),
  (3005716, 2, 7),
  (3007054, 2, 7),
  (3007279, 0, 7),
  (3008646, 1, 7),
  (3010552, 6, 7),
  (3015978, 7, 7),
  (3015988, 5, 7),
  (3017788, 1, 0),
  (3020564, 6, 6),
  (3021480, 0, 7),
  (3022961, 0, 0),
  (3024510, 0, 7),
  (3028238, 6, 6),
  (3031655, 1, 0),
  (3031756, 6, 0),
  (3033204, 6, 5),
  (3034704, 3, 2),
  (3035027, 4, 3),
  (3040182, 7, 3),
  (3040528, 6, 7),
  (3044053, 4, 7),
  (3045432, 3, 7),
  (3045587, 5, 7),
  (3047278, 1, 0),
  (3056038, 0, 7),
  (3059378, 7, 7),
  (3060165, 6, 7),
  (3060791, 1, 7),
  (3065168, 4, 3),
  (3070556, 5, 2),
  (3071979, 0, 7),
  (3072822, 4, 7),
  (3074275, 0, 7),
  (3084665, 7, 7),
  (3085988, 6, 7),
  (3087038, 5, 7),
  (3087658, 0, 6),
  (3089437, 3, 6),
  (3089611, 7, 7),
  (3092214, 0, 7),
  (3093031, 7, 7),
  (3093263, 1, 3),
  (3094842, 4, 7),
  (3098672, 5, 7),
  (3100129, 7, 3),
  (3100270, 4, 7),
  (3101345, 6, 3),
  (3102627, 0, 7),
  (3103564, 5, 3),
  (3104280, 5, 2),
  (3106243, 2, 7),
  (3106550, 1, 7),
  (3110661, 2, 6),
  (3111456, 3, 7),
  (3111825, 5, 2),
  (3112715, 5, 7),
  (3114801, 7, 0),
  (3122296, 2, 7),
  (3122468, 0, 7),
  (3122959, 2, 3),
  (3127427, 5, 3),
  (3127725, 6, 7),
  (3128664, 7, 3),
  (3131333, 7, 0),
  (3132350, 2, 6),
  (3135238, 2, 3),
  (3136176, 6, 3),
  (3137018, 4, 7),
  (3138149, 4, 7),
  (3139878, 6, 7),
  (3141909, 2, 7),
  (3143752, 2, 7),
  (3144243, 4, 7),
  (3144861, 3, 3),
  (3145933, 7, 0),
  (3146830, 2, 2),
  (3151123, 5, 3),
  (3154184, 7, 7),
  (3156357, 1, 7),
  (3158684, 0, 7),
  (3159469, 6, 7),
  (3159648, 2, 5),
  (3159898, 7, 3),
  (3162692, 7, 7),
  (3163162, 4, 7),
  (3167006, 3, 6),
  (3169720, 3, 7),
  (3176965, 6, 7),
  (3177515, 2, 6),
  (3177532, 1, 7),
  (3179643, 5, 2),
  (3181299, 5, 2),
  (3183988, 5, 7),
  (3183999, 0, 7),
  (3184621, 2, 2),
  (3185589, 3, 1),
  (3190524, 5, 2),
  (3190654, 7, 0),
  (3192515, 5, 6),
  (3193811, 0, 3),
  (3198340, 0, 7),
  (3198496, 1, 3),
  (3199130, 7, 7),
  (3199836, 1, 0),
  (3202383, 1, 7),
  (3204844, 2, 6),
  (3205013, 3, 3),
  (3210422, 4, 6),
  (3212210, 2, 5),
  (3212295, 1, 0),
  (3212489, 5, 7),
  (3213268, 6, 7),
  (3213993, 7, 7),
  (3214985, 2, 7),
  (3217802, 2, 7),
  (3220798, 6, 7),
  (3221697, 5, 7),
  (3223103, 0, 7),
  (3223530, 6, 7),
  (3226272, 2, 2),
  (3226850, 5, 7),
  (3226959, 4, 7),
  (3228459, 4, 7),
  (3229215, 7, 7),
  (3229281, 4, 7),
  (3231466, 6, 3),
  (3231472, 1, 7),
  (3232551, 1, 2),
  (3241346, 2, 3),
  (3242005, 2, 2),
  (3249762, 6, 7),
  (3250228, 1, 7),
  (3252489, 3, 7),
  (3255911, 1, 6),
  (3259254, 4, 7),
  (3259976, 5, 5),
  (3260475, 2, 7),
  (3260562, 7, 7),
  (3261612, 3, 7),
  (3262212, 7, 5),
  (3262532, 1, 7),
  (3263286, 6, 7),
  (3264136, 1, 7),
  (3264521, 4, 7),
  (3265269, 1, 2),
  (3265936, 4, 7),
  (3268366, 4, 3),
  (3268897, 7, 4),
  (3273697, 1, 7),
  (3273791, 2, 7),
  (3279249, 3, 5),
  (3280920, 1, 7),
  (3281375, 7, 4),
  (3281766, 3, 7),
  (3285002, 7, 7),
  (3285068, 7, 4),
  (3286689, 5, 7),
  (3289108, 6, 6),
  (3289530, 1, 6),
  (3289987, 1, 7),
  (3294739, 5, 7),
  (3299000, 6, 7),
  (3300490, 5, 7),
  (3301022, 7, 6),
  (3301424, 1, 7),
  (3306499, 0, 7),
  (3306637, 6, 4),
  (3309666, 6, 7),
  (3310016, 3, 7),
  (3321723, 1, 7),
  (3325865, 5, 7),
  (3326220, 6, 7),
  (3327238, 1, 7),
  (3329559, 7, 0),
  (3330527, 0, 7),
  (3332836, 5, 7),
  (3333500, 6, 4),
  (3339501, 2, 3),
  (3340123, 1, 4),
  (3340338, 7, 7),
  (3341868, 5, 5),
  (3344422, 7, 4),
  (3347564, 0, 6),
  (3347942, 0, 7),
  (3348154, 2, 3),
  (3348759, 6, 7),
  (3349062, 2, 7),
  (3349890, 4, 7),
  (3354491, 0, 7),
  (3356147, 6, 4),
  (3359594, 5, 7),
  (3361537, 0, 4),
  (3362608, 3, 6),
  (3365745, 5, 4),
  (3368897, 6, 7),
  (3369212, 3, 7),
  (3369919, 2, 5),
  (3376578, 5, 3),
  (3376842, 5, 2),
  (3381178, 2, 7),
  (3383126, 6, 0),
  (3383257, 5, 7),
  (3383324, 3, 5),
  (3383451, 2, 2),
  (3383677, 7, 7),
  (3383738, 2, 7),
  (3385768, 3, 7),
  (3388902, 5, 7),
  (3390730, 1, 7),
  (3392212, 7, 0),
  (3394214, 2, 7),
  (3396738, 3, 7),
  (3401083, 1, 7),
  (3406106, 6, 7),
  (3406441, 3, 7),
  (3407033, 2, 3),
  (3407284, 2, 7),
  (3411133, 4, 5),
  (3411266, 5, 5),
  (3411860, 5, 3),
  (3414785, 5, 6),
  (3419739, 1, 7),
  (3424009, 0, 7),
  (3426953, 0, 0),
  (3427606, 0, 7),
  (3428793, 4, 7),
  (3429392, 7, 7),
  (3432335, 1, 6),
  (3433506, 5, 5),
  (3434412, 1, 7),
  (3435224, 4, 7),
  (3436078, 5, 7),
  (3437543, 1, 7),
  (3439227, 1, 0),
  (3439662, 5, 7),
  (3439986, 2, 2),
  (3442553, 1, 7),
  (3447739, 2, 7),
  (3448702, 5, 6),
  (3450451, 7, 7),
  (3452628, 4, 6),
  (3453940, 0, 3),
  (3457634, 5, 7),
  (3459113, 7, 7),
  (3462177, 4, 7),
  (3464966, 4, 4),
  (3465076, 3, 6),
  (3467826, 2, 6),
  (3472952, 3, 7),
  (3474382, 4, 3),
  (3474409, 6, 7),
  (3475662, 3, 7),
  (3477373, 6, 6),
  (3478899, 1, 6),
  (3479443, 4, 3),
  (3479755, 7, 0),
  (3484788, 6, 7),
  (3485257, 7, 3),
  (3486314, 2, 5),
  (3486744, 2, 7),
  (3491688, 4, 7),
  (3494696, 6, 7),
  (3498469, 2, 2),
  (3500188, 6, 2),
  (3501303, 5, 6),
  (3504617, 0, 7),
  (3504717, 7, 4),
  (3513322, 7, 6),
  (3514774, 5, 5),
  (3515572, 3, 7),
  (3516382, 7, 7),
  (3517506, 0, 4),
  (3517710, 0, 7),
  (3519288, 6, 7),
  (3519806, 5, 6),
  (3520614, 4, 7),
  (3520924, 2, 7),
  (3522532, 5, 7),
  (3524156, 6, 7),
  (3526111, 6, 7),
  (3527218, 1, 6),
  (3527392, 7, 4),
  (3528333, 7, 7),
  (3528969, 2, 6),
  (3529050, 5, 7),
  (3529177, 5, 7),
  (3529747, 1, 0),
  (3529892, 6, 3),
  (3535863, 4, 7),
  (3535902, 6, 7),
  (3539125, 1, 0),
  (3539225, 0, 7),
  (3543672, 1, 4),
  (3545312, 2, 7),
  (3546682, 0, 7),
  (3547218, 0, 3),
  (3547234, 5, 7),
  (3548108, 7, 3),
  (3549861, 5, 7),
  (3552011, 4, 3),
  (3555535, 1, 7),
  (3556346, 5, 3),
  (3556654, 0, 7),
  (3560418, 0, 7),
  (3560808, 1, 2),
  (3563768, 2, 6),
  (3563840, 0, 7),
  (3563920, 5, 7),
  (3568550, 7, 6),
  (3570003, 0, 7),
  (3570352, 5, 3),
  (3570845, 2, 3),
  (3573539, 2, 7),
  (3573559, 5, 3),
  (3575767, 5, 7),
  (3576468, 6, 7),
  (3576740, 1, 7),
  (3580265, 0, 6),
  (3581955, 6, 7),
  (3583226, 4, 7),
  (3583789, 2, 6),
  (3584792, 6, 7),
  (3585670, 2, 7),
  (3585796, 4, 7),
  (3587464, 0, 7),
  (3588924, 4, 7),
  (3591178, 5, 7),
  (3591191, 2, 7),
  (3592161, 6, 7),
  (3592272, 5, 6),
  (3597574, 6, 5),
  (3599858, 2, 2),
])
