from src.util import *
schedule = deque([
  (3470, 2, 0),
  (5979, 1, 0),
  (6896, 2, 0),
  (9851, 3, 0),
  (16696, 3, 1),
  (17049, 2, 2),
  (18815, 3, 1),
  (19449, 1, 1),
  (23006, 0, 1),
  (29474, 1, 0),
  (30620, 2, 2),
  (32721, 0, 0),
  (37202, 1, 1),
  (38188, 0, 0),
  (41529, 1, 1),
  (42555, 1, 1),
  (45049, 0, 2),
  (47761, 0, 1),
  (48384, 2, 1),
  (49228, 2, 1),
  (50749, 3, 0),
  (51279, 2, 0),
  (52273, 1, 2),
  (53704, 2, 2),
  (58602, 2, 2),
  (63095, 1, 0),
  (65635, 0, 1),
  (69124, 3, 0),
  (69293, 1, 2),
  (73780, 3, 1),
  (73808, 1, 2),
  (74168, 1, 1),
  (74509, 0, 2),
  (77788, 0, 0),
  (81074, 3, 1),
  (82571, 0, 1),
  (83629, 0, 0),
  (90271, 2, 1),
  (91708, 1, 1),
  (95481, 3, 2),
  (99238, 0, 0),
  (104665, 2, 1),
  (114439, 2, 1),
  (114603, 0, 2),
  (115037, 1, 0),
  (116702, 1, 0),
  (116718, 1, 1),
  (118878, 3, 1),
  (119995, 3, 2),
  (127922, 0, 2),
  (130056, 2, 0),
  (130158, 2, 2),
  (130733, 0, 2),
  (131555, 3, 0),
  (131571, 2, 2),
  (132689, 1, 0),
  (133796, 3, 1),
  (136121, 0, 2),
  (138853, 3, 2),
  (139386, 0, 0),
  (139886, 0, 1),
  (142391, 1, 1),
  (145018, 0, 2),
  (147217, 2, 1),
  (148892, 2, 0),
  (150766, 2, 1),
  (151457, 3, 1),
  (153379, 3, 2),
  (161479, 2, 2),
  (162124, 3, 0),
  (164522, 2, 0),
  (166035, 1, 1),
  (166639, 1, 0),
  (167076, 1, 1),
  (172237, 3, 0),
  (176141, 1, 0),
  (176550, 1, 0),
  (178084, 1, 2),
  (181085, 1, 2),
  (181178, 3, 0),
  (181261, 1, 2),
  (182433, 0, 0),
  (186119, 3, 2),
  (186233, 0, 2),
  (187121, 1, 2),
  (188958, 3, 2),
  (190959, 2, 1),
  (191252, 2, 0),
  (194676, 3, 1),
  (196384, 3, 1),
  (196989, 0, 0),
  (197240, 3, 2),
  (197518, 3, 0),
  (198084, 2, 1),
  (198219, 2, 0),
  (198311, 2, 0),
  (199361, 3, 0),
  (202366, 1, 2),
  (204044, 1, 0),
  (207276, 2, 1),
  (210380, 3, 0),
  (212703, 0, 2),
  (215400, 0, 2),
  (216912, 1, 2),
  (218888, 2, 2),
  (227885, 2, 1),
  (227914, 2, 2),
  (230712, 2, 1),
  (231482, 3, 0),
  (231595, 3, 2),
  (233565, 3, 0),
  (242241, 3, 1),
  (242662, 3, 2),
  (244630, 1, 1),
  (245546, 3, 2),
  (246373, 2, 1),
  (246628, 0, 2),
  (248058, 1, 2),
  (250464, 1, 0),
  (250992, 1, 2),
  (251019, 0, 1),
  (251503, 3, 2),
  (252050, 1, 2),
  (252438, 3, 2),
  (253120, 2, 0),
  (254572, 1, 1),
  (255971, 0, 0),
  (256664, 2, 2),
  (257615, 3, 0),
  (258829, 0, 1),
  (259376, 2, 1),
  (260552, 1, 2),
  (261851, 1, 0),
  (262869, 2, 1),
  (263414, 2, 0),
  (263671, 2, 0),
  (270541, 1, 1),
  (274029, 3, 1),
  (277730, 2, 2),
  (281233, 0, 1),
  (281478, 3, 2),
  (282407, 3, 0),
  (294659, 3, 2),
  (296276, 1, 0),
  (308850, 3, 2),
  (310039, 1, 2),
  (310045, 3, 0),
  (310803, 0, 0),
  (312773, 3, 2),
  (314905, 3, 2),
  (315651, 3, 0),
  (317782, 3, 0),
  (321307, 1, 1),
  (323170, 0, 0),
  (326809, 2, 2),
  (328249, 2, 2),
  (328407, 1, 0),
  (329878, 2, 1),
  (330663, 2, 2),
  (333740, 0, 2),
  (334211, 0, 0),
  (341236, 0, 0),
  (341506, 0, 1),
  (343318, 2, 1),
  (343634, 3, 0),
  (351289, 0, 0),
  (352716, 0, 0),
  (354440, 2, 1),
  (354678, 2, 1),
  (354708, 0, 2),
  (356741, 0, 0),
  (359320, 3, 2),
  (359380, 3, 2),
  (363803, 2, 0),
  (370014, 1, 0),
  (373088, 2, 1),
  (374023, 1, 1),
  (375213, 0, 0),
  (376347, 2, 1),
  (380432, 3, 2),
  (380471, 1, 0),
  (382242, 3, 1),
  (388601, 0, 1),
  (390073, 3, 2),
  (390469, 2, 0),
  (390895, 1, 2),
  (391201, 0, 1),
  (392329, 0, 1),
  (397935, 3, 0),
  (400178, 1, 2),
  (400760, 0, 0),
  (402543, 1, 0),
  (404136, 2, 1),
  (407378, 1, 1),
  (410474, 0, 0),
  (412056, 1, 0),
  (417392, 3, 1),
  (419761, 1, 1),
  (420030, 1, 1),
  (424862, 2, 0),
  (425299, 2, 1),
  (425380, 0, 0),
  (425509, 3, 2),
  (427855, 1, 0),
  (432619, 2, 2),
  (433566, 1, 1),
  (435148, 0, 2),
  (438016, 1, 1),
  (440017, 3, 0),
  (444480, 2, 1),
  (444644, 2, 2),
  (448726, 1, 2),
  (448755, 3, 2),
  (449403, 1, 0),
  (450045, 0, 1),
  (452290, 1, 2),
  (453247, 0, 0),
  (458412, 0, 0),
  (458468, 1, 2),
  (458546, 3, 2),
  (459230, 3, 1),
  (459718, 1, 2),
  (461328, 1, 2),
  (468426, 0, 0),
  (475195, 3, 1),
  (477924, 3, 0),
  (479227, 1, 2),
  (479998, 2, 0),
  (480960, 2, 1),
  (481453, 2, 0),
  (482373, 0, 1),
  (485533, 0, 0),
  (487227, 3, 0),
  (488327, 0, 0),
  (490911, 1, 2),
  (493534, 1, 2),
  (499056, 1, 1),
  (501078, 0, 0),
  (502686, 1, 0),
  (503716, 3, 2),
  (503867, 1, 2),
  (507727, 3, 1),
  (507735, 2, 2),
  (508378, 0, 0),
  (509740, 0, 0),
  (514045, 2, 2),
  (515267, 3, 0),
  (522573, 0, 1),
  (524546, 1, 1),
  (525346, 0, 2),
  (526349, 1, 1),
  (530929, 2, 0),
  (531919, 0, 1),
  (536230, 1, 2),
  (540214, 2, 0),
  (541655, 3, 1),
  (541798, 2, 0),
  (541959, 2, 2),
  (543537, 1, 0),
  (547187, 0, 1),
  (547804, 1, 1),
  (551727, 1, 0),
  (551977, 1, 0),
  (552721, 0, 2),
  (555307, 3, 2),
  (559016, 3, 1),
  (562235, 3, 2),
  (562304, 1, 0),
  (563456, 1, 0),
  (563846, 2, 2),
  (565185, 1, 1),
  (567796, 1, 2),
  (567837, 2, 0),
  (568913, 0, 1),
  (570266, 2, 2),
  (573772, 2, 1),
  (574957, 0, 2),
  (576019, 3, 2),
  (576172, 1, 2),
  (578205, 0, 2),
  (583427, 3, 2),
  (585046, 0, 0),
  (589577, 2, 1),
  (593805, 0, 2),
  (596352, 1, 1),
  (596471, 1, 2),
  (598960, 2, 1),
  (599182, 0, 2),
  (600444, 2, 0),
  (601543, 2, 2),
  (602348, 2, 1),
  (602731, 3, 2),
  (605269, 3, 0),
  (605460, 1, 0),
  (607830, 3, 0),
  (610725, 1, 0),
  (612112, 0, 2),
  (614478, 1, 0),
  (615552, 2, 1),
  (621032, 2, 0),
  (621608, 3, 1),
  (621979, 3, 1),
  (625677, 0, 0),
  (626812, 3, 1),
  (627715, 3, 0),
  (639083, 0, 2),
  (639125, 3, 2),
  (639379, 0, 1),
  (640298, 0, 2),
  (642440, 3, 2),
  (644911, 3, 1),
  (645682, 3, 1),
  (646123, 3, 1),
  (646958, 1, 1),
  (648258, 0, 0),
  (648632, 1, 2),
  (650832, 3, 1),
  (652109, 1, 0),
  (652465, 3, 1),
  (657818, 2, 0),
  (661896, 0, 0),
  (663889, 2, 0),
  (665664, 3, 1),
  (666704, 2, 1),
  (668699, 3, 2),
  (672378, 0, 2),
  (674530, 3, 2),
  (679007, 1, 1),
  (687401, 3, 0),
  (688761, 1, 2),
  (688859, 1, 0),
  (693383, 2, 1),
  (695848, 1, 0),
  (697193, 3, 0),
  (699197, 0, 2),
  (706124, 2, 0),
  (706647, 2, 1),
  (706704, 1, 1),
  (707468, 0, 2),
  (708653, 0, 0),
  (708779, 2, 1),
  (716121, 3, 2),
  (717016, 1, 1),
  (720312, 3, 0),
  (720696, 2, 1),
  (722378, 0, 2),
  (725391, 2, 0),
  (727695, 3, 0),
  (731572, 1, 1),
  (731796, 3, 2),
  (733700, 1, 2),
  (737971, 1, 1),
  (738237, 3, 2),
  (739475, 0, 2),
  (739925, 2, 2),
  (740004, 2, 2),
  (743459, 0, 1),
  (743571, 0, 0),
  (746606, 0, 2),
  (747879, 3, 1),
  (748237, 2, 0),
  (749679, 2, 1),
  (750702, 3, 2),
  (754341, 2, 0),
  (755288, 3, 1),
  (756763, 3, 1),
  (758194, 2, 1),
  (759993, 0, 1),
  (760323, 2, 2),
  (763694, 1, 0),
  (768703, 1, 1),
  (771594, 0, 1),
  (775740, 3, 1),
  (780356, 2, 0),
  (781646, 2, 0),
  (784826, 0, 2),
  (791103, 0, 0),
  (795789, 0, 1),
  (796912, 1, 0),
  (799356, 1, 2),
  (800752, 0, 2),
  (801143, 2, 1),
  (806444, 0, 2),
  (806488, 1, 1),
  (807968, 0, 1),
  (808420, 0, 0),
  (808522, 1, 2),
  (815604, 0, 0),
  (816535, 3, 0),
  (818180, 3, 2),
  (822450, 0, 0),
  (822821, 3, 2),
  (825295, 2, 0),
  (825793, 3, 2),
  (827121, 3, 2),
  (827772, 3, 2),
  (828569, 0, 0),
  (828644, 2, 2),
  (831846, 1, 2),
  (832046, 1, 1),
  (836265, 2, 1),
  (837244, 2, 1),
  (838060, 2, 0),
  (841100, 1, 0),
  (844998, 3, 2),
  (848070, 0, 2),
  (849681, 2, 2),
  (850565, 0, 1),
  (852124, 2, 0),
  (855586, 0, 2),
  (857404, 0, 2),
  (864650, 3, 0),
  (865448, 1, 2),
  (866153, 1, 1),
  (866842, 1, 1),
  (867735, 2, 0),
  (874235, 1, 1),
  (877851, 1, 0),
  (878002, 2, 1),
  (879122, 0, 1),
  (885770, 2, 0),
  (886291, 3, 0),
  (886320, 1, 1),
  (886783, 2, 0),
  (891818, 2, 2),
  (898128, 3, 2),
  (906933, 1, 1),
  (908122, 0, 2),
  (912341, 1, 2),
  (916539, 1, 0),
  (920174, 3, 1),
  (921254, 1, 1),
  (922077, 3, 1),
  (925206, 1, 1),
  (928842, 2, 1),
  (929158, 2, 1),
  (930300, 2, 2),
  (934528, 0, 0),
  (939196, 1, 1),
  (941064, 0, 2),
  (947354, 0, 1),
  (947354, 3, 1),
  (948698, 1, 2),
  (952702, 2, 2),
  (956125, 2, 2),
  (956758, 3, 2),
  (956812, 3, 0),
  (960936, 1, 1),
  (963623, 2, 1),
  (964795, 3, 1),
  (967052, 1, 0),
  (969295, 2, 0),
  (972680, 0, 1),
  (976362, 0, 2),
  (977795, 2, 0),
  (978544, 2, 0),
  (981135, 2, 2),
  (981228, 1, 1),
  (981344, 3, 2),
  (983947, 1, 1),
  (986885, 1, 2),
  (988649, 1, 0),
  (994068, 3, 1),
  (994678, 0, 0),
  (994709, 1, 1),
  (998058, 1, 2),
  (1001019, 0, 1),
  (1003671, 0, 1),
  (1008680, 2, 2),
  (1012025, 0, 2),
  (1012657, 0, 0),
  (1012658, 2, 1),
  (1012770, 0, 0),
  (1014679, 2, 2),
  (1020440, 1, 1),
  (1020506, 0, 0),
  (1022203, 2, 2),
  (1023419, 0, 1),
  (1025862, 0, 1),
  (1026803, 0, 2),
  (1030395, 0, 1),
  (1036234, 1, 1),
  (1038094, 3, 1),
  (1039167, 2, 2),
  (1041114, 1, 2),
  (1045827, 2, 1),
  (1046211, 3, 1),
  (1046992, 0, 0),
  (1047237, 0, 1),
  (1047978, 1, 2),
  (1048673, 0, 0),
  (1054730, 2, 2),
  (1060715, 1, 1),
  (1063180, 3, 2),
  (1065043, 1, 1),
  (1068820, 1, 2),
  (1068967, 1, 1),
  (1069788, 3, 2),
  (1072592, 3, 2),
  (1072711, 0, 1),
  (1080550, 2, 2),
  (1083246, 0, 2),
  (1084661, 1, 1),
  (1085919, 1, 2),
  (1088127, 0, 1),
  (1088312, 3, 2),
  (1091755, 3, 2),
  (1092097, 1, 0),
  (1093750, 2, 2),
  (1097171, 3, 1),
  (1097562, 1, 1),
  (1100147, 3, 1),
  (1102185, 3, 0),
  (1107824, 0, 2),
  (1108298, 2, 2),
  (1111019, 3, 0),
  (1111451, 0, 1),
  (1111861, 1, 1),
  (1112555, 0, 1),
  (1114603, 2, 1),
  (1119038, 0, 0),
  (1120447, 1, 1),
  (1127850, 0, 1),
  (1133366, 2, 1),
  (1133782, 3, 1),
  (1138888, 1, 1),
  (1139906, 1, 2),
  (1141244, 1, 2),
  (1143503, 0, 0),
  (1146378, 0, 2),
  (1147481, 1, 0),
  (1148303, 2, 1),
  (1149565, 1, 0),
  (1150555, 0, 1),
  (1151229, 1, 1),
  (1152831, 2, 2),
  (1154094, 3, 2),
  (1154402, 0, 1),
  (1158630, 1, 0),
  (1163489, 2, 0),
  (1166197, 1, 1),
  (1166732, 2, 0),
  (1168365, 2, 1),
  (1170804, 3, 0),
  (1171749, 3, 2),
  (1174605, 3, 1),
  (1175252, 0, 0),
  (1175544, 2, 1),
  (1176719, 2, 2),
  (1176948, 2, 2),
  (1181213, 0, 0),
  (1183710, 1, 2),
  (1184178, 0, 1),
  (1186613, 1, 1),
  (1187256, 2, 1),
  (1187622, 2, 1),
  (1192600, 2, 2),
  (1194568, 3, 1),
  (1197227, 2, 1),
  (1198437, 3, 2),
  (1199778, 2, 2),
  (1201456, 1, 2),
  (1203704, 3, 0),
  (1203926, 1, 2),
  (1204345, 3, 0),
  (1205966, 3, 2),
  (1206375, 2, 2),
  (1209056, 2, 0),
  (1209260, 2, 2),
  (1211544, 2, 2),
  (1212097, 2, 2),
  (1215105, 2, 1),
  (1215351, 2, 1),
  (1217780, 1, 2),
  (1231323, 0, 0),
  (1231658, 0, 0),
  (1233277, 3, 0),
  (1235102, 3, 0),
  (1236209, 3, 2),
  (1238886, 0, 2),
  (1239896, 0, 2),
  (1239912, 0, 1),
  (1241009, 0, 2),
  (1242709, 0, 2),
  (1242888, 1, 0),
  (1243566, 3, 2),
  (1245753, 1, 0),
  (1246311, 3, 1),
  (1246519, 1, 1),
  (1254839, 3, 1),
  (1256685, 3, 2),
  (1256766, 1, 2),
  (1257773, 0, 0),
  (1257941, 1, 2),
  (1261161, 3, 0),
  (1263106, 3, 2),
  (1269062, 0, 0),
  (1270841, 0, 2),
  (1272998, 0, 0),
  (1274234, 3, 1),
  (1277900, 3, 1),
  (1278942, 3, 2),
  (1279002, 3, 0),
  (1279494, 1, 2),
  (1281422, 2, 0),
  (1281818, 2, 1),
  (1282165, 1, 2),
  (1282488, 0, 0),
  (1283552, 3, 0),
  (1284223, 1, 1),
  (1285721, 3, 1),
  (1287396, 0, 2),
  (1289147, 2, 0),
  (1291526, 2, 2),
  (1292139, 2, 1),
  (1292705, 2, 2),
  (1293012, 3, 0),
  (1293906, 1, 1),
  (1300327, 0, 1),
  (1302340, 3, 0),
  (1303858, 0, 2),
  (1307712, 3, 2),
  (1307850, 3, 1),
  (1308156, 2, 1),
  (1315312, 0, 2),
  (1315674, 3, 2),
  (1316790, 2, 1),
  (1316864, 0, 1),
  (1317465, 1, 0),
  (1318733, 0, 2),
  (1321050, 3, 0),
  (1321084, 0, 1),
  (1323915, 3, 0),
  (1324712, 2, 0),
  (1325330, 0, 0),
  (1329613, 3, 1),
  (1330719, 0, 0),
  (1330830, 3, 1),
  (1330846, 0, 1),
  (1334742, 2, 1),
  (1337833, 3, 0),
  (1338021, 3, 1),
  (1340403, 1, 2),
  (1344545, 0, 1),
  (1349216, 2, 0),
  (1353427, 1, 2),
  (1354731, 3, 0),
  (1356167, 0, 2),
  (1357250, 1, 1),
  (1357972, 3, 1),
  (1358100, 0, 0),
  (1363360, 1, 0),
  (1363810, 1, 1),
  (1364098, 2, 1),
  (1364607, 2, 0),
  (1364982, 1, 1),
  (1367960, 1, 0),
  (1368301, 3, 2),
  (1368533, 3, 0),
  (1369629, 2, 0),
  (1374138, 0, 2),
  (1376311, 1, 0),
  (1376365, 2, 0),
  (1377532, 2, 0),
  (1379979, 2, 1),
  (1380420, 0, 2),
  (1381313, 1, 0),
  (1381924, 1, 1),
  (1385679, 2, 0),
  (1388862, 3, 0),
  (1389092, 2, 2),
  (1394819, 3, 0),
  (1397412, 2, 2),
  (1398886, 1, 1),
  (1403378, 0, 2),
  (1403886, 3, 1),
  (1406916, 1, 2),
  (1408898, 2, 0),
  (1408907, 3, 1),
  (1410294, 1, 2),
  (1410561, 0, 1),
  (1412842, 2, 1),
  (1413686, 0, 1),
  (1413913, 2, 2),
  (1413966, 0, 2),
  (1418497, 2, 0),
  (1418879, 1, 2),
  (1419141, 3, 0),
  (1422708, 1, 0),
  (1424503, 3, 2),
  (1425518, 2, 0),
  (1429541, 3, 1),
  (1435756, 1, 2),
  (1435768, 1, 1),
  (1436923, 0, 0),
  (1440082, 3, 2),
  (1446133, 1, 1),
  (1448205, 1, 2),
  (1448329, 0, 0),
  (1449293, 1, 0),
  (1454866, 0, 0),
  (1455094, 0, 1),
  (1456387, 1, 0),
  (1457343, 3, 0),
  (1459512, 3, 0),
  (1463245, 1, 1),
  (1464071, 2, 0),
  (1467013, 2, 2),
  (1472439, 0, 1),
  (1474406, 1, 2),
  (1476234, 1, 2),
  (1483834, 1, 1),
  (1486286, 2, 2),
  (1487915, 3, 0),
  (1487956, 2, 1),
  (1491212, 1, 2),
  (1491269, 3, 2),
  (1491933, 3, 0),
  (1492759, 3, 0),
  (1496049, 1, 2),
  (1499398, 1, 1),
  (1499645, 0, 0),
  (1504395, 0, 1),
  (1505936, 2, 2),
  (1510058, 2, 0),
  (1512089, 3, 0),
  (1512824, 1, 2),
  (1514346, 3, 1),
  (1516222, 2, 0),
  (1516772, 0, 1),
  (1517068, 0, 0),
  (1521472, 3, 1),
  (1528246, 3, 0),
  (1530648, 3, 2),
  (1536499, 0, 1),
  (1541813, 0, 1),
  (1542990, 3, 1),
  (1544799, 3, 1),
  (1545238, 1, 0),
  (1547361, 3, 1),
  (1547557, 3, 2),
  (1549493, 1, 2),
  (1552091, 2, 1),
  (1562850, 1, 1),
  (1563059, 0, 0),
  (1563175, 0, 1),
  (1565130, 3, 0),
  (1570166, 1, 2),
  (1571052, 0, 1),
  (1571273, 0, 1),
  (1571456, 1, 0),
  (1572484, 3, 1),
  (1575231, 0, 1),
  (1576257, 0, 2),
  (1582744, 3, 1),
  (1586150, 3, 0),
  (1587281, 1, 2),
  (1589779, 3, 2),
  (1593038, 3, 2),
  (1594302, 0, 1),
  (1595081, 0, 1),
  (1596736, 0, 1),
  (1598795, 1, 0),
  (1599443, 3, 2),
  (1600247, 2, 1),
  (1602538, 3, 1),
  (1606130, 1, 0),
  (1606478, 0, 2),
  (1611741, 2, 0),
  (1615697, 2, 1),
  (1616161, 0, 0),
  (1616868, 3, 0),
  (1620969, 3, 0),
  (1621467, 2, 0),
  (1621568, 0, 0),
  (1622670, 3, 2),
  (1623809, 3, 1),
  (1625478, 3, 1),
  (1626211, 1, 2),
  (1633860, 2, 1),
  (1634195, 2, 0),
  (1634848, 3, 0),
  (1636315, 0, 2),
  (1636788, 0, 2),
  (1637854, 2, 2),
  (1638570, 2, 0),
  (1640725, 2, 1),
  (1640962, 0, 0),
  (1641585, 1, 0),
  (1644158, 0, 0),
  (1645041, 1, 0),
  (1648086, 0, 1),
  (1651235, 2, 0),
  (1652083, 3, 1),
  (1652353, 3, 1),
  (1652756, 3, 0),
  (1654607, 0, 1),
  (1659025, 3, 1),
  (1662146, 3, 0),
  (1662203, 2, 2),
  (1663573, 2, 1),
  (1665747, 0, 0),
  (1666865, 2, 2),
  (1670394, 1, 2),
  (1673853, 3, 2),
  (1681743, 3, 0),
  (1682063, 1, 0),
  (1682251, 1, 2),
  (1683402, 0, 0),
  (1685636, 0, 0),
  (1689716, 0, 1),
  (1690133, 0, 2),
  (1690596, 2, 2),
  (1690977, 1, 1),
  (1691065, 1, 1),
  (1691502, 3, 2),
  (1693747, 2, 1),
  (1695163, 0, 2),
  (1695764, 2, 2),
  (1698943, 2, 1),
  (1703755, 1, 1),
  (1704079, 3, 0),
  (1706179, 2, 1),
  (1710575, 1, 0),
  (1719248, 2, 2),
  (1719445, 0, 1),
  (1721142, 3, 0),
  (1723381, 1, 2),
  (1724865, 1, 2),
  (1733066, 1, 0),
  (1735410, 2, 0),
  (1737432, 0, 1),
  (1737781, 0, 0),
  (1738288, 2, 1),
  (1741259, 2, 2),
  (1745554, 3, 2),
  (1746524, 0, 1),
  (1747695, 3, 1),
  (1747696, 0, 2),
  (1749397, 0, 0),
  (1758003, 2, 2),
  (1765234, 3, 1),
  (1765531, 1, 2),
  (1768822, 1, 1),
  (1769280, 0, 2),
  (1770180, 2, 0),
  (1771274, 2, 0),
  (1774787, 2, 1),
  (1776155, 3, 0),
  (1776332, 1, 2),
  (1776689, 0, 0),
  (1776799, 1, 1),
  (1784221, 0, 1),
  (1786794, 0, 2),
  (1787731, 2, 2),
  (1788556, 2, 1),
  (1789737, 2, 0),
  (1798715, 0, 1),
  (1801935, 2, 0),
  (1801939, 0, 2),
  (1802942, 3, 2),
  (1805764, 1, 1),
  (1806881, 2, 0),
  (1807678, 0, 1),
  (1807959, 0, 0),
  (1807985, 0, 2),
  (1808633, 0, 2),
  (1811909, 0, 1),
  (1812295, 0, 0),
  (1813211, 0, 2),
  (1814270, 3, 0),
  (1814604, 1, 2),
  (1816405, 0, 0),
  (1816842, 2, 0),
  (1819078, 0, 1),
  (1819086, 1, 1),
  (1821785, 0, 1),
  (1822987, 0, 1),
  (1823338, 1, 1),
  (1823936, 3, 2),
  (1830768, 3, 1),
  (1831486, 3, 1),
  (1836128, 3, 2),
  (1836374, 3, 0),
  (1839301, 2, 0),
  (1841346, 2, 1),
  (1841544, 0, 1),
  (1841631, 1, 0),
  (1845570, 3, 1),
  (1847028, 2, 2),
  (1847656, 2, 2),
  (1847901, 3, 1),
  (1848647, 0, 2),
  (1850214, 3, 1),
  (1852119, 1, 1),
  (1852150, 1, 0),
  (1853517, 1, 2),
  (1855380, 1, 1),
  (1855768, 3, 0),
  (1858720, 2, 2),
  (1860771, 3, 2),
  (1863958, 2, 1),
  (1864482, 2, 0),
  (1867134, 0, 2),
  (1867943, 0, 1),
  (1868270, 1, 1),
  (1873739, 1, 1),
  (1877476, 0, 2),
  (1878945, 0, 0),
  (1883316, 2, 0),
  (1886121, 3, 2),
  (1888251, 1, 1),
  (1889254, 3, 0),
  (1890501, 0, 2),
  (1890730, 0, 1),
  (1890783, 3, 2),
  (1898600, 2, 1),
  (1899978, 3, 0),
  (1900008, 1, 2),
  (1900817, 2, 2),
  (1900988, 1, 0),
  (1904651, 0, 0),
  (1904805, 2, 2),
  (1905918, 3, 0),
  (1906284, 0, 0),
  (1907915, 3, 1),
  (1908618, 3, 2),
  (1911987, 3, 1),
  (1912040, 0, 0),
  (1914742, 3, 1),
  (1915179, 0, 2),
  (1915871, 1, 1),
  (1922062, 0, 1),
  (1927923, 3, 1),
  (1928354, 1, 2),
  (1928723, 1, 2),
  (1929835, 0, 1),
  (1937459, 2, 2),
  (1937884, 1, 0),
  (1938395, 2, 0),
  (1938992, 0, 1),
  (1939100, 1, 0),
  (1942380, 0, 0),
  (1943834, 1, 2),
  (1944528, 2, 2),
  (1945185, 3, 0),
  (1946185, 3, 2),
  (1947071, 0, 2),
  (1947544, 0, 1),
  (1949449, 2, 0),
  (1950065, 1, 1),
  (1951987, 0, 0),
  (1953548, 1, 1),
  (1953963, 2, 1),
  (1954342, 3, 1),
  (1959402, 2, 1),
  (1960903, 2, 0),
  (1966047, 1, 0),
  (1968290, 1, 2),
  (1969633, 0, 2),
  (1970945, 2, 1),
  (1971400, 2, 0),
  (1974287, 1, 1),
  (1976540, 3, 2),
  (1977612, 3, 2),
  (1977625, 1, 1),
  (1979345, 0, 1),
  (1981928, 1, 2),
  (1983450, 3, 0),
  (1985589, 3, 0),
  (1989846, 0, 2),
  (1989878, 2, 2),
  (1992251, 1, 0),
  (1994042, 1, 0),
  (1999512, 3, 1),
  (2000134, 3, 0),
  (2001028, 2, 0),
  (2001864, 1, 1),
  (2008065, 2, 1),
  (2008270, 3, 0),
  (2009914, 1, 0),
  (2011732, 2, 2),
  (2013250, 0, 1),
  (2015160, 3, 1),
  (2016655, 1, 2),
  (2016892, 0, 2),
  (2017024, 2, 1),
  (2017872, 0, 1),
  (2030194, 2, 2),
  (2032555, 0, 2),
  (2033542, 0, 0),
  (2033565, 3, 0),
  (2035790, 2, 2),
  (2038340, 1, 1),
  (2043663, 1, 1),
  (2045544, 0, 2),
  (2050276, 0, 0),
  (2050943, 3, 1),
  (2054593, 3, 2),
  (2054602, 1, 1),
  (2060697, 0, 1),
  (2065060, 0, 0),
  (2065315, 1, 1),
  (2065492, 1, 0),
  (2065840, 1, 0),
  (2065887, 0, 0),
  (2067215, 3, 2),
  (2081580, 1, 1),
  (2083622, 2, 2),
  (2086464, 1, 0),
  (2093501, 2, 1),
  (2098064, 1, 1),
  (2102469, 2, 1),
  (2103641, 0, 0),
  (2103786, 1, 0),
  (2104843, 3, 1),
  (2106509, 3, 1),
  (2111117, 0, 0),
  (2112981, 3, 1),
  (2112996, 3, 1),
  (2113808, 3, 2),
  (2116198, 1, 2),
  (2117572, 1, 1),
  (2118104, 0, 0),
  (2121552, 2, 2),
  (2122165, 2, 2),
  (2123263, 2, 1),
  (2124059, 2, 0),
  (2128509, 1, 2),
  (2130673, 0, 2),
  (2133242, 2, 0),
  (2134076, 1, 1),
  (2136113, 3, 0),
  (2137979, 0, 0),
  (2140121, 0, 2),
  (2149733, 3, 1),
  (2150261, 1, 2),
  (2154446, 1, 0),
  (2156683, 1, 0),
  (2162229, 1, 2),
  (2162918, 2, 2),
  (2163065, 0, 2),
  (2167651, 0, 0),
  (2174342, 2, 2),
  (2174896, 3, 2),
  (2180565, 1, 1),
  (2185119, 2, 1),
  (2187546, 2, 1),
  (2189724, 2, 0),
  (2192951, 1, 1),
  (2193870, 2, 0),
  (2194044, 2, 2),
  (2194844, 3, 1),
  (2195343, 3, 2),
  (2196970, 0, 1),
  (2198801, 0, 0),
  (2203922, 2, 1),
  (2204272, 3, 1),
  (2206592, 1, 1),
  (2207163, 3, 1),
  (2208483, 1, 2),
  (2209342, 2, 2),
  (2212721, 0, 1),
  (2213882, 3, 0),
  (2216542, 1, 1),
  (2216614, 3, 0),
  (2219896, 1, 2),
  (2224309, 0, 2),
  (2227503, 0, 0),
  (2227951, 1, 1),
  (2228524, 3, 0),
  (2229832, 2, 2),
  (2231141, 0, 2),
  (2231364, 3, 2),
  (2231518, 2, 0),
  (2235544, 0, 1),
  (2238178, 1, 2),
  (2239496, 0, 1),
  (2243179, 2, 2),
  (2243370, 1, 0),
  (2245361, 1, 0),
  (2246036, 0, 1),
  (2251974, 0, 0),
  (2252250, 3, 0),
  (2252254, 3, 1),
  (2252424, 0, 1),
  (2252492, 3, 1),
  (2252600, 1, 2),
  (2253431, 2, 0),
  (2254299, 0, 0),
  (2254309, 1, 1),
  (2257243, 1, 0),
  (2258140, 1, 2),
  (2258360, 2, 2),
  (2258661, 1, 1),
  (2259814, 0, 2),
  (2262111, 2, 2),
  (2263923, 2, 1),
  (2263957, 0, 1),
  (2266061, 3, 2),
  (2267972, 3, 1),
  (2268297, 1, 1),
  (2268558, 1, 2),
  (2269102, 1, 1),
  (2272117, 0, 0),
  (2274697, 3, 2),
  (2280600, 0, 2),
  (2280782, 1, 1),
  (2282311, 3, 2),
  (2286232, 3, 2),
  (2289640, 0, 0),
  (2294179, 2, 0),
  (2294190, 0, 1),
  (2297269, 2, 2),
  (2297719, 0, 0),
  (2302469, 2, 1),
  (2303929, 1, 1),
  (2305316, 0, 2),
  (2306273, 3, 1),
  (2312305, 0, 2),
  (2315024, 1, 0),
  (2315496, 2, 1),
  (2316449, 2, 2),
  (2317969, 3, 0),
  (2318652, 1, 1),
  (2321863, 1, 0),
  (2325460, 0, 1),
  (2326569, 3, 2),
  (2327329, 3, 2),
  (2327460, 3, 1),
  (2328429, 3, 1),
  (2330721, 2, 1),
  (2332513, 3, 2),
  (2336335, 2, 1),
  (2339613, 3, 1),
  (2343716, 3, 0),
  (2346377, 0, 2),
  (2347441, 1, 0),
  (2351268, 1, 1),
  (2352051, 3, 0),
  (2352570, 1, 1),
  (2355705, 3, 0),
  (2358245, 1, 2),
  (2360653, 2, 0),
  (2361197, 1, 0),
  (2373861, 3, 2),
  (2374398, 1, 0),
  (2374974, 2, 2),
  (2376023, 3, 2),
  (2378014, 3, 1),
  (2378858, 2, 2),
  (2379225, 1, 0),
  (2379640, 2, 0),
  (2380288, 1, 2),
  (2380451, 3, 1),
  (2380642, 3, 2),
  (2383625, 0, 0),
  (2385918, 2, 1),
  (2386272, 1, 1),
  (2387655, 2, 2),
  (2390802, 3, 0),
  (2395221, 2, 0),
  (2395560, 1, 1),
  (2396701, 2, 0),
  (2397106, 2, 2),
  (2397274, 2, 0),
  (2397311, 0, 2),
  (2399754, 1, 1),
  (2402756, 0, 2),
  (2404827, 2, 0),
  (2407355, 0, 1),
  (2407815, 3, 2),
  (2408085, 0, 0),
  (2413606, 1, 2),
  (2414438, 3, 1),
  (2416303, 0, 2),
  (2416369, 3, 2),
  (2417142, 1, 2),
  (2417906, 3, 0),
  (2418934, 1, 2),
  (2420091, 1, 0),
  (2420363, 2, 1),
  (2422804, 2, 1),
  (2423667, 0, 0),
  (2423958, 0, 2),
  (2425731, 3, 2),
  (2431941, 1, 2),
  (2435225, 2, 0),
  (2436709, 0, 2),
  (2444242, 0, 0),
  (2445852, 3, 0),
  (2446397, 1, 2),
  (2446790, 0, 0),
  (2450512, 1, 1),
  (2452379, 1, 1),
  (2455729, 3, 0),
  (2455826, 2, 2),
  (2456323, 1, 0),
  (2457582, 1, 0),
  (2459243, 1, 1),
  (2459855, 1, 1),
  (2461048, 0, 1),
  (2462226, 1, 0),
  (2464816, 1, 0),
  (2466501, 3, 1),
  (2466508, 1, 0),
  (2466768, 3, 0),
  (2468214, 3, 1),
  (2468479, 1, 1),
  (2468930, 2, 0),
  (2468950, 0, 1),
  (2470216, 3, 0),
  (2471648, 0, 2),
  (2472401, 2, 0),
  (2473121, 0, 0),
  (2476706, 0, 2),
  (2478218, 0, 2),
  (2478223, 0, 1),
  (2481092, 3, 2),
  (2481429, 1, 0),
  (2483479, 0, 0),
  (2484231, 3, 0),
  (2487318, 0, 1),
  (2491071, 2, 1),
  (2491488, 1, 2),
  (2495750, 0, 1),
  (2496926, 3, 0),
  (2504383, 1, 2),
  (2508745, 0, 0),
  (2511443, 0, 1),
  (2513138, 0, 2),
  (2516494, 3, 0),
  (2518027, 0, 0),
  (2518059, 3, 0),
  (2519518, 3, 2),
  (2519851, 3, 1),
  (2524041, 3, 1),
  (2526889, 3, 0),
  (2527732, 3, 1),
  (2528074, 3, 2),
  (2528390, 1, 0),
  (2531382, 2, 1),
  (2531778, 3, 0),
  (2534762, 3, 0),
  (2538112, 2, 0),
  (2538840, 3, 1),
  (2538977, 1, 1),
  (2542389, 1, 2),
  (2543431, 3, 1),
  (2543575, 1, 2),
  (2544095, 0, 0),
  (2546423, 1, 2),
  (2547464, 3, 0),
  (2549774, 0, 2),
  (2550914, 2, 1),
  (2553140, 0, 0),
  (2554477, 0, 2),
  (2556274, 3, 0),
  (2556574, 1, 2),
  (2557749, 3, 0),
  (2558684, 2, 1),
  (2563528, 0, 2),
  (2565352, 3, 0),
  (2573988, 2, 1),
  (2575314, 3, 1),
  (2579022, 2, 1),
  (2584458, 1, 1),
  (2586624, 2, 1),
  (2586941, 3, 0),
  (2587066, 1, 1),
  (2587916, 0, 2),
  (2593666, 0, 2),
  (2597230, 0, 2),
  (2597764, 2, 2),
  (2606111, 2, 0),
  (2618982, 2, 1),
  (2619637, 0, 1),
  (2620765, 1, 2),
  (2621501, 2, 0),
  (2624880, 2, 1),
  (2625311, 0, 2),
  (2630734, 0, 2),
  (2636491, 1, 2),
  (2638342, 3, 2),
  (2639775, 1, 2),
  (2642125, 1, 2),
  (2642497, 0, 2),
  (2644845, 3, 0),
  (2648232, 2, 1),
  (2648603, 0, 0),
  (2649661, 1, 0),
  (2651696, 2, 1),
  (2656914, 2, 2),
  (2657341, 2, 0),
  (2658526, 0, 0),
  (2668310, 0, 2),
  (2668964, 2, 0),
  (2669178, 0, 2),
  (2670303, 3, 1),
  (2671192, 1, 0),
  (2674721, 2, 2),
  (2677859, 1, 1),
  (2683140, 2, 0),
  (2683605, 3, 1),
  (2685094, 3, 0),
  (2686872, 2, 1),
  (2688521, 0, 2),
  (2693062, 1, 0),
  (2693875, 2, 2),
  (2697320, 0, 1),
  (2698185, 1, 0),
  (2698880, 0, 1),
  (2703217, 1, 0),
  (2703705, 2, 0),
  (2705009, 2, 2),
  (2706095, 0, 2),
  (2706127, 2, 1),
  (2711215, 1, 1),
  (2711540, 2, 0),
  (2712011, 3, 1),
  (2715420, 2, 0),
  (2715900, 0, 1),
  (2715959, 1, 1),
  (2718326, 2, 0),
  (2720160, 2, 1),
  (2721142, 1, 2),
  (2721187, 2, 2),
  (2723956, 2, 0),
  (2724458, 2, 0),
  (2725249, 2, 1),
  (2726514, 0, 2),
  (2727444, 2, 2),
  (2731086, 1, 0),
  (2734710, 3, 0),
  (2736482, 3, 0),
  (2736806, 2, 2),
  (2739731, 0, 2),
  (2746058, 1, 2),
  (2746443, 1, 1),
  (2746704, 1, 1),
  (2746833, 3, 1),
  (2747903, 1, 1),
  (2750700, 3, 1),
  (2750964, 1, 0),
  (2752538, 3, 2),
  (2752808, 3, 2),
  (2755357, 0, 0),
  (2755531, 3, 1),
  (2756965, 3, 1),
  (2758009, 1, 2),
  (2758880, 1, 2),
  (2760147, 2, 1),
  (2760601, 2, 0),
  (2762064, 2, 1),
  (2763599, 1, 1),
  (2765307, 3, 1),
  (2765753, 1, 0),
  (2766534, 0, 1),
  (2767734, 3, 0),
  (2770971, 0, 1),
  (2771557, 1, 2),
  (2775236, 3, 1),
  (2777064, 1, 1),
  (2777981, 1, 2),
  (2784182, 2, 1),
  (2786329, 2, 0),
  (2788876, 2, 2),
  (2790989, 1, 1),
  (2792340, 2, 2),
  (2792938, 0, 2),
  (2794534, 2, 1),
  (2794783, 0, 1),
  (2796191, 2, 0),
  (2797780, 2, 1),
  (2811607, 2, 0),
  (2813174, 1, 0),
  (2817070, 0, 1),
  (2818327, 1, 0),
  (2818579, 0, 0),
  (2818822, 0, 0),
  (2820590, 1, 0),
  (2822873, 2, 0),
  (2832190, 0, 0),
  (2836106, 3, 0),
  (2840088, 0, 0),
  (2840347, 3, 1),
  (2842487, 2, 2),
  (2843435, 2, 0),
  (2846336, 2, 2),
  (2847628, 2, 2),
  (2850488, 1, 2),
  (2850634, 3, 0),
  (2850838, 2, 2),
  (2851040, 0, 0),
  (2852904, 3, 2),
  (2853958, 1, 1),
  (2855566, 2, 0),
  (2860575, 3, 1),
  (2863199, 3, 2),
  (2864834, 2, 2),
  (2865375, 3, 2),
  (2866007, 1, 0),
  (2869575, 3, 1),
  (2871809, 1, 1),
  (2872701, 2, 0),
  (2874475, 2, 1),
  (2878269, 0, 0),
  (2879622, 2, 1),
  (2881457, 1, 0),
  (2881788, 3, 2),
  (2882307, 1, 2),
  (2882778, 3, 1),
  (2884625, 1, 1),
  (2885100, 0, 0),
  (2886850, 2, 2),
  (2890805, 0, 2),
  (2891761, 3, 2),
  (2896589, 3, 1),
  (2897075, 2, 0),
  (2898689, 2, 2),
  (2902626, 0, 2),
  (2908141, 3, 0),
  (2908270, 1, 2),
  (2910187, 2, 1),
  (2911035, 2, 2),
  (2911457, 1, 1),
  (2915243, 2, 1),
  (2919765, 1, 2),
  (2922146, 1, 0),
  (2923976, 3, 1),
  (2926191, 2, 1),
  (2928432, 3, 2),
  (2930012, 2, 0),
  (2932654, 1, 1),
  (2936373, 1, 2),
  (2937232, 0, 0),
  (2940394, 1, 2),
  (2941662, 1, 2),
  (2945974, 2, 0),
  (2947783, 2, 1),
  (2948043, 2, 1),
  (2949564, 2, 2),
  (2950915, 1, 2),
  (2952597, 2, 0),
  (2954161, 1, 1),
  (2955384, 3, 2),
  (2955458, 3, 0),
  (2956346, 2, 1),
  (2958382, 0, 1),
  (2959010, 2, 1),
  (2959885, 3, 0),
  (2959906, 3, 2),
  (2961663, 0, 1),
  (2962345, 0, 0),
  (2963279, 3, 2),
  (2964908, 2, 1),
  (2966778, 0, 1),
  (2966940, 0, 0),
  (2969426, 1, 0),
  (2971908, 1, 1),
  (2972584, 0, 0),
  (2974002, 0, 1),
  (2976834, 1, 2),
  (2977590, 0, 2),
  (2982920, 0, 2),
  (2983821, 2, 1),
  (2984272, 0, 1),
  (2990317, 0, 2),
  (2993135, 2, 0),
  (2993273, 1, 0),
  (2994317, 1, 0),
  (2994506, 2, 1),
  (2995734, 1, 0),
  (2996190, 0, 1),
  (2996823, 1, 2),
  (2997981, 2, 2),
  (3001281, 0, 2),
  (3002254, 3, 1),
  (3003123, 0, 2),
  (3005159, 1, 2),
  (3006320, 1, 1),
  (3006977, 0, 1),
  (3009924, 1, 1),
  (3010170, 2, 0),
  (3010303, 1, 2),
  (3013679, 3, 1),
  (3014497, 3, 0),
  (3015968, 3, 0),
  (3017422, 1, 1),
  (3017981, 3, 2),
  (3023164, 2, 0),
  (3023967, 0, 2),
  (3024686, 0, 0),
  (3032999, 2, 2),
  (3035873, 3, 2),
  (3039175, 2, 0),
  (3039444, 3, 1),
  (3040234, 3, 0),
  (3041976, 3, 0),
  (3042019, 0, 0),
  (3045195, 0, 1),
  (3047000, 1, 1),
  (3047051, 0, 0),
  (3047581, 3, 0),
  (3048059, 3, 0),
  (3049831, 3, 1),
  (3050279, 3, 1),
  (3054049, 3, 0),
  (3064961, 1, 0),
  (3065627, 2, 2),
  (3066640, 3, 1),
  (3070283, 3, 2),
  (3071627, 0, 0),
  (3075735, 2, 1),
  (3081966, 1, 0),
  (3083341, 1, 1),
  (3084929, 3, 2),
  (3085498, 1, 1),
  (3086780, 0, 2),
  (3088519, 2, 2),
  (3091697, 0, 2),
  (3092336, 0, 1),
  (3092415, 3, 0),
  (3094177, 1, 0),
  (3095239, 1, 0),
  (3095523, 0, 0),
  (3095971, 2, 0),
  (3097343, 2, 2),
  (3101567, 2, 1),
  (3101951, 0, 1),
  (3103650, 0, 0),
  (3106213, 2, 0),
  (3109307, 0, 2),
  (3110213, 0, 2),
  (3111694, 3, 0),
  (3112083, 3, 0),
  (3117112, 2, 1),
  (3117379, 2, 0),
  (3117444, 1, 0),
  (3124683, 2, 2),
  (3127557, 1, 2),
  (3128884, 0, 1),
  (3129692, 2, 1),
  (3129749, 1, 0),
  (3130367, 3, 0),
  (3130503, 0, 2),
  (3131057, 2, 2),
  (3131661, 1, 1),
  (3137454, 1, 2),
  (3138918, 0, 0),
  (3140085, 0, 1),
  (3144564, 0, 0),
  (3147051, 0, 0),
  (3151507, 0, 2),
  (3153612, 3, 1),
  (3153876, 1, 0),
  (3153939, 3, 1),
  (3155066, 0, 0),
  (3156290, 1, 2),
  (3157385, 0, 2),
  (3158899, 0, 2),
  (3163718, 3, 0),
  (3166464, 0, 0),
  (3168968, 3, 2),
  (3170428, 0, 1),
  (3170517, 0, 2),
  (3170826, 2, 0),
  (3171346, 2, 2),
  (3172117, 0, 2),
  (3174560, 1, 1),
  (3176910, 3, 1),
  (3177619, 0, 2),
  (3179897, 0, 1),
  (3181159, 0, 2),
  (3181703, 3, 1),
  (3182138, 3, 0),
  (3182166, 3, 1),
  (3184553, 1, 2),
  (3185495, 0, 2),
  (3186145, 0, 0),
  (3188856, 3, 2),
  (3191259, 2, 1),
  (3196044, 3, 1),
  (3199472, 2, 0),
  (3199749, 3, 0),
  (3199861, 1, 1),
  (3201606, 0, 1),
  (3202636, 1, 2),
  (3203220, 1, 1),
  (3203315, 0, 0),
  (3205195, 3, 0),
  (3206758, 1, 1),
  (3208435, 2, 2),
  (3211956, 0, 1),
  (3215593, 2, 1),
  (3216496, 3, 0),
  (3216888, 3, 0),
  (3218361, 2, 0),
  (3220593, 0, 2),
  (3225923, 2, 2),
  (3227178, 3, 0),
  (3227226, 0, 1),
  (3227871, 2, 2),
  (3233423, 0, 1),
  (3233777, 3, 0),
  (3233934, 3, 2),
  (3234970, 1, 2),
  (3237912, 2, 1),
  (3242663, 3, 1),
  (3245314, 3, 0),
  (3245744, 2, 2),
  (3249401, 1, 2),
  (3252186, 3, 1),
  (3252676, 2, 2),
  (3253885, 0, 0),
  (3258047, 0, 2),
  (3258424, 2, 2),
  (3258500, 0, 1),
  (3260207, 3, 2),
  (3261637, 2, 2),
  (3262667, 0, 0),
  (3262687, 2, 2),
  (3267384, 2, 1),
  (3271017, 2, 0),
  (3271572, 2, 1),
  (3278088, 2, 0),
  (3278251, 3, 0),
  (3279871, 0, 1),
  (3282199, 1, 2),
  (3283080, 1, 0),
  (3284124, 2, 2),
  (3285052, 1, 2),
  (3286382, 3, 0),
  (3287961, 1, 1),
  (3292424, 3, 0),
  (3295637, 0, 0),
  (3297281, 2, 2),
  (3299563, 2, 0),
  (3300230, 1, 1),
  (3303051, 2, 1),
  (3311530, 2, 2),
  (3313810, 0, 1),
  (3313949, 3, 2),
  (3314482, 0, 1),
  (3317004, 2, 0),
  (3321192, 3, 1),
  (3321358, 3, 0),
  (3323416, 1, 2),
  (3323601, 2, 2),
  (3329212, 0, 1),
  (3332469, 1, 2),
  (3333181, 3, 0),
  (3333399, 2, 2),
  (3333501, 3, 2),
  (3334512, 0, 0),
  (3334647, 0, 2),
  (3335307, 1, 1),
  (3336007, 3, 2),
  (3337718, 1, 2),
  (3339855, 0, 0),
  (3340240, 1, 0),
  (3345168, 2, 2),
  (3346104, 1, 1),
  (3348210, 0, 0),
  (3349239, 2, 0),
  (3350083, 3, 2),
  (3351383, 1, 0),
  (3353181, 0, 1),
  (3353839, 0, 0),
  (3354898, 2, 0),
  (3356419, 1, 1),
  (3362374, 1, 2),
  (3363758, 3, 1),
  (3369140, 0, 1),
  (3369560, 1, 0),
  (3370903, 1, 0),
  (3372744, 1, 2),
  (3373102, 2, 2),
  (3373899, 0, 2),
  (3374147, 0, 1),
  (3374167, 0, 1),
  (3376259, 1, 1),
  (3376581, 1, 2),
  (3377514, 2, 1),
  (3377629, 1, 1),
  (3379357, 1, 1),
  (3380167, 2, 2),
  (3381459, 2, 1),
  (3386485, 2, 1),
  (3387425, 2, 1),
  (3400343, 2, 2),
  (3400698, 2, 2),
  (3401728, 2, 0),
  (3403861, 3, 2),
  (3405564, 1, 2),
  (3406849, 3, 0),
  (3420421, 2, 1),
  (3421710, 0, 1),
  (3426654, 1, 1),
  (3429548, 1, 0),
  (3435337, 0, 1),
  (3435549, 2, 1),
  (3436736, 1, 2),
  (3437821, 3, 1),
  (3437889, 0, 1),
  (3439524, 0, 0),
  (3441907, 2, 0),
  (3445151, 1, 1),
  (3449649, 2, 0),
  (3451198, 2, 0),
  (3451426, 1, 1),
  (3452278, 1, 1),
  (3461941, 0, 1),
  (3461949, 3, 1),
  (3463135, 2, 0),
  (3464255, 0, 1),
  (3464437, 1, 1),
  (3467769, 2, 1),
  (3470166, 2, 0),
  (3474615, 1, 1),
  (3476917, 2, 0),
  (3479101, 0, 1),
  (3480998, 0, 0),
  (3486119, 3, 0),
  (3487902, 1, 0),
  (3488845, 0, 2),
  (3489282, 3, 1),
  (3490541, 2, 0),
  (3493889, 1, 1),
  (3494660, 3, 2),
  (3495747, 0, 2),
  (3500665, 1, 2),
  (3500902, 3, 1),
  (3503857, 0, 1),
  (3505902, 2, 1),
  (3506047, 3, 0),
  (3507592, 3, 0),
  (3509323, 3, 2),
  (3509568, 2, 2),
  (3509659, 3, 1),
  (3511824, 1, 1),
  (3514661, 1, 2),
  (3515796, 3, 1),
  (3520848, 2, 0),
  (3523358, 3, 2),
  (3523382, 2, 2),
  (3526492, 1, 2),
  (3530887, 0, 0),
  (3531024, 0, 1),
  (3532921, 1, 0),
  (3534438, 2, 2),
  (3534717, 2, 0),
  (3535634, 1, 2),
  (3541592, 1, 2),
  (3542020, 1, 0),
  (3543783, 2, 2),
  (3544090, 3, 2),
  (3545383, 1, 1),
  (3547752, 1, 1),
  (3548571, 2, 0),
  (3549709, 3, 2),
  (3552532, 0, 2),
  (3553996, 3, 1),
  (3555194, 0, 1),
  (3557356, 0, 2),
  (3557705, 0, 1),
  (3561537, 3, 1),
  (3561614, 1, 1),
  (3562783, 0, 0),
  (3562965, 2, 0),
  (3565355, 1, 1),
  (3565669, 3, 2),
  (3566743, 3, 2),
  (3568231, 1, 1),
  (3569398, 2, 0),
  (3569713, 1, 2),
  (3570186, 3, 2),
  (3571061, 0, 1),
  (3571815, 2, 1),
  (3573896, 0, 1),
  (3576203, 1, 0),
  (3577322, 3, 0),
  (3580889, 0, 1),
  (3581975, 0, 2),
  (3582308, 3, 1),
  (3583054, 2, 1),
  (3583646, 2, 2),
  (3584642, 1, 2),
  (3584810, 1, 1),
  (3588014, 3, 1),
  (3588191, 0, 1),
  (3588386, 2, 2),
  (3589120, 0, 1),
  (3589963, 2, 0),
  (3592952, 0, 2),
  (3594314, 2, 0),
  (3594607, 1, 2),
  (3596734, 0, 1),
  (3598794, 2, 0),
  (3599651, 0, 2),
])
