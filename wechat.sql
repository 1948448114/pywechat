/*
Navicat MySQL Data Transfer

Source Server         : allicloud
Source Server Version : 50541
Source Host           : 123.57.221.18:3306
Source Database       : wechat

Target Server Type    : MYSQL
Target Server Version : 50541
File Encoding         : 65001

Date: 2015-09-20 12:10:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `openid` varchar(50) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `state` int(11) NOT NULL,
  `school` varchar(50) DEFAULT NULL,
  `room` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('o22yYs9YWHQgRY-oNl2wi901m9IU', '刘祯祯', '000000', '1', '大连理工大学', '305');
INSERT INTO `teacher` VALUES (null, '周文娜', '000000', '0', '东南大学', '000');
INSERT INTO `teacher` VALUES ('', '孙卫国', '000000', '0', '兰州理工大学', '307');
INSERT INTO `teacher` VALUES ('o22yYsxhbPWIF43wvxDHEyo29vto', '巴璐', '000000', '1', '哈尔滨工业大学', '315');
INSERT INTO `teacher` VALUES ('o22yYs--XBmNNBuqJ9fhHH4gi0vY', '张学同', '000000', '1', '天津大学', '323');
INSERT INTO `teacher` VALUES ('o22yYsxSGn8OK3iHhfF82P62P6u8', '张玉涛', '000000', '1', '哈尔滨工业大学', '315');
INSERT INTO `teacher` VALUES ('o22yYs5KXYlU7w2zE7VQZfwl3TkQ', '张磊', '000000', '1', '北京理工大学', '301');
INSERT INTO `teacher` VALUES ('o22yYs-AZoOf4dyxRHV765ES-ES8', '张飞', '000000', '1', '兰州理工大学', '307');
INSERT INTO `teacher` VALUES (null, '施杰', '000000', '0', '东南大学', '000');
INSERT INTO `teacher` VALUES (null, '曹奕', '000000', '0', '东南大学', '000');
INSERT INTO `teacher` VALUES ('o22yYsyr1LayYo8VgEL4PCF6omXI', '曹良玉', '000000', '1', '西北工业大学', '431');
INSERT INTO `teacher` VALUES ('o22yYs0GTNKw22HP2YXn1OR7Z0RA', '李丞杰', '000000', '1', '重庆大学', '303');
INSERT INTO `teacher` VALUES ('o22yYs_ugovW0zHo_g_Bdm3GMER8', '李然', '000000', '1', '大连理工大学', '305');
INSERT INTO `teacher` VALUES (null, '林梅', '000000', '0', '同济大学', '327');
INSERT INTO `teacher` VALUES (null, '江莉莉', '000000', '0', '东南大学', '000');
INSERT INTO `teacher` VALUES (null, '江雪华', '000000', '0', '东南大学', '000');
INSERT INTO `teacher` VALUES ('o22yYsxADWmRpDvDbk6yD-OjxpBI', '王莹', '000000', '1', '哈尔滨工业大学', '321');
INSERT INTO `teacher` VALUES ('', '白杨', '000000', '1', '兰州理工大学', '307');
INSERT INTO `teacher` VALUES (null, '石雪珺', '000000', '0', '同济大学', '327');
INSERT INTO `teacher` VALUES ('o22yYs_MSo72BmSlGbXZZ8T7AEtk', '舒泽民', '000000', '1', '重庆大学', '303');
INSERT INTO `teacher` VALUES ('', '郝君明', '000000', '1', '兰州理工大学', '405');
INSERT INTO `teacher` VALUES ('o22yYs6jGcVuugn3vZ8XPB0bVrKs', '陈木龙', '000000', '1', '华南理工大学', '317');
INSERT INTO `teacher` VALUES ('o22yYs5teRH2U6BUcFkWKSoJVDNU', '陶森', '000000', '1', '天津大学', '323');
INSERT INTO `teacher` VALUES ('o22yYs9wDAcnxFxEBchAZXpyEaWs', '韩阳', '000000', '1', '北京理工大学', '301');
INSERT INTO `teacher` VALUES ('o22yYsxOHHdud9L6sJmTcR_6FaC4', '高惠君', '000000', '1', '华南理工大学', '311');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `openid` varchar(50) NOT NULL,
  `number` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`openid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('o22yYs-ceXbMUxIUuhERStY0MtPk', '213150273', 'as936231', '0');
INSERT INTO `user` VALUES ('o22yYs-G4Y4o6JjAujemiz6g7Gdc', '213141666', 'zjh15003466920', '0');
INSERT INTO `user` VALUES ('o22yYs-H3u4kXR05K1uk8lg9CDmk', '213130509', 'xxw103000', '0');
INSERT INTO `user` VALUES ('o22yYs-ICabWJchRisJmtD3p8kkI', '213153674', 'tianyu1027', '0');
INSERT INTO `user` VALUES ('o22yYs-Kjn4Hamv7wMjpt4O2n69E', '213153011', 'zhangaihong123', '0');
INSERT INTO `user` VALUES ('o22yYs-M20k9MDhc_-FoHtTGxcCY', '213150645', 'cjh521', '0');
INSERT INTO `user` VALUES ('o22yYs-o4RFizWt5l8XSMhuGyVY0', '213140826', 'Keepmoving521lj', '0');
INSERT INTO `user` VALUES ('o22yYs-pGb6srHq9j_eu-wNgPSgo', '213143706', 'danfeis960924', '0');
INSERT INTO `user` VALUES ('o22yYs-s1ZczufvK2D3606XrmJCA', '213150547', 'jiawei0917791', '0');
INSERT INTO `user` VALUES ('o22yYs-TSfLC2pI-dVwtAEnMGkfs', '213133975', '282716', '0');
INSERT INTO `user` VALUES ('o22yYs-Yyzcto-26TGGOr3EWWiP0', '213140775', 'wjy486862', '0');
INSERT INTO `user` VALUES ('o22yYs01y4LrfDeiN-DK-E9Nw-Ik', '213152083', 'zyhdndxds1997', '0');
INSERT INTO `user` VALUES ('o22yYs0bwUTuN631EzwdnkSiz0oM', '213140879', '1216tanglin', '0');
INSERT INTO `user` VALUES ('o22yYs0CcnWC8b7at7EzwJH0qOrI', '213143655', 'danyang0126', '0');
INSERT INTO `user` VALUES ('o22yYs0CjNGSZzu4HXFhcZxTLdY8', '213152601', 'chenhan3833813', '0');
INSERT INTO `user` VALUES ('o22yYs0cOKFt9-GTWH8TxLbzsxDI', '213141264', 'z13257', '0');
INSERT INTO `user` VALUES ('o22yYs0Fi-6lY4oDY2yBNUeR-EQE', '213150539', 'Zxcv1234', '0');
INSERT INTO `user` VALUES ('o22yYs0G7FQYM8BAOYFPd7TdLxuQ', '213150400', '18266987791MHY', '0');
INSERT INTO `user` VALUES ('o22yYs0ix-p1mX_15184jeO209dQ', '213150308', '51zhishan', '0');
INSERT INTO `user` VALUES ('o22yYs0JfcntZFj1Jcm9VLQIN2Ow', '220141201', '17881X', '0');
INSERT INTO `user` VALUES ('o22yYs0ked5pKUryqBy-ZOIjLwTc', '213151150', '054919', '0');
INSERT INTO `user` VALUES ('o22yYs0ofzdzQ_sWxIyiTl6_5tFc', '213153408', '51840AK47', '0');
INSERT INTO `user` VALUES ('o22yYs0Q2KaWWLdtPIahT0acFAy4', '213122734', '13152X', '0');
INSERT INTO `user` VALUES ('o22yYs0Wc49AJ3cWjZKi-w1Mw8pA', '220152131', 'Being0326', '0');
INSERT INTO `user` VALUES ('o22yYs0wt3jtS7J3DRZqnllvR6Fo', '213150240', 'Lyn1006638247', '0');
INSERT INTO `user` VALUES ('o22yYs0ZQIKg4rHcIur3PEZl_O8M', '213143266', '32995wtossc', '0');
INSERT INTO `user` VALUES ('o22yYs0_ahBGR0wXG7ZsoWAYuY78', '213133077', 'Suoqu520', '0');
INSERT INTO `user` VALUES ('o22yYs112KVl5_qN7n9EG00gURJo', '220151908', 'gegeqihan3344', '0');
INSERT INTO `user` VALUES ('o22yYs14ELUsvyF5_-JtBzDCaJno', '213140672', '1995yyz', '0');
INSERT INTO `user` VALUES ('o22yYs1AHGZpl8k0Si3jsFICaXVQ', '213143504', 'gongxue0103', '0');
INSERT INTO `user` VALUES ('o22yYs1fPjBl9mqpsbNgIfjpaHyI', '213140916', 'Hz707296', '0');
INSERT INTO `user` VALUES ('o22yYs1hs-woxCSXeHYMgx-Td_fI', '220151518', 'zf1993', '0');
INSERT INTO `user` VALUES ('o22yYs1jdol-AHGQ1m6ZqE-h_85U', '213140647', 'cdqlxgcxh58', '0');
INSERT INTO `user` VALUES ('o22yYs1O5SgOuWuLNRPcR3xcopVs', '213130406', 'wxc520966', '0');
INSERT INTO `user` VALUES ('o22yYs1S84tW5GpQ0jyHazOjt9OI', '213143688', '196728n', '0');
INSERT INTO `user` VALUES ('o22yYs1SKBxlFD6TnxZ_07RPxBIo', '213143109', '135246ZHAOYAQION', '0');
INSERT INTO `user` VALUES ('o22yYs1vbqNFTn2m2OsBJLNPITsU', '213143842', '99999a', '0');
INSERT INTO `user` VALUES ('o22yYs1_q5qg_wzzdmj4GU-4_IeM', '213131332', 'lyx123456', '0');
INSERT INTO `user` VALUES ('o22yYs2-O6Zzd54VtNrchNQyRneY', '213152464', '21614X', '0');
INSERT INTO `user` VALUES ('o22yYs2ERdCpA0qkjJW4iGQvIOnY', '220151500', 'tmx5052103824', '0');
INSERT INTO `user` VALUES ('o22yYs2fXQdU9eEHWwekjanW0F-o', '213150168', 'BallKing961006', '0');
INSERT INTO `user` VALUES ('o22yYs2Gj8rjhrpRozjgJyl9bm4k', '213112015', 'fumika930529', '0');
INSERT INTO `user` VALUES ('o22yYs2HQPS47TQRDq_Jf9-xPge0', '213120469', 'GCHily123', '0');
INSERT INTO `user` VALUES ('o22yYs2l4KuWlrmJ-bHGeJnXYqV0', '213133799', '199408c', '0');
INSERT INTO `user` VALUES ('o22yYs2nEeMWmJ_gV6yRiZI9dxXA', '213153015', '5tao1995', '0');
INSERT INTO `user` VALUES ('o22yYs2UKn9T2OFScLu5T-hA1glU', '213152913', '617860344hh', '0');
INSERT INTO `user` VALUES ('o22yYs3-TU9_2R9K-OXfRloVkkkI', '213121664', '19931103iamsean', '0');
INSERT INTO `user` VALUES ('o22yYs37rc23Ow__lUp3CIsrikTk', '213151043', 'princewrh50772', '0');
INSERT INTO `user` VALUES ('o22yYs3BEnnQ4w9ivpKnAv9uTCl8', '213120843', '197004', '0');
INSERT INTO `user` VALUES ('o22yYs3GjY6SqsiYi4sG2yLVfgSo', '213150533', 'xieyiyun0814', '0');
INSERT INTO `user` VALUES ('o22yYs3H0Ee5yEClnLZF5qjWyzMQ', '213133781', '140046', '0');
INSERT INTO `user` VALUES ('o22yYs3iFBUIJ569N9aIQF1bkGIY', '213130530', 'guyu12345', '0');
INSERT INTO `user` VALUES ('o22yYs3uK788wOl75Sb6mC7Kfhfg', '213140097', '427abc', '0');
INSERT INTO `user` VALUES ('o22yYs3XotkotuJlxU6jcFhmzkRI', '213152044', 'hjm62849331223', '0');
INSERT INTO `user` VALUES ('o22yYs3Y72-yRwZ2LJzAUxMnWhFE', '220132128', '284078', '0');
INSERT INTO `user` VALUES ('o22yYs3ZOiPl9g3_2ycmOfRN_vCo', '213153445', '172812', '0');
INSERT INTO `user` VALUES ('o22yYs4-b3JshUaoijW_rYDFCsTo', '213153006', '62006ZMXzmx', '0');
INSERT INTO `user` VALUES ('o22yYs441_hObn86T46KunhJqJ6E', '103008160', 'zhaoguang1988', '0');
INSERT INTO `user` VALUES ('o22yYs45D5ANYEuRnIwoo_M9r_6I', '213150362', 'MHF1127412267mhf', '0');
INSERT INTO `user` VALUES ('o22yYs4HIlyonmmC0FcrAkeeqEsM', '220153219', 'yjy19930628', '0');
INSERT INTO `user` VALUES ('o22yYs4J5nwMwXLl5untOITcJO80', '213121303', '6452689wang', '0');
INSERT INTO `user` VALUES ('o22yYs4jd29QlGkjkXOsXlUoG0yU', '213123508', '0621xy', '0');
INSERT INTO `user` VALUES ('o22yYs4kNmQWTZxwncgmnFn8F348', '213143187', '1089yneq1089YNEQ', '0');
INSERT INTO `user` VALUES ('o22yYs4lckloWYOZq79z8qL6PduM', '213133518', 'kobe1996', '0');
INSERT INTO `user` VALUES ('o22yYs4MIEYtSAk3HiQ_s592txiA', '213130746', '055217', '0');
INSERT INTO `user` VALUES ('o22yYs4v5kbx1EnxAbc4J86mmhkY', '213143056', '341727ab9929', '0');
INSERT INTO `user` VALUES ('o22yYs4VgCszGU5cVnqzXkqiefJs', '213120878', '010922', '0');
INSERT INTO `user` VALUES ('o22yYs4VJF6lDJVH_MkRhF4Vg81o', '213132187', 'zxm941123', '0');
INSERT INTO `user` VALUES ('o22yYs4wqn0P7REP96Yh3l8b3ZF4', '213142931', 'szz123', '0');
INSERT INTO `user` VALUES ('o22yYs4yfiXmtIDYnTao4ZrvYG1U', '213151889', 'zhinianMM2014', '0');
INSERT INTO `user` VALUES ('o22yYs57u96jl8yJe9-LKeHYutLU', '213150748', 'huang2015', '0');
INSERT INTO `user` VALUES ('o22yYs5AiBI0YPnRy2YxfhMarV-o', '213153381', 'cai961215', '0');
INSERT INTO `user` VALUES ('o22yYs5BwzcKscP4cGw1UsxOdc3A', '213153571', 'qead2020', '0');
INSERT INTO `user` VALUES ('o22yYs5cZFdq3GlF3OQQHdpjwULQ', '213150701', 'jy625598', '0');
INSERT INTO `user` VALUES ('o22yYs5EO9_mFAfzEpvniei1DDYY', '213142683', '2244xbs', '0');
INSERT INTO `user` VALUES ('o22yYs5OGzelQW9uikc-bD8qHIeQ', '213140758', 'ltylove1215', '0');
INSERT INTO `user` VALUES ('o22yYs5q7aXUx8DS-pS5fU1t1GTQ', '213153354', 'dl1597532580', '0');
INSERT INTO `user` VALUES ('o22yYs5tuAZhIEG9tax3YNT8di-Q', '213150723', 'zxsun0814', '0');
INSERT INTO `user` VALUES ('o22yYs5UhSzSTy2z2JeI9dc4XmvM', '213152552', '141592sam', '0');
INSERT INTO `user` VALUES ('o22yYs5wPlcYdxTt7a2WV9Fo61cs', '213153692', '1wojidewoaiguo', '0');
INSERT INTO `user` VALUES ('o22yYs5XBAo6Kfms3ynRyCwL8QyQ', '213134076', 'yz928428', '0');
INSERT INTO `user` VALUES ('o22yYs64xG7mkHCOgCPA6ZlyTSJA', '213122232', 'wxc823039', '0');
INSERT INTO `user` VALUES ('o22yYs6Ae--clsSKnIEEzszBZb8k', '213123014', '19941114201x', '0');
INSERT INTO `user` VALUES ('o22yYs6hxp8ScvBum9ofcLwLyw5o', '213133563', 'uu079668', '0');
INSERT INTO `user` VALUES ('o22yYs6ibS1sJcwvdd3nDHYdckDY', '220132941', 'chu3468', '0');
INSERT INTO `user` VALUES ('o22yYs6jc3ES0HQziGjTrE3m4Ljg', '213150562', 'wl11240301', '0');
INSERT INTO `user` VALUES ('o22yYs6wNUwj4PVW7JGqKjJvk5pM', '213152064', 'j970130', '0');
INSERT INTO `user` VALUES ('o22yYs6xjrfIxqXnG4x0yG_ijt_Q', '213133582', 'zhaoquan236', '0');
INSERT INTO `user` VALUES ('o22yYs70skNBvi-nbnaCj7FYN1Q4', '213121410', '1qaz2wsx', '0');
INSERT INTO `user` VALUES ('o22yYs71xKo-Pzd9Y7bmS21L0Ye4', '213153514', 'LzhXydjs1226', '0');
INSERT INTO `user` VALUES ('o22yYs770Sl5TH9tEavt2LO5Lf0g', '213151643', '19970210zxj', '0');
INSERT INTO `user` VALUES ('o22yYs7f32w-LsA-W8ug-klQbmUw', '213120617', 'victorzyf3969625', '0');
INSERT INTO `user` VALUES ('o22yYs7NkNA503ZfFc7c4olBr6jI', '213142258', 'hpc83399041', '0');
INSERT INTO `user` VALUES ('o22yYs7reD4pbBatuNkExPcqjs7g', '213153794', 'bela2001', '0');
INSERT INTO `user` VALUES ('o22yYs7s94gUm_MFAM7lKhklN9xA', '213121089', 'wsad123', '0');
INSERT INTO `user` VALUES ('o22yYs7VeFyp7zvWsaWsHGcmBk9U', '213141206', 'Hcl1996815', '0');
INSERT INTO `user` VALUES ('o22yYs7wKs9PPhEkjFZJTacadN3c', '213152412', 'dcl19961120', '0');
INSERT INTO `user` VALUES ('o22yYs83V748HFLub-COwSYaPJRU', '213141045', '081272jgf', '0');
INSERT INTO `user` VALUES ('o22yYs87_QOhzsdglJlNh7NSf5nA', '220142495', '13459205962kz', '0');
INSERT INTO `user` VALUES ('o22yYs89qjsiLTgDHiwgAERLEVxI', '213123787', '666888aaa', '0');
INSERT INTO `user` VALUES ('o22yYs8egzrME9-gitHLRV4_dEZk', '213151344', '2dj3kx', '0');
INSERT INTO `user` VALUES ('o22yYs8f6LEsdEM78kuJfbuuPS8o', '213132459', '972667', '0');
INSERT INTO `user` VALUES ('o22yYs8HOU8JP_WBikDnzKLqsc_U', '213150387', 'LJFqwer0319', '0');
INSERT INTO `user` VALUES ('o22yYs8ITacfTHSSAeisdlS6dgtw', '213141053', 'A27353247023187', '0');
INSERT INTO `user` VALUES ('o22yYs8jaXNrLW-acLpGx9lDMPaU', '213142998', '15224895717wj', '0');
INSERT INTO `user` VALUES ('o22yYs8kHOBXU08q8hAHyxm_vjas', '213130678', 'ZYZ4377697', '0');
INSERT INTO `user` VALUES ('o22yYs8MvTycskeJZSHnFLPfEe1M', '213120661', 'Aa258188', '0');
INSERT INTO `user` VALUES ('o22yYs8oBIV3wIUhEZRLFDjRyiIo', '213153111', 'youOK213153111', '0');
INSERT INTO `user` VALUES ('o22yYs8sikmzNumgYge5XE8E9too', '213120856', '526799x', '0');
INSERT INTO `user` VALUES ('o22yYs8VuQFiGtqIA2mfkx2YXtss', '220152171', '081144', '0');
INSERT INTO `user` VALUES ('o22yYs8wsn2ypuS4PvY8nq2JYbMY', '213142634', 'fengyuewubian03', '0');
INSERT INTO `user` VALUES ('o22yYs8XbQ6O3n4FfDTdAQKQXTr8', '213150814', 'qiuwei2233632', '0');
INSERT INTO `user` VALUES ('o22yYs92ZdKuXi96c4--DrQtkQpI', '213122056', 'hzw1116770', '0');
INSERT INTO `user` VALUES ('o22yYs98JFhh9ei7i-MFUSaFU7IA', '213133025', 'blh119105', '0');
INSERT INTO `user` VALUES ('o22yYs9eFxYDRfUCxvQVsPPfQbYQ', '213151865', 'njligjb9714', '0');
INSERT INTO `user` VALUES ('o22yYs9g6ThNlwi13KqW-NjFLHT0', '213132260', 'tanying262508', '0');
INSERT INTO `user` VALUES ('o22yYs9IZ2vCw3rOngjI1OV9fhvc', '213123598', 'Lwj168472598', '0');
INSERT INTO `user` VALUES ('o22yYs9J3y1__gsu_WuqR1Rl7vFc', '213150355', '1996lxs96', '0');
INSERT INTO `user` VALUES ('o22yYs9JxVI4_gWd27XrCLEYPar0', '213122109', '52doubao026', '0');
INSERT INTO `user` VALUES ('o22yYs9N7LeiLrRA8VBgZ3G6xrcE', '213123080', '1994623yie', '0');
INSERT INTO `user` VALUES ('o22yYs9nOl_5ouX-VUJYaV4qzD2Y', '213121081', 'ly10021993', '0');
INSERT INTO `user` VALUES ('o22yYs9oe-q7adNQ8Cw2v-0XKpzc', '213133620', 'lp940812', '0');
INSERT INTO `user` VALUES ('o22yYs9sTt7znTt32ArPavAmdUk4', '213120056', '824675391lwq', '0');
INSERT INTO `user` VALUES ('o22yYs9Td-qgDPmn3ls3dJKgDw0M', '213123420', '061025xqawqf', '0');
INSERT INTO `user` VALUES ('o22yYs9Vzd9gK6oRBhzEB0jngIag', '213141519', 'ygx5922', '0');
INSERT INTO `user` VALUES ('o22yYswBCcw8z0rDkKOvywrUx2A0', '213141706', 'h199677', '0');
INSERT INTO `user` VALUES ('o22yYswhgWx5DliUUNZCDSZ7sXBM', '213150991', 'yx343416', '0');
INSERT INTO `user` VALUES ('o22yYswJvgQesTKsVBmplP9czMm0', '213153886', '261921', '0');
INSERT INTO `user` VALUES ('o22yYswmG_feCMMBswkfEqMzv0_8', '213152569', 'qwe123', '0');
INSERT INTO `user` VALUES ('o22yYswOsSnLIdEQaIPiqGhWbqSk', '213153903', 'abd140826', '0');
INSERT INTO `user` VALUES ('o22yYswRahFqm3OKVrkTnckw3B5U', '213153725', 'Dd112886', '0');
INSERT INTO `user` VALUES ('o22yYswWiKlVaHFdXeZNw1AaadVk', '213142549', 'www960227', '0');
INSERT INTO `user` VALUES ('o22yYswx2WAYzYHPmsYQcfBBK-3k', '213142529', 'ab951105', '0');
INSERT INTO `user` VALUES ('o22yYswYPC-xk9Wt8cMTmkhGH92Q', '220152757', 'yangsong20301', '0');
INSERT INTO `user` VALUES ('o22yYsx8hj5djqPip6xRiLSIntMk', '213132597', 'cxy668', '0');
INSERT INTO `user` VALUES ('o22yYsxfu2Yo9n8RRsZGB6ubo3PE', '213113961', 'aa120313', '0');
INSERT INTO `user` VALUES ('o22yYsxKEpd8FuYHwUVQ-EYippCk', '213152502', 'zs13033877126', '0');
INSERT INTO `user` VALUES ('o22yYsxqxE5dWi-ySHKaiLaqmUsg', '213151038', 'zhangmc980430', '0');
INSERT INTO `user` VALUES ('o22yYsxS5ybk0-MZ4d0_nBtAxxWY', '213132483', '133645', '0');
INSERT INTO `user` VALUES ('o22yYsxWsO1vj1YJ3oQccFMfJQ2E', '213150306', 'yk5832950', '0');
INSERT INTO `user` VALUES ('o22yYsxYNc_JzLfiB8v7lfjZ4X08', '213121266', '5546ll', '0');
INSERT INTO `user` VALUES ('o22yYsx_abLylmsdksB-g-_bgKRE', '213152990', '1028qwebnmdyh', '0');
INSERT INTO `user` VALUES ('o22yYsyAdIFmgC19wRMDX-ZaP8Yk', '213143850', 'abc123', '0');
INSERT INTO `user` VALUES ('o22yYsyerOULTBPIwEZQRhHFt-sQ', '213153575', 'zmhZMH731100', '0');
INSERT INTO `user` VALUES ('o22yYsysRVgSaFjLiycBVdhLveKQ', '213153524', 'fjzly5kr6789', '0');
INSERT INTO `user` VALUES ('o22yYsy_Qwp-Xn0dbksJr66tlbss', '213150397', '673087dong', '0');
INSERT INTO `user` VALUES ('o22yYsz0avRs2PTUsbuO77hMBI3U', '213133640', 'zhangweidong', '0');
INSERT INTO `user` VALUES ('o22yYsz2wb4wZqiA7ovt5kNS0wBw', '213142832', 'wei666888', '0');
INSERT INTO `user` VALUES ('o22yYsz3AKQRY54bLsSRP4-qbYF8', '213153168', 'turanxiangqini97', '0');
INSERT INTO `user` VALUES ('o22yYsz4J5V_ZUUFxazdxOqxyZ8c', '213142517', 'slj314440', '0');
INSERT INTO `user` VALUES ('o22yYsz8RxK1V1syhgucGI2z1GRE', '213141008', 'z00000', '0');
INSERT INTO `user` VALUES ('o22yYszBGlL0XzIYy7yQmGQhiTCQ', '213131150', 'qsm199549', '0');
INSERT INTO `user` VALUES ('o22yYszchaYAOq0ivaVf9unwrdlc', '213133608', 'qmzp10g', '0');
INSERT INTO `user` VALUES ('o22yYszDlxRjy8XRJtjizmJFPNQ8', '213150942', '741239638wt74wt', '0');
INSERT INTO `user` VALUES ('o22yYszmrDebab0PC6hKIVTw9cvc', '213130147', '2013joezhou', '0');
INSERT INTO `user` VALUES ('o22yYszpksAucn9bD7BUfjPlEpNs', '213133426', 'zhu21199412', '0');
INSERT INTO `user` VALUES ('o22yYszqQge7igofwaGFTHnsDZD0', '213152655', 'a1593574682', '0');
INSERT INTO `user` VALUES ('o22yYszS94MVH3r1akW2VNybl8dI', '213121762', 'njzhanglh931221', '0');
INSERT INTO `user` VALUES ('o22yYszsfhbPNUt5CZuq-8AsrGIE', '213122272', '696993', '0');
INSERT INTO `user` VALUES ('o22yYsztuifxTiSOKkSKAjqA9Axo', '213153174', '96325279ly', '0');
INSERT INTO `user` VALUES ('o22yYszWl2UxX8rn0Gv6jLB0mJsk', '213121819', 'y884816', '0');
INSERT INTO `user` VALUES ('o22yYs_8H6OgXeBToCuAEBxZ4O1k', '213140773', 'tang961315', '0');
INSERT INTO `user` VALUES ('o22yYs_A2pdMxseIH9qbtb5mxQhc', '213122316', '844884', '0');
INSERT INTO `user` VALUES ('o22yYs_Dk02GG57Q46Rl7-kmFZrQ', '213150698', '8199810jm', '0');
INSERT INTO `user` VALUES ('o22yYs_Hn00cf1I-nWB5Me4KstGo', '220151472', 'BIN201131007', '0');
INSERT INTO `user` VALUES ('o22yYs_JgwDPC_aUkBx38TPgV0JQ', '213143498', 'lsy1996', '0');
INSERT INTO `user` VALUES ('o22yYs_mS9woa_tCEvLTD1GS3s7g', '213152961', 'czyczy1201', '0');
INSERT INTO `user` VALUES ('o22yYs_qdGq5Nzy4h2USgEzwl_Fg', '213142325', 'MICKEY1996112061', '0');
