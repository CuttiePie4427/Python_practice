-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: myweb
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `platform` varchar(20) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `photo_url` varchar(150) DEFAULT NULL,
  `link_url` varchar(150) DEFAULT NULL,
  `post_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (85,'setn','涉毒遭逮！Joeman上月暴瘦　媽媽表情母湯',NULL,'https://star.setn.com/news/1379165?utm_campaign=viewallnews','2023-11-06 18:36:00'),(86,'setn','獨／Joeman持有大麻被逮　瞬間反應曝光',NULL,'https://www.setn.com/News.aspx?NewsID=1379193&utm_campaign=viewallnews','2023-11-06 19:08:00'),(87,'setn','拿身分證！「姓名中1字」喝飲料只要11元',NULL,'https://www.setn.com/News.aspx?NewsID=1379036&utm_campaign=viewallnews','2023-11-06 15:04:00'),(88,'setn','網敲碗奢華vs.平價看守所　Joeman反應曝',NULL,'https://star.setn.com/news/1379233?utm_campaign=viewallnews','2023-11-06 20:56:00'),(89,'setn','6旬叔娶嫩妹給「超浮誇聘金」網一看笑了',NULL,'https://www.setn.com/News.aspx?NewsID=1378777&utm_campaign=viewallnews','2023-11-06 06:05:00'),(90,'setn','獨／Joeman、蕾菈夫婦持毒被逮　警方證實',NULL,'https://star.setn.com/news/1378791?utm_campaign=viewallnews','2023-11-06 17:28:00'),(91,'setn','蕾菈恐加1罪　律師揭九妹下場：沒會客菜',NULL,'https://star.setn.com/news/1379244?utm_campaign=viewallnews','2023-11-06 21:30:00'),(92,'setn','女星認愛3個月結婚了　親揭有孕閃婚真相',NULL,'https://star.setn.com/news/1379042?utm_campaign=viewallnews','2023-11-06 15:22:00'),(93,'setn','獨／Joeman疑持毒被逮！他認：在網路購買',NULL,'https://star.setn.com/news/1378792?utm_campaign=viewallnews','2023-11-06 17:30:00'),(94,'setn','Joeman翻車黑歷史曝光！賣課程挨轟割韭菜',NULL,'https://star.setn.com/news/1379144?utm_campaign=viewallnews','2023-11-06 18:06:00'),(95,'setn','切割Lisa寶格麗總裁怒了！一連發7張照片',NULL,'https://star.setn.com/news/1378903?utm_campaign=viewallnews','2023-11-06 10:31:00'),(96,'setn','Joeman蕾菈持毒遭逮　謝和弦喊以後自己人',NULL,'https://star.setn.com/news/1379138?utm_campaign=viewallnews','2023-11-06 17:52:00'),(97,'setn','蕾菈夫妻、九妹涉持麻遭逮！大麻證物曝光',NULL,'https://www.setn.com/News.aspx?NewsID=1379196&utm_campaign=viewallnews','2023-11-06 19:54:00'),(98,'setn','蕾拉穿家居服應門　還要刑警自己去找大麻',NULL,'https://star.setn.com/news/1379214?utm_campaign=viewallnews','2023-11-06 20:12:00'),(99,'setn','BLACKPINK誰續約太好猜！YG全力捧「她」',NULL,'https://star.setn.com/news/1378694?utm_campaign=viewallnews','2023-11-05 19:17:00'),(100,'setn','餐廳合夥人認了是上游藥頭　酷炫求饒發聲',NULL,'https://star.setn.com/news/1379191?utm_campaign=viewallnews','2023-11-06 19:01:00'),(101,'setn','台灣塩酥雞傳奇　2.8億蓋大樓當員工宿舍',NULL,'https://www.setn.com/News.aspx?NewsID=1379079&utm_campaign=viewallnews','2023-11-06 16:17:00'),(102,'setn','蕾菈持麻發聲明澄清：沒有攜帶毒品入境！',NULL,'https://star.setn.com/news/1379235?utm_campaign=viewallnews','2023-11-06 20:54:00'),(103,'setn','爆朱立倫為藍白合「動怒」！郭正亮曝內幕',NULL,'https://www.setn.com/News.aspx?NewsID=1378818&utm_campaign=viewallnews','2023-11-06 06:40:00'),(104,'setn','獨／Joeman持毒遭逮　24字回應了',NULL,'https://star.setn.com/news/1379125?utm_campaign=viewallnews','2023-11-06 17:37:00'),(105,'setn','NONO、朱海君離定了？好友不忍曝她心境',NULL,'https://star.setn.com/news/1378921?utm_campaign=viewallnews','2023-11-06 11:02:00'),(106,'setn','楊繡惠砸9千萬孝親　開箱新家內裝超氣派',NULL,'https://star.setn.com/news/1379045?utm_campaign=viewallnews','2023-11-06 15:25:00'),(107,'setn','新／威力彩頭獎飆5億　獎號出爐快來對',NULL,'https://www.setn.com/News.aspx?NewsID=1379230&utm_campaign=viewallnews','2023-11-06 20:54:00'),(108,'setn','只有今天快囤　超商「咖啡買6送6」限時搶',NULL,'https://www.setn.com/News.aspx?NewsID=1378867&utm_campaign=viewallnews','2023-11-06 09:32:00'),(109,'setn','獨／「外患罪」遭傳喚　傳馬文君17日出庭',NULL,'https://www.setn.com/News.aspx?NewsID=1379176&utm_campaign=viewallnews','2023-11-06 20:54:00'),(110,'setn','女友不菸不酒爆罹肺腺癌　曾奕翔淚曝心聲',NULL,'https://star.setn.com/news/1378897?utm_campaign=viewallnews','2023-11-06 10:38:00'),(111,'setn','Joeman昨夜在他家　開心合照朋友圈全曝光',NULL,'https://star.setn.com/news/1379173?utm_campaign=viewallnews','2023-11-06 18:39:00'),(112,'setn','蕾菈夫妻、九妹涉持麻　無保請回理由曝光',NULL,'https://www.setn.com/News.aspx?NewsID=1379243&utm_campaign=viewallnews','2023-11-06 21:21:00'),(113,'setn','BTS驚喜合體！親密拍貼V直接對柾國親下去',NULL,'https://star.setn.com/news/1379137?utm_campaign=viewallnews','2023-11-06 18:00:00'),(114,'setn','Joeman涉毒能像Toyz東山再起？內行搖頭了',NULL,'https://star.setn.com/news/1379200?utm_campaign=viewallnews','2023-11-06 19:36:00'),(115,'setn','GD現身警局又一神畫面！陣容以為走紅毯',NULL,'https://star.setn.com/news/1378963?utm_campaign=viewallnews','2023-11-06 12:56:00'),(116,'setn','張柏芝被爆罹癌首露面　真實近況驚呆全場',NULL,'https://star.setn.com/news/1378886?utm_campaign=viewallnews','2023-11-06 12:11:00'),(117,'setn','蕾菈、Joeman持大麻　遭新北警逮捕',NULL,'https://www.setn.com/News.aspx?NewsID=1379130&utm_campaign=viewallnews','2023-11-06 17:35:00'),(118,'setn','蕾菈涉嫌持毒被捕！2年前1舉動如今超諷刺',NULL,'https://star.setn.com/news/1379106?utm_campaign=viewallnews','2023-11-06 17:34:00'),(119,'setn','Joeman涉毒「YT今晚照上片」在線人數狂飆',NULL,'https://star.setn.com/news/1379218?utm_campaign=viewallnews','2023-11-06 20:01:00'),(120,'setn','獨／Joeman新莊「賺錢房」內持毒被逮！',NULL,'https://www.setn.com/News.aspx?NewsID=1379211&utm_campaign=viewallnews','2023-11-06 19:59:00'),(121,'setn','女星宣布懷孕閃婚！3頁手寫信分享幸福',NULL,'https://star.setn.com/news/1378894?utm_campaign=viewallnews','2023-11-06 10:00:00'),(122,'setn','吳淡如赴中國攻讀博士　罕見發飆：X娘',NULL,'https://star.setn.com/news/1378707?utm_campaign=viewallnews','2023-11-05 18:59:00'),(123,'setn','超哥臉鐵青險揍人！無預警同框Toyz嚇壞',NULL,'https://star.setn.com/news/1377963?utm_campaign=viewallnews','2023-11-06 14:03:00'),(124,'setn','林昱珉、孫易磊領軍　亞錦賽24人名單曝光',NULL,'https://www.setn.com/News.aspx?NewsID=1379184&utm_campaign=viewallnews','2023-11-06 18:58:00'),(125,'setn','博恩突破萬分之9機率當爸　突宣布要結紮',NULL,'https://star.setn.com/news/1379016?utm_campaign=viewallnews','2023-11-06 14:34:00'),(126,'setn','當兵被分到嘉義1地　過來人笑了：地獄營',NULL,'https://www.setn.com/News.aspx?NewsID=1378328&utm_campaign=viewallnews','2023-11-04 17:42:00');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-06 22:03:09
