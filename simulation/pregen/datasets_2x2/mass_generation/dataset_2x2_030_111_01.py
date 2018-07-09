from util import *
schedule = deque([
  (764, 11, 0),
  (5241, 8, 7),
  (5558, 2, 18),
  (6729, 2, 7),
  (7126, 10, 15),
  (8199, 8, 8),
  (8617, 11, 18),
  (11932, 7, 13),
  (12781, 2, 8),
  (13431, 0, 0),
  (14450, 8, 18),
  (15290, 3, 3),
  (16972, 6, 17),
  (17937, 8, 7),
  (22251, 1, 0),
  (22668, 11, 11),
  (26691, 1, 22),
  (37213, 1, 0),
  (39797, 3, 0),
  (41837, 10, 0),
  (45639, 5, 10),
  (45672, 3, 16),
  (46173, 8, 18),
  (46182, 10, 0),
  (46190, 6, 10),
  (47627, 8, 4),
  (47804, 0, 0),
  (49121, 11, 0),
  (50592, 2, 7),
  (52166, 1, 11),
  (53029, 10, 0),
  (57192, 11, 0),
  (58768, 1, 0),
  (64781, 3, 16),
  (65496, 8, 10),
  (72458, 4, 10),
  (74064, 11, 18),
  (75148, 4, 18),
  (76898, 0, 18),
  (77089, 9, 9),
  (78010, 10, 0),
  (79918, 1, 0),
  (84297, 2, 7),
  (84556, 3, 7),
  (87187, 6, 10),
  (92833, 4, 10),
  (96943, 11, 0),
  (100333, 7, 22),
  (100685, 11, 0),
  (101543, 10, 0),
  (101597, 2, 3),
  (106252, 6, 10),
  (106760, 11, 0),
  (108022, 5, 10),
  (109269, 7, 10),
  (112304, 4, 18),
  (113045, 1, 14),
  (114531, 9, 8),
  (117717, 8, 7),
  (120042, 4, 13),
  (126407, 7, 10),
  (129922, 3, 7),
  (130011, 11, 6),
  (131635, 10, 6),
  (132567, 3, 3),
  (132886, 6, 10),
  (132918, 4, 14),
  (136807, 6, 10),
  (137453, 4, 17),
  (138892, 8, 3),
  (139672, 7, 10),
  (141394, 1, 11),
  (153202, 9, 15),
  (159704, 5, 10),
  (159722, 7, 10),
  (161746, 2, 3),
  (166290, 7, 10),
  (168095, 4, 10),
  (168268, 4, 13),
  (170541, 3, 8),
  (172165, 10, 0),
  (172221, 11, 14),
  (173986, 3, 3),
  (174900, 9, 15),
  (175768, 10, 0),
  (176416, 2, 3),
  (177732, 5, 10),
  (178621, 10, 0),
  (178877, 7, 6),
  (182274, 6, 10),
  (183000, 9, 8),
  (184523, 0, 0),
  (185126, 0, 4),
  (186463, 5, 2),
  (186635, 6, 10),
  (187664, 8, 18),
  (187817, 5, 10),
  (188259, 11, 11),
  (191677, 1, 11),
  (192062, 1, 10),
  (192452, 9, 3),
  (192716, 2, 12),
  (194779, 4, 17),
  (196901, 0, 0),
  (198294, 0, 1),
  (199726, 9, 16),
  (203275, 6, 10),
  (203849, 3, 9),
  (205028, 8, 0),
  (207229, 8, 3),
  (212019, 9, 3),
  (213109, 11, 0),
  (214847, 10, 0),
  (215433, 10, 0),
  (216749, 0, 11),
  (217816, 6, 14),
  (218202, 2, 13),
  (219560, 9, 7),
  (223147, 5, 10),
  (223239, 8, 0),
  (226764, 4, 14),
  (230474, 11, 17),
  (233559, 5, 17),
  (234046, 4, 10),
  (238545, 10, 3),
  (240745, 11, 11),
  (243838, 3, 6),
  (245283, 0, 0),
  (248341, 10, 0),
  (248903, 4, 2),
  (251236, 0, 11),
  (252727, 5, 22),
  (255838, 1, 11),
  (256986, 0, 11),
  (257913, 0, 11),
  (259051, 0, 0),
  (260018, 6, 10),
  (260254, 5, 1),
  (262014, 1, 22),
  (262663, 0, 0),
  (263003, 10, 0),
  (265282, 0, 10),
  (270356, 4, 17),
  (270660, 1, 22),
  (272238, 7, 10),
  (275814, 1, 0),
  (276222, 11, 0),
  (277043, 1, 0),
  (277317, 7, 22),
  (277600, 5, 10),
  (278410, 4, 18),
  (280043, 2, 2),
  (284974, 9, 14),
  (285007, 8, 10),
  (293729, 7, 10),
  (294985, 6, 2),
  (298029, 11, 11),
  (299121, 10, 0),
  (302458, 9, 16),
  (302765, 11, 0),
  (303758, 10, 7),
  (304853, 1, 18),
  (305151, 5, 22),
  (318607, 8, 0),
  (320727, 5, 9),
  (320866, 0, 0),
  (324717, 10, 0),
  (326572, 10, 0),
  (326924, 3, 9),
  (328824, 6, 17),
  (333116, 5, 9),
  (334819, 4, 10),
  (337880, 1, 0),
  (338716, 2, 10),
  (339422, 6, 10),
  (339671, 6, 11),
  (345019, 8, 7),
  (347658, 4, 18),
  (348850, 11, 0),
  (353285, 4, 10),
  (358948, 8, 18),
  (360489, 8, 17),
  (360780, 6, 17),
  (366440, 7, 10),
  (369840, 2, 3),
  (370076, 5, 10),
  (378093, 5, 8),
  (379280, 6, 10),
  (381834, 11, 0),
  (383094, 5, 10),
  (383559, 7, 10),
  (383875, 6, 13),
  (386911, 7, 10),
  (387686, 3, 10),
  (391561, 11, 11),
  (391696, 4, 10),
  (394136, 1, 10),
  (395194, 6, 10),
  (396250, 6, 17),
  (398569, 7, 10),
  (402858, 8, 3),
  (403663, 3, 7),
  (403926, 1, 12),
  (406519, 3, 7),
  (406662, 3, 14),
  (407525, 5, 10),
  (407873, 5, 10),
  (410452, 0, 18),
  (412310, 2, 10),
  (415564, 11, 0),
  (415607, 3, 7),
  (415694, 8, 7),
  (420822, 2, 7),
  (421377, 3, 3),
  (424930, 8, 4),
  (425383, 11, 17),
  (427119, 3, 9),
  (431243, 1, 14),
  (433527, 8, 10),
  (434221, 8, 5),
  (437296, 1, 0),
  (437740, 11, 11),
  (439184, 11, 0),
  (441751, 5, 10),
  (444797, 6, 22),
  (446753, 11, 0),
  (447560, 2, 10),
  (452612, 4, 0),
  (452820, 2, 13),
  (453017, 7, 10),
  (453116, 6, 20),
  (454653, 3, 7),
  (458167, 11, 19),
  (460617, 9, 17),
  (461148, 10, 0),
  (462129, 1, 0),
  (466369, 0, 18),
  (466983, 6, 10),
  (473755, 1, 7),
  (474805, 1, 17),
  (475247, 6, 17),
  (475362, 4, 20),
  (476626, 11, 11),
  (477533, 6, 10),
  (477563, 11, 0),
  (478127, 6, 18),
  (479748, 11, 11),
  (480937, 7, 18),
  (486519, 9, 7),
  (489120, 2, 15),
  (493651, 5, 10),
  (496719, 6, 17),
  (497606, 4, 10),
  (498178, 10, 0),
  (500211, 11, 0),
  (501569, 1, 7),
  (504198, 10, 0),
  (505263, 2, 7),
  (507807, 2, 16),
  (512365, 8, 7),
  (515485, 2, 14),
  (519562, 6, 17),
  (520257, 2, 7),
  (520759, 11, 0),
  (520932, 5, 10),
  (522722, 2, 13),
  (524832, 5, 22),
  (527106, 7, 17),
  (528858, 5, 10),
  (529939, 10, 10),
  (531239, 0, 10),
  (532333, 2, 3),
  (532472, 1, 10),
  (534114, 7, 10),
  (534330, 8, 13),
  (537359, 5, 10),
  (537938, 4, 10),
  (538839, 8, 17),
  (538901, 10, 0),
  (540647, 3, 2),
  (540743, 11, 0),
  (541587, 5, 10),
  (545660, 11, 0),
  (547968, 10, 0),
  (548673, 1, 6),
  (549576, 3, 3),
  (552710, 11, 0),
  (554814, 7, 10),
  (554956, 2, 9),
  (555508, 2, 3),
  (556238, 4, 9),
  (556940, 2, 7),
  (567726, 3, 7),
  (570402, 7, 22),
  (573852, 0, 18),
  (582511, 5, 2),
  (583180, 1, 18),
  (584260, 0, 0),
  (585126, 3, 15),
  (586446, 8, 5),
  (586722, 7, 17),
  (586824, 6, 10),
  (588998, 9, 13),
  (589672, 2, 7),
  (590323, 7, 10),
  (591806, 3, 7),
  (592223, 0, 0),
  (594306, 11, 0),
  (597095, 3, 8),
  (598899, 4, 18),
  (599063, 9, 7),
  (609426, 0, 0),
  (611843, 10, 0),
  (613511, 2, 13),
  (615368, 4, 10),
  (620078, 3, 9),
  (621567, 2, 6),
  (622564, 6, 9),
  (623040, 8, 10),
  (623518, 0, 11),
  (623625, 5, 22),
  (624574, 1, 0),
  (627621, 6, 10),
  (629045, 6, 10),
  (629254, 5, 9),
  (635604, 2, 3),
  (636668, 5, 22),
  (638192, 10, 10),
  (640148, 0, 0),
  (641196, 5, 10),
  (643239, 8, 0),
  (643259, 11, 11),
  (646370, 6, 10),
  (647100, 0, 3),
  (648568, 2, 13),
  (655070, 1, 0),
  (656265, 9, 7),
  (656504, 6, 10),
  (658233, 10, 18),
  (660131, 1, 0),
  (661488, 7, 10),
  (661722, 2, 7),
  (670915, 2, 13),
  (672989, 1, 0),
  (673574, 9, 3),
  (675341, 6, 18),
  (675767, 7, 10),
  (678042, 1, 0),
  (679201, 7, 12),
  (679228, 10, 19),
  (680023, 9, 0),
  (680105, 2, 3),
  (688155, 3, 18),
  (689302, 1, 4),
  (690951, 10, 0),
  (698976, 3, 10),
  (701244, 10, 0),
  (701545, 2, 5),
  (702432, 7, 10),
  (702776, 3, 16),
  (703270, 4, 10),
  (708717, 5, 5),
  (712080, 7, 10),
  (712307, 10, 22),
  (714137, 4, 17),
  (714445, 2, 10),
  (720199, 6, 9),
  (721342, 11, 0),
  (721363, 1, 0),
  (723529, 0, 0),
  (723553, 9, 3),
  (724608, 11, 18),
  (727160, 0, 14),
  (728569, 0, 18),
  (731854, 10, 11),
  (732699, 6, 16),
  (733945, 11, 18),
  (734327, 0, 0),
  (737797, 3, 13),
  (743431, 1, 11),
  (743726, 9, 13),
  (744109, 4, 22),
  (750577, 5, 17),
  (754048, 0, 0),
  (754051, 9, 4),
  (755545, 0, 0),
  (756630, 0, 2),
  (757307, 5, 10),
  (757328, 0, 11),
  (757447, 2, 6),
  (760987, 0, 10),
  (762640, 4, 10),
  (762676, 7, 10),
  (763264, 11, 11),
  (763662, 10, 0),
  (764100, 0, 11),
  (765873, 8, 10),
  (774110, 7, 2),
  (776296, 11, 3),
  (776389, 8, 18),
  (778607, 5, 3),
  (780075, 11, 0),
  (781399, 8, 10),
  (781690, 2, 9),
  (781853, 6, 10),
  (789139, 7, 10),
  (790409, 6, 10),
  (791599, 10, 0),
  (791978, 4, 10),
  (792497, 4, 7),
  (794321, 8, 3),
  (794589, 0, 11),
  (796620, 10, 0),
  (798256, 9, 7),
  (803336, 4, 10),
  (811265, 3, 3),
  (814117, 10, 0),
  (816195, 1, 0),
  (817943, 4, 10),
  (819125, 8, 3),
  (819706, 11, 0),
  (820526, 2, 13),
  (821128, 4, 18),
  (821757, 1, 0),
  (821969, 1, 0),
  (824435, 2, 9),
  (827086, 11, 0),
  (829520, 7, 10),
  (833612, 4, 17),
  (834748, 2, 0),
  (835493, 0, 4),
  (837811, 0, 0),
  (841592, 8, 7),
  (844486, 7, 21),
  (850909, 7, 21),
  (852856, 7, 21),
  (856092, 2, 10),
  (856136, 7, 17),
  (857029, 4, 10),
  (857964, 5, 10),
  (860711, 6, 21),
  (865796, 4, 21),
  (869718, 10, 2),
  (870483, 9, 3),
  (871361, 7, 17),
  (875144, 5, 14),
  (876376, 7, 9),
  (879317, 2, 7),
  (883434, 2, 5),
  (887448, 11, 10),
  (888245, 4, 10),
  (890851, 4, 18),
  (891000, 8, 12),
  (891509, 3, 10),
  (891638, 5, 17),
  (892685, 5, 10),
  (895657, 5, 10),
  (896961, 0, 3),
  (898056, 7, 10),
  (898534, 11, 0),
  (900256, 7, 10),
  (902681, 9, 4),
  (903804, 8, 8),
  (905042, 4, 21),
  (906789, 10, 11),
  (914779, 4, 21),
  (923774, 11, 11),
  (929317, 6, 10),
  (929919, 8, 7),
  (930730, 9, 11),
  (933104, 11, 0),
  (938443, 8, 7),
  (938891, 3, 3),
  (943830, 7, 10),
  (944692, 5, 17),
  (944912, 0, 0),
  (945241, 2, 7),
  (947280, 4, 2),
  (948033, 10, 0),
  (948625, 9, 11),
  (951629, 9, 7),
  (957467, 8, 17),
  (958471, 5, 17),
  (958691, 11, 18),
  (959186, 11, 0),
  (959196, 0, 0),
  (959499, 8, 7),
  (969152, 11, 11),
  (971079, 9, 18),
  (974675, 6, 5),
  (976961, 2, 3),
  (979050, 11, 5),
  (979087, 7, 21),
  (979248, 1, 0),
  (980590, 7, 10),
  (980703, 11, 0),
  (981238, 7, 6),
  (982603, 9, 10),
  (983652, 7, 10),
  (985185, 4, 10),
  (985324, 3, 10),
  (985629, 0, 0),
  (985630, 2, 18),
  (985951, 4, 19),
  (988140, 8, 0),
  (991083, 11, 11),
  (991583, 0, 10),
  (995501, 7, 4),
  (996740, 6, 21),
  (1000446, 11, 0),
  (1003555, 5, 10),
  (1006474, 2, 3),
  (1008236, 6, 10),
  (1009050, 5, 9),
  (1010827, 1, 0),
  (1011273, 9, 12),
  (1013606, 8, 3),
  (1019100, 8, 3),
  (1032073, 5, 6),
  (1032199, 6, 19),
  (1038656, 8, 7),
  (1039940, 10, 18),
  (1040735, 3, 1),
  (1045975, 1, 6),
  (1050593, 8, 0),
  (1051493, 1, 11),
  (1053306, 7, 17),
  (1057949, 5, 9),
  (1058335, 9, 4),
  (1058787, 10, 10),
  (1061855, 8, 4),
  (1063019, 1, 0),
  (1065346, 4, 10),
  (1066244, 4, 10),
  (1066606, 9, 3),
  (1067616, 5, 10),
  (1070018, 10, 10),
  (1070542, 10, 0),
  (1073723, 4, 10),
  (1074644, 3, 3),
  (1076772, 0, 0),
  (1077748, 3, 7),
  (1081124, 5, 17),
  (1081866, 8, 0),
  (1083131, 5, 6),
  (1083917, 5, 22),
  (1086854, 2, 0),
  (1089639, 6, 10),
  (1094800, 11, 0),
  (1095308, 11, 5),
  (1096696, 7, 17),
  (1099050, 11, 11),
  (1099729, 7, 10),
  (1100446, 5, 22),
  (1102303, 11, 22),
  (1106005, 3, 4),
  (1106821, 3, 1),
  (1107211, 6, 10),
  (1108174, 11, 0),
  (1108255, 6, 10),
  (1108310, 1, 11),
  (1111911, 10, 0),
  (1118338, 4, 9),
  (1118965, 10, 0),
  (1120098, 1, 19),
  (1120831, 7, 21),
  (1121052, 6, 10),
  (1123363, 4, 10),
  (1126090, 2, 1),
  (1126508, 6, 10),
  (1126528, 2, 7),
  (1129899, 7, 3),
  (1130002, 2, 12),
  (1132746, 4, 17),
  (1133198, 4, 17),
  (1133638, 1, 0),
  (1137597, 4, 17),
  (1138127, 11, 0),
  (1141458, 6, 10),
  (1142871, 4, 10),
  (1144329, 0, 11),
  (1144826, 6, 10),
  (1144845, 11, 10),
  (1145187, 7, 6),
  (1145377, 2, 1),
  (1147469, 8, 1),
  (1151870, 9, 18),
  (1151923, 7, 14),
  (1152601, 1, 10),
  (1152781, 11, 0),
  (1153657, 3, 10),
  (1158022, 6, 9),
  (1164338, 8, 10),
  (1166006, 2, 4),
  (1166431, 9, 9),
  (1166581, 2, 7),
  (1166612, 9, 14),
  (1170669, 3, 4),
  (1177749, 8, 7),
  (1179147, 0, 11),
  (1182370, 10, 0),
  (1183060, 11, 0),
  (1186903, 8, 7),
  (1188729, 10, 15),
  (1189137, 0, 0),
  (1191185, 5, 10),
  (1191574, 4, 10),
  (1196375, 2, 18),
  (1196841, 10, 0),
  (1197401, 0, 18),
  (1197742, 6, 20),
  (1198097, 6, 10),
  (1199190, 1, 0),
  (1199425, 3, 0),
  (1200725, 6, 10),
  (1200918, 8, 11),
  (1201511, 0, 0),
  (1204660, 4, 10),
  (1213099, 3, 7),
  (1213711, 6, 5),
  (1215446, 3, 13),
  (1219916, 5, 7),
  (1220988, 8, 10),
  (1221295, 5, 22),
  (1221301, 1, 11),
  (1221832, 8, 3),
  (1221891, 0, 3),
  (1227318, 2, 18),
  (1228106, 9, 0),
  (1229118, 1, 11),
  (1229412, 6, 6),
  (1230011, 11, 18),
  (1231694, 9, 3),
  (1232529, 8, 4),
  (1233619, 5, 10),
  (1242056, 4, 9),
  (1243758, 4, 10),
  (1244883, 6, 10),
  (1245642, 2, 17),
  (1247297, 11, 0),
  (1248305, 8, 12),
  (1249706, 7, 16),
  (1253689, 10, 20),
  (1254494, 11, 0),
  (1255803, 3, 10),
  (1263718, 7, 6),
  (1269040, 10, 0),
  (1269143, 3, 14),
  (1269729, 5, 6),
  (1269978, 3, 6),
  (1269990, 0, 0),
  (1270670, 8, 16),
  (1274506, 3, 5),
  (1276319, 1, 0),
  (1276951, 6, 17),
  (1277950, 7, 9),
  (1278304, 4, 17),
  (1282525, 2, 10),
  (1289990, 4, 10),
  (1291206, 0, 11),
  (1296746, 0, 11),
  (1300090, 6, 13),
  (1301661, 6, 21),
  (1302737, 1, 0),
  (1303486, 4, 10),
  (1304750, 1, 0),
  (1305176, 6, 10),
  (1308201, 3, 15),
  (1309121, 11, 0),
  (1311452, 0, 20),
  (1314100, 6, 10),
  (1315656, 6, 22),
  (1316939, 7, 10),
  (1318082, 5, 10),
  (1320129, 7, 22),
  (1320389, 5, 10),
  (1324879, 7, 10),
  (1325748, 9, 3),
  (1326875, 0, 11),
  (1327115, 10, 11),
  (1327443, 8, 5),
  (1329503, 8, 12),
  (1332955, 11, 10),
  (1333383, 7, 10),
  (1336490, 9, 3),
  (1338065, 1, 18),
  (1339570, 9, 13),
  (1347428, 2, 10),
  (1348858, 1, 0),
  (1348881, 4, 17),
  (1350064, 11, 11),
  (1359952, 1, 0),
  (1360293, 7, 10),
  (1360469, 1, 0),
  (1363530, 6, 10),
  (1364337, 4, 10),
  (1364522, 11, 17),
  (1368230, 5, 10),
  (1368444, 6, 16),
  (1371229, 11, 0),
  (1372574, 3, 7),
  (1372599, 7, 10),
  (1374692, 3, 7),
  (1381096, 9, 13),
  (1383203, 7, 10),
  (1390080, 3, 3),
  (1393805, 11, 18),
  (1395934, 1, 11),
  (1396035, 1, 0),
  (1396339, 3, 17),
  (1398256, 1, 0),
  (1400998, 11, 0),
  (1407118, 10, 18),
  (1408569, 8, 9),
  (1410345, 9, 13),
  (1413369, 9, 13),
  (1414085, 3, 3),
  (1417635, 6, 9),
  (1419559, 6, 10),
  (1419614, 7, 5),
  (1421243, 8, 3),
  (1421310, 7, 10),
  (1427036, 4, 10),
  (1427147, 8, 3),
  (1428073, 3, 1),
  (1429997, 10, 11),
  (1430181, 0, 6),
  (1431683, 8, 7),
  (1431922, 7, 17),
  (1434450, 8, 9),
  (1434672, 2, 1),
  (1434853, 0, 1),
  (1437612, 1, 0),
  (1439095, 2, 18),
  (1439293, 6, 10),
  (1440489, 6, 10),
  (1441851, 8, 7),
  (1443217, 7, 17),
  (1443405, 1, 18),
  (1446524, 4, 10),
  (1446563, 11, 15),
  (1447100, 4, 10),
  (1448765, 10, 11),
  (1451660, 7, 16),
  (1453624, 9, 7),
  (1454183, 8, 3),
  (1456320, 3, 4),
  (1460611, 11, 0),
  (1461256, 2, 3),
  (1468206, 6, 10),
  (1469481, 4, 17),
  (1472676, 0, 0),
  (1478000, 6, 22),
  (1486551, 9, 3),
  (1490914, 7, 8),
  (1491817, 2, 13),
  (1491862, 6, 3),
  (1493099, 7, 2),
  (1494685, 10, 11),
  (1494924, 4, 19),
  (1496303, 7, 10),
  (1499435, 8, 13),
  (1500009, 2, 7),
  (1500493, 9, 10),
  (1500636, 7, 8),
  (1500837, 6, 11),
  (1508369, 6, 10),
  (1514323, 4, 10),
  (1518109, 8, 17),
  (1518644, 0, 0),
  (1518668, 1, 0),
  (1525908, 9, 13),
  (1529178, 8, 17),
  (1533337, 0, 0),
  (1538106, 10, 11),
  (1540551, 8, 7),
  (1540931, 0, 19),
  (1546246, 2, 7),
  (1546349, 1, 0),
  (1547703, 4, 10),
  (1549660, 4, 10),
  (1551602, 1, 0),
  (1552242, 7, 10),
  (1554186, 2, 4),
  (1555252, 3, 3),
  (1557461, 7, 21),
  (1559665, 10, 11),
  (1569806, 7, 10),
  (1570519, 7, 17),
  (1571596, 2, 16),
  (1571868, 11, 0),
  (1573990, 1, 1),
  (1577657, 3, 7),
  (1579198, 8, 14),
  (1579202, 9, 0),
  (1581128, 7, 9),
  (1581383, 8, 16),
  (1585025, 0, 10),
  (1585644, 11, 0),
  (1586583, 1, 0),
  (1588660, 8, 16),
  (1589485, 2, 10),
  (1590882, 5, 6),
  (1592126, 0, 11),
  (1597670, 3, 10),
  (1599069, 5, 7),
  (1601991, 9, 12),
  (1603362, 0, 6),
  (1603506, 8, 7),
  (1604087, 10, 16),
  (1607063, 7, 10),
  (1609501, 5, 10),
  (1609606, 8, 4),
  (1616641, 9, 13),
  (1618573, 9, 18),
  (1619405, 7, 10),
  (1621005, 11, 22),
  (1623336, 3, 4),
  (1630974, 9, 13),
  (1632114, 2, 4),
  (1634819, 6, 17),
  (1637129, 0, 0),
  (1639973, 8, 4),
  (1641348, 0, 0),
  (1643332, 10, 0),
  (1643572, 10, 10),
  (1645746, 5, 10),
  (1646735, 8, 8),
  (1658758, 1, 0),
  (1661437, 9, 10),
  (1672718, 11, 0),
  (1678407, 6, 9),
  (1678790, 3, 18),
  (1680016, 0, 11),
  (1680116, 7, 10),
  (1683569, 8, 10),
  (1684239, 5, 2),
  (1687356, 9, 13),
  (1689542, 8, 3),
  (1691308, 3, 14),
  (1691550, 11, 0),
  (1693317, 1, 0),
  (1703154, 11, 0),
  (1703372, 10, 22),
  (1704750, 7, 10),
  (1710955, 3, 13),
  (1712736, 10, 8),
  (1714789, 9, 8),
  (1716508, 4, 21),
  (1718252, 7, 17),
  (1719876, 7, 22),
  (1724662, 11, 0),
  (1725991, 1, 6),
  (1728582, 6, 14),
  (1728781, 2, 3),
  (1732602, 7, 10),
  (1733624, 2, 2),
  (1734856, 8, 3),
  (1738676, 2, 3),
  (1741087, 0, 0),
  (1746625, 1, 11),
  (1751381, 4, 10),
  (1757414, 6, 10),
  (1757815, 9, 7),
  (1758839, 0, 0),
  (1761563, 6, 17),
  (1764132, 7, 17),
  (1765505, 7, 5),
  (1765958, 3, 7),
  (1766020, 7, 17),
  (1767205, 8, 14),
  (1777106, 10, 20),
  (1779809, 3, 4),
  (1782584, 4, 10),
  (1782650, 9, 4),
  (1782855, 10, 10),
  (1785001, 6, 10),
  (1788828, 1, 0),
  (1790404, 11, 0),
  (1790708, 7, 10),
  (1790799, 6, 10),
  (1791499, 6, 10),
  (1792031, 9, 2),
  (1797098, 0, 0),
  (1799400, 11, 11),
  (1799534, 0, 0),
  (1799563, 3, 18),
  (1799669, 5, 17),
  (1801207, 11, 0),
  (1801733, 11, 1),
  (1803225, 3, 10),
  (1805671, 7, 10),
  (1806254, 9, 7),
  (1807634, 9, 10),
  (1808178, 0, 6),
  (1809229, 0, 0),
  (1810902, 3, 3),
  (1813588, 10, 0),
  (1815227, 4, 10),
  (1817838, 7, 10),
  (1818785, 7, 10),
  (1821894, 7, 21),
  (1825096, 8, 0),
  (1826324, 5, 10),
  (1826598, 5, 10),
  (1827895, 7, 17),
  (1828224, 5, 10),
  (1828758, 2, 4),
  (1829862, 4, 6),
  (1830293, 3, 7),
  (1834032, 11, 22),
  (1836105, 8, 7),
  (1841108, 4, 10),
  (1841745, 10, 0),
  (1842351, 6, 10),
  (1844260, 4, 10),
  (1846547, 5, 10),
  (1846778, 5, 21),
  (1848833, 6, 10),
  (1849820, 11, 10),
  (1853123, 1, 0),
  (1855789, 5, 10),
  (1859461, 1, 18),
  (1859470, 1, 3),
  (1859493, 4, 5),
  (1862438, 10, 0),
  (1862578, 6, 17),
  (1863175, 8, 7),
  (1863321, 0, 11),
  (1863669, 7, 10),
  (1868237, 0, 0),
  (1868747, 8, 3),
  (1868758, 5, 10),
  (1876319, 1, 0),
  (1880115, 10, 0),
  (1882150, 10, 4),
  (1883739, 10, 0),
  (1884181, 10, 0),
  (1884924, 7, 10),
  (1885057, 3, 7),
  (1887748, 0, 22),
  (1896627, 7, 10),
  (1913221, 2, 6),
  (1913416, 1, 0),
  (1913521, 1, 10),
  (1917549, 5, 10),
  (1919242, 9, 15),
  (1922053, 6, 17),
  (1922747, 6, 10),
  (1922898, 11, 0),
  (1925043, 0, 0),
  (1925098, 7, 10),
  (1926908, 8, 7),
  (1927933, 5, 21),
  (1930015, 3, 3),
  (1935384, 7, 10),
  (1937263, 9, 0),
  (1938788, 9, 15),
  (1938839, 5, 10),
  (1942067, 2, 7),
  (1942567, 10, 3),
  (1944585, 0, 0),
  (1944760, 2, 3),
  (1945883, 2, 7),
  (1947300, 10, 0),
  (1947339, 5, 9),
  (1955771, 5, 21),
  (1957478, 5, 10),
  (1958770, 1, 0),
  (1962118, 6, 10),
  (1962941, 5, 2),
  (1964281, 9, 7),
  (1964983, 1, 0),
  (1975110, 11, 11),
  (1975615, 2, 12),
  (1976677, 4, 17),
  (1983046, 7, 10),
  (1984806, 9, 0),
  (1985804, 0, 0),
  (1995113, 1, 0),
  (1995778, 0, 0),
  (1996081, 6, 10),
  (2002805, 10, 11),
  (2005179, 8, 3),
  (2009141, 3, 7),
  (2009498, 8, 10),
  (2011328, 1, 0),
  (2012062, 9, 5),
  (2014375, 10, 19),
  (2014633, 0, 11),
  (2019740, 10, 11),
  (2021220, 11, 14),
  (2022794, 1, 0),
  (2024425, 0, 0),
  (2024758, 4, 21),
  (2026211, 7, 9),
  (2027488, 11, 22),
  (2029251, 7, 9),
  (2029301, 1, 2),
  (2031040, 10, 0),
  (2034354, 0, 9),
  (2036674, 10, 11),
  (2037806, 9, 3),
  (2039985, 5, 10),
  (2043479, 10, 0),
  (2044123, 8, 18),
  (2044595, 4, 10),
  (2045032, 9, 4),
  (2054273, 2, 13),
  (2058291, 11, 0),
  (2059032, 11, 6),
  (2059953, 9, 18),
  (2060085, 2, 7),
  (2060240, 3, 8),
  (2062099, 3, 16),
  (2063207, 10, 0),
  (2068538, 2, 4),
  (2069835, 7, 10),
  (2074585, 4, 10),
  (2074892, 1, 17),
  (2076972, 5, 17),
  (2077630, 0, 0),
  (2081244, 8, 4),
  (2082444, 10, 17),
  (2086447, 8, 7),
  (2087499, 1, 15),
  (2088268, 11, 12),
  (2089455, 2, 5),
  (2091708, 3, 18),
  (2092342, 11, 0),
  (2093024, 10, 6),
  (2093898, 0, 0),
  (2093923, 9, 17),
  (2094378, 8, 3),
  (2095263, 0, 0),
  (2096470, 5, 6),
  (2098039, 0, 18),
  (2098162, 11, 5),
  (2102293, 1, 2),
  (2102404, 10, 19),
  (2102831, 5, 17),
  (2102915, 8, 3),
  (2103551, 9, 14),
  (2115482, 4, 6),
  (2118583, 2, 9),
  (2118755, 7, 22),
  (2121371, 9, 14),
  (2123734, 5, 10),
  (2127668, 3, 13),
  (2128234, 11, 7),
  (2132468, 6, 10),
  (2133340, 7, 10),
  (2134635, 4, 2),
  (2135057, 9, 7),
  (2138169, 2, 17),
  (2139737, 3, 0),
  (2140839, 7, 10),
  (2141863, 4, 21),
  (2142132, 0, 19),
  (2142886, 8, 15),
  (2145689, 2, 10),
  (2146705, 9, 3),
  (2149545, 4, 10),
  (2150039, 2, 9),
  (2150770, 10, 0),
  (2151222, 1, 10),
  (2152345, 9, 3),
  (2153749, 3, 10),
  (2154179, 8, 7),
  (2155576, 0, 17),
  (2158011, 11, 18),
  (2160542, 6, 10),
  (2161542, 2, 13),
  (2163508, 8, 13),
  (2171063, 4, 10),
  (2171232, 7, 9),
  (2176965, 0, 0),
  (2177885, 11, 0),
  (2184056, 4, 11),
  (2184517, 2, 11),
  (2186083, 7, 4),
  (2187167, 6, 21),
  (2187550, 4, 10),
  (2187985, 7, 22),
  (2188030, 8, 6),
  (2189317, 3, 4),
  (2192207, 0, 0),
  (2192352, 11, 0),
  (2195043, 6, 10),
  (2198545, 8, 10),
  (2204164, 10, 0),
  (2205710, 3, 7),
  (2208921, 7, 5),
  (2210728, 8, 3),
  (2213069, 8, 2),
  (2215422, 9, 7),
  (2217143, 9, 13),
  (2217476, 8, 2),
  (2219212, 8, 18),
  (2220602, 6, 17),
  (2225082, 1, 22),
  (2225138, 0, 10),
  (2231166, 11, 7),
  (2234858, 1, 0),
  (2239036, 5, 19),
  (2239776, 1, 0),
  (2246942, 2, 3),
  (2250412, 6, 9),
  (2251093, 8, 11),
  (2251875, 1, 0),
  (2255622, 4, 2),
  (2256562, 9, 4),
  (2263168, 11, 0),
  (2266123, 0, 0),
  (2268860, 3, 14),
  (2269392, 10, 0),
  (2275222, 7, 17),
  (2279840, 7, 17),
  (2288818, 11, 0),
  (2290415, 3, 14),
  (2290916, 11, 0),
  (2292389, 1, 0),
  (2296910, 1, 0),
  (2297419, 5, 10),
  (2298246, 3, 10),
  (2299843, 4, 21),
  (2304201, 4, 3),
  (2304479, 8, 11),
  (2305035, 1, 15),
  (2305940, 3, 13),
  (2307086, 0, 19),
  (2308370, 4, 10),
  (2308558, 7, 10),
  (2309574, 6, 10),
  (2310948, 2, 10),
  (2316803, 6, 17),
  (2317319, 3, 5),
  (2317429, 11, 18),
  (2317446, 9, 10),
  (2318444, 8, 11),
  (2321363, 5, 17),
  (2323067, 10, 0),
  (2325627, 3, 3),
  (2325702, 11, 11),
  (2326260, 10, 0),
  (2327622, 4, 17),
  (2327795, 1, 0),
  (2330340, 10, 0),
  (2330467, 1, 11),
  (2332653, 7, 5),
  (2332668, 8, 7),
  (2333589, 0, 4),
  (2335309, 5, 21),
  (2338562, 11, 0),
  (2338765, 5, 0),
  (2340166, 7, 10),
  (2340815, 3, 2),
  (2342055, 5, 10),
  (2343004, 6, 10),
  (2345723, 2, 6),
  (2345995, 4, 10),
  (2349158, 2, 13),
  (2349253, 9, 7),
  (2349913, 4, 21),
  (2351589, 3, 3),
  (2353207, 8, 3),
  (2355807, 8, 3),
  (2357616, 9, 18),
  (2358772, 1, 22),
  (2361506, 6, 10),
  (2362187, 3, 7),
  (2363052, 9, 0),
  (2363106, 7, 9),
  (2366197, 4, 10),
  (2366302, 6, 10),
  (2371974, 2, 1),
  (2373212, 5, 10),
  (2374712, 8, 3),
  (2376636, 4, 8),
  (2376742, 4, 17),
  (2379156, 10, 0),
  (2379285, 7, 13),
  (2379503, 3, 13),
  (2381728, 4, 17),
  (2383398, 9, 0),
  (2387847, 1, 0),
  (2388594, 8, 18),
  (2388907, 4, 17),
  (2389723, 8, 3),
  (2390992, 11, 0),
  (2391110, 5, 22),
  (2393300, 4, 17),
  (2394291, 0, 14),
  (2394482, 3, 15),
  (2395446, 4, 10),
  (2396653, 6, 17),
  (2400026, 3, 11),
  (2401950, 10, 0),
  (2402750, 11, 0),
  (2405517, 5, 21),
  (2409395, 3, 16),
  (2410380, 6, 17),
  (2410508, 5, 13),
  (2413760, 2, 13),
  (2414679, 4, 10),
  (2414775, 6, 16),
  (2415331, 3, 2),
  (2417507, 1, 0),
  (2432421, 4, 17),
  (2435373, 7, 10),
  (2436358, 7, 10),
  (2442684, 1, 0),
  (2443010, 1, 0),
  (2444466, 11, 0),
  (2445049, 2, 3),
  (2445376, 5, 15),
  (2453927, 1, 0),
  (2454349, 9, 4),
  (2459037, 1, 20),
  (2459323, 11, 11),
  (2465510, 9, 2),
  (2467520, 0, 0),
  (2468056, 9, 13),
  (2468971, 11, 22),
  (2470051, 2, 7),
  (2475422, 4, 17),
  (2482390, 0, 0),
  (2482789, 8, 10),
  (2483660, 0, 10),
  (2485728, 4, 10),
  (2486837, 6, 17),
  (2488298, 3, 3),
  (2490937, 0, 6),
  (2494604, 11, 11),
  (2494646, 0, 0),
  (2500487, 10, 11),
  (2503446, 5, 10),
  (2504139, 4, 17),
  (2504296, 10, 0),
  (2507514, 4, 10),
  (2507555, 0, 0),
  (2508243, 2, 1),
  (2508528, 0, 18),
  (2509318, 5, 17),
  (2512219, 6, 22),
  (2514818, 4, 17),
  (2520969, 7, 21),
  (2523917, 3, 7),
  (2526079, 8, 4),
  (2527253, 3, 7),
  (2536771, 2, 18),
  (2539241, 3, 13),
  (2539522, 8, 10),
  (2542774, 10, 18),
  (2544831, 11, 0),
  (2546358, 8, 18),
  (2548309, 2, 17),
  (2549102, 8, 4),
  (2556044, 8, 4),
  (2559333, 8, 0),
  (2560836, 9, 1),
  (2561649, 0, 0),
  (2562222, 4, 10),
  (2562875, 9, 3),
  (2564507, 5, 18),
  (2566764, 10, 0),
  (2567124, 10, 0),
  (2567949, 8, 10),
  (2568191, 1, 11),
  (2569114, 1, 0),
  (2569228, 4, 19),
  (2570196, 6, 9),
  (2570573, 7, 10),
  (2571879, 2, 3),
  (2580074, 10, 11),
  (2580194, 7, 6),
  (2581821, 11, 0),
  (2586509, 10, 0),
  (2588287, 11, 0),
  (2588625, 9, 10),
  (2590461, 10, 7),
  (2592243, 11, 0),
  (2594264, 11, 0),
  (2596350, 2, 13),
  (2596395, 6, 17),
  (2597068, 2, 3),
  (2598265, 5, 10),
  (2600434, 2, 3),
  (2600503, 0, 11),
  (2602177, 6, 10),
  (2603421, 5, 10),
  (2603523, 5, 10),
  (2603856, 3, 14),
  (2605844, 4, 10),
  (2607041, 8, 13),
  (2607826, 0, 0),
  (2609682, 6, 10),
  (2610017, 6, 17),
  (2610602, 10, 3),
  (2615953, 11, 0),
  (2616555, 11, 0),
  (2617779, 3, 4),
  (2619448, 5, 17),
  (2619475, 5, 10),
  (2621242, 9, 13),
  (2621610, 6, 4),
  (2622916, 11, 22),
  (2624673, 6, 10),
  (2624735, 5, 6),
  (2625144, 9, 3),
  (2631433, 3, 7),
  (2636175, 4, 10),
  (2639187, 10, 0),
  (2639209, 2, 7),
  (2641812, 11, 0),
  (2646218, 5, 10),
  (2646744, 1, 18),
  (2649487, 5, 10),
  (2650869, 5, 10),
  (2651835, 4, 21),
  (2652563, 8, 7),
  (2656124, 11, 0),
  (2660408, 2, 4),
  (2660466, 11, 0),
  (2662731, 0, 17),
  (2662885, 4, 2),
  (2672780, 5, 3),
  (2676028, 10, 0),
  (2676309, 8, 7),
  (2678149, 8, 3),
  (2679093, 0, 11),
  (2683968, 6, 10),
  (2684143, 1, 18),
  (2685909, 0, 0),
  (2686170, 11, 0),
  (2687767, 9, 18),
  (2689652, 3, 3),
  (2693865, 8, 5),
  (2694541, 7, 9),
  (2695810, 6, 9),
  (2695968, 1, 10),
  (2698849, 1, 11),
  (2701812, 11, 10),
  (2703567, 8, 10),
  (2703621, 3, 17),
  (2704703, 6, 9),
  (2704792, 1, 0),
  (2710829, 5, 10),
  (2712454, 6, 10),
  (2714864, 9, 0),
  (2717064, 8, 0),
  (2717794, 10, 11),
  (2717820, 1, 0),
  (2717985, 5, 12),
  (2719506, 8, 18),
  (2720286, 1, 22),
  (2724647, 2, 13),
  (2726644, 2, 3),
  (2727060, 2, 4),
  (2727152, 0, 0),
  (2728564, 5, 10),
  (2733912, 6, 10),
  (2734687, 1, 0),
  (2736145, 8, 18),
  (2737007, 3, 7),
  (2737883, 10, 22),
  (2738936, 4, 21),
  (2739849, 3, 17),
  (2740428, 9, 7),
  (2743207, 9, 7),
  (2744365, 5, 10),
  (2745403, 6, 10),
  (2745956, 3, 0),
  (2748114, 7, 10),
  (2748244, 3, 18),
  (2749067, 3, 13),
  (2749705, 2, 4),
  (2752788, 7, 10),
  (2755782, 3, 7),
  (2756718, 11, 18),
  (2758220, 2, 13),
  (2759832, 11, 6),
  (2760802, 7, 10),
  (2761127, 9, 18),
  (2763203, 11, 18),
  (2768600, 9, 10),
  (2773613, 9, 2),
  (2774039, 6, 10),
  (2775487, 0, 19),
  (2779929, 11, 22),
  (2780089, 4, 17),
  (2780454, 5, 17),
  (2781365, 3, 3),
  (2782293, 2, 10),
  (2782773, 6, 10),
  (2785130, 9, 0),
  (2789458, 9, 3),
  (2790572, 6, 16),
  (2790857, 11, 11),
  (2791613, 0, 0),
  (2791982, 7, 10),
  (2797642, 4, 10),
  (2799045, 10, 0),
  (2799077, 1, 0),
  (2799883, 4, 10),
  (2800409, 6, 10),
  (2800821, 10, 10),
  (2801027, 9, 10),
  (2803556, 3, 7),
  (2812231, 8, 9),
  (2814252, 1, 22),
  (2815694, 6, 6),
  (2816214, 4, 18),
  (2818268, 2, 13),
  (2823658, 4, 10),
  (2823663, 4, 22),
  (2824364, 10, 0),
  (2825514, 9, 18),
  (2825584, 6, 10),
  (2831213, 9, 0),
  (2833829, 6, 10),
  (2834468, 6, 10),
  (2834472, 9, 15),
  (2834662, 11, 0),
  (2836179, 2, 17),
  (2838640, 1, 0),
  (2838671, 4, 17),
  (2843962, 11, 15),
  (2844091, 1, 14),
  (2844848, 6, 10),
  (2855078, 8, 10),
  (2863264, 1, 11),
  (2863678, 0, 0),
  (2864024, 11, 0),
  (2864814, 1, 0),
  (2868387, 4, 10),
  (2868717, 8, 11),
  (2869374, 5, 22),
  (2871695, 2, 11),
  (2872960, 9, 8),
  (2873695, 3, 7),
  (2876908, 6, 10),
  (2882021, 3, 4),
  (2885124, 1, 18),
  (2885216, 2, 4),
  (2886140, 0, 0),
  (2887971, 11, 5),
  (2890009, 11, 0),
  (2891931, 10, 0),
  (2897439, 0, 22),
  (2898218, 9, 7),
  (2899370, 10, 0),
  (2901094, 7, 10),
  (2904892, 4, 10),
  (2905347, 9, 13),
  (2908577, 4, 17),
  (2912146, 9, 18),
  (2914577, 1, 11),
  (2915527, 9, 0),
  (2916565, 9, 7),
  (2920037, 0, 0),
  (2924271, 10, 0),
  (2926054, 8, 10),
  (2932904, 0, 0),
  (2933208, 5, 17),
  (2934020, 0, 0),
  (2934822, 6, 10),
  (2934928, 5, 17),
  (2935756, 2, 5),
  (2935802, 10, 0),
  (2938107, 8, 15),
  (2943564, 2, 7),
  (2944911, 10, 0),
  (2945648, 3, 2),
  (2947649, 10, 21),
  (2948549, 3, 4),
  (2952511, 8, 18),
  (2952768, 2, 7),
  (2953243, 6, 10),
  (2955604, 10, 0),
  (2956720, 0, 0),
  (2959092, 9, 18),
  (2960248, 6, 21),
  (2960362, 1, 20),
  (2963845, 4, 22),
  (2965757, 8, 3),
  (2965921, 1, 22),
  (2966390, 2, 7),
  (2969455, 11, 18),
  (2970524, 9, 0),
  (2971785, 5, 10),
  (2972435, 10, 0),
  (2973321, 6, 10),
  (2973615, 8, 12),
  (2975818, 6, 22),
  (2977081, 7, 4),
  (2978788, 6, 10),
  (2983549, 8, 0),
  (2983628, 3, 7),
  (2984779, 0, 19),
  (2989328, 10, 0),
  (2991567, 6, 17),
  (2992398, 9, 3),
  (2998261, 7, 22),
  (3010421, 9, 7),
  (3013276, 5, 17),
  (3015564, 5, 19),
  (3019958, 1, 0),
  (3020620, 1, 17),
  (3021001, 2, 10),
  (3031765, 6, 10),
  (3032201, 3, 3),
  (3032653, 5, 10),
  (3035419, 6, 10),
  (3035862, 9, 3),
  (3037520, 5, 6),
  (3043084, 3, 3),
  (3043102, 11, 0),
  (3044695, 7, 10),
  (3045468, 4, 10),
  (3045589, 4, 2),
  (3045665, 2, 15),
  (3048896, 8, 9),
  (3049298, 7, 2),
  (3049429, 3, 17),
  (3049875, 0, 0),
  (3050215, 7, 17),
  (3051084, 2, 8),
  (3053363, 7, 10),
  (3054236, 3, 7),
  (3054440, 6, 9),
  (3056991, 4, 10),
  (3060318, 0, 10),
  (3069824, 9, 3),
  (3070158, 10, 11),
  (3070333, 5, 9),
  (3073938, 0, 0),
  (3074062, 8, 12),
  (3076721, 2, 10),
  (3077282, 5, 10),
  (3077770, 0, 22),
  (3078117, 2, 7),
  (3083810, 6, 21),
  (3085991, 9, 7),
  (3086759, 7, 2),
  (3088684, 0, 0),
  (3088774, 8, 7),
  (3090068, 11, 11),
  (3090129, 2, 7),
  (3090419, 10, 0),
  (3091127, 0, 22),
  (3094863, 11, 0),
  (3095055, 11, 0),
  (3096370, 11, 0),
  (3100539, 11, 0),
  (3104079, 7, 10),
  (3106018, 5, 11),
  (3107041, 3, 4),
  (3108514, 5, 20),
  (3110226, 6, 17),
  (3111919, 5, 9),
  (3113896, 3, 10),
  (3115872, 0, 0),
  (3116350, 1, 0),
  (3117240, 8, 2),
  (3117825, 11, 11),
  (3118288, 7, 1),
  (3118513, 7, 10),
  (3119175, 1, 0),
  (3119499, 2, 1),
  (3119779, 11, 0),
  (3119887, 6, 17),
  (3123866, 1, 0),
  (3126081, 2, 18),
  (3126086, 11, 0),
  (3126964, 9, 1),
  (3128602, 4, 9),
  (3138634, 0, 11),
  (3138810, 0, 11),
  (3139495, 5, 1),
  (3140304, 9, 7),
  (3140537, 3, 0),
  (3141504, 0, 0),
  (3141589, 9, 13),
  (3143852, 4, 10),
  (3143887, 4, 10),
  (3145070, 3, 1),
  (3145668, 4, 17),
  (3146690, 6, 10),
  (3147510, 1, 18),
  (3149763, 1, 22),
  (3152242, 4, 17),
  (3152556, 4, 17),
  (3156038, 1, 5),
  (3156339, 2, 3),
  (3160713, 8, 8),
  (3162005, 7, 3),
  (3162034, 0, 11),
  (3164463, 10, 3),
  (3165915, 4, 10),
  (3166373, 11, 0),
  (3167513, 3, 9),
  (3174632, 0, 0),
  (3175002, 11, 0),
  (3175568, 10, 0),
  (3176615, 8, 4),
  (3177765, 10, 0),
  (3177917, 4, 10),
  (3180807, 11, 10),
  (3182227, 6, 17),
  (3182331, 11, 22),
  (3190283, 8, 3),
  (3198595, 9, 2),
  (3200092, 3, 2),
  (3200633, 6, 5),
  (3203368, 9, 8),
  (3207373, 11, 0),
  (3208752, 9, 9),
  (3211782, 8, 9),
  (3213045, 1, 2),
  (3215780, 9, 11),
  (3216247, 1, 11),
  (3224938, 0, 16),
  (3227317, 4, 10),
  (3227562, 10, 22),
  (3227854, 6, 10),
  (3227907, 11, 0),
  (3230531, 8, 3),
  (3232544, 7, 22),
  (3232616, 0, 11),
  (3236950, 8, 7),
  (3240808, 6, 17),
  (3244067, 3, 0),
  (3247298, 6, 10),
  (3248909, 5, 10),
  (3249562, 0, 0),
  (3251827, 6, 10),
  (3252475, 1, 11),
  (3257072, 11, 0),
  (3258759, 6, 17),
  (3263102, 9, 7),
  (3263339, 7, 3),
  (3268124, 8, 7),
  (3268863, 8, 6),
  (3274778, 6, 9),
  (3275203, 7, 17),
  (3276146, 6, 10),
  (3276799, 9, 10),
  (3282282, 9, 4),
  (3282716, 11, 0),
  (3282757, 7, 18),
  (3285219, 4, 10),
  (3287162, 1, 0),
  (3290380, 10, 10),
  (3291574, 4, 18),
  (3292204, 11, 0),
  (3292857, 1, 5),
  (3293343, 11, 0),
  (3293718, 11, 11),
  (3295926, 9, 10),
  (3296347, 0, 0),
  (3300496, 1, 10),
  (3304831, 6, 17),
  (3305415, 3, 7),
  (3306045, 0, 0),
  (3308411, 4, 17),
  (3311382, 2, 2),
  (3312951, 5, 10),
  (3314078, 4, 11),
  (3317900, 3, 7),
  (3325691, 2, 7),
  (3328666, 3, 4),
  (3332218, 2, 3),
  (3335223, 4, 9),
  (3339587, 6, 10),
  (3346064, 0, 0),
  (3353154, 3, 18),
  (3353330, 3, 6),
  (3358337, 0, 0),
  (3359509, 2, 7),
  (3359829, 9, 3),
  (3361827, 5, 17),
  (3363377, 6, 10),
  (3364497, 4, 10),
  (3365021, 2, 4),
  (3365215, 8, 3),
  (3372384, 10, 11),
  (3375319, 8, 12),
  (3379232, 6, 17),
  (3379531, 0, 1),
  (3384275, 4, 6),
  (3385387, 4, 10),
  (3386368, 2, 3),
  (3387866, 2, 7),
  (3388722, 1, 11),
  (3390593, 4, 10),
  (3394095, 8, 1),
  (3397501, 2, 10),
  (3398172, 5, 10),
  (3404234, 2, 4),
  (3404859, 3, 10),
  (3416914, 2, 16),
  (3420517, 9, 7),
  (3421724, 0, 11),
  (3422292, 6, 13),
  (3428040, 3, 13),
  (3430153, 2, 10),
  (3430306, 2, 13),
  (3430326, 3, 4),
  (3439088, 6, 10),
  (3441839, 7, 18),
  (3441908, 3, 7),
  (3443643, 9, 0),
  (3443952, 8, 13),
  (3447822, 4, 10),
  (3448607, 4, 9),
  (3451260, 3, 10),
  (3455747, 4, 10),
  (3456377, 4, 21),
  (3460390, 4, 21),
  (3460494, 7, 10),
  (3460871, 8, 9),
  (3462616, 7, 10),
  (3463222, 0, 0),
  (3466683, 1, 22),
  (3468238, 4, 7),
  (3469796, 4, 10),
  (3471098, 11, 0),
  (3471560, 7, 22),
  (3472474, 0, 19),
  (3475994, 3, 7),
  (3476086, 2, 7),
  (3476147, 4, 10),
  (3476618, 2, 1),
  (3479470, 1, 1),
  (3480888, 11, 0),
  (3482605, 3, 3),
  (3486667, 9, 7),
  (3490764, 7, 10),
  (3501629, 6, 17),
  (3501821, 4, 16),
  (3503475, 5, 10),
  (3504716, 0, 10),
  (3505716, 2, 3),
  (3508534, 6, 9),
  (3509272, 5, 10),
  (3511458, 6, 13),
  (3512300, 5, 10),
  (3512416, 9, 0),
  (3515917, 0, 0),
  (3522083, 5, 10),
  (3522087, 10, 0),
  (3523082, 8, 8),
  (3524161, 7, 10),
  (3525078, 11, 0),
  (3533160, 2, 3),
  (3534660, 7, 10),
  (3534691, 9, 10),
  (3535415, 0, 10),
  (3538457, 11, 0),
  (3538930, 4, 10),
  (3539281, 0, 0),
  (3542066, 11, 14),
  (3542597, 1, 0),
  (3545624, 5, 15),
  (3546928, 7, 19),
  (3547244, 8, 3),
  (3549397, 8, 0),
  (3553528, 2, 4),
  (3554523, 6, 10),
  (3556624, 10, 11),
  (3557167, 9, 13),
  (3557852, 0, 10),
  (3558101, 10, 0),
  (3560648, 7, 10),
  (3561565, 7, 10),
  (3563983, 3, 13),
  (3565729, 0, 0),
  (3566507, 11, 0),
  (3567023, 11, 0),
  (3569079, 7, 17),
  (3569983, 3, 7),
  (3574727, 1, 0),
  (3577739, 10, 0),
  (3577878, 7, 9),
  (3579264, 11, 0),
  (3582532, 9, 3),
  (3583343, 2, 15),
  (3583419, 6, 10),
  (3584934, 9, 17),
  (3585490, 4, 10),
  (3586615, 0, 0),
  (3591046, 2, 12),
  (3591713, 0, 0),
  (3593820, 4, 10),
  (3596097, 8, 3),
  (3596624, 6, 10),
  (3597191, 7, 10),
  (3597462, 11, 0),
  (3597603, 2, 13),
])