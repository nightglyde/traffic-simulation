from src.util import *
schedule = deque([
  (1854, 3, 1),
  (4074, 0, 0),
  (4506, 2, 1),
  (14919, 3, 0),
  (14958, 3, 2),
  (16126, 2, 2),
  (19513, 0, 1),
  (20251, 3, 2),
  (20298, 0, 1),
  (20813, 1, 2),
  (21713, 0, 0),
  (22028, 1, 2),
  (22628, 1, 0),
  (23036, 3, 1),
  (27595, 3, 1),
  (30222, 3, 0),
  (30451, 2, 2),
  (33069, 1, 2),
  (35876, 1, 1),
  (36211, 1, 0),
  (37685, 0, 1),
  (40657, 1, 2),
  (43404, 2, 0),
  (44281, 2, 1),
  (45363, 0, 2),
  (46515, 0, 1),
  (47971, 0, 0),
  (48814, 1, 1),
  (54180, 0, 0),
  (57379, 0, 0),
  (57982, 1, 0),
  (58890, 1, 0),
  (60829, 1, 1),
  (63509, 1, 2),
  (64561, 0, 1),
  (67461, 0, 0),
  (68192, 3, 1),
  (69559, 0, 2),
  (71285, 0, 1),
  (73443, 0, 1),
  (74881, 3, 0),
  (84317, 3, 1),
  (84664, 1, 0),
  (85327, 0, 2),
  (88939, 3, 2),
  (91032, 1, 1),
  (97012, 1, 2),
  (98055, 0, 1),
  (98621, 0, 1),
  (102680, 3, 0),
  (104852, 1, 0),
  (107797, 1, 0),
  (108021, 0, 1),
  (108697, 3, 0),
  (109158, 2, 1),
  (109453, 3, 1),
  (110693, 2, 2),
  (111465, 3, 1),
  (112216, 0, 2),
  (114499, 3, 1),
  (116773, 1, 1),
  (116882, 1, 0),
  (119127, 2, 2),
  (119680, 2, 1),
  (125563, 0, 2),
  (128551, 3, 0),
  (130651, 2, 1),
  (133326, 2, 0),
  (140354, 3, 2),
  (140409, 0, 1),
  (142247, 3, 2),
  (149563, 1, 1),
  (150299, 1, 0),
  (152024, 3, 2),
  (155221, 3, 1),
  (167285, 3, 1),
  (167302, 3, 1),
  (169514, 1, 0),
  (169529, 1, 1),
  (172910, 1, 1),
  (172936, 1, 0),
  (173500, 0, 1),
  (176654, 0, 2),
  (179583, 1, 0),
  (179734, 3, 2),
  (180490, 2, 0),
  (180546, 2, 1),
  (181988, 1, 2),
  (182467, 1, 0),
  (186437, 2, 1),
  (187308, 0, 0),
  (191519, 1, 1),
  (195061, 2, 0),
  (197342, 1, 0),
  (197377, 3, 1),
  (204574, 3, 1),
  (204661, 1, 2),
  (205175, 1, 1),
  (211175, 1, 1),
  (213080, 2, 0),
  (217914, 0, 1),
  (221060, 0, 2),
  (222438, 1, 1),
  (224933, 3, 2),
  (228102, 0, 2),
  (231828, 2, 2),
  (233547, 2, 2),
  (234592, 3, 1),
  (234730, 0, 0),
  (237004, 0, 2),
  (238203, 2, 0),
  (238840, 1, 1),
  (243066, 1, 2),
  (246599, 0, 2),
  (248800, 3, 2),
  (248828, 1, 2),
  (252159, 2, 2),
  (253459, 0, 2),
  (258598, 0, 1),
  (259845, 3, 2),
  (260658, 2, 0),
  (261060, 1, 1),
  (269560, 3, 0),
  (269837, 2, 1),
  (270250, 3, 2),
  (276208, 2, 1),
  (277233, 0, 2),
  (278382, 2, 1),
  (279146, 2, 1),
  (286084, 2, 2),
  (289711, 3, 1),
  (289723, 1, 1),
  (291643, 0, 1),
  (292591, 2, 2),
  (292720, 2, 2),
  (294696, 0, 0),
  (297740, 0, 1),
  (299021, 1, 1),
  (304609, 1, 1),
  (313610, 0, 0),
  (320327, 2, 0),
  (322191, 0, 1),
  (325730, 2, 2),
  (328212, 2, 0),
  (328448, 3, 1),
  (329447, 0, 1),
  (330860, 3, 2),
  (335889, 2, 1),
  (337386, 3, 0),
  (339884, 2, 0),
  (342191, 1, 1),
  (342599, 2, 0),
  (346559, 2, 2),
  (347351, 2, 0),
  (348151, 3, 1),
  (348730, 3, 2),
  (350827, 1, 2),
  (354420, 1, 2),
  (357815, 0, 2),
  (360126, 0, 2),
  (364280, 1, 0),
  (371171, 2, 0),
  (372932, 1, 2),
  (374850, 0, 0),
  (382482, 0, 2),
  (383905, 1, 2),
  (385842, 3, 0),
  (391655, 3, 1),
  (393730, 0, 1),
  (394369, 1, 1),
  (395680, 3, 0),
  (397671, 0, 0),
  (401182, 0, 0),
  (402208, 2, 1),
  (404377, 1, 2),
  (408991, 2, 2),
  (414065, 1, 0),
  (417484, 2, 0),
  (421254, 0, 0),
  (422292, 2, 1),
  (424286, 0, 1),
  (430743, 1, 0),
  (432201, 1, 1),
  (434201, 3, 2),
  (438555, 3, 0),
  (440801, 2, 2),
  (445786, 2, 0),
  (446434, 0, 1),
  (448105, 3, 1),
  (449248, 1, 0),
  (450468, 1, 1),
  (454572, 2, 2),
  (454603, 3, 1),
  (455187, 1, 2),
  (462067, 3, 1),
  (464696, 3, 2),
  (464928, 1, 0),
  (464948, 1, 0),
  (465552, 0, 2),
  (466026, 2, 1),
  (466100, 1, 1),
  (471730, 0, 0),
  (472610, 2, 1),
  (479639, 3, 0),
  (484199, 1, 2),
  (484627, 1, 0),
  (485804, 0, 1),
  (487116, 3, 2),
  (491045, 0, 2),
  (493180, 1, 0),
  (495057, 0, 2),
  (495390, 3, 1),
  (496175, 1, 0),
  (505777, 2, 2),
  (506585, 1, 2),
  (506807, 0, 1),
  (506980, 3, 2),
  (509473, 2, 1),
  (512337, 2, 1),
  (514026, 2, 0),
  (518172, 3, 1),
  (528805, 0, 2),
  (529852, 2, 2),
  (533313, 0, 2),
  (539406, 2, 1),
  (540967, 2, 1),
  (544834, 0, 0),
  (549937, 3, 0),
  (553391, 3, 2),
  (554249, 3, 0),
  (554385, 0, 0),
  (557759, 1, 0),
  (558299, 1, 2),
  (561331, 3, 1),
  (564424, 2, 2),
  (565536, 3, 1),
  (571856, 3, 1),
  (572864, 3, 2),
  (573763, 1, 2),
  (576495, 3, 1),
  (580028, 1, 1),
  (580834, 2, 2),
  (581130, 0, 2),
  (581272, 2, 0),
  (583221, 1, 1),
  (584381, 2, 1),
  (585279, 2, 2),
  (587820, 1, 1),
  (588117, 1, 2),
  (589299, 1, 1),
  (589471, 1, 0),
  (590312, 0, 1),
  (590815, 1, 1),
  (592069, 2, 1),
  (596317, 3, 1),
  (599572, 3, 0),
  (600767, 2, 0),
  (601077, 0, 0),
  (601709, 1, 0),
  (602256, 2, 2),
  (605316, 0, 2),
  (605875, 3, 2),
  (607885, 1, 0),
  (610609, 3, 2),
  (612600, 3, 1),
  (614654, 2, 0),
  (616113, 0, 0),
  (617127, 1, 2),
  (617842, 0, 2),
  (617871, 2, 1),
  (619020, 2, 0),
  (619363, 3, 2),
  (620828, 0, 1),
  (622219, 1, 2),
  (622860, 1, 1),
  (627858, 2, 0),
  (633768, 1, 1),
  (636543, 3, 0),
  (638186, 2, 1),
  (638610, 2, 2),
  (639380, 2, 0),
  (640154, 3, 1),
  (642138, 3, 0),
  (642465, 1, 2),
  (643342, 2, 1),
  (643419, 2, 0),
  (644119, 0, 0),
  (644220, 0, 2),
  (656979, 2, 0),
  (657471, 3, 0),
  (658956, 2, 1),
  (659236, 3, 2),
  (659796, 1, 2),
  (660654, 2, 1),
  (661758, 3, 1),
  (664016, 0, 0),
  (666500, 0, 0),
  (669993, 1, 1),
  (671674, 2, 0),
  (672422, 1, 0),
  (672627, 3, 2),
  (674099, 2, 1),
  (675105, 0, 0),
  (675705, 1, 2),
  (676410, 3, 2),
  (676747, 1, 1),
  (677030, 2, 2),
  (677510, 2, 0),
  (679421, 1, 0),
  (682305, 3, 0),
  (682935, 3, 0),
  (683497, 0, 0),
  (686825, 3, 2),
  (690945, 1, 2),
  (693089, 1, 1),
  (694899, 0, 2),
  (695537, 1, 2),
  (700008, 3, 0),
  (700237, 0, 1),
  (702363, 3, 0),
  (704002, 1, 1),
  (704631, 2, 1),
  (707665, 0, 2),
  (707851, 3, 0),
  (709512, 2, 0),
  (709758, 1, 0),
  (711524, 3, 2),
  (712434, 2, 2),
  (713990, 2, 2),
  (715090, 1, 2),
  (716832, 0, 1),
  (717138, 1, 2),
  (722861, 0, 2),
  (730439, 0, 2),
  (732020, 2, 1),
  (732154, 1, 0),
  (733253, 1, 0),
  (735564, 3, 1),
  (736376, 2, 1),
  (737080, 0, 1),
  (742841, 0, 1),
  (744702, 3, 2),
  (748453, 1, 1),
  (749157, 3, 2),
  (753168, 2, 0),
  (755059, 1, 1),
  (755321, 2, 1),
  (770474, 3, 1),
  (771090, 3, 1),
  (774315, 3, 0),
  (775367, 2, 2),
  (783298, 0, 1),
  (784880, 1, 0),
  (790137, 0, 2),
  (790203, 0, 0),
  (790895, 0, 0),
  (791957, 1, 0),
  (795466, 1, 1),
  (796541, 0, 1),
  (798187, 2, 1),
  (798954, 0, 1),
  (801752, 0, 1),
  (803165, 2, 0),
  (803687, 3, 2),
  (809185, 3, 2),
  (810354, 2, 2),
  (812050, 1, 2),
  (812821, 1, 1),
  (814290, 1, 2),
  (817139, 3, 0),
  (817788, 2, 1),
  (818739, 1, 2),
  (819676, 1, 1),
  (819944, 1, 0),
  (820558, 2, 1),
  (822730, 0, 2),
  (823572, 1, 2),
  (823803, 3, 0),
  (825007, 3, 2),
  (833660, 2, 0),
  (835297, 2, 0),
  (838545, 3, 0),
  (841981, 0, 2),
  (846575, 1, 2),
  (848959, 2, 1),
  (850181, 1, 0),
  (856233, 2, 1),
  (858077, 3, 0),
  (860947, 0, 2),
  (866713, 2, 0),
  (868182, 2, 0),
  (869046, 1, 1),
  (874243, 0, 1),
  (876192, 3, 1),
  (880125, 3, 1),
  (881279, 3, 1),
  (881741, 2, 2),
  (890086, 2, 2),
  (894440, 0, 0),
  (894733, 2, 1),
  (895094, 3, 0),
  (895602, 0, 0),
  (895866, 1, 2),
  (897279, 1, 0),
  (902192, 1, 0),
  (907550, 3, 2),
  (907587, 2, 2),
  (913097, 0, 1),
  (914534, 0, 0),
  (919117, 0, 2),
  (921585, 2, 0),
  (921728, 2, 0),
  (922483, 0, 1),
  (925297, 3, 0),
  (927286, 0, 0),
  (928572, 2, 2),
  (930824, 2, 1),
  (932875, 2, 0),
  (935320, 0, 2),
  (936923, 2, 2),
  (937301, 0, 1),
  (938194, 3, 2),
  (938936, 2, 2),
  (942144, 0, 0),
  (942784, 3, 0),
  (943225, 3, 2),
  (946019, 3, 1),
  (950445, 2, 1),
  (950533, 1, 2),
  (951578, 0, 2),
  (953062, 3, 0),
  (954706, 0, 0),
  (960684, 2, 1),
  (960824, 1, 1),
  (965186, 0, 2),
  (969098, 1, 0),
  (969912, 1, 2),
  (969945, 1, 0),
  (971232, 2, 1),
  (971245, 1, 1),
  (973933, 0, 1),
  (980379, 0, 2),
  (982091, 1, 2),
  (983275, 0, 2),
  (983452, 3, 0),
  (988767, 3, 2),
  (998712, 2, 0),
  (999294, 1, 0),
  (999353, 3, 2),
  (1003234, 2, 1),
  (1003339, 1, 1),
  (1010135, 2, 1),
  (1012050, 0, 2),
  (1012480, 2, 1),
  (1013741, 3, 0),
  (1017132, 0, 0),
  (1018499, 0, 1),
  (1018813, 3, 1),
  (1019314, 3, 0),
  (1023931, 2, 0),
  (1027289, 3, 1),
  (1029100, 0, 2),
  (1031761, 1, 1),
  (1031955, 2, 1),
  (1033660, 2, 2),
  (1033784, 2, 0),
  (1036714, 0, 0),
  (1038115, 3, 1),
  (1047896, 2, 0),
  (1048588, 0, 1),
  (1049351, 0, 0),
  (1052027, 3, 1),
  (1053765, 3, 1),
  (1054002, 3, 1),
  (1059024, 2, 0),
  (1059980, 2, 2),
  (1060866, 2, 1),
  (1062212, 3, 0),
  (1064292, 3, 0),
  (1066258, 3, 2),
  (1067555, 0, 1),
  (1069921, 2, 2),
  (1070409, 1, 2),
  (1070747, 3, 2),
  (1070774, 1, 2),
  (1075474, 2, 2),
  (1081516, 0, 1),
  (1082169, 3, 2),
  (1082198, 1, 1),
  (1084740, 2, 0),
  (1088971, 0, 1),
  (1091390, 3, 0),
  (1094398, 1, 2),
  (1095876, 2, 2),
  (1098454, 2, 0),
  (1109175, 0, 2),
  (1113426, 2, 2),
  (1114068, 1, 0),
  (1116623, 3, 0),
  (1117400, 0, 1),
  (1118438, 3, 2),
  (1118613, 2, 0),
  (1122887, 2, 1),
  (1124089, 1, 1),
  (1125699, 3, 0),
  (1126970, 0, 0),
  (1128019, 3, 2),
  (1131270, 3, 2),
  (1136807, 3, 2),
  (1140191, 3, 0),
  (1144575, 2, 1),
  (1145265, 2, 1),
  (1148847, 0, 1),
  (1149105, 0, 0),
  (1149808, 1, 0),
  (1149916, 2, 2),
  (1151113, 1, 1),
  (1152977, 0, 2),
  (1153623, 0, 2),
  (1155971, 2, 1),
  (1157332, 0, 2),
  (1158045, 3, 0),
  (1158938, 2, 0),
  (1159559, 0, 0),
  (1161559, 1, 2),
  (1162542, 1, 0),
  (1163867, 2, 1),
  (1165809, 0, 1),
  (1167822, 3, 1),
  (1170725, 1, 1),
  (1171060, 0, 2),
  (1171916, 1, 0),
  (1173332, 3, 0),
  (1174349, 3, 0),
  (1175863, 0, 2),
  (1177248, 0, 0),
  (1181763, 0, 2),
  (1184985, 0, 2),
  (1186082, 1, 0),
  (1187265, 1, 1),
  (1187980, 0, 2),
  (1190590, 3, 2),
  (1191365, 2, 2),
  (1196722, 3, 0),
  (1197371, 0, 1),
  (1198432, 0, 1),
  (1198697, 3, 0),
  (1206470, 3, 0),
  (1207591, 2, 0),
  (1207741, 3, 2),
  (1210598, 1, 1),
  (1213629, 2, 2),
  (1213713, 0, 0),
  (1214446, 0, 2),
  (1217280, 0, 2),
  (1218979, 2, 2),
  (1222430, 3, 2),
  (1222973, 1, 2),
  (1230122, 3, 0),
  (1230415, 0, 0),
  (1231270, 0, 2),
  (1232653, 1, 1),
  (1235636, 3, 2),
  (1237491, 1, 1),
  (1240285, 2, 0),
  (1241934, 1, 2),
  (1242605, 0, 1),
  (1246020, 0, 1),
  (1246078, 1, 0),
  (1248851, 2, 2),
  (1249076, 1, 0),
  (1250487, 1, 0),
  (1250521, 2, 0),
  (1251595, 0, 1),
  (1254362, 2, 1),
  (1255247, 3, 2),
  (1255908, 0, 0),
  (1258622, 1, 1),
  (1259125, 2, 2),
  (1262468, 1, 0),
  (1264478, 3, 0),
  (1267900, 0, 2),
  (1273551, 2, 1),
  (1274939, 0, 0),
  (1280697, 3, 1),
  (1281026, 3, 0),
  (1285514, 3, 2),
  (1287041, 0, 2),
  (1287165, 0, 1),
  (1288469, 1, 2),
  (1291467, 2, 0),
  (1294252, 1, 1),
  (1297841, 2, 2),
  (1299404, 2, 1),
  (1303587, 1, 0),
  (1304559, 0, 1),
  (1309947, 3, 0),
  (1313582, 3, 2),
  (1314725, 2, 0),
  (1316207, 3, 2),
  (1316816, 3, 1),
  (1318330, 0, 1),
  (1321510, 1, 2),
  (1322292, 3, 1),
  (1323011, 2, 0),
  (1324221, 3, 2),
  (1330000, 1, 1),
  (1331368, 1, 0),
  (1332352, 2, 1),
  (1344380, 3, 1),
  (1346225, 1, 2),
  (1347216, 0, 0),
  (1350645, 2, 1),
  (1352591, 0, 1),
  (1353648, 1, 2),
  (1353668, 0, 1),
  (1353948, 2, 2),
  (1362591, 1, 2),
  (1365346, 2, 1),
  (1366521, 0, 0),
  (1367763, 2, 1),
  (1368178, 2, 1),
  (1368781, 1, 2),
  (1368867, 0, 1),
  (1369927, 3, 1),
  (1370464, 3, 1),
  (1375026, 0, 2),
  (1376091, 0, 1),
  (1376402, 0, 0),
  (1376408, 3, 0),
  (1378957, 2, 2),
  (1380766, 2, 0),
  (1382537, 3, 2),
  (1383350, 2, 2),
  (1383700, 1, 1),
  (1386789, 1, 2),
  (1387343, 0, 2),
  (1388153, 2, 2),
  (1388184, 1, 0),
  (1391323, 3, 2),
  (1392537, 3, 0),
  (1392541, 1, 0),
  (1394789, 3, 2),
  (1395071, 0, 2),
  (1396913, 1, 2),
  (1401434, 1, 1),
  (1403268, 1, 2),
  (1403476, 1, 0),
  (1406202, 2, 2),
  (1407119, 3, 0),
  (1407480, 2, 0),
  (1407544, 0, 1),
  (1413035, 1, 1),
  (1413364, 1, 2),
  (1417362, 0, 2),
  (1418566, 2, 1),
  (1419471, 2, 1),
  (1423549, 3, 0),
  (1423927, 0, 0),
  (1426003, 3, 0),
  (1430435, 1, 2),
  (1430609, 3, 0),
  (1430986, 0, 0),
  (1432698, 1, 0),
  (1433893, 1, 1),
  (1434904, 0, 2),
  (1437043, 2, 0),
  (1437939, 1, 0),
  (1438360, 2, 2),
  (1440842, 2, 2),
  (1441835, 2, 1),
  (1445301, 1, 1),
  (1445980, 2, 2),
  (1448190, 0, 0),
  (1450265, 3, 0),
  (1450982, 2, 1),
  (1453265, 3, 0),
  (1457181, 1, 2),
  (1457586, 3, 1),
  (1457699, 0, 2),
  (1458127, 1, 2),
  (1460798, 0, 1),
  (1462918, 2, 2),
  (1463951, 3, 0),
  (1465056, 1, 1),
  (1465838, 3, 1),
  (1470747, 2, 0),
  (1472193, 0, 1),
  (1473983, 0, 1),
  (1479108, 2, 2),
  (1479716, 1, 0),
  (1481527, 3, 1),
  (1487977, 0, 1),
  (1489399, 2, 1),
  (1489895, 1, 0),
  (1489968, 1, 1),
  (1491652, 3, 0),
  (1494290, 0, 1),
  (1496482, 1, 2),
  (1496862, 0, 1),
  (1497049, 0, 1),
  (1498196, 2, 2),
  (1499630, 0, 2),
  (1500010, 1, 0),
  (1506201, 2, 1),
  (1506419, 1, 0),
  (1506487, 2, 1),
  (1510116, 1, 0),
  (1511734, 0, 1),
  (1513798, 3, 0),
  (1514188, 1, 0),
  (1517457, 1, 2),
  (1517539, 1, 2),
  (1521055, 1, 2),
  (1522394, 3, 0),
  (1522460, 1, 1),
  (1524804, 1, 2),
  (1527541, 2, 2),
  (1529115, 1, 0),
  (1531566, 2, 0),
  (1536543, 1, 0),
  (1537567, 2, 0),
  (1540309, 3, 1),
  (1543140, 2, 0),
  (1546563, 0, 1),
  (1547904, 0, 1),
  (1547956, 0, 2),
  (1548420, 3, 0),
  (1549173, 1, 0),
  (1553957, 3, 1),
  (1557256, 1, 1),
  (1558402, 3, 1),
  (1558404, 3, 0),
  (1558567, 2, 0),
  (1559448, 1, 1),
  (1560892, 2, 2),
  (1561891, 3, 1),
  (1564493, 2, 1),
  (1567360, 0, 2),
  (1568330, 2, 1),
  (1569761, 3, 0),
  (1571509, 2, 2),
  (1572943, 0, 0),
  (1574563, 3, 0),
  (1575024, 1, 0),
  (1575922, 3, 1),
  (1577867, 3, 0),
  (1578435, 3, 1),
  (1579202, 2, 2),
  (1581250, 3, 0),
  (1584746, 1, 0),
  (1584826, 3, 2),
  (1585704, 2, 0),
  (1586075, 3, 1),
  (1589297, 1, 0),
  (1589453, 3, 0),
  (1594711, 0, 1),
  (1594897, 3, 1),
  (1596382, 1, 1),
  (1596790, 0, 1),
  (1598881, 2, 0),
  (1600072, 2, 1),
  (1601002, 1, 2),
  (1601341, 2, 0),
  (1602853, 0, 0),
  (1602972, 1, 0),
  (1607884, 1, 0),
  (1607901, 0, 0),
  (1608319, 2, 0),
  (1609148, 0, 2),
  (1614239, 3, 1),
  (1614847, 1, 0),
  (1616079, 3, 1),
  (1616524, 2, 2),
  (1617603, 3, 0),
  (1622224, 1, 2),
  (1622255, 0, 0),
  (1622789, 3, 2),
  (1624421, 0, 0),
  (1625161, 2, 0),
  (1625347, 2, 0),
  (1625389, 2, 1),
  (1627053, 0, 2),
  (1628095, 3, 0),
  (1628363, 3, 1),
  (1636229, 2, 0),
  (1636912, 0, 2),
  (1639965, 0, 2),
  (1640088, 1, 0),
  (1643615, 2, 2),
  (1644169, 1, 2),
  (1644578, 3, 2),
  (1645551, 0, 0),
  (1645890, 2, 1),
  (1646629, 2, 0),
  (1650917, 2, 0),
  (1654048, 2, 0),
  (1660315, 2, 2),
  (1660523, 2, 1),
  (1661775, 2, 1),
  (1665973, 2, 2),
  (1667939, 1, 0),
  (1672100, 3, 2),
  (1673538, 0, 1),
  (1673963, 0, 2),
  (1679773, 3, 1),
  (1680386, 3, 0),
  (1680992, 2, 1),
  (1681724, 3, 0),
  (1685179, 0, 2),
  (1687847, 0, 1),
  (1689906, 0, 2),
  (1690529, 2, 1),
  (1691103, 3, 2),
  (1693639, 1, 2),
  (1699510, 3, 2),
  (1702927, 1, 1),
  (1706733, 3, 2),
  (1706802, 0, 2),
  (1709387, 0, 0),
  (1712219, 0, 0),
  (1713184, 3, 0),
  (1716430, 0, 2),
  (1716592, 3, 1),
  (1721199, 2, 0),
  (1723281, 0, 1),
  (1724721, 0, 0),
  (1726048, 3, 2),
  (1727652, 0, 0),
  (1728872, 3, 2),
  (1730157, 3, 0),
  (1730873, 0, 1),
  (1731285, 3, 2),
  (1732955, 0, 2),
  (1733298, 2, 1),
  (1733582, 3, 0),
  (1737366, 0, 1),
  (1740142, 1, 2),
  (1748613, 2, 2),
  (1750065, 3, 1),
  (1752718, 3, 0),
  (1755539, 3, 0),
  (1755678, 0, 0),
  (1755831, 3, 1),
  (1757673, 1, 2),
  (1758605, 2, 0),
  (1759520, 0, 2),
  (1759966, 1, 1),
  (1761951, 0, 0),
  (1763775, 1, 1),
  (1764570, 3, 1),
  (1767653, 1, 0),
  (1767976, 0, 2),
  (1769266, 3, 1),
  (1773773, 1, 0),
  (1774307, 1, 0),
  (1777816, 2, 1),
  (1782504, 0, 1),
  (1791018, 0, 2),
  (1792666, 1, 0),
  (1794281, 0, 2),
  (1799017, 0, 1),
  (1800121, 1, 2),
  (1800605, 2, 2),
  (1802513, 2, 2),
  (1808061, 1, 2),
  (1809011, 3, 0),
  (1812618, 2, 2),
  (1813089, 2, 0),
  (1814626, 2, 0),
  (1816998, 0, 1),
  (1822400, 3, 2),
  (1825907, 0, 2),
  (1827410, 1, 0),
  (1829899, 3, 0),
  (1832882, 1, 1),
  (1833143, 0, 0),
  (1833419, 2, 0),
  (1834403, 1, 0),
  (1837721, 0, 1),
  (1839000, 1, 0),
  (1840473, 2, 1),
  (1841405, 2, 1),
  (1847123, 2, 0),
  (1856029, 0, 1),
  (1859096, 1, 1),
  (1861804, 2, 2),
  (1862193, 2, 0),
  (1864083, 2, 1),
  (1872133, 2, 2),
  (1875236, 3, 1),
  (1877792, 1, 1),
  (1882611, 3, 1),
  (1882895, 2, 1),
  (1884811, 1, 2),
  (1888477, 0, 0),
  (1889290, 3, 0),
  (1890435, 3, 1),
  (1891658, 1, 0),
  (1894676, 0, 0),
  (1894947, 3, 1),
  (1896503, 2, 0),
  (1899068, 0, 0),
  (1899828, 2, 1),
  (1902132, 3, 1),
  (1904367, 1, 2),
  (1914053, 3, 2),
  (1914497, 0, 1),
  (1916525, 0, 2),
  (1917035, 1, 0),
  (1919486, 1, 1),
  (1919708, 2, 0),
  (1919734, 0, 1),
  (1923046, 0, 2),
  (1925295, 1, 2),
  (1927403, 3, 2),
  (1927919, 2, 1),
  (1933198, 3, 0),
  (1933232, 1, 2),
  (1933696, 0, 2),
  (1934317, 2, 2),
  (1935017, 1, 1),
  (1935971, 3, 2),
  (1939252, 2, 0),
  (1940948, 1, 2),
  (1944294, 3, 0),
  (1945017, 0, 0),
  (1947781, 3, 2),
  (1952276, 0, 0),
  (1952457, 3, 2),
  (1952489, 3, 1),
  (1956925, 2, 1),
  (1958149, 1, 2),
  (1960162, 2, 2),
  (1960290, 0, 0),
  (1960301, 3, 1),
  (1960976, 1, 1),
  (1962125, 1, 0),
  (1963675, 1, 1),
  (1964515, 1, 2),
  (1965445, 3, 2),
  (1966588, 0, 2),
  (1967454, 1, 2),
  (1967744, 1, 2),
  (1967968, 1, 0),
  (1970842, 0, 1),
  (1972844, 0, 1),
  (1974878, 0, 2),
  (1975581, 2, 1),
  (1979299, 2, 2),
  (1983569, 0, 1),
  (1985181, 1, 0),
  (1986950, 0, 2),
  (1987199, 1, 0),
  (1987552, 3, 0),
  (1990301, 2, 2),
  (1990923, 1, 1),
  (1991823, 0, 2),
  (1996271, 0, 1),
  (1997524, 3, 1),
  (1998608, 2, 2),
  (2001583, 1, 2),
  (2002083, 0, 0),
  (2005082, 2, 1),
  (2005139, 0, 0),
  (2006109, 0, 0),
  (2007388, 1, 2),
  (2008472, 3, 0),
  (2011401, 0, 0),
  (2012930, 0, 0),
  (2016569, 1, 2),
  (2017195, 3, 1),
  (2017386, 2, 1),
  (2019472, 3, 2),
  (2021304, 2, 1),
  (2023911, 1, 0),
  (2027073, 0, 2),
  (2030099, 3, 1),
  (2030446, 2, 0),
  (2030962, 1, 0),
  (2031116, 1, 2),
  (2032019, 2, 1),
  (2033952, 2, 0),
  (2035458, 3, 1),
  (2036054, 3, 0),
  (2037620, 1, 1),
  (2039435, 3, 1),
  (2043238, 1, 2),
  (2043279, 3, 0),
  (2044238, 2, 2),
  (2046498, 1, 1),
  (2047464, 2, 0),
  (2051805, 3, 1),
  (2052397, 2, 0),
  (2059584, 0, 0),
  (2062746, 2, 0),
  (2065163, 0, 0),
  (2067137, 0, 0),
  (2068694, 1, 1),
  (2071846, 3, 1),
  (2072490, 0, 2),
  (2076714, 0, 1),
  (2079461, 0, 2),
  (2081173, 0, 0),
  (2084888, 1, 1),
  (2084950, 1, 0),
  (2090768, 2, 2),
  (2091844, 0, 0),
  (2092496, 3, 2),
  (2095689, 1, 2),
  (2095721, 3, 0),
  (2095736, 3, 2),
  (2098635, 3, 1),
  (2100841, 0, 0),
  (2101098, 1, 1),
  (2106310, 0, 0),
  (2109115, 2, 2),
  (2109148, 1, 0),
  (2110306, 3, 0),
  (2110570, 3, 0),
  (2111564, 0, 1),
  (2112777, 1, 1),
  (2114295, 0, 2),
  (2115776, 2, 1),
  (2116863, 1, 0),
  (2119940, 2, 1),
  (2120097, 2, 2),
  (2126970, 3, 0),
  (2127391, 2, 2),
  (2130928, 3, 2),
  (2132153, 2, 2),
  (2134003, 1, 2),
  (2134639, 2, 2),
  (2135094, 3, 1),
  (2136016, 2, 0),
  (2137673, 0, 0),
  (2137940, 3, 0),
  (2138788, 0, 1),
  (2141199, 3, 1),
  (2141890, 0, 2),
  (2148753, 3, 0),
  (2150097, 2, 0),
  (2151954, 0, 2),
  (2152131, 2, 1),
  (2158670, 1, 2),
  (2160357, 1, 0),
  (2162336, 1, 1),
  (2162602, 3, 0),
  (2163260, 2, 1),
  (2167552, 3, 2),
  (2168242, 3, 1),
  (2168492, 2, 0),
  (2171739, 3, 0),
  (2172957, 0, 2),
  (2173259, 0, 2),
  (2177924, 0, 2),
  (2182615, 0, 1),
  (2183344, 1, 2),
  (2183911, 1, 2),
  (2183966, 1, 0),
  (2184991, 1, 0),
  (2185078, 1, 0),
  (2186726, 1, 1),
  (2192077, 2, 1),
  (2196186, 2, 2),
  (2197174, 0, 0),
  (2201113, 0, 1),
  (2201837, 3, 0),
  (2204608, 3, 0),
  (2205402, 3, 1),
  (2205644, 0, 2),
  (2206709, 1, 1),
  (2211170, 3, 0),
  (2214484, 2, 1),
  (2221058, 0, 0),
  (2221622, 2, 0),
  (2222658, 0, 1),
  (2224958, 0, 0),
  (2225468, 3, 2),
  (2230125, 3, 2),
  (2235595, 0, 1),
  (2235649, 0, 0),
  (2237265, 2, 0),
  (2241349, 0, 2),
  (2243412, 1, 1),
  (2244464, 0, 2),
  (2244999, 1, 2),
  (2247440, 2, 0),
  (2247514, 2, 1),
  (2251110, 0, 1),
  (2251544, 3, 0),
  (2252586, 3, 1),
  (2252695, 3, 2),
  (2253485, 3, 1),
  (2254272, 1, 0),
  (2255573, 3, 1),
  (2255951, 3, 1),
  (2257443, 3, 2),
  (2260032, 3, 1),
  (2261794, 3, 2),
  (2268758, 1, 0),
  (2269336, 0, 1),
  (2269527, 1, 2),
  (2270284, 0, 1),
  (2272431, 1, 2),
  (2272730, 3, 2),
  (2276429, 1, 1),
  (2276613, 3, 2),
  (2284450, 3, 0),
  (2287013, 2, 0),
  (2287178, 0, 2),
  (2293374, 3, 1),
  (2301816, 1, 0),
  (2301837, 1, 0),
  (2304712, 3, 2),
  (2306507, 2, 1),
  (2309970, 2, 1),
  (2314407, 1, 0),
  (2314618, 1, 0),
  (2319249, 2, 2),
  (2323110, 2, 1),
  (2323806, 3, 2),
  (2325040, 2, 1),
  (2325112, 3, 0),
  (2331191, 3, 1),
  (2331584, 2, 2),
  (2332720, 3, 0),
  (2334104, 3, 0),
  (2335869, 2, 1),
  (2336198, 2, 0),
  (2340397, 3, 2),
  (2341129, 2, 2),
  (2343631, 0, 2),
  (2343877, 3, 0),
  (2344104, 1, 0),
  (2346066, 1, 0),
  (2348151, 3, 1),
  (2348759, 1, 1),
  (2351226, 2, 2),
  (2355191, 1, 2),
  (2356091, 3, 1),
  (2356618, 3, 0),
  (2356719, 2, 2),
  (2359516, 3, 1),
  (2359627, 0, 1),
  (2367951, 0, 2),
  (2374891, 2, 1),
  (2375517, 1, 0),
  (2375583, 1, 2),
  (2376256, 0, 0),
  (2376445, 2, 1),
  (2377519, 1, 2),
  (2380945, 0, 2),
  (2381969, 0, 2),
  (2383886, 2, 2),
  (2386786, 3, 1),
  (2393863, 2, 2),
  (2394154, 1, 0),
  (2396088, 3, 1),
  (2397275, 3, 1),
  (2398540, 3, 1),
  (2399083, 1, 0),
  (2399206, 2, 0),
  (2400564, 0, 1),
  (2400942, 0, 0),
  (2401671, 2, 0),
  (2402582, 3, 0),
  (2407722, 3, 2),
  (2408456, 0, 0),
  (2411957, 2, 2),
  (2414012, 1, 0),
  (2419207, 1, 2),
  (2419308, 1, 1),
  (2420822, 1, 1),
  (2426902, 1, 2),
  (2427824, 3, 2),
  (2432175, 3, 2),
  (2435902, 2, 2),
  (2436291, 1, 0),
  (2437614, 3, 1),
  (2440153, 2, 1),
  (2440629, 1, 2),
  (2440923, 3, 0),
  (2441408, 2, 2),
  (2442956, 2, 2),
  (2443856, 0, 0),
  (2444657, 3, 1),
  (2445622, 0, 2),
  (2448334, 3, 1),
  (2448808, 3, 2),
  (2449733, 0, 0),
  (2450172, 1, 2),
  (2457501, 1, 1),
  (2459293, 1, 2),
  (2460309, 1, 1),
  (2466435, 3, 2),
  (2468974, 1, 1),
  (2469244, 2, 2),
  (2471881, 2, 2),
  (2474902, 2, 1),
  (2480191, 2, 0),
  (2480508, 3, 1),
  (2485558, 1, 2),
  (2486409, 2, 2),
  (2488185, 3, 1),
  (2489348, 2, 1),
  (2489517, 0, 0),
  (2489765, 2, 1),
  (2492987, 2, 2),
  (2494546, 0, 0),
  (2494640, 1, 2),
  (2496072, 1, 2),
  (2497472, 1, 0),
  (2497647, 0, 2),
  (2499271, 0, 1),
  (2501413, 3, 1),
  (2503191, 0, 0),
  (2503970, 0, 2),
  (2504649, 1, 1),
  (2505248, 1, 1),
  (2507633, 2, 1),
  (2508074, 0, 1),
  (2512304, 2, 2),
  (2513493, 3, 1),
  (2514521, 2, 1),
  (2516396, 3, 0),
  (2521179, 3, 2),
  (2521693, 2, 2),
  (2524785, 1, 0),
  (2527614, 3, 2),
  (2528208, 3, 0),
  (2529251, 3, 1),
  (2529521, 3, 0),
  (2529881, 0, 1),
  (2531350, 3, 0),
  (2531996, 3, 2),
  (2532071, 3, 1),
  (2532177, 2, 1),
  (2532667, 3, 1),
  (2533737, 2, 1),
  (2533986, 3, 0),
  (2535525, 1, 2),
  (2535715, 3, 1),
  (2536078, 0, 2),
  (2539406, 2, 0),
  (2540179, 1, 2),
  (2540948, 2, 0),
  (2542298, 0, 2),
  (2542466, 3, 1),
  (2544376, 3, 2),
  (2545103, 1, 1),
  (2546350, 2, 0),
  (2551354, 1, 0),
  (2553330, 3, 2),
  (2557773, 2, 0),
  (2560112, 3, 2),
  (2561293, 2, 0),
  (2561444, 1, 2),
  (2566465, 1, 1),
  (2566593, 0, 1),
  (2567196, 1, 0),
  (2569414, 0, 2),
  (2569755, 2, 2),
  (2571851, 2, 1),
  (2577492, 2, 2),
  (2578600, 3, 0),
  (2578991, 2, 1),
  (2579777, 0, 2),
  (2580538, 3, 0),
  (2582204, 3, 0),
  (2582530, 2, 1),
  (2584714, 2, 1),
  (2586066, 3, 1),
  (2587845, 0, 1),
  (2588611, 2, 1),
  (2596716, 1, 0),
  (2597157, 3, 0),
  (2598186, 2, 1),
  (2599637, 2, 2),
  (2601038, 1, 2),
  (2604613, 2, 2),
  (2605642, 2, 1),
  (2606395, 3, 0),
  (2608589, 1, 2),
  (2611626, 0, 0),
  (2611821, 0, 2),
  (2615564, 3, 2),
  (2615728, 2, 1),
  (2615871, 3, 2),
  (2617595, 1, 0),
  (2619557, 3, 2),
  (2619593, 0, 1),
  (2619749, 3, 1),
  (2619764, 3, 2),
  (2619796, 1, 2),
  (2620026, 0, 0),
  (2621462, 1, 2),
  (2623315, 2, 2),
  (2625997, 1, 1),
  (2628520, 0, 0),
  (2628824, 1, 0),
  (2638337, 2, 2),
  (2638866, 2, 0),
  (2640285, 3, 0),
  (2640302, 1, 1),
  (2640994, 1, 1),
  (2643551, 2, 0),
  (2643633, 2, 0),
  (2643729, 0, 0),
  (2647844, 0, 2),
  (2649675, 1, 1),
  (2650115, 1, 1),
  (2650504, 2, 1),
  (2652276, 3, 2),
  (2654336, 3, 2),
  (2656762, 1, 2),
  (2658955, 2, 0),
  (2660419, 2, 0),
  (2661994, 0, 2),
  (2662406, 0, 0),
  (2662508, 1, 1),
  (2663156, 0, 2),
  (2666464, 0, 2),
  (2667490, 1, 0),
  (2669625, 0, 2),
  (2671374, 3, 2),
  (2675964, 2, 1),
  (2676214, 3, 0),
  (2676498, 3, 1),
  (2679103, 3, 1),
  (2680413, 1, 1),
  (2683084, 1, 1),
  (2684018, 2, 2),
  (2686742, 2, 2),
  (2687070, 2, 1),
  (2688528, 3, 2),
  (2688881, 3, 2),
  (2690153, 0, 2),
  (2696941, 2, 1),
  (2700118, 0, 0),
  (2701441, 1, 2),
  (2702006, 1, 2),
  (2702435, 3, 2),
  (2706692, 3, 2),
  (2707313, 2, 1),
  (2707481, 2, 0),
  (2709641, 1, 1),
  (2710675, 0, 0),
  (2721329, 2, 1),
  (2726257, 3, 1),
  (2726831, 1, 2),
  (2727873, 0, 0),
  (2728512, 0, 0),
  (2729304, 0, 2),
  (2733901, 0, 0),
  (2735851, 2, 0),
  (2735870, 2, 0),
  (2738602, 1, 0),
  (2740343, 1, 2),
  (2742515, 0, 2),
  (2745696, 2, 0),
  (2747582, 1, 2),
  (2748724, 3, 0),
  (2748771, 3, 1),
  (2749405, 2, 2),
  (2751702, 1, 2),
  (2752167, 2, 0),
  (2755276, 0, 0),
  (2756054, 1, 0),
  (2759380, 0, 0),
  (2759489, 1, 0),
  (2760796, 1, 1),
  (2762974, 3, 1),
  (2764102, 2, 2),
  (2764517, 3, 0),
  (2764539, 2, 1),
  (2768015, 2, 1),
  (2769837, 2, 2),
  (2776894, 0, 1),
  (2777949, 1, 1),
  (2784246, 3, 0),
  (2784373, 3, 2),
  (2786590, 1, 2),
  (2787402, 1, 0),
  (2788621, 2, 2),
  (2793712, 2, 2),
  (2794229, 3, 0),
  (2794523, 0, 1),
  (2795794, 0, 2),
  (2797840, 2, 0),
  (2803542, 2, 0),
  (2806153, 0, 2),
  (2807216, 3, 2),
  (2807411, 1, 2),
  (2808571, 3, 2),
  (2811326, 2, 1),
  (2812565, 2, 1),
  (2815003, 0, 0),
  (2815877, 3, 1),
  (2817887, 2, 2),
  (2818681, 0, 0),
  (2819293, 0, 1),
  (2821033, 2, 1),
  (2821404, 3, 1),
  (2821853, 0, 1),
  (2822042, 1, 1),
  (2824325, 2, 1),
  (2827016, 0, 0),
  (2827553, 3, 2),
  (2828329, 2, 1),
  (2831191, 0, 0),
  (2833343, 3, 2),
  (2842642, 0, 2),
  (2842914, 1, 2),
  (2844944, 3, 2),
  (2845822, 2, 2),
  (2848780, 3, 0),
  (2849577, 3, 2),
  (2850353, 1, 2),
  (2850906, 1, 1),
  (2855080, 0, 1),
  (2859870, 2, 2),
  (2861249, 1, 2),
  (2863197, 2, 1),
  (2865069, 3, 0),
  (2876576, 0, 2),
  (2887903, 3, 1),
  (2889203, 1, 2),
  (2890543, 2, 1),
  (2893844, 0, 0),
  (2895250, 3, 1),
  (2896542, 1, 0),
  (2899127, 0, 2),
  (2900289, 3, 1),
  (2904022, 3, 1),
  (2904429, 3, 0),
  (2904950, 2, 2),
  (2909473, 1, 1),
  (2912249, 3, 2),
  (2912307, 3, 2),
  (2912711, 3, 0),
  (2914319, 3, 2),
  (2916357, 0, 2),
  (2917228, 0, 1),
  (2918930, 0, 1),
  (2920215, 3, 1),
  (2922372, 3, 2),
  (2922542, 3, 2),
  (2922663, 0, 0),
  (2924296, 0, 0),
  (2924455, 0, 1),
  (2926985, 3, 2),
  (2930172, 0, 2),
  (2933334, 2, 0),
  (2933800, 1, 1),
  (2942796, 0, 0),
  (2942864, 2, 0),
  (2944524, 2, 1),
  (2947175, 3, 0),
  (2947610, 3, 2),
  (2951104, 2, 1),
  (2952290, 2, 1),
  (2952745, 0, 2),
  (2956455, 3, 1),
  (2958195, 3, 0),
  (2958563, 1, 1),
  (2959665, 2, 2),
  (2963654, 3, 1),
  (2966531, 2, 1),
  (2969056, 2, 0),
  (2973690, 1, 2),
  (2977163, 2, 2),
  (2977577, 0, 2),
  (2980366, 0, 1),
  (2982018, 3, 2),
  (2983405, 1, 2),
  (2989599, 3, 1),
  (2989724, 2, 2),
  (2991759, 0, 2),
  (2992305, 1, 0),
  (2993153, 3, 0),
  (2993235, 3, 0),
  (2996754, 2, 1),
  (3000650, 0, 0),
  (3003460, 3, 0),
  (3005791, 0, 0),
  (3005993, 0, 1),
  (3006513, 0, 2),
  (3008130, 2, 1),
  (3012514, 3, 2),
  (3014497, 3, 2),
  (3014805, 2, 0),
  (3015456, 0, 2),
  (3015949, 0, 1),
  (3017039, 0, 2),
  (3018074, 0, 2),
  (3018115, 1, 2),
  (3018153, 3, 0),
  (3018595, 0, 1),
  (3021128, 0, 1),
  (3021775, 0, 2),
  (3025430, 0, 0),
  (3030110, 3, 1),
  (3030897, 0, 1),
  (3031482, 1, 2),
  (3033700, 0, 2),
  (3035260, 1, 0),
  (3036734, 1, 0),
  (3041191, 0, 0),
  (3041255, 2, 2),
  (3043855, 1, 0),
  (3048424, 3, 2),
  (3049432, 3, 0),
  (3052838, 0, 1),
  (3053090, 0, 0),
  (3054552, 1, 1),
  (3055112, 0, 2),
  (3056385, 1, 0),
  (3059581, 2, 2),
  (3062451, 3, 0),
  (3063977, 2, 2),
  (3064976, 3, 1),
  (3068329, 1, 2),
  (3068857, 1, 2),
  (3071065, 0, 0),
  (3071988, 2, 0),
  (3076004, 0, 2),
  (3078334, 1, 0),
  (3078842, 3, 1),
  (3080149, 3, 1),
  (3083477, 1, 0),
  (3087643, 2, 2),
  (3090167, 2, 1),
  (3090541, 2, 0),
  (3091180, 2, 1),
  (3092144, 2, 1),
  (3092985, 3, 1),
  (3093026, 0, 2),
  (3096780, 0, 0),
  (3099677, 3, 2),
  (3103291, 2, 0),
  (3104621, 3, 1),
  (3106701, 0, 0),
  (3107228, 2, 0),
  (3107486, 0, 0),
  (3117281, 3, 0),
  (3118761, 0, 0),
  (3119352, 2, 0),
  (3121102, 2, 0),
  (3121634, 1, 1),
  (3123609, 3, 1),
  (3125498, 1, 2),
  (3125722, 2, 2),
  (3126683, 2, 0),
  (3130757, 0, 2),
  (3130905, 0, 2),
  (3133976, 1, 1),
  (3134430, 2, 1),
  (3135772, 1, 1),
  (3136989, 1, 0),
  (3138089, 1, 1),
  (3141079, 2, 1),
  (3141638, 1, 2),
  (3141641, 2, 0),
  (3142249, 3, 2),
  (3143660, 2, 2),
  (3146115, 0, 0),
  (3149650, 1, 2),
  (3152353, 1, 0),
  (3155590, 1, 0),
  (3156521, 0, 1),
  (3156981, 1, 0),
  (3157116, 1, 1),
  (3157143, 2, 0),
  (3158575, 1, 1),
  (3159306, 1, 1),
  (3164942, 3, 0),
  (3165014, 1, 2),
  (3165583, 0, 2),
  (3168417, 3, 0),
  (3168482, 1, 0),
  (3168682, 3, 2),
  (3171469, 1, 0),
  (3175740, 1, 2),
  (3175893, 2, 1),
  (3177802, 0, 2),
  (3184929, 3, 1),
  (3185156, 1, 1),
  (3185640, 1, 1),
  (3185989, 1, 0),
  (3187152, 0, 1),
  (3190124, 1, 1),
  (3191467, 3, 0),
  (3192861, 2, 2),
  (3194827, 1, 2),
  (3197790, 3, 2),
  (3199775, 2, 2),
  (3200450, 2, 2),
  (3200991, 2, 1),
  (3201359, 3, 1),
  (3210342, 1, 0),
  (3212932, 3, 0),
  (3215999, 0, 0),
  (3222542, 0, 0),
  (3223528, 1, 0),
  (3225024, 0, 1),
  (3225835, 3, 2),
  (3226428, 0, 2),
  (3228187, 0, 2),
  (3228446, 0, 2),
  (3228466, 3, 1),
  (3229529, 1, 1),
  (3230398, 0, 1),
  (3230573, 3, 1),
  (3231437, 2, 1),
  (3232679, 1, 0),
  (3234004, 0, 0),
  (3235476, 0, 2),
  (3236024, 2, 1),
  (3238647, 0, 1),
  (3240349, 3, 0),
  (3244224, 1, 1),
  (3245893, 2, 2),
  (3249073, 3, 0),
  (3250262, 3, 2),
  (3250362, 1, 2),
  (3252126, 0, 1),
  (3256122, 2, 2),
  (3256623, 3, 0),
  (3257018, 0, 0),
  (3257442, 2, 0),
  (3261164, 2, 0),
  (3264973, 0, 0),
  (3267311, 0, 0),
  (3267760, 2, 0),
  (3268966, 2, 0),
  (3275099, 0, 2),
  (3277878, 2, 1),
  (3280969, 3, 1),
  (3281317, 3, 1),
  (3281616, 3, 1),
  (3283023, 1, 1),
  (3284410, 3, 0),
  (3285210, 2, 1),
  (3285483, 2, 2),
  (3289605, 3, 1),
  (3290333, 0, 0),
  (3290679, 3, 1),
  (3292946, 3, 2),
  (3294020, 0, 2),
  (3294179, 1, 2),
  (3297391, 0, 0),
  (3297514, 3, 2),
  (3298909, 1, 1),
  (3301325, 0, 1),
  (3302395, 0, 2),
  (3302718, 3, 0),
  (3306648, 1, 0),
  (3306946, 1, 1),
  (3308536, 1, 0),
  (3309061, 3, 1),
  (3309627, 1, 2),
  (3312689, 3, 2),
  (3314080, 1, 2),
  (3315137, 3, 1),
  (3328729, 0, 2),
  (3331653, 3, 0),
  (3331949, 3, 2),
  (3333445, 3, 1),
  (3335188, 1, 2),
  (3335683, 1, 0),
  (3336928, 0, 2),
  (3337301, 0, 0),
  (3337703, 0, 2),
  (3338879, 2, 0),
  (3339207, 1, 1),
  (3347199, 2, 2),
  (3355002, 1, 1),
  (3359104, 2, 1),
  (3359314, 0, 0),
  (3363607, 3, 2),
  (3363884, 2, 0),
  (3364511, 3, 2),
  (3365175, 3, 1),
  (3365386, 1, 1),
  (3368393, 2, 1),
  (3370593, 3, 1),
  (3371805, 2, 1),
  (3381369, 2, 2),
  (3381733, 2, 1),
  (3383189, 0, 2),
  (3385115, 2, 1),
  (3390273, 0, 2),
  (3391671, 3, 0),
  (3393256, 2, 0),
  (3393626, 0, 1),
  (3396897, 2, 2),
  (3401599, 2, 1),
  (3409034, 1, 1),
  (3412634, 3, 2),
  (3419815, 3, 2),
  (3422276, 1, 0),
  (3422335, 0, 1),
  (3422882, 1, 0),
  (3423571, 2, 1),
  (3424930, 2, 1),
  (3428366, 0, 1),
  (3429321, 2, 2),
  (3433206, 2, 2),
  (3435680, 1, 0),
  (3436351, 2, 2),
  (3441889, 0, 2),
  (3442074, 3, 2),
  (3443800, 2, 2),
  (3445830, 0, 0),
  (3451864, 1, 0),
  (3453329, 0, 2),
  (3454203, 3, 0),
  (3455042, 3, 1),
  (3457361, 3, 2),
  (3457372, 2, 2),
  (3459855, 1, 1),
  (3461769, 1, 1),
  (3462650, 2, 1),
  (3465544, 3, 1),
  (3466928, 0, 2),
  (3467247, 3, 2),
  (3467759, 1, 0),
  (3472011, 3, 1),
  (3472070, 0, 0),
  (3474088, 3, 0),
  (3478095, 2, 1),
  (3480266, 0, 1),
  (3482928, 3, 0),
  (3484541, 0, 0),
  (3485436, 3, 1),
  (3485952, 3, 2),
  (3486207, 2, 1),
  (3488296, 2, 1),
  (3492591, 2, 2),
  (3496691, 2, 0),
  (3496744, 3, 0),
  (3497205, 0, 0),
  (3498056, 0, 2),
  (3499598, 1, 2),
  (3506185, 1, 0),
  (3511128, 3, 1),
  (3511783, 2, 0),
  (3512998, 3, 0),
  (3515415, 1, 2),
  (3516791, 0, 1),
  (3517028, 0, 0),
  (3521913, 1, 0),
  (3522235, 3, 2),
  (3522918, 1, 2),
  (3523252, 0, 2),
  (3524633, 0, 1),
  (3524979, 0, 1),
  (3529460, 2, 0),
  (3530615, 3, 1),
  (3533058, 0, 1),
  (3533079, 0, 2),
  (3535095, 1, 1),
  (3539776, 2, 0),
  (3540363, 2, 1),
  (3540697, 2, 0),
  (3540954, 2, 0),
  (3541316, 3, 0),
  (3542342, 3, 2),
  (3543552, 2, 2),
  (3543913, 3, 1),
  (3544269, 0, 1),
  (3549392, 3, 1),
  (3550162, 0, 1),
  (3551540, 2, 2),
  (3555232, 3, 1),
  (3556511, 2, 0),
  (3558007, 1, 2),
  (3563077, 0, 2),
  (3565767, 3, 2),
  (3570386, 1, 0),
  (3570878, 1, 0),
  (3573456, 0, 0),
  (3573759, 1, 1),
  (3575228, 3, 0),
  (3577087, 2, 0),
  (3578640, 0, 2),
  (3584261, 1, 1),
  (3585982, 1, 0),
  (3586474, 3, 1),
  (3588469, 1, 2),
  (3589186, 0, 1),
  (3589807, 2, 0),
  (3590365, 3, 1),
  (3591632, 2, 1),
  (3593408, 3, 1),
  (3593588, 3, 1),
  (3593653, 3, 0),
  (3594451, 3, 1),
  (3598909, 0, 1),
])
