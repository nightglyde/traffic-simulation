from src.util import *
schedule = deque([
  (1019, 3, 1),
  (1384, 1, 1),
  (3017, 3, 1),
  (8148, 0, 0),
  (8305, 0, 1),
  (9305, 3, 2),
  (11677, 1, 2),
  (11850, 1, 2),
  (13214, 0, 1),
  (13328, 1, 0),
  (13505, 2, 0),
  (16574, 1, 1),
  (16607, 2, 1),
  (17301, 1, 2),
  (21511, 0, 1),
  (21685, 2, 1),
  (23911, 3, 1),
  (25621, 3, 0),
  (30408, 3, 0),
  (30640, 3, 2),
  (33858, 3, 0),
  (34113, 2, 1),
  (37061, 2, 1),
  (41499, 0, 2),
  (46315, 2, 0),
  (50812, 1, 2),
  (51924, 3, 2),
  (52427, 1, 1),
  (53368, 2, 0),
  (57683, 0, 0),
  (58241, 3, 1),
  (58476, 1, 0),
  (58498, 1, 2),
  (60530, 3, 2),
  (62120, 0, 2),
  (62906, 1, 2),
  (63040, 2, 2),
  (68755, 3, 0),
  (69810, 2, 1),
  (70831, 3, 1),
  (72756, 1, 0),
  (74018, 2, 1),
  (77152, 0, 2),
  (78399, 3, 1),
  (81460, 0, 0),
  (82018, 2, 0),
  (82607, 0, 0),
  (84111, 3, 2),
  (87198, 2, 0),
  (89840, 1, 0),
  (90866, 0, 1),
  (93085, 0, 0),
  (93203, 1, 0),
  (94268, 2, 1),
  (96242, 0, 2),
  (96521, 1, 0),
  (96969, 2, 2),
  (96989, 1, 2),
  (97046, 1, 0),
  (100032, 2, 0),
  (100137, 1, 1),
  (102081, 0, 0),
  (102400, 0, 0),
  (103170, 3, 0),
  (104782, 1, 2),
  (107848, 0, 1),
  (110006, 0, 0),
  (111745, 0, 1),
  (118662, 2, 1),
  (120452, 2, 1),
  (122002, 1, 0),
  (122699, 1, 0),
  (124888, 1, 0),
  (125647, 3, 0),
  (137163, 1, 2),
  (139629, 0, 2),
  (143607, 3, 1),
  (144525, 1, 1),
  (145261, 3, 2),
  (146682, 1, 1),
  (152105, 1, 2),
  (156639, 0, 0),
  (157790, 0, 1),
  (158005, 2, 2),
  (159631, 3, 0),
  (163523, 2, 0),
  (164357, 1, 0),
  (170065, 3, 2),
  (170105, 1, 0),
  (170759, 2, 2),
  (174299, 3, 2),
  (176882, 3, 0),
  (181540, 1, 0),
  (185417, 3, 0),
  (192058, 3, 2),
  (195010, 2, 0),
  (195534, 1, 1),
  (195966, 3, 0),
  (196590, 1, 0),
  (200095, 3, 2),
  (205676, 1, 1),
  (206063, 1, 1),
  (206180, 1, 0),
  (209166, 0, 0),
  (210881, 1, 0),
  (211215, 1, 1),
  (218137, 3, 1),
  (218329, 1, 1),
  (218394, 1, 2),
  (220769, 1, 2),
  (221133, 1, 2),
  (222621, 3, 0),
  (222803, 0, 2),
  (223393, 2, 2),
  (224585, 0, 0),
  (225450, 0, 1),
  (227306, 2, 0),
  (231399, 2, 1),
  (231536, 2, 1),
  (231773, 3, 1),
  (231846, 0, 2),
  (236180, 1, 2),
  (236870, 3, 2),
  (239852, 3, 0),
  (241682, 3, 2),
  (242220, 2, 2),
  (244475, 1, 2),
  (245942, 1, 1),
  (249453, 1, 2),
  (251678, 0, 1),
  (255440, 1, 2),
  (255915, 0, 0),
  (258625, 1, 2),
  (268215, 3, 0),
  (268755, 1, 0),
  (269532, 1, 1),
  (272775, 3, 1),
  (273039, 2, 0),
  (275961, 0, 0),
  (287507, 2, 2),
  (289426, 2, 0),
  (291683, 2, 0),
  (292550, 1, 0),
  (299519, 3, 2),
  (299808, 1, 2),
  (302575, 1, 1),
  (303087, 0, 0),
  (307230, 2, 0),
  (308973, 1, 0),
  (309285, 1, 0),
  (312043, 3, 0),
  (313532, 3, 1),
  (314744, 1, 0),
  (317243, 3, 2),
  (318189, 3, 0),
  (320255, 2, 2),
  (320656, 0, 2),
  (325396, 2, 2),
  (325913, 2, 2),
  (332920, 0, 1),
  (336643, 3, 0),
  (337071, 1, 1),
  (337241, 3, 0),
  (339679, 2, 2),
  (344066, 0, 1),
  (347221, 1, 1),
  (347662, 2, 1),
  (349299, 1, 2),
  (351233, 0, 2),
  (354176, 2, 0),
  (354289, 3, 2),
  (356935, 0, 2),
  (358606, 0, 2),
  (359871, 0, 2),
  (360235, 2, 0),
  (360265, 1, 2),
  (362331, 1, 0),
  (363100, 2, 0),
  (363349, 2, 0),
  (370149, 3, 1),
  (370443, 2, 0),
  (371284, 0, 0),
  (378762, 0, 0),
  (380600, 2, 0),
  (380658, 1, 0),
  (381953, 2, 2),
  (383309, 2, 1),
  (383453, 3, 2),
  (385416, 2, 1),
  (391231, 0, 1),
  (395553, 1, 2),
  (395831, 0, 1),
  (395921, 3, 1),
  (396388, 2, 0),
  (398901, 1, 2),
  (399558, 2, 2),
  (400443, 0, 0),
  (401175, 3, 2),
  (402968, 3, 1),
  (403363, 3, 0),
  (405128, 0, 1),
  (407200, 1, 0),
  (408912, 3, 1),
  (409278, 1, 2),
  (409762, 3, 1),
  (410391, 1, 0),
  (417981, 2, 0),
  (420603, 1, 2),
  (421900, 3, 0),
  (423988, 2, 0),
  (425273, 0, 2),
  (430098, 2, 2),
  (430148, 3, 1),
  (432592, 0, 2),
  (433377, 0, 0),
  (434730, 2, 2),
  (436166, 0, 1),
  (436994, 0, 0),
  (437734, 3, 0),
  (438244, 0, 1),
  (439115, 3, 0),
  (444858, 1, 2),
  (445632, 1, 1),
  (446065, 2, 2),
  (446181, 1, 0),
  (447358, 1, 1),
  (448185, 0, 2),
  (448547, 1, 2),
  (449262, 3, 2),
  (451750, 1, 1),
  (453982, 0, 0),
  (457599, 1, 1),
  (459599, 0, 0),
  (461649, 1, 2),
  (465614, 2, 2),
  (466600, 1, 0),
  (468466, 2, 2),
  (469282, 2, 2),
  (469545, 1, 2),
  (471137, 3, 2),
  (471747, 0, 1),
  (474202, 1, 1),
  (474329, 3, 2),
  (476015, 1, 0),
  (477407, 0, 2),
  (477608, 1, 0),
  (485235, 0, 0),
  (487336, 3, 2),
  (488303, 0, 2),
  (490156, 2, 1),
  (490879, 0, 2),
  (490996, 0, 0),
  (491376, 3, 2),
  (491419, 0, 2),
  (496568, 1, 1),
  (499508, 0, 1),
  (499709, 2, 0),
  (499833, 1, 1),
  (501295, 3, 2),
  (501815, 0, 2),
  (501841, 0, 2),
  (502143, 2, 2),
  (504520, 1, 2),
  (505711, 2, 0),
  (506484, 1, 2),
  (508029, 0, 2),
  (508830, 1, 0),
  (509270, 0, 2),
  (510911, 2, 0),
  (512054, 0, 2),
  (512158, 3, 2),
  (513313, 3, 2),
  (515328, 1, 1),
  (518300, 1, 2),
  (519284, 2, 0),
  (520526, 0, 0),
  (521227, 0, 0),
  (521803, 1, 0),
  (523529, 3, 0),
  (526562, 2, 0),
  (526706, 1, 1),
  (530653, 2, 1),
  (530988, 0, 0),
  (532929, 1, 0),
  (534571, 3, 1),
  (543415, 0, 2),
  (544833, 3, 1),
  (548416, 3, 1),
  (554585, 2, 1),
  (554934, 1, 0),
  (557879, 2, 0),
  (559897, 2, 0),
  (565798, 1, 0),
  (566297, 3, 0),
  (568004, 3, 0),
  (569274, 2, 2),
  (570305, 1, 1),
  (570483, 3, 1),
  (571819, 3, 0),
  (572713, 0, 0),
  (574099, 3, 1),
  (577370, 0, 2),
  (581016, 3, 0),
  (585072, 0, 2),
  (585498, 0, 2),
  (590868, 3, 0),
  (590892, 2, 0),
  (592992, 1, 0),
  (593919, 0, 1),
  (596408, 1, 2),
  (597216, 2, 0),
  (598525, 3, 0),
  (599200, 1, 0),
  (601954, 2, 1),
  (605310, 2, 1),
  (605770, 2, 0),
  (607213, 3, 1),
  (613351, 3, 2),
  (613366, 1, 0),
  (616834, 0, 0),
  (619764, 2, 1),
  (621718, 3, 1),
  (623959, 0, 1),
  (627647, 0, 1),
  (630080, 0, 0),
  (631259, 3, 1),
  (633456, 1, 1),
  (635826, 3, 2),
  (642492, 2, 2),
  (644336, 3, 2),
  (648347, 0, 1),
  (655226, 3, 2),
  (655765, 0, 1),
  (657213, 2, 0),
  (658862, 1, 1),
  (663243, 2, 2),
  (663630, 0, 1),
  (668030, 3, 0),
  (671536, 0, 2),
  (672814, 2, 1),
  (677676, 0, 2),
  (685437, 0, 1),
  (685820, 3, 0),
  (687302, 0, 0),
  (688821, 2, 1),
  (691700, 0, 0),
  (697302, 2, 0),
  (697665, 2, 1),
  (702171, 1, 0),
  (704077, 3, 1),
  (710878, 2, 0),
  (712161, 2, 2),
  (712555, 1, 2),
  (713250, 1, 0),
  (713899, 0, 2),
  (713980, 1, 2),
  (714659, 0, 0),
  (715041, 1, 0),
  (715949, 3, 1),
  (716757, 2, 0),
  (717076, 3, 2),
  (718497, 0, 2),
  (719772, 0, 2),
  (726452, 1, 2),
  (728595, 0, 1),
  (731011, 2, 1),
  (731304, 0, 2),
  (731935, 1, 1),
  (732340, 2, 2),
  (733445, 3, 1),
  (735665, 0, 2),
  (740289, 0, 0),
  (748078, 3, 0),
  (748157, 3, 2),
  (749242, 2, 0),
  (750799, 1, 2),
  (751074, 3, 2),
  (751185, 2, 2),
  (751675, 2, 2),
  (755560, 0, 1),
  (756848, 3, 1),
  (758415, 2, 1),
  (759480, 3, 2),
  (763163, 0, 1),
  (763986, 1, 1),
  (767062, 1, 1),
  (770756, 1, 1),
  (774385, 0, 1),
  (775052, 3, 1),
  (776340, 1, 0),
  (781133, 1, 1),
  (784745, 1, 2),
  (787990, 1, 2),
  (789931, 3, 1),
  (791705, 1, 0),
  (797484, 0, 0),
  (797588, 3, 2),
  (799782, 2, 1),
  (800123, 1, 0),
  (801147, 2, 0),
  (801986, 1, 0),
  (804985, 2, 2),
  (812813, 2, 1),
  (816947, 3, 0),
  (818816, 0, 1),
  (819349, 2, 0),
  (820062, 0, 1),
  (820842, 0, 2),
  (821469, 0, 0),
  (825516, 2, 0),
  (826165, 1, 2),
  (827106, 3, 1),
  (827653, 1, 0),
  (831937, 2, 1),
  (837087, 3, 0),
  (837894, 0, 2),
  (838862, 0, 2),
  (840494, 3, 2),
  (840928, 2, 0),
  (844640, 1, 1),
  (846627, 0, 2),
  (846790, 3, 1),
  (848020, 2, 1),
  (849117, 1, 0),
  (849350, 0, 2),
  (853815, 0, 0),
  (856311, 0, 1),
  (857317, 2, 1),
  (858050, 1, 0),
  (858065, 1, 1),
  (859235, 1, 1),
  (859612, 2, 0),
  (861194, 2, 1),
  (861336, 3, 1),
  (862926, 1, 2),
  (863134, 2, 0),
  (863921, 2, 0),
  (867144, 3, 0),
  (868829, 2, 1),
  (871385, 3, 1),
  (871529, 0, 2),
  (873678, 0, 1),
  (876134, 1, 0),
  (877704, 0, 2),
  (879366, 0, 1),
  (882468, 3, 0),
  (886535, 3, 2),
  (891460, 3, 2),
  (891496, 0, 2),
  (892109, 2, 0),
  (893177, 3, 1),
  (899327, 1, 1),
  (900306, 2, 0),
  (901346, 2, 2),
  (901393, 1, 1),
  (904797, 1, 1),
  (906595, 1, 1),
  (906919, 0, 2),
  (909019, 1, 0),
  (909282, 3, 2),
  (911455, 1, 0),
  (911603, 1, 1),
  (913608, 2, 1),
  (917602, 0, 1),
  (919691, 1, 2),
  (921479, 2, 1),
  (926286, 1, 2),
  (930070, 2, 2),
  (931569, 3, 2),
  (931590, 3, 0),
  (932121, 2, 0),
  (935536, 0, 1),
  (940979, 1, 0),
  (941269, 3, 0),
  (942103, 3, 0),
  (942590, 3, 1),
  (942637, 1, 0),
  (943102, 2, 2),
  (943307, 1, 1),
  (945574, 3, 2),
  (946699, 3, 0),
  (947289, 1, 0),
  (948486, 0, 0),
  (949479, 3, 2),
  (952134, 1, 0),
  (952910, 2, 0),
  (954210, 2, 2),
  (955610, 3, 2),
  (958425, 3, 2),
  (959093, 2, 0),
  (959465, 0, 1),
  (960448, 0, 2),
  (962131, 2, 2),
  (962601, 2, 1),
  (964025, 1, 2),
  (965188, 1, 1),
  (965973, 2, 1),
  (968300, 3, 1),
  (968807, 2, 2),
  (973332, 0, 0),
  (977709, 2, 0),
  (978291, 1, 0),
  (980573, 1, 1),
  (985284, 0, 0),
  (985285, 2, 1),
  (990104, 2, 1),
  (993431, 2, 2),
  (993749, 3, 2),
  (993826, 1, 2),
  (995518, 0, 0),
  (996378, 0, 0),
  (996452, 1, 1),
  (997671, 0, 0),
  (999795, 2, 0),
  (1000614, 1, 1),
  (1001250, 3, 1),
  (1002810, 0, 2),
  (1004837, 0, 0),
  (1007479, 2, 2),
  (1010793, 1, 1),
  (1018465, 3, 1),
  (1023103, 2, 1),
  (1027362, 1, 0),
  (1030551, 1, 0),
  (1031263, 3, 1),
  (1032208, 2, 2),
  (1034605, 3, 1),
  (1035197, 0, 2),
  (1037778, 3, 1),
  (1038553, 3, 0),
  (1040265, 0, 1),
  (1044825, 0, 2),
  (1045038, 0, 0),
  (1045337, 1, 2),
  (1046474, 1, 2),
  (1047125, 3, 2),
  (1048295, 1, 1),
  (1048572, 1, 1),
  (1053875, 0, 2),
  (1054638, 3, 0),
  (1059464, 2, 0),
  (1060032, 1, 0),
  (1063416, 3, 0),
  (1067871, 1, 2),
  (1068980, 0, 0),
  (1070102, 2, 2),
  (1071639, 1, 0),
  (1075046, 1, 2),
  (1075119, 1, 1),
  (1078212, 0, 0),
  (1078589, 0, 1),
  (1079529, 0, 2),
  (1081192, 0, 0),
  (1083572, 2, 2),
  (1087517, 0, 2),
  (1091053, 0, 2),
  (1093720, 2, 2),
  (1094261, 1, 0),
  (1097694, 2, 1),
  (1100628, 0, 1),
  (1106080, 0, 0),
  (1107167, 1, 0),
  (1108339, 0, 1),
  (1110045, 0, 0),
  (1112712, 2, 0),
  (1113972, 2, 2),
  (1114044, 1, 1),
  (1121808, 3, 2),
  (1121887, 1, 2),
  (1123694, 2, 2),
  (1126677, 0, 2),
  (1127834, 1, 1),
  (1128528, 0, 0),
  (1128597, 0, 2),
  (1132643, 2, 1),
  (1132889, 3, 1),
  (1134250, 1, 1),
  (1136126, 3, 2),
  (1139562, 2, 2),
  (1140901, 2, 2),
  (1143505, 3, 2),
  (1144380, 1, 1),
  (1147705, 2, 0),
  (1149145, 1, 1),
  (1153035, 1, 2),
  (1157848, 3, 1),
  (1160036, 3, 1),
  (1160209, 0, 0),
  (1161264, 3, 2),
  (1162271, 1, 1),
  (1162349, 1, 1),
  (1165438, 3, 0),
  (1166995, 2, 1),
  (1169251, 2, 0),
  (1169823, 3, 1),
  (1171368, 2, 2),
  (1177106, 1, 1),
  (1177469, 1, 2),
  (1180758, 0, 2),
  (1180890, 1, 2),
  (1182534, 1, 1),
  (1184040, 0, 2),
  (1187124, 3, 0),
  (1190014, 1, 1),
  (1193064, 0, 2),
  (1194502, 0, 2),
  (1194632, 3, 1),
  (1196857, 0, 0),
  (1197241, 1, 2),
  (1197242, 3, 1),
  (1199041, 0, 2),
  (1199618, 3, 0),
  (1199958, 3, 1),
  (1200370, 2, 1),
  (1200621, 1, 0),
  (1205026, 0, 2),
  (1206576, 0, 0),
  (1209303, 0, 2),
  (1210877, 0, 0),
  (1214056, 1, 0),
  (1214452, 1, 2),
  (1215196, 1, 2),
  (1215800, 1, 2),
  (1218022, 0, 1),
  (1218215, 3, 0),
  (1218321, 3, 0),
  (1218779, 3, 0),
  (1219626, 3, 2),
  (1221079, 1, 1),
  (1224670, 0, 2),
  (1225703, 2, 1),
  (1225993, 1, 2),
  (1227942, 1, 1),
  (1232430, 3, 2),
  (1236522, 3, 2),
  (1239325, 2, 2),
  (1240510, 0, 0),
  (1241622, 3, 2),
  (1246973, 0, 0),
  (1250216, 2, 0),
  (1250841, 1, 2),
  (1251194, 2, 1),
  (1254973, 1, 1),
  (1257373, 2, 1),
  (1258518, 0, 1),
  (1262034, 1, 0),
  (1264845, 2, 1),
  (1267158, 0, 2),
  (1267231, 3, 0),
  (1267358, 2, 2),
  (1275486, 2, 2),
  (1277305, 0, 2),
  (1277417, 3, 0),
  (1281021, 0, 1),
  (1285382, 1, 0),
  (1286420, 1, 1),
  (1290012, 0, 0),
  (1290853, 3, 0),
  (1295734, 3, 0),
  (1296635, 3, 0),
  (1298580, 0, 0),
  (1298584, 3, 0),
  (1300679, 1, 2),
  (1305451, 0, 0),
  (1308350, 0, 1),
  (1309856, 1, 0),
  (1310233, 1, 1),
  (1314676, 2, 0),
  (1318470, 3, 1),
  (1320430, 2, 2),
  (1324536, 3, 1),
  (1329149, 2, 2),
  (1329230, 1, 2),
  (1330769, 1, 1),
  (1332989, 1, 0),
  (1335275, 1, 1),
  (1336239, 1, 1),
  (1337613, 2, 0),
  (1337758, 3, 2),
  (1337908, 0, 2),
  (1338381, 1, 1),
  (1339644, 2, 1),
  (1340612, 3, 0),
  (1341809, 2, 0),
  (1342317, 3, 2),
  (1344079, 3, 0),
  (1347032, 3, 1),
  (1347729, 0, 2),
  (1348915, 0, 0),
  (1349473, 1, 2),
  (1352349, 3, 0),
  (1352471, 1, 1),
  (1355521, 3, 0),
  (1359717, 2, 2),
  (1359898, 3, 0),
  (1360952, 3, 2),
  (1362471, 3, 0),
  (1366847, 2, 2),
  (1367916, 0, 1),
  (1368114, 0, 2),
  (1368391, 2, 1),
  (1371904, 2, 1),
  (1374681, 0, 1),
  (1375123, 1, 1),
  (1376884, 3, 0),
  (1380772, 3, 1),
  (1381562, 0, 1),
  (1383904, 0, 2),
  (1386998, 3, 1),
  (1389214, 1, 1),
  (1389895, 2, 0),
  (1394047, 0, 2),
  (1394373, 3, 1),
  (1397965, 1, 1),
  (1398625, 2, 2),
  (1400548, 1, 2),
  (1400906, 1, 2),
  (1404897, 1, 2),
  (1404979, 1, 0),
  (1407084, 2, 1),
  (1408474, 2, 0),
  (1410795, 3, 1),
  (1410839, 3, 0),
  (1411353, 2, 2),
  (1416369, 3, 2),
  (1420908, 0, 2),
  (1421423, 0, 2),
  (1424501, 2, 0),
  (1426708, 3, 1),
  (1435633, 3, 2),
  (1440126, 0, 1),
  (1442171, 1, 1),
  (1442862, 3, 1),
  (1443263, 1, 0),
  (1443319, 0, 2),
  (1444891, 2, 2),
  (1448104, 3, 2),
  (1449802, 3, 1),
  (1452854, 0, 0),
  (1454101, 0, 2),
  (1454855, 2, 1),
  (1455923, 3, 1),
  (1456089, 2, 2),
  (1457357, 3, 0),
  (1461653, 2, 1),
  (1462014, 2, 2),
  (1466338, 0, 2),
  (1469463, 3, 2),
  (1470592, 0, 2),
  (1471054, 1, 0),
  (1472932, 3, 0),
  (1476393, 1, 2),
  (1477442, 1, 2),
  (1477505, 3, 1),
  (1478856, 1, 2),
  (1480203, 3, 1),
  (1481453, 1, 0),
  (1489339, 0, 0),
  (1494184, 1, 1),
  (1494394, 0, 0),
  (1494417, 0, 0),
  (1496199, 3, 1),
  (1500585, 2, 0),
  (1504942, 0, 2),
  (1505025, 3, 1),
  (1507404, 1, 2),
  (1508121, 0, 1),
  (1508333, 3, 1),
  (1508563, 1, 1),
  (1509770, 0, 0),
  (1510656, 1, 1),
  (1513604, 3, 2),
  (1514129, 2, 0),
  (1516371, 3, 0),
  (1519830, 1, 2),
  (1523300, 3, 1),
  (1526693, 3, 2),
  (1530039, 1, 0),
  (1530145, 3, 1),
  (1533732, 0, 1),
  (1537427, 0, 0),
  (1537678, 0, 0),
  (1538292, 2, 1),
  (1543890, 1, 1),
  (1545709, 0, 2),
  (1545751, 2, 2),
  (1546094, 1, 1),
  (1547353, 2, 2),
  (1548503, 3, 2),
  (1548627, 2, 2),
  (1548745, 0, 2),
  (1549240, 1, 2),
  (1549726, 2, 2),
  (1551385, 3, 2),
  (1552138, 0, 1),
  (1552967, 2, 2),
  (1553323, 3, 0),
  (1553359, 2, 0),
  (1553929, 3, 2),
  (1557537, 0, 1),
  (1560235, 3, 1),
  (1563123, 3, 2),
  (1564418, 0, 2),
  (1566525, 2, 1),
  (1566703, 0, 1),
  (1567232, 3, 1),
  (1569545, 3, 1),
  (1573440, 0, 2),
  (1574568, 1, 2),
  (1575042, 1, 2),
  (1577615, 3, 0),
  (1578074, 0, 2),
  (1579446, 2, 2),
  (1581721, 3, 2),
  (1583248, 2, 0),
  (1584898, 2, 2),
  (1585170, 3, 0),
  (1585360, 3, 0),
  (1591075, 2, 0),
  (1591751, 0, 2),
  (1596192, 2, 2),
  (1599073, 0, 0),
  (1603971, 3, 1),
  (1604013, 0, 0),
  (1610642, 2, 2),
  (1610969, 0, 0),
  (1614304, 2, 0),
  (1614344, 0, 1),
  (1614841, 3, 0),
  (1615880, 2, 1),
  (1618123, 2, 0),
  (1618256, 0, 1),
  (1619768, 2, 0),
  (1620883, 3, 2),
  (1623272, 1, 0),
  (1626580, 1, 2),
  (1629601, 3, 2),
  (1632001, 3, 2),
  (1633094, 0, 0),
  (1634354, 3, 0),
  (1634481, 2, 2),
  (1638782, 3, 1),
  (1639257, 0, 0),
  (1640157, 1, 0),
  (1644728, 2, 2),
  (1644908, 3, 0),
  (1646993, 2, 2),
  (1647857, 3, 1),
  (1648196, 2, 0),
  (1651540, 1, 1),
  (1656361, 3, 1),
  (1658383, 1, 1),
  (1660912, 1, 0),
  (1665251, 3, 2),
  (1666934, 0, 2),
  (1670007, 3, 1),
  (1672652, 2, 1),
  (1679722, 1, 0),
  (1680721, 1, 2),
  (1684639, 3, 0),
  (1685610, 2, 0),
  (1685813, 3, 1),
  (1686165, 0, 0),
  (1686420, 1, 2),
  (1686838, 2, 2),
  (1693310, 2, 2),
  (1697457, 0, 0),
  (1698919, 3, 0),
  (1699151, 1, 1),
  (1699762, 3, 0),
  (1702824, 0, 2),
  (1704248, 2, 0),
  (1704672, 2, 2),
  (1704681, 3, 1),
  (1705784, 1, 0),
  (1705936, 1, 0),
  (1706185, 3, 1),
  (1708965, 0, 1),
  (1709009, 0, 2),
  (1709368, 0, 2),
  (1712488, 3, 1),
  (1713745, 1, 1),
  (1714770, 2, 2),
  (1716201, 0, 1),
  (1717562, 2, 0),
  (1720849, 1, 1),
  (1723189, 0, 0),
  (1723575, 1, 0),
  (1725980, 2, 0),
  (1728203, 2, 0),
  (1729858, 3, 2),
  (1731206, 0, 1),
  (1731423, 2, 1),
  (1732196, 2, 0),
  (1735353, 1, 2),
  (1735501, 0, 2),
  (1735842, 1, 0),
  (1737149, 2, 0),
  (1739340, 1, 0),
  (1742832, 0, 2),
  (1750706, 3, 2),
  (1755313, 2, 1),
  (1756759, 1, 2),
  (1757253, 2, 1),
  (1764365, 3, 0),
  (1765348, 0, 1),
  (1765677, 0, 2),
  (1766433, 1, 1),
  (1770398, 1, 2),
  (1770461, 2, 2),
  (1772840, 2, 2),
  (1773006, 0, 0),
  (1773059, 1, 1),
  (1774245, 0, 0),
  (1776687, 3, 2),
  (1777818, 1, 1),
  (1784181, 3, 1),
  (1785518, 0, 1),
  (1795062, 2, 0),
  (1795804, 2, 0),
  (1796042, 0, 2),
  (1798661, 3, 0),
  (1799540, 1, 2),
  (1800298, 1, 0),
  (1801516, 1, 0),
  (1803268, 0, 0),
  (1804514, 2, 0),
  (1806267, 3, 2),
  (1806601, 1, 0),
  (1808267, 1, 0),
  (1808590, 1, 1),
  (1808740, 1, 0),
  (1811293, 3, 1),
  (1811364, 1, 0),
  (1811591, 0, 1),
  (1811703, 2, 0),
  (1814725, 0, 1),
  (1817339, 0, 0),
  (1817640, 0, 0),
  (1820543, 1, 0),
  (1820617, 3, 2),
  (1821474, 2, 1),
  (1823912, 1, 0),
  (1827037, 2, 0),
  (1827320, 0, 2),
  (1827341, 3, 0),
  (1831159, 1, 1),
  (1831468, 2, 2),
  (1833620, 1, 0),
  (1834509, 3, 1),
  (1844973, 3, 0),
  (1846396, 3, 1),
  (1848585, 0, 1),
  (1849751, 1, 0),
  (1851756, 3, 0),
  (1853474, 1, 2),
  (1855756, 0, 0),
  (1861526, 1, 2),
  (1862053, 3, 1),
  (1863082, 2, 0),
  (1869025, 0, 0),
  (1869389, 0, 2),
  (1869866, 2, 1),
  (1869986, 1, 0),
  (1871477, 2, 0),
  (1872601, 0, 2),
  (1873702, 1, 0),
  (1876812, 1, 0),
  (1878181, 1, 0),
  (1882683, 0, 1),
  (1887329, 0, 0),
  (1889560, 2, 1),
  (1890620, 3, 0),
  (1891144, 1, 1),
  (1891691, 3, 1),
  (1892601, 1, 1),
  (1892619, 2, 2),
  (1893890, 3, 2),
  (1897369, 1, 1),
  (1898358, 3, 1),
  (1905318, 0, 1),
  (1905515, 0, 0),
  (1905645, 1, 2),
  (1906809, 2, 0),
  (1906901, 1, 0),
  (1909132, 1, 2),
  (1909897, 1, 2),
  (1913156, 1, 1),
  (1913816, 1, 1),
  (1914575, 2, 1),
  (1924651, 1, 0),
  (1924764, 1, 0),
  (1927623, 3, 1),
  (1934885, 2, 2),
  (1939078, 3, 1),
  (1942394, 3, 2),
  (1944833, 0, 1),
  (1948647, 3, 2),
  (1950561, 0, 0),
  (1953423, 0, 2),
  (1958394, 3, 1),
  (1958773, 3, 0),
  (1961990, 1, 2),
  (1965431, 0, 1),
  (1967495, 2, 2),
  (1967621, 2, 1),
  (1969632, 3, 2),
  (1970864, 0, 1),
  (1972322, 0, 2),
  (1972640, 3, 0),
  (1974972, 2, 2),
  (1980100, 2, 2),
  (1980733, 2, 1),
  (1984027, 3, 0),
  (1994989, 2, 1),
  (1995224, 3, 2),
  (1998256, 0, 0),
  (2002374, 1, 1),
  (2002796, 2, 1),
  (2009528, 3, 2),
  (2010533, 2, 2),
  (2011836, 1, 1),
  (2017725, 2, 2),
  (2017938, 3, 2),
  (2019084, 1, 0),
  (2020185, 3, 0),
  (2026708, 3, 2),
  (2026717, 1, 2),
  (2027368, 2, 0),
  (2029324, 3, 1),
  (2032598, 1, 1),
  (2035275, 0, 2),
  (2035567, 3, 2),
  (2036101, 0, 1),
  (2036608, 1, 0),
  (2036951, 3, 0),
  (2038614, 3, 2),
  (2040650, 1, 1),
  (2044277, 0, 2),
  (2046413, 2, 0),
  (2049800, 0, 2),
  (2050391, 3, 0),
  (2052165, 3, 0),
  (2053365, 3, 1),
  (2054049, 1, 0),
  (2054833, 3, 1),
  (2056013, 0, 1),
  (2057724, 0, 2),
  (2066441, 1, 1),
  (2067063, 2, 2),
  (2067432, 2, 2),
  (2069638, 2, 1),
  (2070757, 2, 2),
  (2072558, 2, 2),
  (2072609, 3, 1),
  (2077162, 0, 1),
  (2079861, 0, 0),
  (2080520, 2, 2),
  (2082455, 0, 1),
  (2085099, 3, 2),
  (2085354, 3, 0),
  (2085395, 3, 2),
  (2085865, 0, 0),
  (2086177, 2, 0),
  (2086382, 2, 2),
  (2087449, 2, 2),
  (2087450, 2, 0),
  (2090095, 1, 0),
  (2090367, 3, 2),
  (2092615, 2, 2),
  (2094790, 0, 2),
  (2098031, 2, 2),
  (2100912, 1, 0),
  (2110711, 3, 0),
  (2111486, 1, 2),
  (2111931, 0, 1),
  (2113422, 2, 0),
  (2117170, 1, 1),
  (2117659, 1, 1),
  (2118405, 2, 1),
  (2124869, 1, 2),
  (2128018, 3, 1),
  (2129540, 0, 2),
  (2133355, 3, 1),
  (2133526, 3, 1),
  (2137293, 1, 1),
  (2138640, 0, 0),
  (2144304, 1, 0),
  (2145780, 2, 0),
  (2145875, 1, 1),
  (2148632, 3, 0),
  (2149796, 3, 1),
  (2150442, 0, 0),
  (2156968, 0, 2),
  (2160528, 1, 1),
  (2163189, 2, 0),
  (2163849, 0, 0),
  (2164667, 2, 2),
  (2167424, 0, 0),
  (2169011, 2, 1),
  (2169374, 3, 1),
  (2170350, 0, 2),
  (2172183, 2, 1),
  (2172326, 3, 1),
  (2176388, 2, 0),
  (2176517, 3, 1),
  (2179899, 1, 1),
  (2181354, 0, 0),
  (2185922, 3, 2),
  (2187958, 2, 1),
  (2188344, 2, 1),
  (2188507, 0, 1),
  (2190012, 0, 0),
  (2197786, 3, 0),
  (2198214, 2, 2),
  (2199839, 2, 2),
  (2201609, 2, 1),
  (2202381, 1, 1),
  (2205996, 0, 2),
  (2212819, 3, 2),
  (2215198, 3, 2),
  (2216981, 1, 2),
  (2221752, 2, 2),
  (2222836, 0, 2),
  (2223896, 2, 0),
  (2225237, 3, 2),
  (2227314, 0, 2),
  (2231032, 3, 0),
  (2244486, 0, 1),
  (2245125, 2, 2),
  (2246216, 1, 0),
  (2248874, 2, 0),
  (2254864, 3, 1),
  (2255150, 1, 2),
  (2256065, 0, 0),
  (2259649, 1, 0),
  (2259923, 2, 0),
  (2260353, 3, 0),
  (2260754, 2, 2),
  (2267310, 0, 1),
  (2267332, 2, 0),
  (2268865, 1, 1),
  (2271719, 0, 0),
  (2272339, 1, 1),
  (2274007, 2, 0),
  (2275265, 1, 1),
  (2278568, 1, 2),
  (2278839, 0, 0),
  (2282940, 2, 2),
  (2284652, 1, 0),
  (2285681, 2, 0),
  (2287280, 3, 0),
  (2289044, 1, 1),
  (2289848, 3, 1),
  (2291751, 1, 2),
  (2293157, 3, 0),
  (2293668, 2, 0),
  (2301646, 3, 2),
  (2302308, 0, 1),
  (2302757, 0, 1),
  (2303754, 0, 2),
  (2304107, 1, 1),
  (2304482, 0, 1),
  (2305755, 3, 2),
  (2309457, 3, 1),
  (2312797, 1, 0),
  (2313273, 3, 1),
  (2315945, 2, 1),
  (2317594, 3, 2),
  (2317917, 1, 1),
  (2320320, 3, 1),
  (2321853, 2, 1),
  (2322362, 1, 0),
  (2323635, 3, 2),
  (2325543, 0, 2),
  (2330599, 1, 2),
  (2332282, 2, 1),
  (2332623, 3, 1),
  (2340045, 0, 2),
  (2341945, 0, 1),
  (2342500, 1, 0),
  (2347877, 3, 0),
  (2349672, 0, 2),
  (2350297, 2, 0),
  (2350490, 3, 0),
  (2353297, 1, 2),
  (2353601, 2, 1),
  (2356837, 0, 2),
  (2360512, 0, 0),
  (2361225, 3, 0),
  (2363226, 1, 1),
  (2368555, 2, 2),
  (2371125, 0, 0),
  (2373869, 2, 0),
  (2384066, 3, 2),
  (2392538, 3, 0),
  (2393402, 3, 0),
  (2394067, 2, 0),
  (2395437, 1, 0),
  (2398218, 1, 2),
  (2399933, 3, 0),
  (2401826, 2, 2),
  (2402186, 1, 0),
  (2402534, 3, 1),
  (2403575, 0, 0),
  (2408818, 0, 2),
  (2409502, 3, 0),
  (2415580, 0, 2),
  (2416679, 2, 1),
  (2416865, 2, 0),
  (2419884, 3, 2),
  (2424763, 0, 0),
  (2428690, 1, 1),
  (2432509, 0, 0),
  (2434322, 2, 1),
  (2436376, 3, 2),
  (2437267, 0, 2),
  (2440881, 2, 2),
  (2442015, 1, 2),
  (2442153, 2, 2),
  (2445175, 1, 2),
  (2446264, 2, 1),
  (2447930, 3, 1),
  (2448752, 3, 0),
  (2452013, 3, 2),
  (2452507, 3, 1),
  (2452877, 3, 1),
  (2454587, 0, 2),
  (2458654, 1, 2),
  (2459842, 3, 2),
  (2460964, 0, 0),
  (2464471, 2, 2),
  (2465178, 2, 0),
  (2467191, 2, 0),
  (2471905, 0, 1),
  (2478522, 1, 1),
  (2478832, 0, 2),
  (2479347, 3, 0),
  (2481027, 2, 0),
  (2481873, 3, 0),
  (2483074, 3, 2),
  (2488882, 1, 1),
  (2491537, 3, 1),
  (2493035, 3, 2),
  (2493257, 3, 1),
  (2493591, 1, 0),
  (2497501, 2, 0),
  (2497999, 3, 0),
  (2501331, 3, 1),
  (2503403, 3, 1),
  (2504429, 0, 0),
  (2505257, 2, 2),
  (2506041, 2, 1),
  (2506500, 3, 2),
  (2509890, 1, 0),
  (2509942, 1, 0),
  (2513096, 2, 2),
  (2519061, 2, 1),
  (2520310, 2, 0),
  (2521175, 3, 0),
  (2522874, 1, 2),
  (2528739, 1, 2),
  (2528805, 1, 1),
  (2529888, 0, 2),
  (2533082, 2, 2),
  (2533083, 2, 1),
  (2533433, 3, 1),
  (2535509, 3, 0),
  (2537011, 2, 0),
  (2538042, 0, 2),
  (2539940, 0, 1),
  (2541837, 1, 2),
  (2546640, 1, 0),
  (2547750, 3, 2),
  (2550678, 2, 0),
  (2551640, 2, 2),
  (2551665, 1, 1),
  (2553657, 0, 2),
  (2555057, 3, 1),
  (2556621, 3, 2),
  (2561972, 2, 1),
  (2562889, 2, 2),
  (2563042, 2, 1),
  (2563107, 3, 1),
  (2564474, 3, 1),
  (2567984, 3, 2),
  (2568576, 0, 1),
  (2570385, 2, 1),
  (2570749, 1, 0),
  (2573571, 1, 0),
  (2574014, 0, 0),
  (2574256, 2, 2),
  (2574684, 1, 2),
  (2578213, 2, 1),
  (2579817, 3, 1),
  (2580811, 1, 1),
  (2580937, 1, 0),
  (2581958, 3, 0),
  (2586078, 1, 1),
  (2587906, 0, 2),
  (2588011, 2, 2),
  (2588606, 1, 0),
  (2592851, 3, 2),
  (2593843, 1, 0),
  (2593971, 1, 2),
  (2595091, 0, 0),
  (2597141, 1, 2),
  (2597141, 3, 1),
  (2597306, 3, 2),
  (2600164, 2, 1),
  (2601048, 2, 2),
  (2601528, 2, 1),
  (2603610, 3, 0),
  (2603729, 3, 0),
  (2605027, 0, 1),
  (2606820, 0, 0),
  (2608095, 1, 1),
  (2610279, 0, 0),
  (2612150, 2, 0),
  (2615618, 1, 2),
  (2616183, 2, 2),
  (2616602, 2, 1),
  (2617361, 0, 1),
  (2617666, 0, 0),
  (2619708, 0, 0),
  (2626487, 1, 2),
  (2627646, 3, 0),
  (2633123, 0, 1),
  (2634254, 3, 0),
  (2635008, 0, 0),
  (2635552, 2, 2),
  (2639556, 3, 1),
  (2641698, 0, 0),
  (2643416, 3, 1),
  (2643427, 0, 1),
  (2645816, 3, 0),
  (2649206, 0, 0),
  (2650322, 0, 2),
  (2653235, 1, 1),
  (2654067, 3, 1),
  (2655696, 1, 2),
  (2657990, 3, 0),
  (2658807, 1, 1),
  (2659986, 1, 2),
  (2660479, 3, 2),
  (2664581, 3, 1),
  (2666160, 2, 1),
  (2666305, 2, 1),
  (2671025, 2, 2),
  (2673476, 3, 0),
  (2673702, 0, 2),
  (2674665, 1, 0),
  (2678279, 3, 1),
  (2678458, 3, 2),
  (2682651, 0, 1),
  (2684137, 3, 1),
  (2684211, 3, 1),
  (2684351, 0, 1),
  (2686343, 2, 1),
  (2686538, 1, 1),
  (2690889, 2, 0),
  (2692110, 3, 0),
  (2692382, 2, 1),
  (2695007, 3, 1),
  (2698278, 2, 0),
  (2699870, 0, 1),
  (2700573, 0, 0),
  (2700817, 0, 1),
  (2703760, 0, 1),
  (2703920, 0, 1),
  (2707410, 3, 1),
  (2709799, 2, 2),
  (2710609, 0, 2),
  (2711931, 0, 0),
  (2716687, 2, 1),
  (2717988, 3, 2),
  (2718551, 1, 2),
  (2722215, 0, 0),
  (2723443, 3, 1),
  (2729379, 1, 0),
  (2734236, 2, 0),
  (2734738, 3, 2),
  (2736730, 3, 0),
  (2740228, 0, 1),
  (2740507, 1, 1),
  (2743537, 0, 1),
  (2744977, 1, 2),
  (2748675, 0, 1),
  (2749094, 0, 2),
  (2749848, 1, 2),
  (2751363, 3, 0),
  (2753023, 0, 1),
  (2753875, 0, 1),
  (2755479, 0, 0),
  (2756622, 2, 1),
  (2760050, 2, 1),
  (2760167, 1, 1),
  (2764101, 2, 2),
  (2764174, 1, 1),
  (2764584, 1, 2),
  (2765552, 2, 1),
  (2765799, 3, 2),
  (2769849, 1, 2),
  (2770123, 1, 2),
  (2778722, 3, 0),
  (2779547, 3, 0),
  (2780261, 3, 2),
  (2780650, 2, 0),
  (2783260, 3, 0),
  (2784804, 0, 0),
  (2785158, 1, 1),
  (2789529, 3, 2),
  (2790328, 1, 2),
  (2791116, 2, 0),
  (2792369, 3, 2),
  (2792863, 3, 1),
  (2795134, 3, 1),
  (2797264, 2, 1),
  (2798082, 1, 0),
  (2802131, 1, 2),
  (2803425, 3, 0),
  (2804505, 3, 1),
  (2808692, 0, 0),
  (2810908, 1, 1),
  (2812631, 3, 0),
  (2813522, 3, 2),
  (2816485, 3, 0),
  (2819306, 2, 2),
  (2821471, 2, 1),
  (2822085, 3, 2),
  (2824275, 0, 2),
  (2827177, 3, 0),
  (2832432, 2, 2),
  (2834157, 0, 2),
  (2835228, 2, 2),
  (2835636, 1, 1),
  (2835811, 0, 0),
  (2836481, 2, 2),
  (2836653, 1, 1),
  (2841330, 1, 2),
  (2842327, 3, 1),
  (2844172, 2, 1),
  (2845334, 0, 1),
  (2847720, 1, 0),
  (2848540, 1, 2),
  (2849813, 1, 1),
  (2851566, 1, 2),
  (2855545, 0, 1),
  (2857772, 2, 0),
  (2857834, 3, 2),
  (2859080, 3, 2),
  (2868642, 2, 1),
  (2868819, 0, 0),
  (2872673, 3, 1),
  (2872741, 0, 0),
  (2873064, 0, 0),
  (2874556, 3, 2),
  (2876920, 1, 0),
  (2877529, 2, 2),
  (2877886, 1, 2),
  (2877948, 0, 0),
  (2878750, 0, 0),
  (2879337, 0, 2),
  (2879609, 2, 0),
  (2883714, 0, 1),
  (2885261, 1, 1),
  (2885316, 2, 2),
  (2886165, 0, 0),
  (2890774, 2, 0),
  (2894683, 0, 0),
  (2894931, 1, 2),
  (2895260, 1, 2),
  (2895693, 3, 0),
  (2897241, 1, 1),
  (2898673, 0, 0),
  (2903775, 3, 0),
  (2905006, 2, 1),
  (2909116, 1, 2),
  (2909364, 0, 0),
  (2912228, 0, 1),
  (2915647, 0, 1),
  (2917687, 2, 2),
  (2929716, 2, 1),
  (2931319, 3, 2),
  (2931554, 3, 0),
  (2932295, 3, 1),
  (2932738, 1, 0),
  (2932752, 1, 2),
  (2932914, 3, 1),
  (2934116, 1, 2),
  (2939345, 1, 1),
  (2943880, 0, 0),
  (2944290, 2, 0),
  (2944614, 2, 2),
  (2945630, 1, 0),
  (2947700, 3, 1),
  (2947870, 3, 1),
  (2949126, 2, 2),
  (2950624, 2, 2),
  (2952496, 0, 2),
  (2952682, 2, 1),
  (2957142, 3, 0),
  (2958530, 2, 2),
  (2958772, 0, 1),
  (2959900, 0, 1),
  (2965718, 0, 2),
  (2966659, 3, 2),
  (2967196, 0, 2),
  (2967779, 0, 1),
  (2970731, 2, 2),
  (2970865, 0, 1),
  (2971450, 3, 1),
  (2971865, 1, 2),
  (2972077, 3, 2),
  (2972365, 0, 0),
  (2975057, 3, 1),
  (2976090, 1, 1),
  (2976333, 2, 0),
  (2977872, 3, 0),
  (2977889, 3, 0),
  (2979833, 1, 2),
  (2982095, 3, 1),
  (2985497, 2, 1),
  (2990507, 1, 0),
  (2994032, 0, 1),
  (2996020, 2, 0),
  (2997821, 0, 0),
  (3002853, 3, 2),
  (3005007, 0, 0),
  (3008942, 2, 1),
  (3011033, 1, 2),
  (3016594, 3, 0),
  (3017781, 1, 1),
  (3020308, 2, 1),
  (3020973, 2, 0),
  (3023323, 1, 2),
  (3028257, 3, 1),
  (3028722, 0, 0),
  (3032604, 1, 0),
  (3034265, 1, 2),
  (3034442, 3, 1),
  (3038488, 3, 1),
  (3038659, 0, 2),
  (3038870, 1, 2),
  (3040576, 1, 2),
  (3041985, 3, 1),
  (3046756, 1, 0),
  (3049139, 1, 2),
  (3050150, 3, 2),
  (3050626, 2, 2),
  (3054879, 3, 2),
  (3062421, 0, 2),
  (3066425, 3, 1),
  (3067337, 0, 0),
  (3070545, 3, 2),
  (3072954, 1, 2),
  (3072973, 2, 0),
  (3073788, 0, 1),
  (3077937, 3, 0),
  (3079342, 1, 0),
  (3081245, 3, 0),
  (3082330, 3, 2),
  (3088290, 2, 1),
  (3089942, 0, 2),
  (3093182, 3, 2),
  (3097604, 1, 0),
  (3102386, 1, 2),
  (3103735, 2, 1),
  (3104417, 3, 0),
  (3104483, 1, 2),
  (3104654, 3, 1),
  (3105422, 2, 1),
  (3106098, 0, 1),
  (3106742, 1, 2),
  (3107028, 3, 1),
  (3109993, 1, 1),
  (3110436, 0, 1),
  (3110448, 3, 2),
  (3115278, 0, 1),
  (3119642, 1, 1),
  (3121008, 1, 2),
  (3124530, 3, 0),
  (3124573, 2, 1),
  (3125092, 3, 2),
  (3125271, 3, 1),
  (3129711, 2, 1),
  (3130627, 0, 0),
  (3131676, 3, 0),
  (3136579, 0, 0),
  (3141928, 1, 1),
  (3145694, 1, 1),
  (3148461, 3, 1),
  (3151775, 3, 2),
  (3152952, 0, 0),
  (3154106, 0, 0),
  (3158745, 3, 1),
  (3165101, 1, 1),
  (3165504, 3, 2),
  (3165844, 1, 0),
  (3179227, 2, 0),
  (3181469, 1, 2),
  (3185400, 3, 2),
  (3186633, 1, 1),
  (3187166, 0, 0),
  (3190298, 1, 2),
  (3190317, 0, 2),
  (3190395, 3, 1),
  (3192914, 1, 2),
  (3199176, 0, 1),
  (3199288, 0, 1),
  (3200908, 2, 1),
  (3201285, 0, 0),
  (3203242, 3, 2),
  (3205349, 2, 0),
  (3206320, 3, 2),
  (3206911, 1, 0),
  (3209222, 3, 0),
  (3211683, 3, 1),
  (3212062, 0, 0),
  (3212471, 2, 1),
  (3216312, 1, 1),
  (3223875, 2, 1),
  (3225768, 3, 2),
  (3226046, 0, 2),
  (3229625, 1, 0),
  (3238094, 0, 2),
  (3240103, 2, 1),
  (3241529, 1, 0),
  (3243486, 2, 0),
  (3245911, 0, 2),
  (3247007, 1, 1),
  (3248622, 2, 2),
  (3253968, 0, 0),
  (3255410, 3, 2),
  (3255422, 1, 1),
  (3259711, 2, 1),
  (3259734, 3, 1),
  (3261165, 0, 1),
  (3264621, 2, 1),
  (3268071, 1, 0),
  (3269326, 0, 1),
  (3270442, 3, 1),
  (3271261, 0, 2),
  (3273029, 2, 0),
  (3275167, 3, 2),
  (3289768, 0, 2),
  (3290675, 1, 0),
  (3292906, 1, 2),
  (3295734, 3, 0),
  (3300850, 3, 0),
  (3303638, 0, 1),
  (3308599, 3, 2),
  (3308834, 0, 2),
  (3310506, 0, 1),
  (3312000, 3, 2),
  (3312932, 3, 0),
  (3324081, 1, 1),
  (3327033, 2, 1),
  (3330418, 0, 0),
  (3331255, 3, 1),
  (3332571, 3, 2),
  (3333968, 1, 1),
  (3335389, 3, 0),
  (3335538, 0, 1),
  (3335872, 1, 0),
  (3337087, 0, 0),
  (3340669, 2, 2),
  (3345449, 0, 1),
  (3345661, 2, 1),
  (3346068, 1, 1),
  (3346792, 0, 2),
  (3347515, 2, 1),
  (3350080, 2, 1),
  (3350181, 2, 2),
  (3351030, 0, 1),
  (3352625, 0, 2),
  (3354029, 1, 0),
  (3361322, 1, 1),
  (3361344, 1, 1),
  (3366817, 0, 2),
  (3369206, 2, 2),
  (3374584, 1, 2),
  (3376471, 1, 0),
  (3378396, 2, 2),
  (3378397, 0, 2),
  (3380208, 0, 0),
  (3380657, 3, 2),
  (3380736, 3, 0),
  (3382572, 3, 1),
  (3383083, 2, 0),
  (3388387, 2, 2),
  (3390724, 3, 0),
  (3391366, 3, 1),
  (3394251, 0, 0),
  (3396463, 0, 2),
  (3398811, 0, 2),
  (3398925, 0, 2),
  (3399116, 0, 2),
  (3403796, 3, 0),
  (3406525, 1, 2),
  (3410493, 3, 2),
  (3410899, 3, 0),
  (3411949, 1, 1),
  (3414048, 2, 2),
  (3415311, 2, 2),
  (3417163, 1, 2),
  (3417727, 2, 2),
  (3422299, 0, 2),
  (3423651, 0, 0),
  (3425483, 3, 0),
  (3426673, 3, 1),
  (3428379, 3, 2),
  (3429811, 2, 1),
  (3433256, 0, 2),
  (3439639, 3, 2),
  (3441250, 3, 0),
  (3452270, 2, 2),
  (3452848, 1, 2),
  (3453282, 2, 0),
  (3453421, 0, 2),
  (3453684, 0, 0),
  (3455045, 2, 0),
  (3457349, 0, 1),
  (3457622, 1, 1),
  (3458941, 3, 2),
  (3461385, 3, 0),
  (3465755, 3, 0),
  (3470672, 3, 1),
  (3473233, 0, 0),
  (3474666, 1, 2),
  (3475274, 0, 1),
  (3481605, 3, 1),
  (3486132, 2, 1),
  (3487291, 2, 2),
  (3492783, 1, 0),
  (3497256, 2, 0),
  (3502981, 2, 1),
  (3509719, 2, 2),
  (3511000, 3, 0),
  (3511913, 3, 1),
  (3512078, 3, 2),
  (3513175, 1, 1),
  (3514362, 1, 0),
  (3515116, 0, 2),
  (3517907, 2, 1),
  (3521358, 0, 1),
  (3523741, 1, 2),
  (3525328, 2, 1),
  (3525680, 0, 0),
  (3526908, 2, 2),
  (3529164, 0, 1),
  (3529769, 2, 1),
  (3529801, 1, 1),
  (3530481, 0, 2),
  (3530621, 1, 2),
  (3531865, 2, 0),
  (3532224, 1, 2),
  (3532323, 3, 0),
  (3532778, 2, 2),
  (3534167, 0, 0),
  (3535115, 0, 2),
  (3535498, 0, 0),
  (3536173, 2, 0),
  (3536184, 0, 1),
  (3536885, 2, 1),
  (3538690, 3, 0),
  (3543688, 0, 0),
  (3544748, 3, 1),
  (3544926, 2, 0),
  (3545446, 2, 0),
  (3547099, 0, 1),
  (3548123, 2, 2),
  (3550607, 2, 0),
  (3553111, 1, 1),
  (3557003, 3, 2),
  (3558764, 0, 1),
  (3558813, 3, 0),
  (3559625, 1, 0),
  (3561846, 1, 0),
  (3563699, 3, 0),
  (3565074, 2, 2),
  (3567137, 2, 2),
  (3567293, 3, 2),
  (3568546, 3, 0),
  (3570816, 1, 2),
  (3579059, 3, 1),
  (3579136, 1, 0),
  (3580296, 3, 2),
  (3581299, 3, 2),
  (3582540, 1, 0),
  (3583147, 1, 1),
  (3583389, 2, 1),
  (3584351, 2, 0),
  (3584928, 0, 2),
  (3590647, 2, 1),
  (3591196, 3, 0),
  (3592947, 3, 2),
  (3593587, 0, 1),
  (3599491, 3, 2),
  (3599949, 0, 2),
])