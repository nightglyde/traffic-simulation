from util import *
schedule = deque([
  (34, 1, 3),
  (3224, 4, 2),
  (5225, 4, 7),
  (6783, 0, 4),
  (8092, 7, 4),
  (9547, 0, 4),
  (11768, 4, 3),
  (13592, 0, 4),
  (14739, 5, 3),
  (17981, 4, 3),
  (22012, 0, 6),
  (22538, 1, 3),
  (23037, 6, 0),
  (25392, 2, 0),
  (25885, 6, 0),
  (27704, 6, 0),
  (29149, 7, 3),
  (29675, 7, 7),
  (33250, 5, 5),
  (35749, 6, 7),
  (45702, 7, 7),
  (47392, 7, 6),
  (48997, 2, 5),
  (49476, 1, 3),
  (49579, 1, 3),
  (50356, 2, 7),
  (51947, 3, 7),
  (54041, 5, 3),
  (55296, 1, 7),
  (55430, 0, 7),
  (55964, 6, 0),
  (56142, 5, 1),
  (57223, 0, 7),
  (58605, 4, 6),
  (59050, 6, 3),
  (59155, 2, 7),
  (59748, 4, 3),
  (59757, 4, 2),
  (65885, 4, 7),
  (72083, 2, 5),
  (72975, 2, 3),
  (73086, 6, 0),
  (73155, 6, 7),
  (73459, 5, 1),
  (74878, 2, 3),
  (77941, 5, 2),
  (79317, 4, 7),
  (80871, 1, 7),
  (82328, 0, 0),
  (83290, 4, 7),
  (84414, 6, 5),
  (85599, 7, 3),
  (86205, 1, 7),
  (87018, 1, 4),
  (88055, 6, 0),
  (88056, 6, 7),
  (89103, 7, 3),
  (91284, 6, 7),
  (91681, 6, 2),
  (91739, 4, 2),
  (92368, 5, 6),
  (95676, 5, 3),
  (96942, 3, 3),
  (97809, 2, 7),
  (104049, 3, 7),
  (106490, 6, 7),
  (108355, 6, 0),
  (108469, 3, 1),
  (117060, 1, 3),
  (120397, 2, 6),
  (121203, 4, 2),
  (126552, 2, 3),
  (126829, 7, 3),
  (134633, 0, 7),
  (139006, 7, 3),
  (139831, 0, 0),
  (144775, 0, 6),
  (145767, 3, 6),
  (150529, 4, 3),
  (155835, 1, 3),
  (157005, 2, 6),
  (157161, 7, 7),
  (157554, 1, 2),
  (157566, 3, 5),
  (158058, 3, 2),
  (160162, 6, 3),
  (161579, 3, 7),
  (162316, 7, 0),
  (163058, 0, 6),
  (167632, 1, 7),
  (167917, 4, 2),
  (176856, 7, 0),
  (177169, 5, 7),
  (179751, 4, 5),
  (180457, 4, 7),
  (187689, 7, 7),
  (189225, 7, 0),
  (189765, 4, 3),
  (191560, 3, 3),
  (194400, 6, 4),
  (197499, 1, 0),
  (198838, 5, 3),
  (201303, 1, 7),
  (204078, 0, 0),
  (205554, 1, 4),
  (205867, 4, 1),
  (209218, 3, 3),
  (210476, 2, 2),
  (212137, 5, 0),
  (212265, 3, 3),
  (215503, 7, 0),
  (217393, 0, 0),
  (217609, 2, 5),
  (219780, 6, 7),
  (220861, 1, 7),
  (220999, 7, 7),
  (222205, 3, 1),
  (223458, 7, 1),
  (225604, 5, 3),
  (226054, 4, 3),
  (227669, 5, 3),
  (228887, 2, 7),
  (230319, 7, 4),
  (231706, 7, 7),
  (232937, 3, 2),
  (234228, 4, 3),
  (237009, 7, 3),
  (237993, 4, 2),
  (240319, 6, 6),
  (240578, 0, 3),
  (243755, 7, 4),
  (244443, 3, 2),
  (246971, 4, 2),
  (249253, 6, 3),
  (251484, 6, 7),
  (252326, 5, 2),
  (256555, 1, 4),
  (256769, 3, 7),
  (261389, 0, 6),
  (261997, 5, 2),
  (262854, 6, 0),
  (263662, 1, 2),
  (263700, 3, 3),
  (264414, 3, 7),
  (264542, 5, 7),
  (265079, 6, 0),
  (265950, 6, 7),
  (267664, 3, 3),
  (269127, 6, 5),
  (271647, 7, 7),
  (272429, 4, 2),
  (273231, 7, 4),
  (276204, 5, 7),
  (278949, 2, 7),
  (281469, 5, 6),
  (281620, 6, 0),
  (281787, 3, 6),
  (281945, 5, 3),
  (282997, 0, 0),
  (286505, 5, 7),
  (287982, 1, 0),
  (288225, 7, 0),
  (290105, 6, 5),
  (292726, 1, 3),
  (292926, 1, 6),
  (293224, 6, 0),
  (293279, 1, 3),
  (293473, 6, 7),
  (296795, 2, 3),
  (297753, 0, 4),
  (298131, 0, 7),
  (305954, 0, 0),
  (306297, 1, 3),
  (306547, 4, 7),
  (310338, 3, 3),
  (310782, 5, 1),
  (310918, 0, 7),
  (313726, 2, 7),
  (315584, 2, 7),
  (318681, 5, 3),
  (319428, 1, 4),
  (320326, 6, 0),
  (324950, 0, 0),
  (326066, 7, 6),
  (330645, 0, 4),
  (331789, 2, 6),
  (333057, 7, 4),
  (334247, 4, 7),
  (338364, 6, 3),
  (340027, 6, 6),
  (343195, 0, 4),
  (343217, 6, 0),
  (345834, 2, 3),
  (346260, 6, 6),
  (347497, 5, 6),
  (348886, 6, 7),
  (351371, 6, 0),
  (354573, 3, 2),
  (358002, 1, 0),
  (358171, 4, 6),
  (360460, 2, 2),
  (367636, 6, 7),
  (371452, 0, 7),
  (373595, 5, 3),
  (374799, 5, 3),
  (374808, 5, 1),
  (375357, 6, 3),
  (375895, 5, 6),
  (388756, 6, 3),
  (388986, 3, 2),
  (391068, 3, 7),
  (392604, 5, 3),
  (397167, 3, 5),
  (397424, 5, 6),
  (398191, 0, 7),
  (403249, 7, 6),
  (404924, 7, 2),
  (405387, 5, 3),
  (406341, 4, 4),
  (407899, 3, 2),
  (413813, 3, 1),
  (415880, 6, 6),
  (416976, 4, 7),
  (417464, 5, 7),
  (417732, 0, 4),
  (418224, 5, 7),
  (418227, 7, 0),
  (419480, 0, 4),
  (423441, 3, 3),
  (429146, 2, 7),
  (429732, 2, 5),
  (431054, 1, 7),
  (432127, 1, 0),
  (434643, 0, 3),
  (436982, 7, 7),
  (437797, 3, 6),
  (437880, 6, 3),
  (438219, 6, 4),
  (440060, 7, 7),
  (442060, 7, 7),
  (446351, 1, 3),
  (450100, 0, 3),
  (452874, 1, 0),
  (454655, 1, 4),
  (455204, 7, 7),
  (455727, 4, 7),
  (456883, 5, 3),
  (460796, 1, 0),
  (461364, 2, 7),
  (464320, 6, 0),
  (464345, 4, 6),
  (465318, 0, 5),
  (465981, 1, 3),
  (467850, 0, 7),
  (468562, 0, 3),
  (478127, 5, 6),
  (479233, 2, 6),
  (480970, 0, 0),
  (481085, 2, 6),
  (482523, 7, 3),
  (485099, 0, 3),
  (486606, 4, 1),
  (486973, 1, 7),
  (489155, 5, 5),
  (492070, 2, 7),
  (492592, 1, 3),
  (501422, 1, 7),
  (503512, 2, 3),
  (504551, 7, 7),
  (506130, 4, 3),
  (514612, 7, 7),
  (517911, 0, 0),
  (519152, 0, 2),
  (519486, 1, 4),
  (521260, 3, 2),
  (525893, 1, 0),
  (526533, 7, 0),
  (526882, 5, 6),
  (527829, 1, 3),
  (528742, 1, 0),
  (532253, 3, 3),
  (533701, 2, 1),
  (535014, 6, 7),
  (535584, 4, 2),
  (536985, 7, 4),
  (538330, 3, 5),
  (539590, 4, 3),
  (548732, 2, 2),
  (550330, 5, 3),
  (550870, 1, 6),
  (551173, 0, 3),
  (552110, 7, 4),
  (554397, 6, 7),
  (555195, 1, 7),
  (555941, 3, 3),
  (558916, 6, 0),
  (559007, 6, 0),
  (561684, 4, 5),
  (563715, 5, 2),
  (563952, 4, 3),
  (576511, 3, 2),
  (577343, 0, 7),
  (579759, 4, 7),
  (580227, 6, 3),
  (582039, 2, 7),
  (582445, 6, 0),
  (582537, 0, 0),
  (585096, 0, 0),
  (585584, 1, 5),
  (587635, 2, 1),
  (587651, 0, 4),
  (587794, 3, 3),
  (588921, 1, 6),
  (590562, 7, 3),
  (591546, 4, 2),
  (594228, 3, 5),
  (595047, 1, 0),
  (595938, 0, 4),
  (599603, 2, 3),
  (600129, 4, 4),
  (600816, 5, 1),
  (600987, 4, 7),
  (603920, 3, 3),
  (604425, 5, 7),
  (604436, 3, 7),
  (608985, 6, 3),
  (611162, 4, 2),
  (612853, 7, 0),
  (614509, 0, 4),
  (615184, 6, 5),
  (620280, 0, 0),
  (624721, 4, 7),
  (624920, 4, 6),
  (625958, 3, 3),
  (635467, 0, 3),
  (639184, 1, 0),
  (640352, 0, 0),
  (641026, 7, 3),
  (644217, 5, 7),
  (646863, 2, 4),
  (647336, 7, 7),
  (648083, 5, 3),
  (648312, 2, 7),
  (652369, 3, 3),
  (653563, 4, 6),
  (655145, 0, 0),
  (655341, 6, 7),
  (656127, 5, 3),
  (658368, 7, 7),
  (663111, 0, 7),
  (667820, 6, 0),
  (669081, 7, 0),
  (671780, 3, 3),
  (672345, 3, 3),
  (673569, 2, 3),
  (674663, 5, 7),
  (689246, 4, 2),
  (689332, 5, 3),
  (689674, 5, 3),
  (689853, 7, 0),
  (690297, 5, 4),
  (691600, 3, 3),
  (692120, 4, 2),
  (694530, 3, 7),
  (696914, 7, 0),
  (703397, 0, 0),
  (704569, 6, 3),
  (705239, 2, 7),
  (707609, 7, 4),
  (708060, 0, 4),
  (709304, 6, 0),
  (710764, 6, 7),
  (713044, 6, 2),
  (714204, 7, 7),
  (715924, 4, 1),
  (716390, 0, 3),
  (716901, 3, 3),
  (717601, 4, 2),
  (718482, 0, 6),
  (719171, 3, 7),
  (721456, 2, 7),
  (721467, 5, 4),
  (721475, 0, 0),
  (721731, 0, 0),
  (722422, 4, 7),
  (723029, 7, 6),
  (724828, 2, 7),
  (726012, 5, 3),
  (726327, 3, 6),
  (728226, 4, 5),
  (728967, 3, 2),
  (730290, 2, 5),
  (737918, 2, 3),
  (743018, 7, 7),
  (745396, 5, 7),
  (748349, 6, 6),
  (749437, 4, 3),
  (750696, 7, 0),
  (750757, 2, 3),
  (751276, 3, 3),
  (759094, 3, 3),
  (759369, 2, 1),
  (759819, 7, 7),
  (760995, 4, 5),
  (762364, 7, 7),
  (762475, 2, 7),
  (763132, 7, 7),
  (764667, 7, 5),
  (771571, 3, 1),
  (771588, 1, 6),
  (776630, 4, 6),
  (777153, 4, 4),
  (777851, 5, 2),
  (779708, 4, 7),
  (780284, 2, 5),
  (790756, 4, 5),
  (793678, 5, 7),
  (795241, 6, 7),
  (796143, 1, 7),
  (796235, 6, 5),
  (798104, 7, 3),
  (799444, 5, 7),
  (800034, 2, 2),
  (802201, 1, 4),
  (804026, 7, 6),
  (804438, 2, 7),
  (806900, 4, 3),
  (808073, 4, 6),
  (811166, 1, 6),
  (812587, 3, 7),
  (812756, 5, 7),
  (812958, 4, 5),
  (813219, 2, 3),
  (820177, 7, 6),
  (820225, 5, 7),
  (821965, 2, 2),
  (824105, 7, 7),
  (826876, 2, 1),
  (827305, 4, 7),
  (828643, 6, 7),
  (828773, 5, 3),
  (830028, 7, 7),
  (830076, 3, 3),
  (832978, 5, 3),
  (837075, 1, 7),
  (839382, 3, 3),
  (841317, 1, 7),
  (841852, 7, 5),
  (842474, 4, 5),
  (845111, 7, 4),
  (845706, 4, 1),
  (846133, 4, 7),
  (852287, 4, 5),
  (852368, 4, 3),
  (853695, 6, 0),
  (858384, 5, 3),
  (858525, 4, 2),
  (863667, 0, 6),
  (864304, 5, 7),
  (865918, 4, 3),
  (872129, 4, 0),
  (873612, 3, 7),
  (874668, 5, 2),
  (875401, 6, 7),
  (875489, 1, 7),
  (875996, 3, 2),
  (876901, 4, 6),
  (880060, 1, 7),
  (881319, 7, 6),
  (882948, 7, 4),
  (889869, 6, 3),
  (890417, 6, 3),
  (890672, 1, 3),
  (894064, 0, 3),
  (895635, 1, 7),
  (899046, 2, 2),
  (905288, 0, 3),
  (909298, 7, 4),
  (909720, 1, 0),
  (912306, 1, 0),
  (913380, 3, 3),
  (919263, 6, 4),
  (919555, 4, 2),
  (921122, 1, 0),
  (921461, 2, 3),
  (923624, 3, 3),
  (924351, 4, 3),
  (925135, 0, 2),
  (926585, 6, 4),
  (929851, 7, 0),
  (933655, 2, 3),
  (933677, 3, 7),
  (935483, 4, 3),
  (936297, 6, 3),
  (939521, 0, 7),
  (942803, 6, 3),
  (943009, 5, 7),
  (946870, 1, 7),
  (953739, 2, 6),
  (953756, 4, 3),
  (953899, 7, 4),
  (953920, 4, 3),
  (954218, 1, 3),
  (955586, 6, 7),
  (956080, 5, 2),
  (958192, 7, 0),
  (959376, 3, 2),
  (960498, 3, 3),
  (961156, 4, 6),
  (968380, 7, 0),
  (969333, 2, 3),
  (971942, 5, 6),
  (973025, 3, 3),
  (974004, 0, 0),
  (979708, 3, 4),
  (983024, 2, 6),
  (984277, 4, 4),
  (989305, 0, 7),
  (992276, 2, 5),
  (992803, 4, 1),
  (993032, 4, 3),
  (995248, 4, 5),
  (996992, 6, 6),
  (1001227, 4, 7),
  (1002532, 1, 0),
  (1009412, 5, 2),
  (1011453, 5, 2),
  (1012272, 0, 6),
  (1013702, 0, 7),
  (1014035, 1, 0),
  (1014664, 2, 7),
  (1014817, 3, 6),
  (1015687, 0, 2),
  (1016607, 0, 7),
  (1019419, 2, 3),
  (1020786, 4, 7),
  (1024572, 2, 3),
  (1024731, 4, 2),
  (1026950, 5, 6),
  (1027599, 5, 3),
  (1027666, 1, 3),
  (1036397, 7, 0),
  (1036471, 3, 3),
  (1039306, 1, 7),
  (1040140, 7, 3),
  (1041683, 1, 4),
  (1042219, 3, 2),
  (1044329, 3, 3),
  (1053009, 2, 7),
  (1053371, 7, 7),
  (1054695, 1, 3),
  (1054762, 4, 7),
  (1054839, 2, 3),
  (1055965, 7, 6),
  (1060710, 4, 3),
  (1065746, 4, 3),
  (1066179, 5, 5),
  (1066792, 1, 4),
  (1067262, 1, 5),
  (1073465, 2, 6),
  (1074793, 3, 7),
  (1079855, 7, 3),
  (1080416, 2, 7),
  (1081812, 5, 3),
  (1083222, 2, 3),
  (1087617, 5, 5),
  (1087838, 5, 7),
  (1092757, 7, 7),
  (1093189, 1, 0),
  (1096394, 6, 2),
  (1099158, 1, 3),
  (1102086, 0, 3),
  (1103943, 4, 3),
  (1110215, 1, 6),
  (1112309, 6, 3),
  (1114420, 2, 3),
  (1115584, 7, 5),
  (1118760, 3, 1),
  (1129804, 2, 3),
  (1133320, 4, 6),
  (1134541, 2, 7),
  (1134616, 6, 3),
  (1136608, 1, 7),
  (1137397, 0, 7),
  (1140833, 3, 6),
  (1143886, 3, 7),
  (1144138, 5, 7),
  (1146257, 6, 0),
  (1148973, 2, 6),
  (1150511, 7, 3),
  (1151418, 3, 2),
  (1152251, 7, 6),
  (1155365, 2, 7),
  (1155534, 0, 7),
  (1157835, 4, 1),
  (1157842, 5, 6),
  (1159101, 1, 7),
  (1162426, 0, 7),
  (1165629, 5, 3),
  (1165953, 1, 0),
  (1166379, 7, 0),
  (1171706, 2, 7),
  (1172061, 7, 7),
  (1175381, 6, 0),
  (1176248, 7, 7),
  (1176551, 7, 4),
  (1178543, 3, 7),
  (1179939, 0, 0),
  (1180548, 6, 3),
  (1183162, 6, 0),
  (1185592, 7, 7),
  (1186405, 1, 7),
  (1190447, 0, 3),
  (1190957, 7, 4),
  (1192373, 6, 7),
  (1198025, 7, 6),
  (1198092, 1, 7),
  (1201236, 0, 5),
  (1202261, 2, 2),
  (1203408, 2, 0),
  (1204398, 3, 5),
  (1205914, 6, 7),
  (1208509, 1, 0),
  (1210601, 3, 7),
  (1214210, 1, 7),
  (1216426, 5, 6),
  (1221062, 5, 5),
  (1223608, 5, 2),
  (1226550, 2, 2),
  (1228645, 5, 2),
  (1228728, 7, 6),
  (1229183, 5, 2),
  (1229768, 5, 2),
  (1229989, 1, 0),
  (1230249, 7, 3),
  (1232232, 2, 2),
  (1237031, 0, 3),
  (1244305, 5, 4),
  (1244860, 6, 0),
  (1245408, 6, 7),
  (1246617, 5, 2),
  (1247003, 2, 7),
  (1247172, 5, 7),
  (1247549, 0, 2),
  (1248193, 1, 3),
  (1249306, 2, 5),
  (1249772, 0, 0),
  (1252168, 1, 7),
  (1257808, 5, 3),
  (1259067, 7, 0),
  (1260844, 0, 6),
  (1261012, 1, 3),
  (1261178, 6, 3),
  (1264703, 7, 1),
  (1265292, 2, 7),
  (1267005, 3, 3),
  (1273554, 0, 3),
  (1276467, 7, 0),
  (1277261, 1, 3),
  (1278003, 1, 7),
  (1278809, 0, 7),
  (1279740, 3, 6),
  (1280953, 7, 0),
  (1282491, 7, 6),
  (1286454, 2, 6),
  (1286605, 6, 6),
  (1290593, 1, 6),
  (1293209, 6, 2),
  (1293690, 6, 5),
  (1296311, 1, 3),
  (1297062, 1, 3),
  (1299095, 4, 3),
  (1299226, 5, 7),
  (1300297, 7, 7),
  (1302981, 0, 3),
  (1304270, 1, 7),
  (1305791, 2, 6),
  (1306973, 6, 6),
  (1308386, 0, 6),
  (1308518, 0, 1),
  (1312471, 7, 6),
  (1313861, 2, 7),
  (1314580, 6, 7),
  (1316276, 1, 6),
  (1316734, 7, 3),
  (1320810, 7, 3),
  (1321066, 3, 2),
  (1321963, 3, 3),
  (1323867, 2, 5),
  (1327750, 7, 6),
  (1328896, 7, 7),
  (1329438, 2, 7),
  (1329895, 4, 6),
  (1333796, 0, 4),
  (1335454, 3, 5),
  (1338236, 7, 7),
  (1341227, 1, 7),
  (1341868, 0, 4),
  (1343655, 4, 4),
  (1345807, 3, 3),
  (1348827, 0, 3),
  (1349207, 2, 3),
  (1350501, 1, 3),
  (1351306, 2, 2),
  (1351317, 4, 3),
  (1354013, 0, 6),
  (1362498, 7, 0),
  (1365843, 2, 3),
  (1367629, 2, 6),
  (1367920, 5, 3),
  (1368372, 5, 3),
  (1373657, 1, 7),
  (1376974, 7, 4),
  (1378413, 3, 2),
  (1381584, 7, 7),
  (1384524, 0, 7),
  (1387253, 3, 2),
  (1388955, 3, 5),
  (1389244, 2, 2),
  (1391720, 1, 7),
  (1391773, 7, 7),
  (1398288, 5, 6),
  (1398462, 4, 2),
  (1398559, 2, 3),
  (1406273, 0, 0),
  (1410158, 3, 2),
  (1410281, 2, 3),
  (1412526, 5, 2),
  (1418425, 3, 7),
  (1421688, 6, 6),
  (1422641, 0, 7),
  (1427056, 5, 3),
  (1427839, 4, 6),
  (1428564, 3, 3),
  (1429848, 7, 4),
  (1436492, 6, 3),
  (1436695, 4, 0),
  (1436971, 6, 6),
  (1437635, 6, 7),
  (1438212, 1, 6),
  (1444852, 0, 4),
  (1448026, 7, 0),
  (1456205, 4, 2),
  (1456242, 6, 1),
  (1458018, 7, 7),
  (1463903, 0, 6),
  (1464091, 6, 0),
  (1466229, 5, 2),
  (1468084, 2, 3),
  (1474503, 6, 0),
  (1478459, 1, 7),
  (1479230, 5, 1),
  (1479801, 7, 0),
  (1480523, 6, 6),
  (1485201, 7, 6),
  (1489109, 5, 2),
  (1492504, 0, 7),
  (1495073, 4, 6),
  (1495626, 5, 6),
  (1497330, 5, 3),
  (1498193, 6, 3),
  (1499355, 0, 3),
  (1500377, 4, 2),
  (1500690, 5, 3),
  (1502626, 5, 3),
  (1505178, 0, 4),
  (1508137, 5, 7),
  (1512749, 0, 4),
  (1515692, 7, 5),
  (1516418, 3, 7),
  (1521372, 2, 7),
  (1523561, 3, 2),
  (1525969, 1, 5),
  (1528721, 3, 3),
  (1530374, 2, 6),
  (1530521, 5, 6),
  (1533199, 2, 2),
  (1534614, 1, 7),
  (1539338, 1, 4),
  (1547820, 6, 7),
  (1554445, 3, 7),
  (1558108, 4, 3),
  (1558615, 6, 4),
  (1559024, 4, 2),
  (1560312, 6, 0),
  (1562501, 7, 7),
  (1564260, 5, 7),
  (1567520, 7, 6),
  (1568094, 1, 0),
  (1571327, 6, 5),
  (1572143, 7, 3),
  (1575708, 7, 4),
  (1579098, 4, 3),
  (1585843, 7, 0),
  (1595524, 3, 5),
  (1597079, 4, 7),
  (1600987, 1, 0),
  (1607542, 2, 3),
  (1608334, 2, 3),
  (1610614, 1, 0),
  (1615598, 0, 1),
  (1616310, 0, 0),
  (1617145, 7, 7),
  (1617968, 7, 0),
  (1628183, 1, 6),
  (1628558, 5, 5),
  (1629863, 5, 3),
  (1637112, 1, 1),
  (1639351, 1, 6),
  (1639703, 3, 6),
  (1640503, 2, 2),
  (1640838, 3, 6),
  (1640935, 0, 6),
  (1641321, 7, 7),
  (1641874, 4, 2),
  (1642556, 2, 3),
  (1644766, 1, 0),
  (1647462, 5, 5),
  (1652192, 4, 2),
  (1655035, 2, 7),
  (1657958, 4, 7),
  (1658293, 1, 6),
  (1661621, 0, 7),
  (1667658, 4, 2),
  (1671650, 6, 3),
  (1671937, 5, 7),
  (1674846, 0, 7),
  (1677255, 4, 2),
  (1679729, 7, 7),
  (1680337, 1, 4),
  (1680403, 3, 7),
  (1682159, 5, 1),
  (1682588, 2, 2),
  (1683127, 3, 4),
  (1685308, 0, 0),
  (1693420, 1, 3),
  (1695254, 0, 0),
  (1695689, 5, 7),
  (1696173, 7, 4),
  (1696796, 3, 3),
  (1696879, 6, 6),
  (1696902, 5, 5),
  (1702875, 6, 0),
  (1704534, 1, 0),
  (1710190, 3, 3),
  (1713834, 6, 4),
  (1715930, 0, 0),
  (1717048, 6, 0),
  (1718089, 3, 5),
  (1719753, 0, 0),
  (1721118, 1, 0),
  (1721528, 2, 7),
  (1721741, 4, 5),
  (1723514, 7, 0),
  (1724771, 6, 7),
  (1727048, 4, 7),
  (1734214, 3, 2),
  (1738796, 6, 3),
  (1739795, 0, 1),
  (1740807, 0, 3),
  (1744848, 7, 7),
  (1745209, 6, 0),
  (1747206, 5, 1),
  (1748293, 2, 6),
  (1748362, 5, 7),
  (1748813, 0, 7),
  (1752226, 6, 6),
  (1754523, 6, 7),
  (1756166, 6, 4),
  (1756537, 0, 6),
  (1757014, 1, 3),
  (1757755, 5, 3),
  (1757892, 2, 6),
  (1759851, 7, 3),
  (1760589, 0, 7),
  (1763850, 4, 6),
  (1764700, 0, 6),
  (1767306, 0, 0),
  (1769530, 5, 7),
  (1769807, 0, 0),
  (1771421, 4, 7),
  (1771520, 5, 0),
  (1773170, 3, 2),
  (1773517, 6, 3),
  (1775127, 6, 0),
  (1778044, 0, 4),
  (1781271, 1, 4),
  (1782936, 0, 0),
  (1784598, 7, 7),
  (1784850, 3, 5),
  (1785179, 3, 4),
  (1787392, 1, 0),
  (1788207, 0, 0),
  (1795405, 4, 5),
  (1795535, 0, 7),
  (1797044, 0, 3),
  (1801474, 1, 0),
  (1807993, 2, 7),
  (1815173, 3, 5),
  (1815608, 3, 3),
  (1816158, 3, 3),
  (1818106, 6, 5),
  (1820430, 3, 5),
  (1820976, 5, 7),
  (1821519, 0, 7),
  (1822838, 5, 5),
  (1825378, 5, 7),
  (1827650, 0, 4),
  (1829828, 4, 3),
  (1835402, 6, 4),
  (1836177, 3, 3),
  (1838928, 7, 6),
  (1847465, 3, 2),
  (1849335, 2, 2),
  (1849803, 1, 4),
  (1853262, 4, 2),
  (1857871, 3, 2),
  (1858333, 7, 0),
  (1862345, 3, 2),
  (1863523, 5, 2),
  (1864393, 2, 2),
  (1866873, 4, 3),
  (1869258, 6, 4),
  (1870014, 3, 7),
  (1870685, 5, 4),
  (1871348, 3, 2),
  (1871826, 3, 5),
  (1873384, 2, 7),
  (1877656, 1, 2),
  (1879641, 5, 3),
  (1879837, 1, 4),
  (1882149, 6, 0),
  (1887087, 2, 7),
  (1889160, 6, 0),
  (1890772, 0, 3),
  (1894509, 7, 0),
  (1895551, 5, 1),
  (1896091, 6, 7),
  (1896944, 6, 0),
  (1905013, 4, 2),
  (1905263, 7, 3),
  (1908324, 7, 3),
  (1908670, 7, 2),
  (1911814, 7, 7),
  (1913712, 0, 7),
  (1917808, 5, 5),
  (1918084, 1, 3),
  (1923515, 7, 4),
  (1925753, 0, 6),
  (1928140, 0, 3),
  (1931291, 0, 3),
  (1932081, 4, 3),
  (1932363, 7, 6),
  (1936346, 5, 4),
  (1942148, 5, 4),
  (1952862, 5, 3),
  (1954915, 5, 3),
  (1955127, 7, 5),
  (1956481, 3, 2),
  (1958048, 1, 4),
  (1960066, 3, 6),
  (1961942, 2, 7),
  (1962066, 5, 5),
  (1964510, 6, 3),
  (1965717, 5, 5),
  (1970056, 0, 3),
  (1970322, 7, 3),
  (1970754, 1, 4),
  (1973810, 6, 3),
  (1975694, 7, 6),
  (1977867, 7, 0),
  (1979672, 6, 4),
  (1980836, 2, 2),
  (1980989, 4, 7),
  (1983408, 7, 0),
  (1984787, 1, 0),
  (1987095, 4, 3),
  (1988618, 7, 4),
  (1988629, 4, 7),
  (1991769, 3, 2),
  (1993064, 5, 2),
  (1993981, 4, 4),
  (1996560, 7, 4),
  (1998354, 0, 7),
  (1998939, 6, 7),
  (2000141, 4, 2),
  (2002012, 3, 3),
  (2003181, 1, 3),
  (2011604, 0, 7),
  (2012258, 3, 2),
  (2013509, 0, 6),
  (2013900, 7, 2),
  (2016628, 2, 0),
  (2017042, 1, 6),
  (2020906, 4, 3),
  (2020933, 4, 5),
  (2022633, 0, 0),
  (2028852, 0, 0),
  (2032789, 6, 0),
  (2033982, 0, 6),
  (2034074, 6, 7),
  (2035387, 0, 6),
  (2036715, 1, 0),
  (2037530, 0, 0),
  (2039564, 0, 3),
  (2040945, 5, 5),
  (2043989, 3, 2),
  (2044611, 2, 7),
  (2046331, 0, 3),
  (2047130, 1, 4),
  (2048385, 6, 6),
  (2049986, 7, 0),
  (2052205, 4, 5),
  (2054028, 2, 3),
  (2055410, 0, 5),
  (2056066, 2, 7),
  (2058183, 2, 0),
  (2058352, 4, 6),
  (2064019, 1, 7),
  (2066564, 0, 3),
  (2066855, 1, 7),
  (2068464, 1, 0),
  (2070877, 6, 0),
  (2072860, 7, 3),
  (2074082, 5, 3),
  (2074476, 2, 7),
  (2076249, 6, 3),
  (2077625, 2, 7),
  (2082490, 4, 6),
  (2082971, 7, 4),
  (2083310, 5, 1),
  (2083425, 5, 7),
  (2087006, 0, 0),
  (2089443, 1, 0),
  (2090039, 4, 3),
  (2090211, 4, 3),
  (2091028, 6, 0),
  (2093640, 0, 3),
  (2100334, 3, 6),
  (2101852, 4, 6),
  (2105384, 4, 3),
  (2107772, 4, 2),
  (2108984, 3, 6),
  (2109473, 1, 0),
  (2111786, 4, 3),
  (2112376, 3, 7),
  (2112476, 6, 7),
  (2115471, 1, 4),
  (2115501, 4, 7),
  (2117323, 2, 2),
  (2117651, 6, 5),
  (2118458, 1, 0),
  (2119738, 4, 7),
  (2119857, 0, 7),
  (2120560, 7, 4),
  (2120615, 6, 7),
  (2123405, 4, 4),
  (2124307, 1, 0),
  (2124698, 0, 7),
  (2126896, 2, 7),
  (2129154, 3, 7),
  (2136344, 0, 3),
  (2137285, 5, 5),
  (2137790, 4, 4),
  (2141644, 3, 6),
  (2144106, 5, 3),
  (2144300, 3, 3),
  (2145419, 7, 0),
  (2146404, 3, 7),
  (2147616, 6, 3),
  (2148593, 2, 6),
  (2152312, 0, 7),
  (2156646, 2, 3),
  (2156832, 5, 7),
  (2158929, 4, 7),
  (2163432, 5, 6),
  (2165285, 6, 7),
  (2166405, 1, 3),
  (2166549, 2, 3),
  (2169040, 7, 0),
  (2170287, 5, 7),
  (2171293, 6, 3),
  (2171317, 1, 0),
  (2172491, 2, 3),
  (2174449, 5, 3),
  (2174788, 1, 3),
  (2175188, 3, 3),
  (2175428, 7, 0),
  (2175891, 0, 6),
  (2178548, 6, 0),
  (2189813, 3, 6),
  (2190457, 4, 3),
  (2193810, 1, 7),
  (2195074, 6, 3),
  (2198591, 3, 2),
  (2200251, 7, 0),
  (2200433, 6, 4),
  (2203132, 7, 7),
  (2203910, 4, 6),
  (2207939, 7, 0),
  (2208822, 2, 6),
  (2210043, 6, 3),
  (2212031, 6, 3),
  (2214072, 4, 7),
  (2221239, 1, 3),
  (2225993, 6, 7),
  (2229079, 7, 7),
  (2231737, 7, 4),
  (2231840, 1, 3),
  (2234475, 3, 3),
  (2236538, 2, 2),
  (2239722, 7, 3),
  (2243699, 3, 7),
  (2246569, 3, 4),
  (2249223, 1, 0),
  (2250346, 1, 7),
  (2250706, 6, 0),
  (2257819, 2, 5),
  (2260553, 1, 0),
  (2262477, 0, 3),
  (2265397, 6, 7),
  (2266377, 3, 5),
  (2268281, 1, 4),
  (2272280, 4, 3),
  (2273820, 4, 3),
  (2275325, 1, 0),
  (2275972, 7, 3),
  (2276581, 1, 4),
  (2278125, 4, 7),
  (2278981, 1, 7),
  (2285392, 7, 7),
  (2288441, 1, 6),
  (2288887, 3, 5),
  (2291008, 5, 5),
  (2293858, 0, 7),
  (2297302, 0, 7),
  (2304461, 7, 0),
  (2305393, 0, 3),
  (2306059, 2, 6),
  (2307013, 6, 4),
  (2308662, 2, 7),
  (2309456, 6, 3),
  (2309637, 3, 6),
  (2311414, 1, 0),
  (2311665, 2, 2),
  (2311908, 7, 7),
  (2313359, 7, 7),
  (2319971, 7, 0),
  (2329623, 4, 7),
  (2333245, 6, 6),
  (2335192, 1, 6),
  (2336401, 1, 0),
  (2338502, 3, 6),
  (2340347, 1, 0),
  (2344477, 0, 7),
  (2345419, 4, 3),
  (2346287, 4, 3),
  (2347854, 5, 6),
  (2349087, 6, 6),
  (2349271, 0, 7),
  (2349525, 4, 6),
  (2349671, 7, 0),
  (2351949, 3, 1),
  (2352743, 7, 4),
  (2356275, 1, 4),
  (2357622, 2, 3),
  (2359752, 3, 6),
  (2364060, 6, 3),
  (2364354, 5, 3),
  (2365970, 5, 7),
  (2369053, 4, 2),
  (2375664, 2, 7),
  (2378091, 1, 0),
  (2380105, 1, 4),
  (2384967, 1, 4),
  (2386373, 1, 7),
  (2386794, 7, 3),
  (2388831, 5, 3),
  (2394846, 5, 7),
  (2398615, 2, 5),
  (2398626, 4, 2),
  (2401108, 4, 6),
  (2402987, 2, 3),
  (2406766, 0, 6),
  (2408577, 6, 6),
  (2408707, 2, 3),
  (2409960, 6, 3),
  (2411388, 6, 3),
  (2413014, 0, 3),
  (2413586, 0, 7),
  (2414038, 4, 6),
  (2415414, 7, 6),
  (2419015, 5, 2),
  (2421792, 2, 1),
  (2429378, 3, 3),
  (2438152, 1, 3),
  (2439852, 7, 6),
  (2440328, 7, 0),
  (2442487, 3, 3),
  (2443108, 7, 4),
  (2446881, 2, 4),
  (2447488, 1, 7),
  (2447713, 1, 0),
  (2447729, 4, 6),
  (2448203, 3, 3),
  (2449791, 4, 2),
  (2449916, 3, 2),
  (2451711, 2, 7),
  (2452064, 5, 2),
  (2453905, 1, 0),
  (2454290, 5, 6),
  (2456665, 2, 3),
  (2457271, 3, 6),
  (2457615, 0, 6),
  (2457694, 1, 6),
  (2459171, 2, 5),
  (2463020, 6, 0),
  (2463997, 1, 7),
  (2464428, 0, 7),
  (2466634, 1, 3),
  (2467236, 4, 7),
  (2467566, 5, 7),
  (2467964, 4, 6),
  (2469796, 5, 2),
  (2471046, 4, 3),
  (2473867, 3, 5),
  (2476392, 3, 7),
  (2480409, 2, 2),
  (2480412, 7, 0),
  (2480439, 6, 4),
  (2488578, 7, 6),
  (2488965, 4, 2),
  (2493024, 0, 4),
  (2494616, 7, 4),
  (2496258, 3, 3),
  (2496311, 4, 3),
  (2500137, 7, 7),
  (2506059, 1, 3),
  (2506313, 0, 4),
  (2507420, 2, 6),
  (2509660, 2, 3),
  (2510381, 6, 6),
  (2517305, 2, 3),
  (2522729, 7, 1),
  (2524000, 6, 4),
  (2526374, 5, 2),
  (2527183, 0, 0),
  (2530934, 3, 0),
  (2531382, 3, 1),
  (2531476, 7, 4),
  (2532242, 7, 4),
  (2534195, 1, 0),
  (2535065, 2, 3),
  (2536204, 4, 7),
  (2542182, 6, 7),
  (2543371, 3, 6),
  (2544594, 3, 7),
  (2546106, 3, 3),
  (2546395, 0, 3),
  (2548338, 3, 5),
  (2548511, 0, 3),
  (2550510, 6, 7),
  (2553601, 2, 6),
  (2554685, 3, 2),
  (2554888, 7, 7),
  (2559983, 0, 4),
  (2564860, 1, 7),
  (2566050, 6, 3),
  (2567416, 1, 3),
  (2569325, 1, 0),
  (2571983, 2, 7),
  (2575932, 2, 6),
  (2579807, 3, 7),
  (2581484, 1, 0),
  (2582466, 7, 3),
  (2582919, 5, 3),
  (2582963, 0, 0),
  (2583102, 5, 4),
  (2584681, 1, 3),
  (2586211, 2, 3),
  (2587296, 0, 0),
  (2587412, 2, 7),
  (2588427, 7, 3),
  (2588713, 6, 7),
  (2588732, 2, 5),
  (2592650, 0, 4),
  (2599398, 1, 3),
  (2600971, 3, 2),
  (2601812, 4, 2),
  (2602674, 4, 0),
  (2602960, 3, 6),
  (2603813, 7, 4),
  (2604860, 2, 1),
  (2605545, 3, 7),
  (2608833, 0, 0),
  (2609536, 5, 4),
  (2610233, 2, 6),
  (2611182, 0, 4),
  (2611543, 7, 5),
  (2613449, 1, 7),
  (2615221, 4, 2),
  (2616292, 3, 2),
  (2617881, 4, 6),
  (2619544, 0, 0),
  (2619931, 0, 0),
  (2620733, 3, 3),
  (2625657, 7, 1),
  (2625699, 6, 7),
  (2625701, 4, 2),
  (2626047, 3, 7),
  (2627698, 6, 7),
  (2631825, 7, 3),
  (2632010, 1, 2),
  (2634719, 2, 2),
  (2636989, 0, 3),
  (2638520, 1, 4),
  (2641911, 6, 6),
  (2643753, 1, 4),
  (2649402, 0, 3),
  (2650893, 6, 4),
  (2653122, 7, 3),
  (2653142, 7, 2),
  (2653432, 7, 6),
  (2657669, 6, 0),
  (2660905, 0, 3),
  (2663351, 0, 4),
  (2665363, 1, 3),
  (2668628, 1, 6),
  (2670091, 2, 3),
  (2671587, 1, 7),
  (2676021, 7, 7),
  (2679099, 4, 6),
  (2680038, 4, 7),
  (2682888, 4, 1),
  (2686632, 7, 3),
  (2686751, 5, 4),
  (2687462, 2, 7),
  (2688590, 3, 7),
  (2688748, 2, 5),
  (2690087, 4, 6),
  (2690668, 7, 5),
  (2691538, 3, 3),
  (2691763, 0, 4),
  (2692586, 1, 2),
  (2692636, 1, 4),
  (2694216, 6, 0),
  (2694303, 3, 2),
  (2695430, 4, 7),
  (2696677, 7, 7),
  (2696707, 5, 3),
  (2707925, 4, 7),
  (2708575, 6, 7),
  (2712819, 0, 7),
  (2717158, 7, 0),
  (2717605, 3, 6),
  (2717803, 4, 5),
  (2718110, 4, 5),
  (2718248, 5, 7),
  (2719678, 6, 0),
  (2719805, 4, 3),
  (2719851, 3, 4),
  (2720427, 5, 2),
  (2721174, 3, 1),
  (2721211, 3, 2),
  (2721236, 3, 2),
  (2725338, 3, 5),
  (2725729, 5, 7),
  (2727774, 7, 7),
  (2728351, 5, 3),
  (2731045, 1, 7),
  (2735228, 5, 6),
  (2735808, 2, 6),
  (2737806, 7, 4),
  (2740156, 0, 0),
  (2744182, 2, 1),
  (2745121, 0, 7),
  (2747187, 6, 4),
  (2747756, 1, 2),
  (2749293, 4, 3),
  (2749817, 6, 3),
  (2750184, 2, 7),
  (2750548, 1, 7),
  (2751362, 1, 6),
  (2751417, 5, 6),
  (2753723, 4, 2),
  (2755456, 6, 3),
  (2763296, 2, 7),
  (2764193, 6, 6),
  (2764754, 0, 7),
  (2766511, 6, 7),
  (2767271, 4, 7),
  (2769070, 4, 7),
  (2769341, 7, 2),
  (2773024, 0, 0),
  (2773225, 4, 3),
  (2774749, 1, 7),
  (2776075, 0, 1),
  (2777985, 4, 3),
  (2779015, 0, 0),
  (2782318, 7, 7),
  (2786210, 3, 5),
  (2788375, 5, 6),
  (2793416, 6, 7),
  (2795804, 5, 6),
  (2795841, 4, 7),
  (2797054, 7, 4),
  (2802740, 5, 1),
  (2803509, 2, 7),
  (2804759, 4, 3),
  (2805888, 3, 2),
  (2808995, 7, 7),
  (2810769, 6, 2),
  (2811628, 4, 7),
  (2811635, 0, 0),
  (2812661, 6, 7),
  (2814053, 7, 7),
  (2814826, 0, 3),
  (2816524, 0, 4),
  (2820080, 3, 7),
  (2824338, 7, 3),
  (2825090, 6, 0),
  (2833228, 4, 7),
  (2834405, 0, 7),
  (2838533, 5, 7),
  (2840020, 2, 3),
  (2843250, 5, 0),
  (2847034, 5, 2),
  (2847912, 1, 6),
  (2848562, 0, 2),
  (2849338, 1, 0),
  (2849741, 2, 7),
  (2850426, 7, 3),
  (2854412, 2, 3),
  (2856856, 1, 0),
  (2859411, 2, 3),
  (2863162, 4, 7),
  (2872377, 2, 3),
  (2872762, 1, 4),
  (2873603, 4, 4),
  (2875282, 5, 3),
  (2877377, 6, 4),
  (2883653, 6, 0),
  (2884328, 7, 3),
  (2884483, 4, 2),
  (2885865, 0, 5),
  (2885991, 0, 0),
  (2889777, 1, 5),
  (2890943, 2, 6),
  (2895983, 1, 0),
  (2898409, 6, 7),
  (2903048, 2, 7),
  (2910111, 7, 4),
  (2911098, 5, 7),
  (2911747, 5, 5),
  (2912682, 5, 3),
  (2913190, 7, 4),
  (2915350, 3, 7),
  (2915950, 3, 7),
  (2919199, 6, 7),
  (2922333, 1, 3),
  (2922613, 1, 4),
  (2925089, 7, 0),
  (2925382, 6, 4),
  (2927263, 0, 4),
  (2928940, 2, 7),
  (2930140, 7, 4),
  (2930494, 0, 3),
  (2931554, 6, 5),
  (2931958, 5, 4),
  (2933110, 2, 3),
  (2934041, 2, 4),
  (2940395, 2, 3),
  (2940422, 3, 7),
  (2941702, 5, 2),
  (2942931, 0, 3),
  (2943699, 4, 7),
  (2945356, 6, 4),
  (2948698, 4, 5),
  (2948916, 0, 0),
  (2950380, 4, 7),
  (2950545, 0, 5),
  (2951569, 7, 3),
  (2951744, 5, 4),
  (2953036, 7, 1),
  (2956150, 2, 6),
  (2956524, 6, 6),
  (2959718, 1, 7),
  (2962131, 6, 0),
  (2962359, 7, 6),
  (2962803, 3, 5),
  (2964183, 4, 2),
  (2964458, 7, 7),
  (2965946, 6, 0),
  (2966836, 7, 0),
  (2969072, 2, 5),
  (2969595, 1, 0),
  (2970388, 6, 1),
  (2971894, 4, 1),
  (2972669, 7, 3),
  (2973163, 2, 5),
  (2973604, 7, 0),
  (2974181, 7, 3),
  (2977408, 5, 3),
  (2977574, 5, 6),
  (2983496, 3, 6),
  (2983607, 3, 7),
  (2984325, 2, 7),
  (2989592, 1, 0),
  (2990616, 6, 0),
  (2992343, 3, 2),
  (2993556, 7, 3),
  (2998920, 6, 7),
  (3002185, 4, 6),
  (3002410, 1, 0),
  (3003616, 2, 7),
  (3007551, 1, 7),
  (3009296, 0, 5),
  (3011488, 2, 7),
  (3018722, 0, 4),
  (3022952, 1, 4),
  (3027027, 2, 6),
  (3030265, 6, 3),
  (3030615, 3, 2),
  (3030845, 1, 7),
  (3031560, 2, 3),
  (3035398, 6, 6),
  (3037332, 0, 0),
  (3038717, 5, 7),
  (3039276, 0, 1),
  (3039512, 6, 7),
  (3040260, 2, 7),
  (3044570, 0, 7),
  (3045878, 2, 4),
  (3046996, 5, 7),
  (3055955, 1, 7),
  (3056572, 0, 7),
  (3057674, 3, 3),
  (3058449, 6, 6),
  (3060816, 7, 3),
  (3061834, 6, 4),
  (3062940, 1, 5),
  (3065605, 2, 6),
  (3069387, 1, 4),
  (3069424, 5, 7),
  (3069891, 0, 5),
  (3070405, 0, 5),
  (3070521, 0, 7),
  (3070618, 1, 2),
  (3072797, 7, 3),
  (3073124, 4, 7),
  (3073679, 4, 2),
  (3074577, 0, 0),
  (3077724, 5, 3),
  (3078729, 7, 7),
  (3080213, 0, 7),
  (3080330, 2, 3),
  (3082805, 1, 0),
  (3083345, 1, 0),
  (3088927, 5, 2),
  (3093395, 1, 3),
  (3093981, 5, 1),
  (3096947, 5, 3),
  (3097821, 1, 0),
  (3101940, 3, 5),
  (3115405, 0, 4),
  (3118278, 3, 2),
  (3121680, 4, 2),
  (3123597, 3, 2),
  (3124683, 7, 7),
  (3132565, 2, 3),
  (3134406, 1, 7),
  (3135840, 6, 3),
  (3136298, 7, 6),
  (3141047, 2, 1),
  (3143211, 7, 4),
  (3146408, 6, 3),
  (3148007, 6, 3),
  (3148220, 7, 2),
  (3148834, 0, 4),
  (3149244, 7, 3),
  (3149567, 1, 4),
  (3149895, 4, 5),
  (3151840, 2, 3),
  (3152022, 5, 3),
  (3153427, 6, 7),
  (3154650, 1, 4),
  (3156283, 3, 3),
  (3156665, 7, 3),
  (3163716, 7, 0),
  (3165378, 5, 3),
  (3167667, 7, 0),
  (3167676, 7, 0),
  (3170090, 7, 7),
  (3171138, 6, 3),
  (3173743, 1, 4),
  (3173985, 6, 0),
  (3177318, 3, 7),
  (3178255, 4, 6),
  (3179662, 5, 2),
  (3182088, 1, 0),
  (3182165, 2, 5),
  (3182303, 6, 3),
  (3187417, 3, 1),
  (3188491, 1, 7),
  (3189079, 2, 5),
  (3193025, 7, 0),
  (3194820, 0, 3),
  (3195162, 3, 2),
  (3195703, 6, 3),
  (3197558, 1, 0),
  (3197667, 7, 0),
  (3198477, 3, 3),
  (3200768, 7, 0),
  (3200772, 5, 6),
  (3200783, 3, 6),
  (3201434, 2, 3),
  (3203371, 7, 2),
  (3203476, 0, 4),
  (3203486, 0, 4),
  (3203989, 6, 6),
  (3212889, 1, 0),
  (3214174, 2, 7),
  (3215263, 4, 7),
  (3217725, 6, 7),
  (3217821, 6, 3),
  (3219311, 2, 7),
  (3226482, 5, 7),
  (3228153, 7, 3),
  (3235611, 7, 6),
  (3236634, 3, 7),
  (3238364, 2, 2),
  (3238825, 2, 3),
  (3238865, 6, 6),
  (3238915, 2, 2),
  (3239166, 1, 7),
  (3239561, 6, 3),
  (3239745, 5, 0),
  (3243926, 4, 7),
  (3245577, 3, 3),
  (3246286, 4, 4),
  (3246553, 0, 7),
  (3246716, 2, 3),
  (3257370, 6, 3),
  (3258331, 2, 0),
  (3262222, 7, 0),
  (3263221, 2, 1),
  (3268014, 7, 0),
  (3268327, 0, 3),
  (3270972, 4, 5),
  (3275249, 7, 2),
  (3275492, 5, 6),
  (3276146, 1, 0),
  (3276173, 5, 2),
  (3278704, 4, 2),
  (3284708, 0, 3),
  (3290756, 5, 2),
  (3291386, 4, 2),
  (3296725, 6, 7),
  (3298083, 3, 5),
  (3298176, 0, 7),
  (3298483, 4, 7),
  (3300949, 6, 6),
  (3301089, 5, 3),
  (3301114, 4, 3),
  (3301276, 7, 6),
  (3304406, 4, 7),
  (3306300, 2, 2),
  (3307816, 2, 1),
  (3308977, 2, 3),
  (3309739, 2, 2),
  (3316288, 2, 3),
  (3318325, 6, 0),
  (3318672, 7, 4),
  (3323481, 2, 6),
  (3323908, 6, 4),
  (3324031, 5, 3),
  (3324164, 7, 0),
  (3326574, 4, 5),
  (3328721, 3, 4),
  (3329690, 4, 7),
  (3330872, 2, 3),
  (3335451, 5, 5),
  (3336601, 0, 0),
  (3339124, 7, 7),
  (3344712, 1, 2),
  (3349051, 1, 7),
  (3350398, 3, 6),
  (3350411, 3, 7),
  (3351601, 4, 7),
  (3352849, 7, 6),
  (3357242, 4, 7),
  (3358707, 6, 7),
  (3360635, 4, 6),
  (3361082, 0, 0),
  (3365115, 7, 4),
  (3366030, 6, 6),
  (3371484, 1, 3),
  (3377140, 3, 7),
  (3378341, 7, 0),
  (3381928, 4, 3),
  (3385859, 6, 7),
  (3385918, 7, 4),
  (3386677, 6, 3),
  (3387927, 6, 6),
  (3388439, 0, 6),
  (3388716, 0, 7),
  (3390271, 0, 7),
  (3390335, 1, 4),
  (3391105, 1, 3),
  (3397262, 0, 0),
  (3401676, 0, 6),
  (3402108, 0, 0),
  (3402145, 6, 4),
  (3408366, 7, 0),
  (3413422, 4, 7),
  (3413947, 2, 7),
  (3414034, 5, 7),
  (3414817, 0, 0),
  (3415393, 1, 0),
  (3415842, 3, 1),
  (3417203, 3, 7),
  (3419603, 4, 5),
  (3422032, 7, 5),
  (3426864, 5, 3),
  (3427763, 1, 7),
  (3431615, 6, 7),
  (3433445, 4, 3),
  (3435195, 7, 7),
  (3435991, 3, 2),
  (3437529, 0, 7),
  (3439442, 5, 6),
  (3442195, 4, 1),
  (3442404, 7, 6),
  (3443225, 5, 2),
  (3444716, 1, 6),
  (3448904, 0, 6),
  (3449329, 0, 3),
  (3449999, 5, 0),
  (3457348, 1, 7),
  (3457432, 2, 7),
  (3459897, 6, 7),
  (3461229, 7, 6),
  (3461509, 5, 6),
  (3465891, 4, 6),
  (3467773, 5, 6),
  (3468482, 3, 7),
  (3470000, 5, 7),
  (3476578, 5, 5),
  (3477222, 0, 3),
  (3477884, 5, 2),
  (3478034, 4, 1),
  (3479697, 2, 3),
  (3483792, 6, 0),
  (3487616, 1, 7),
  (3488784, 3, 2),
  (3489896, 2, 3),
  (3491564, 1, 6),
  (3493106, 3, 3),
  (3500867, 4, 1),
  (3504804, 0, 4),
  (3511135, 2, 2),
  (3511689, 2, 6),
  (3511906, 5, 1),
  (3511938, 4, 7),
  (3514203, 0, 7),
  (3514542, 0, 0),
  (3514997, 1, 7),
  (3517188, 0, 4),
  (3522927, 5, 3),
  (3527899, 2, 6),
  (3533260, 0, 0),
  (3533314, 2, 2),
  (3534478, 3, 5),
  (3536841, 7, 5),
  (3537310, 2, 2),
  (3538022, 7, 5),
  (3538471, 5, 5),
  (3540012, 1, 0),
  (3540032, 5, 7),
  (3542178, 0, 0),
  (3544731, 2, 3),
  (3548980, 6, 0),
  (3562396, 0, 6),
  (3568028, 5, 6),
  (3574267, 4, 7),
  (3575884, 2, 2),
  (3577100, 5, 7),
  (3577374, 5, 5),
  (3577460, 3, 1),
  (3577522, 0, 4),
  (3578961, 0, 4),
  (3581686, 3, 6),
  (3587136, 6, 0),
  (3588347, 1, 7),
  (3589765, 2, 6),
  (3590402, 0, 0),
  (3593066, 0, 0),
  (3595107, 7, 7),
  (3597536, 6, 0),
  (3598065, 1, 3),
])
